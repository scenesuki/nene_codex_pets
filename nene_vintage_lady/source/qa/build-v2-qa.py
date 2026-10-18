"""Build v2 inspection media; clean only after both look rows are accepted."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("stage", choices=["assemble", "clean"])
args = parser.parse_args()
run = Path(__file__).resolve().parents[1]
scripts = Path.home() / ".codex/skills/hatch-pet/scripts"

def native(script, *args):
    subprocess.run([sys.executable, str(scripts / script), *map(str, args)], check=True)

if args.stage == "assemble":
    native("assemble_extended_atlas.py", "--base-atlas", run / "final/spritesheet.webp", "--registered-row-9", run / "qa/look-row-9-registered.png", "--row-9-registration", run / "qa/look-row-9-registration.json", "--look-row-10", run / "decoded/look-row-10.png", "--neutral-cell", run / "frames/idle/00.png", "--chroma-key", "#FF00FF", "--chroma-threshold", "96", "--output", run / "final/spritesheet-extended-preclean.png", "--webp-output", run / "final/spritesheet-extended-preclean.webp", "--manifest-output", run / "final/spritesheet-extended-preclean.json")
    native("make_direction_qa_sheet.py", run / "final/spritesheet-extended-preclean.webp", "--output", run / "qa/look-directions-preclean.png")
    native("measure_direction_continuity.py", run / "final/spritesheet-extended-preclean.webp", "--json-out", run / "qa/look-continuity-preclean.json")
else:
    (run.parent / "preview").mkdir(exist_ok=True)
    assert json.loads((run / "qa/look-row-10-semantics.json").read_text(encoding="utf-8"))["ok"]
    assert not (run / "qa/chroma-despill-extended.json").exists(), "Do not repeat cleanup"
    native("despill_chroma_edges.py", run / "final/spritesheet-extended-preclean.png", "--output", run / "final/spritesheet-extended.png", "--webp-output", run / "final/spritesheet-extended.webp", "--chroma-key", "#FF00FF", "--json-out", run / "qa/chroma-despill-extended.json")
    native("validate_atlas.py", run / "final/spritesheet-extended.webp", "--json-out", run / "final/validation-extended.json", "--chroma-key", "#FF00FF", "--require-v2")
    native("make_contact_sheet.py", run / "final/spritesheet-extended.webp", "--output", run.parent / "preview/contact-sheet.png")
    native("make_direction_qa_sheet.py", run / "final/spritesheet-extended.webp", "--output", run.parent / "preview/look-directions.png")
    native("make_direction_blind_qa_sheet.py", run / "final/spritesheet-extended.webp", "--output", run / "qa/direction-blind-pairs.png", "--answer-key", run / "qa/direction-blind-answer-key.json")
    native("measure_direction_continuity.py", run / "final/spritesheet-extended.webp", "--json-out", run / "qa/look-continuity.json")
    subprocess.run([sys.executable, str(run / "qa/render-final-previews.py")], check=True)
