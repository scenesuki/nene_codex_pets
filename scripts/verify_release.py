"""Check that a release contains every root pet and its current deliverable files."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile


def verify_release(root, archive):
    pets = sorted(path.parent for path in root.glob("*/pet.json"))
    assert pets, "No root pets found"
    with zipfile.ZipFile(archive) as package:
        assert package.testzip() is None, "ZIP corruption"
        names = package.namelist()
        assert len(names) == len(set(names)), "Duplicate ZIP entries"
        expected_ids = {pet.name for pet in pets}
        actual_ids = {name.split("/")[0] for name in names if name.endswith("/pet.json")}
        assert actual_ids == expected_ids, f"Pet inventory differs: {actual_ids} != {expected_ids}"
        expected = [root / name for name in ["README.md", "NOTICE.md", "AGENTS.md", "PET_NAMES.md"]]
        for pet in pets:
            expected.extend(pet / name for name in
                            ["pet.json", "spritesheet.webp", "README.md", "NOTICE.md", "validation.json"])
            if (pet / "installed-validation.json").exists():
                expected.append(pet / "installed-validation.json")
            previews = sorted(path for path in (pet / "preview").rglob("*") if path.is_file())
            assert previews, f"Missing previews: {pet.name}"
            expected.extend(previews)
        expected_names = {path.relative_to(root).as_posix() for path in expected}
        assert set(names) == expected_names, "Missing or unexpected deliverable files"
        for path in expected:
            name = path.relative_to(root).as_posix()
            assert package.read(name) == path.read_bytes(), f"File differs: {name}"
    return {"ok": True, "pet_ids": sorted(expected_ids), "entry_count": len(names),
            "sha256": hashlib.sha256(archive.read_bytes()).hexdigest()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    args = parser.parse_args()
    print(json.dumps(verify_release(Path(__file__).resolve().parent.parent, args.archive), indent=2))
