"""Verify deliverables, preserved resources, documentation links and provenance."""
import ast
import hashlib
import json
import re
from pathlib import Path
from PIL import Image

pet = Path(__file__).resolve().parents[2]
root = pet.parent
run = pet / "source"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda p: json.loads(p.read_text(encoding="utf-8"))
manifest = load(pet / "pet.json")
assert manifest["id"] == manifest["displayName"] == pet.name == "nene_movie"
assert manifest["spriteVersionNumber"] == 2 and manifest["spritesheetPath"] == "spritesheet.webp"
assert (pet / "spritesheet.webp").read_bytes() == (run / "final/spritesheet-extended.webp").read_bytes()
atlas = Image.open(pet / "spritesheet.webp").convert("RGBA")
assert atlas.size == (1536, 2288)
assert Image.open(pet / "preview/readme-portrait.png").convert("RGBA").tobytes() == atlas.crop((0, 0, 192, 208)).tobytes()
preclean = Image.open(run / "final/spritesheet-extended-preclean.png").convert("RGBA")
assert preclean.getchannel("A").tobytes() == atlas.getchannel("A").tobytes()
assert Image.open(run / "qa/look-row-9-registered.png").convert("RGBA").tobytes() == preclean.crop((0, 9*208, 1536, 10*208)).tobytes()
for path in [pet / "validation.json", run / "qa/chroma-despill-extended.json", run / "qa/direction-blind-validation.json", run / "qa/preview-files-check.json", pet / "preview/app-loader-validation.json"]:
    assert load(path)["ok"], path
assert load(run / "qa/final-visual-qa.json")["visual_qa"] == "pass"
directions = load(run / "qa/direction-semantics.json")["directions"]
assert len(directions) == 16 and all(d["verdict"] in ("pass", "warning") for d in directions)
jobs = load(run / "imagegen-jobs.json")["jobs"]
assert len(jobs) == 13 and all(job["status"] == "complete" for job in jobs)
for job in jobs:
    assert Path(job["source_path"]).read_bytes() == (run / job["output_path"]).read_bytes(), job["id"]
baseline = load(run / "qa/existing-pets-baseline.json")
for name, digest in baseline.items():
    assert sha(root / name) == digest, name
links = []
for doc in [root / "README.md", pet / "README.md", pet / "preview/README.md"]:
    text = doc.read_text(encoding="utf-8")
    assert not re.search(r"<img[^>]+\.gif|!\[[^\]]*\]\([^)]*\.gif", text, re.I), doc
    targets = re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text) + re.findall(r'(?:href|src)="([^"]+)"', text)
    for target in targets:
        if target.startswith(("https://", "http://", "#")):
            continue
        path = (doc.parent / target.split("#", 1)[0]).resolve()
        assert path.is_file(), (doc, target)
        links.append(str(path))
for path in run.rglob("*.py"):
    ast.parse(path.read_text(encoding="utf-8-sig"))
old_packages = []
for sums in (root / "release-assets").glob("v*/SHA256SUMS.txt"):
    digest, name = sums.read_text(encoding="utf-8").strip().split(maxsplit=1)
    if not (sums.parent / name.strip()).exists():
        continue  # Historical local ZIPs were removed by the user.
    assert sha(sums.parent / name.strip()) == digest, sums
    old_packages.append(sums.parent.name)
report = {"ok": True, "pet_id": pet.name, "spritesheet_sha256": sha(pet / "spritesheet.webp"), "portrait_exact_final_atlas_crop": True, "alpha_preserved": True, "registered_row9_reused_exactly": True, "generation_jobs": 13, "all_selected_sources_preserved": True, "existing_pet_files_unchanged": len(baseline), "local_links_checked": len(links), "historical_package_hashes_checked": old_packages, "application_ui_verified": False, "installed": (pet / "installed-validation.json").exists(), "uploaded": False}
(run / "qa/delivery-check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
