"""Reflow complete blind-challenge blocks without changing any displayed pixels."""
import hashlib
import json
from pathlib import Path
from PIL import Image

qa = Path(__file__).resolve().parent
source = qa / "direction-blind-pairs.png"
im = Image.open(source).convert("RGB")
assert im.size == (384, 3304)
canvas = Image.new("RGB", (768, 1652))
for index in range(14):
    block = im.crop((0, index * 236, 384, (index + 1) * 236))
    x, y = (index // 7) * 384, (index % 7) * 236
    canvas.paste(block, (x, y))
    assert canvas.crop((x, y, x + 384, y + 236)).tobytes() == block.tobytes()
output = qa / "direction-blind-pairs-compact.png"
canvas.save(output)
(qa / "direction-blind-display-check.json").write_text(json.dumps({"ok": True, "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "reflowed_sha256": hashlib.sha256(output.read_bytes()).hexdigest(), "blocks": 14, "resampled": False, "all_block_pixels_identical": True}, indent=2) + "\n", encoding="utf-8")
