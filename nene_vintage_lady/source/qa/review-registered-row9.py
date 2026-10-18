"""Expose registered row9 at exact cell size and measure native adjacent metrics."""
import importlib.util,json
from pathlib import Path
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("native_continuity",Path.home()/".codex/skills/hatch-pet/scripts/measure_direction_continuity.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
im=Image.open(r/"qa/look-row-9-registered.png").convert("RGBA")
assert im.size==(1536,208)
labels=["000 up","022.5 up-right","045 up-right","067.5 up-right","090 right","112.5 down-right","135 down-right","157.5 down-right"]
cells=[im.crop((i*192,0,(i+1)*192,208)) for i in range(8)]
sheet=Image.new("RGBA",(1536,234),(246,245,248,255));d=ImageDraw.Draw(sheet)
for i,(label,cell) in enumerate(zip(labels,cells)):
    sheet.alpha_composite(cell,(192*i,26));d.text((192*i+4,6),label,fill="#35313d")
sheet.save(r/"qa/look-row-9-review.png")
metrics=[{"from":labels[i],"to":labels[i+1],**m.pair_metric(cells[i],cells[i+1])} for i in range(7)]
(r/"qa/look-row-9-continuity.json").write_text(json.dumps({"ok":True,"pairs":metrics,"alphaHoles":[{"direction":labels[i],"holes":m.transparent_hole_rows(c)} for i,c in enumerate(cells) if m.transparent_hole_rows(c)]},indent=2)+"\n",encoding="utf-8")
print(json.dumps(metrics,indent=2))
