"""Register generated row 10 using the approved row 9 scale; no pose edits."""
import importlib.util
import json
import sys
from pathlib import Path
from PIL import Image
root = Path(__file__).resolve().parents[1]
helper = Path(r"C:/Users/tieha/.codex/skills/hatch-pet/scripts/assemble_extended_atlas.py")
spec = importlib.util.spec_from_file_location("native_assemble", helper)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)
source = root / "decoded/look-row-10.png"
neutral = Image.open(root / "frames/idle/00.png").convert("RGBA")
scale = m.load_registration_scale(root / "qa/look-row-9-registration-r2.json")
cells = m.extract_row_strip_cells(source, (255, 0, 255), 128)
assert len(cells) == 8
cells = m.normalize_cells_to_reference(cells, neutral, scale)
m.validate_normalized_look_cells(cells, 8, m.DEFAULT_EDGE_MARGIN, m.DEFAULT_EDGE_PIXEL_THRESHOLD)
records = []
for label, cell in zip(["180","202.5","225","247.5","270","292.5","315","337.5"], cells):
    alpha = cell.getchannel("A")
    count = sum(a > 0 for a in alpha.getdata())
    assert count > 5000, (label, count)
    records.append({"direction": label, "bbox": alpha.getbbox(), "visible_pixels": count, "edge_pixels": m.edge_alpha_count(cell, m.DEFAULT_EDGE_MARGIN)})
m.save_registered_row(cells, root / "qa/look-row-10-registered.png")
report = {"ok": True, "source": str(source), "scale": scale, "chroma_threshold": 128, "rows_share_exact_scale": True, "cells": records}
(root / "qa/look-row-10-registration.json").write_text(json.dumps(report, indent=2)+"\n",encoding="utf-8")
print(json.dumps(report, indent=2))
