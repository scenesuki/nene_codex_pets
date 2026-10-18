"""Export only the accepted, validated local nene_edo package."""
from pathlib import Path
import json,shutil
from PIL import Image
run=Path(__file__).resolve().parents[1]
pet=run.parent
load=lambda p:json.loads(p.read_text(encoding="utf-8"))
assert load(run/"qa/final-visual-qa.json")["visual_qa"]=="pass"
for p in [run/"final/validation-extended.json",run/"qa/chroma-despill-extended.json",run/"qa/direction-blind-validation.json",run/"qa/preview-files-check.json"]:assert load(p)["ok"],p
assert all(d["verdict"] in ("pass","warning") for d in load(run/"qa/direction-semantics.json")["directions"])
jobs=load(run/"imagegen-jobs.json")["jobs"]
assert len(jobs)==13 and all(j["status"]=="complete" for j in jobs)
manifest={"id":"nene_edo","displayName":"nene_edo","description":"草薙宁宁二星卡「江戸の町並みに飲まれて」黑绿复古洋装的Q版日系宠物。","spriteVersionNumber":2,"spritesheetPath":"spritesheet.webp"}
(pet/"pet.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
shutil.copy2(run/"final/spritesheet-extended.webp",pet/"spritesheet.webp")
shutil.copy2(run/"final/validation-extended.json",pet/"validation.json")
assert (pet/"preview/animation-overview.gif").is_file()
Image.open(pet/"spritesheet.webp").convert("RGBA").crop((0,0,192,208)).save(pet/"preview/readme-portrait.png")
print("Exported local nene_edo; not installed or uploaded")
