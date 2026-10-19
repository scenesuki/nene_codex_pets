"""Keep generated poses intact; register their boot baselines for a small hop."""
from pathlib import Path
import json
from PIL import Image

run = Path(__file__).resolve().parents[1]
origin = run/'qa/jumping-gentle/frames/jumping'
target = run/'qa/rows/jumping/frames/jumping'
images = [Image.open(origin/f'{index:02}.png').convert('RGBA') for index in range(5)]
rest = 203
lifts = [0,4,8,4,0]
records=[]
for index,(image,lift) in enumerate(zip(images,lifts)):
    before=image.getbbox()
    dy=rest-lift-before[3]
    after=Image.new('RGBA',image.size)
    after.alpha_composite(image,(0,dy))
    assert sum(image.getchannel('A').histogram())==sum(after.getchannel('A').histogram())
    assert sum(i*n for i,n in enumerate(image.getchannel('A').histogram()))==sum(i*n for i,n in enumerate(after.getchannel('A').histogram()))
    assert after.getbbox()[3]==rest-lift
    after.save(target/f'{index:02}.png')
    records.append({'frame':index,'source_bbox':before,'vertical_translation_px':dy,'final_bbox':after.getbbox(),'foot_lift_px':lift})
manifest=run/'qa/rows/jumping/frames/frames-manifest.json'
value=json.loads(manifest.read_text(encoding='utf-8'))
value['rows'][0]['method']='components'
value['rows'][0]['vertical_placement']=records
manifest.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(run/'qa/jump-placement.json').write_text(json.dumps({'ok':True,'method':'Native component extraction with 188px height limit, then integer whole-frame vertical registration only; no anatomy edits or warps','max_boot_lift_px':max(lifts),'poses':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'max_boot_lift_px':max(lifts),'vertical_translations':[r['vertical_translation_px'] for r in records]}))
