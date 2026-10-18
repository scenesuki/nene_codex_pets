"""Build a cumulative desktop pet release without altering artwork."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile

from PIL import Image
from verify_release import verify_release


def build_release(root, tag):
    if not re.fullmatch(r"v\d+\.\d+\.\d+", tag):
        raise ValueError("Use a project tag such as v1.1.1")
    output = root / "release-assets" / tag
    if output.exists():
        raise FileExistsError("Preserve existing release directories; use a new tag")
    pets = sorted(path.parent for path in root.glob("*/pet.json"))
    assert pets, "No root pets found"
    files = [root / name for name in ["README.md", "NOTICE.md", "AGENTS.md", "PET_NAMES.md"]]
    counts = dict(zip(["idle", "running-right", "running-left", "waving", "jumping",
                       "failed", "waiting", "running", "review", "look-directions"],
                      [6, 8, 8, 4, 5, 8, 6, 6, 6, 16]))
    inventory = []
    for pet in pets:
        manifest = json.loads((pet / "pet.json").read_text(encoding="utf-8"))
        assert manifest["id"] == pet.name, f"ID differs from folder: {pet.name}"
        assert manifest["spriteVersionNumber"] == 2, pet.name
        assert manifest["spritesheetPath"] == "spritesheet.webp", pet.name
        with Image.open(pet / "spritesheet.webp") as image:
            assert image.format == "WEBP" and image.mode == "RGBA", pet.name
            assert image.size == (1536, 2288), pet.name
            image.load()
        validation = json.loads((pet / "validation.json").read_text(encoding="utf-8"))
        assert validation["ok"] and not validation["errors"], pet.name
        assert validation["transparent_rgb_residue_pixels"] == 0, pet.name
        for name in [*counts, "animation-overview"]:
            with Image.open(pet / "preview" / f"{name}.gif") as image:
                assert image.size == ((576, 678) if name == "animation-overview" else (192, 208))
                if name in counts:
                    assert image.n_frames == counts[name], f"{pet.name}/{name}"
                duration = 0
                for frame in range(image.n_frames):
                    image.seek(frame)
                    image.load()
                    duration += image.info["duration"]
                if name == "animation-overview":
                    assert image.n_frames > 1 and duration == 1680
        files.extend(pet / name for name in
                     ["pet.json", "spritesheet.webp", "README.md", "NOTICE.md", "validation.json"])
        if (pet / "installed-validation.json").exists():
            files.append(pet / "installed-validation.json")
        files.extend(sorted(path for path in (pet / "preview").rglob("*") if path.is_file()))
        inventory.append({"id": pet.name, "display_name": manifest["displayName"],
                          "sprite_sha256": hashlib.sha256((pet / "spritesheet.webp").read_bytes()).hexdigest()})
    for file in files:
        assert file.is_file(), f"Missing deliverable: {file}"
    output.mkdir(parents=True)
    archive = output / f"nene_codex_pets-{tag}.zip"
    with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_DEFLATED) as package:
        for file in files:
            package.write(file, file.relative_to(root).as_posix())
    report = verify_release(root, archive)
    report.update({"version": tag, "archive": archive.name, "size": archive.stat().st_size,
                   "pets": inventory, "state_frames": counts, "publication_status": "local-prepared",
                   "application_ui_detection_verified": False, "floating_display_verified": False})
    (output / "SHA256SUMS.txt").write_text(f"{report['sha256']}  {archive.name}\n", encoding="utf-8", newline="\n")
    (output / "package-check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                                              encoding="utf-8", newline="\n")
    notes = f"# nene_codex_pets {tag}\n\n完整宠物合集：\n\n"
    notes += "\n".join(f"- `{pet['id']}`：{pet['display_name']}。" for pet in inventory)
    notes += (f"\n\n下载 `{archive.name}` 及 `SHA256SUMS.txt`，解压后将所需宠物目录复制到 "
              "`~/.codex/pets/`。每套均附安装文件、来源说明、最终校验记录和完整预览。\n\n"
              "本包使用各宠物目录顶层成品。已核对全量清单、ZIP字节一致性、"
              "WebP规格及全部GIF帧；应用设置识别和浮动显示尚未实测。\n")
    (output / "release-notes.md").write_text(notes, encoding="utf-8", newline="\n")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True)
    args = parser.parse_args()
    print(json.dumps(build_release(Path(__file__).resolve().parent.parent, args.tag), ensure_ascii=False, indent=2))
