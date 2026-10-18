"""Assemble generated standard rows, preserving the original jump arc."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

run = Path(__file__).resolve().parents[1]
scripts = Path.home() / ".codex/skills/hatch-pet/scripts"
manifest_path = run / "frames/frames-manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
stable = run / "qa/jumping-stable/frames/jumping"
for frame in stable.glob("*.png"):
    shutil.copyfile(frame, run / "frames/jumping" / frame.name)
next(row for row in manifest["rows"] if row["state"] == "jumping")["method"] = "stable-slots"
manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

def native(script, *args):
    subprocess.run([sys.executable, str(scripts / script), *map(str, args)], check=True)

native("inspect_frames.py", "--frames-root", run / "frames", "--json-out", run / "qa/review.json", "--require-components", "--allow-stable-slots")
native("compose_atlas.py", "--frames-root", run / "frames", "--output", run / "final/spritesheet.png", "--webp-output", run / "final/spritesheet.webp")
native("make_contact_sheet.py", run / "final/spritesheet.webp", "--output", run / "qa/contact-sheet.png")
native("render_animation_previews.py", "--frames-root", run / "frames", "--output-dir", run / "qa/previews")
