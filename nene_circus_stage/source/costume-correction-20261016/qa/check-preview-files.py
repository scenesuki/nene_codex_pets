"""Decode every final GIF frame and expose those exact frames for visual review."""
import json
from pathlib import Path
from PIL import Image, ImageDraw

run = Path(__file__).resolve().parents[1]
preview = run / "preview"
counts = dict(zip(["idle", "running-right", "running-left", "waving", "jumping", "failed", "waiting", "running", "review", "look-directions"], [6, 8, 8, 4, 5, 8, 6, 6, 6, 16]))
sheet = Image.new("RGB", (1536, 11 * 230), "#f6f5f8")
draw = ImageDraw.Draw(sheet)
records = []
row = 0
for name, count in counts.items():
    with Image.open(preview / f"{name}.gif") as gif:
        assert gif.size == (192, 208) and gif.n_frames == count, name
        durations = []
        for index in range(count):
            gif.seek(index)
            gif.load()
            frame = gif.convert("RGBA")
            target_row = row + index // 8
            x, y = (index % 8) * 192, target_row * 230
            sheet.paste(frame, (x, y + 22), frame)
            draw.text((x + 4, y + 4), f"{name} {index}", fill="#35313d")
            durations.append(gif.info["duration"])
        records.append({"file": f"{name}.gif", "frames": count, "durations_ms": durations, "all_frames_decoded": True})
    row += 2 if name == "look-directions" else 1
with Image.open(preview / "animation-overview.gif") as gif:
    assert gif.size == (576, 678) and gif.n_frames > 1
    duration = 0
    for index in range(gif.n_frames):
        gif.seek(index)
        gif.load()
        duration += gif.info["duration"]
    assert duration == 1680
    records.append({"file": "animation-overview.gif", "frames": gif.n_frames, "duration_ms": duration, "all_frames_decoded": True})
sheet.save(run / "qa/decoded-gif-contact.png")
for block in range(3):
    sheet.crop((0,block*690,1536,(block+1)*690)).save(run / f"qa/final-gif-states-{block+1}.png")
(run / "qa/preview-files-check.json").write_text(json.dumps({"ok": True, "files": records}, indent=2) + "\n", encoding="utf-8")
print("All final GIF frames decoded; exact decoded-frame contact saved")
