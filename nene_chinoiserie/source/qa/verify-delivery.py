"""Verify the completed local pet, its source index and formal preview files."""
from pathlib import Path
import hashlib, json, re
from urllib.parse import unquote
from PIL import Image

run=Path(__file__).resolve().parents[1]
pet=run.parent
root=pet.parent
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=load(pet/'pet.json')
assert manifest['id']=='nene_chinoiserie' and manifest['displayName']=='宁宁 · 新中式礼装'
assert manifest['spriteVersionNumber']==2 and manifest['spritesheetPath']=='spritesheet.webp'
assert (pet/'spritesheet.webp').read_bytes()==(run/'final/spritesheet-extended.webp').read_bytes()
validation=load(pet/'validation.json')
assert validation['ok'] and not validation['errors']
assert validation['transparent_rgb_residue_pixels']==0
assert load(pet/'preview/app-loader-validation.json')['ok']
assert load(pet/'preview/direction-blind-validation.json')['ok']
with Image.open(pet/'spritesheet.webp') as image, Image.open(pet/'preview/readme-portrait.png') as portrait:
    assert image.format=='WEBP' and image.mode=='RGBA' and image.size==(1536,2288)
    assert portrait.mode=='RGBA' and portrait.size==(192,208)
    assert image.crop((0,0,192,208)).tobytes()==portrait.tobytes()
    jump=[image.crop((i*192,4*208,(i+1)*192,5*208)).getbbox()[3] for i in range(5)]
    assert [jump[0]-value for value in jump]==[0,4,8,4,0]

counts=dict(zip(['idle','running-right','running-left','waving','jumping','failed','waiting','running','review','look-directions'],[6,8,8,4,5,8,6,6,6,16]))
preview_reports=[]
for state in [*counts,'animation-overview']:
    file=pet/'preview'/f'{state}.gif'
    with Image.open(file) as image:
        assert image.size==((576,678) if state=='animation-overview' else (192,208))
        if state in counts:assert image.n_frames==counts[state],(state,image.n_frames)
        duration=0
        for index in range(image.n_frames):
            image.seek(index); image.load(); duration+=image.info['duration']
        if state=='animation-overview':assert duration==1680 and image.n_frames>1
        preview_reports.append({'file':file.name,'frames':image.n_frames,'size':list(image.size),'total_duration_ms':duration,'sha256':sha(file)})
(pet/'preview/preview-files-check.json').write_text(json.dumps({'ok':True,'method':'Decoded all GIF frames and checked dimensions, counts and native timings; no live-player or app UI claim','previews':preview_reports},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
materials=load(run/'materials-index.json')
assert materials['current_atlas_sha256']==sha(pet/'spritesheet.webp')
assert len(materials['jobs'])==13
for item in materials['retained_materials']:
    assert sha(root/item['path'])==item['sha256'],item['path']
bad=[]; checked=0
for doc in [root/'README.md',pet/'README.md',pet/'NOTICE.md',pet/'preview/README.md',run/'README.md']:
    text=doc.read_text(encoding='utf-8')
    assert not re.search(r'<img[^>]+src="[^"]+\.gif',text,re.I)
    for url in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text)+re.findall(r'(?:href|src)="([^"]+)"',text):
        if re.match('[a-zA-Z]+:',url) or url.startswith('#'):continue
        target=unquote(url.strip('<>').split('#')[0]); checked+=1
        if not (doc.parent/target).exists():bad.append([str(doc),url])
assert not bad,bad
protected=load(run/'qa/existing-pets-baseline.json')
for rel,digest in protected.items():assert sha(root/rel)==digest,rel
archive=root/'release-assets/v1.8.0/nene_codex_pets-v1.8.0.zip'
assert sha(archive)=='c499ccde22b7aca10c4a48a61298edf836df8eb3b42845ad98ea2ff9364160aa'
report={'ok':True,'pet_id':pet.name,'display_name':manifest['displayName'],'spritesheet_sha256':sha(pet/'spritesheet.webp'),'selected_original_jobs':len(materials['jobs']),'retained_materials_verified':len(materials['retained_materials']),'formal_gifs_verified':len(preview_reports),'local_document_links_checked':checked,'max_jump_boot_lift_px':8,'existing_protected_files_unchanged':len(protected),'published_v1_8_0_zip_unchanged':True,'installed':False,'uploaded':False,'published':False,'application_ui_verified':False}
(run/'qa/delivery-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
