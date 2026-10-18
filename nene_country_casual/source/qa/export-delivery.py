"""Export only the fully validated final pet; source candidates stay preserved."""
import json
import shutil
from pathlib import Path
from PIL import Image

run = Path(__file__).resolve().parents[1]
pet = run.parent
load = lambda p: json.loads(p.read_text(encoding='utf-8'))
assert load(run / 'qa/final-visual-qa.json')['visual_qa'] == 'pass'
for name in ['direction-blind-validation.json', 'preview-files-check.json', 'chroma-despill-extended.json']:
    assert load(run / 'qa' / name)['ok'], name
assert load(run / 'final/validation-extended.json')['ok']
jobs = load(run / 'imagegen-jobs.json')['jobs']
assert len(jobs) == 13 and all(j['status'] == 'complete' for j in jobs)
assert all(d['verdict'] in ('pass','warning') for d in load(run / 'qa/direction-semantics.json')['directions'])
manifest = {'id':'nene_movie','displayName':'nene_movie','description':'草薙宁宁二星卡「Let’s enjoy the movie！」观影造型的Q版日系宠物。','spriteVersionNumber':2,'spritesheetPath':'spritesheet.webp'}
(pet / 'pet.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
shutil.copy2(run / 'final/spritesheet-extended.webp', pet / 'spritesheet.webp')
shutil.copy2(run / 'final/validation-extended.json', pet / 'validation.json')
preview = pet / 'preview'
preview.mkdir(exist_ok=True)
assert (preview / 'animation-overview.gif').is_file()
assert (preview / 'contact-sheet.png').is_file()
assert (preview / 'look-directions.png').is_file()
Image.open(pet / 'spritesheet.webp').convert('RGBA').crop((0,0,192,208)).save(preview / 'readme-portrait.png')
print('Final nene_movie manifest, atlas, validation and previews exported')
