"""Expose fixed-scale row10 diagnostics; never changes or approves an atlas."""
import importlib.util
import json
import sys
from pathlib import Path
from PIL import Image, ImageDraw

run = Path(__file__).resolve().parents[1]
scripts = Path.home() / ".codex/skills/hatch-pet/scripts"
sys.path.insert(0, str(scripts))
spec = importlib.util.spec_from_file_location("native_assembly", scripts / "assemble_extended_atlas.py")
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)
cells = native.extract_row_strip_cells(run / "decoded/look-row-10.png", (255, 0, 255), 96)
scale = native.load_registration_scale(run / "qa/look-row-9-registration.json")
normalized = native.normalize_cells_to_reference(cells, Image.open(run / "frames/idle/00.png"), scale)
labels = ["180", "202.5", "225", "247.5", "270", "292.5", "315", "337.5"]
report = [{"direction": label, "source_height": native.cell_geometry(source).height,
           "source_bbox": source.getbbox(), "final_bbox": cell.getbbox(),
           "edge_pixels": native.edge_alpha_count(cell, 2),
           "used_pixels": sum(cell.getchannel("A").histogram()[1:])}
          for label, source, cell in zip(labels, cells, normalized)]
sheet = Image.new("RGBA", (1536, 234), "#f6f5f8")
draw = ImageDraw.Draw(sheet)
for i, (label, cell) in enumerate(zip(labels, normalized)):
    draw.text((i * 192 + 4, 6), label, fill="#35313d")
    sheet.alpha_composite(cell, (i * 192, 26))
suffix = sys.argv[1]
sheet.save(run / f"qa/look-row-10-{suffix}-diagnostic.png")
(run / f"qa/look-row-10-{suffix}-diagnostic.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
