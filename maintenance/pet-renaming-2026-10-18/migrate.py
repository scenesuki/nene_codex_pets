"""One-time, auditable workspace pet naming migration."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import unquote
import hashlib, json, os, re, sys
from PIL import Image

audit = Path(__file__).resolve().parent
root = audit.parents[1]
plan = json.loads((audit/'plan.json').read_text(encoding='utf-8'))
pets = plan['pets']
mapping = {p['old_id']:p['new_id'] for p in pets}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda p: json.loads(p.read_text(encoding='utf-8'))

def save(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes((json.dumps(value, ensure_ascii=False, indent=2)+'\n').encode('utf-8'))

def mapped(rel):
    parts = Path(rel).parts
    return Path(mapping.get(parts[0],parts[0]), *parts[1:])

def backup(p):
    target = audit/'before-files'/p.relative_to(root)
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(p.read_bytes())

def write(p, text):
    backup(p)
    p.write_bytes(text.encode('utf-8'))

pattern = re.compile(r'(?<![a-z0-9_-])('+ '|'.join(re.escape(k) for k in sorted(mapping,key=len,reverse=True))+r')(?![a-z0-9_-])')
def rename_text(text):
    return pattern.sub(lambda m:mapping[m[0]],text)

if sys.argv[1] == 'snapshot':
    assert not (audit/'before.json').exists(), 'Preserve original audit'
    assert {p.parent.name for p in root.glob('*/pet.json')} == set(mapping)
    files = {}
    for pet in pets:
        folder = root/pet['old_id']
        for file in sorted(folder.rglob('*')):
            if file.is_file(): files[file.relative_to(root).as_posix()] = sha(file)
        index = load(folder/'source/materials-index.json')
        for item in index['retained_materials']:
            assert sha(root/item['path']) == item['sha256'], item['path']
    releases = {p.relative_to(root).as_posix():sha(p) for p in (root/'release-assets').rglob('*') if p.is_file()}
    installed = {}
    pet_home = Path(os.environ.get('CODEX_HOME',str(Path.home()/'.codex')))/'pets'
    for name in set(mapping)|set(mapping.values()):
        for filename in ['pet.json','spritesheet.webp']:
            p=pet_home/name/filename
            if p.is_file(): installed[str(p)]=sha(p)
    save(audit/'before.json', {'files':files,'release_files':releases,'installed_files':installed})
    for p in [root/'README.md',root/'AGENTS.md',root/'.gitattributes']: backup(p)
    print(json.dumps({'files':len(files),'release_files':len(releases),'installed_files':len(installed)}))

elif sys.argv[1] == 'metadata':
    assert not (audit/'applied-plan.json').exists(), 'Metadata migration already applied; preserve original display-name evidence'
    before=load(audit/'before.json')
    for pet in pets:
        old,new,display=pet['old_id'],pet['new_id'],pet['display_name']
        folder=root/new
        assert folder.is_dir() and (old==new or not (root/old).exists())
        manifest=load(folder/'pet.json')
        pet['previous_display_name']=manifest['displayName']
        manifest.update(id=new,displayName=display)
        write(folder/'pet.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        validation=load(folder/'validation.json')
        assert validation['ok'] and not validation['errors']
        validation['file']=str(folder/'spritesheet.webp')
        write(folder/'validation.json',json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
        for rel in ['README.md','preview/README.md','source/README.md']:
            p=folder/rel
            text=rename_text(p.read_text(encoding='utf-8'))
            if rel=='README.md':
                text=re.sub(r'^# .*$', '# '+display,text,count=1,flags=re.M)
                text=re.sub(r'alt="[^"]*"',lambda m:'alt="'+display+'静态预览"',text,count=1)
                text=text.replace('nene_victorian lolita',display).replace('nene_classical lolita',display)
                info=f'**{display}** · ID `{new}` · 9种动画 · 16个注视方向'
                text=re.sub(r'^\*\*.*$',info,text,count=1,flags=re.M) if re.search(r'^\*\*',text,re.M) else re.sub(r'(<img[^>]*>)',lambda m:m[0]+'\n\n'+info,text,count=1)
                if old!='nene_classical_lolita':
                    history=f'命名已统一；上方已发布合集保留当时的目录 `{old}/` 与显示名。当前新命名成品请使用本地文件；历史包按包内说明安装，参见[命名对照](../PET_NAMES.md)。'
                    text=text.replace('\n## 安装', '\n'+history+'\n\n## 安装',1)
                steps=f'''## 安装

1. 将当前工作区的 `{new}/` 复制至 `~/.codex/pets/`，保留顶层的 `pet.json` 与 `spritesheet.webp`。
2. Windows默认目录为 `%USERPROFILE%\\.codex\\pets\\{new}\\`；自定义 `CODEX_HOME` 时使用其下的 `pets/{new}/`。
3. 在Codex设置 > Pets中刷新并选择「{display}」，必要时重启应用。

'''
                if (folder/'installed-validation.json').exists():
                    steps+='[原安装记录](installed-validation.json)保留更名前的名称和文件哈希。本次仅更新项目，未改动本机已安装副本；新名称尚未完成安装验证。\n\n'
                else: steps+='本套当前名称尚未安装；本次未执行安装或切换。\n\n'
                text=re.sub(r'## 安装\n.*?(?=<details>)',lambda m:steps,text,count=1,flags=re.S)
                text=re.sub(r'\[加载算法检查\]\(preview/app-loader-validation.json\)[^。\n]*。','[加载算法检查](preview/app-loader-validation.json)已核对更名后的工作区清单、图片及路径；未执行应用UI显示测试。',text)
                text=text.replace('<summary>规格与验收</summary>','<summary>规格与验收</summary>\n\n- [更名校验](preview/rename-validation.json)记录当前名称及成品哈希；图片、动画和有效制作原素材保持原字节。历史制作与安装记录保留当时标识，当前名称见[命名对照](../PET_NAMES.md)。',1)
            elif rel=='preview/README.md': text=re.sub(r'^# .*$', '# '+display+' · 预览',text,count=1,flags=re.M)
            else:
                text=re.sub(r'^# .*$', '# '+new+' · 制作原素材',text,count=1,flags=re.M)
                text+='\n本次仅迁移外层目录与素材索引路径；生成清单、提示词、原始验收及制作脚本保留制作时的名称和字节。当前路径以素材索引为准，名称对应见[命名对照](../../PET_NAMES.md)。\n'
            write(p,text)
        p=folder/'source/materials-index.json'
        index=json.loads(rename_text(p.read_text(encoding='utf-8')))
        index['pet_id']=new
        index['name_migration']={'date':plan['date'],'previous_pet_id':old,'display_name':display,'production_records_preserved':True}
        for item in index['retained_materials']:
            file=root/item['path']
            actual=sha(file)
            assert actual==item['sha256'] or file==folder/'source/README.md',str(file)
            item['sha256']=actual
        write(p,json.dumps(index,ensure_ascii=False,indent=2)+'\n')
    # Keep published URLs, historical filenames and release receipts untouched.
    p=root/'README.md';text=rename_text(p.read_text(encoding='utf-8'))
    text=text.replace('nene_victorian lolita',pets[7]['display_name']).replace('nene_classical lolita',pets[8]['display_name'])
    labels=[('初始校服 | 宁宁机器人','学院制服 | 宁宁机器人'),('Brand New Style | 初始舞台服 · 新增','羽饰舞台装 | 蝶饰舞台装'),("Let's enjoy the movie！ | 江戸の町並みに飲まれて · 新增",'田园休闲 | 复古淑女'),('ワンダーステッキ | Victorian Lolita · 新增','马戏团礼装 | 维多利亚洛丽塔·花边洋伞'),('Classical Lolita · 本地新增','古典洛丽塔·红心皇后 · 本地新增')]
    for a,b in labels:text=text.replace(a,b)
    text=text.replace('## 选一位宁宁','当前目录、ID和显示名称已按服饰统一，[查看命名对照](PET_NAMES.md)。已发布v1.7.2及更早附件继续使用原名称；新命名成品目前仅在工作区提供。\n\n## 选一位宁宁',1)
    start=text.index('## 三步安装');end=text.index('<details>',start)
    text=text[:start]+'''## 三步安装

1. 使用当前工作区的新命名目录；下载历史合集时，按包内说明及[命名对照](PET_NAMES.md)确认旧名称。
2. 将所需宠物目录复制到 `~/.codex/pets/`，确保顶层同时有 `pet.json` 和 `spritesheet.webp`。
3. 打开Codex设置 > Pets，刷新并选择对应中文名称，必要时重启应用。

Windows默认目录为 `%USERPROFILE%\\.codex\\pets\\`；自定义 `CODEX_HOME` 时使用其下的 `pets/`。本次仅更名项目，未迁移或切换已安装副本，也未重新发布合集；更名前的安装与发布记录继续作为历史凭据。

'''+text[end:]
    text=text.replace('- 首屏静态图直接提取', '- 本次九套名称已统一，当前清单与加载校验见各套 `preview/rename-validation.json`、`preview/app-loader-validation.json`；历史安装记录不表示新名称已安装。\n- 首屏静态图直接提取',1)
    write(p,text)
    p=root/'.gitattributes';write(p,rename_text(p.read_text(encoding='utf-8')))
    save(audit/'applied-plan.json',plan)
    table='# 宠物名称对照\n\n2026-10-18按服饰风格统一当前项目名称。目录与宠物ID一致，显示名称用于Codex宠物列表。\n\n| 原目录／ID | 当前目录／ID | 当前显示名称 |\n| --- | --- | --- |\n'
    table+='\n'.join(f"| `{p['old_id']}` | `{p['new_id']}` | {p['display_name']} |" for p in pets)
    table+='\n\n- 当前目录和显示名以本表及各套 `pet.json` 为准。两套洛丽塔保留英文ID，展示名分别补充“花边洋伞”和“红心皇后”。\n- 已发布Release、附件、校验和、原安装记录及制作原始清单保留当时名称；本次未安装、切换、上传或发布。历史包按包内说明安装，新命名文件使用当前工作区。\n- 制作原图、实际生成输入、提示词、原验收及制作脚本保留原字节；素材索引已迁移至当前路径。\n- 更名及完整性校验见[验收记录](maintenance/pet-renaming-2026-10-18/verification.json)。\n'
    (root/'PET_NAMES.md').write_bytes(table.encode('utf-8'))
    print('Updated nine manifests, current docs and material-index paths; originals and published files retained.')

elif sys.argv[1] == 'verify':
    before=load(audit/'before.json'); changed=[];same=0
    allowed={'pet.json','validation.json','README.md','source/README.md','source/materials-index.json','preview/README.md','preview/app-loader-validation.json'}
    for rel,digest in before['files'].items():
        p=root/mapped(rel)
        assert p.is_file(),f'Missing after rename: {rel}'
        if sha(p)==digest:same+=1
        else:
            assert Path(rel).relative_to(Path(rel).parts[0]).as_posix() in allowed, f'Unexpected change: {rel}'
            changed.append(p.relative_to(root).as_posix())
    for rel,digest in before['release_files'].items():assert sha(root/rel)==digest,rel
    for name,digest in before['installed_files'].items():assert sha(Path(name))==digest,name
    inventory=[];material_count=0;links=0
    assert {p.parent.name for p in root.glob('*/pet.json')}==set(mapping.values())
    applied=load(audit/'applied-plan.json')
    for pet in applied['pets']:
        folder=root/pet['new_id'];manifest=load(folder/'pet.json')
        assert manifest['id']==folder.name and manifest['displayName']==pet['display_name']
        assert manifest['spriteVersionNumber']==2 and manifest['spritesheetPath']=='spritesheet.webp'
        old_manifest=audit/'before-files'/folder.name/'pet.json'
        old_data=load(old_manifest)
        assert {k:v for k,v in manifest.items() if k not in ['id','displayName']}=={k:v for k,v in old_data.items() if k not in ['id','displayName']}
        with Image.open(folder/'spritesheet.webp') as image,Image.open(folder/'preview/readme-portrait.png') as portrait:
            image.load();assert image.size==(1536,2288) and image.mode=='RGBA' and image.format=='WEBP'
            assert image.crop((0,0,192,208)).tobytes()==portrait.tobytes()
        index=load(folder/'source/materials-index.json')
        assert index['pet_id']==folder.name and index['current_atlas_sha256']==sha(folder/'spritesheet.webp')
        for item in index['retained_materials']:assert sha(root/item['path'])==item['sha256'],item['path'];material_count+=1
        for job in index['jobs']:
            assert sha(root/job['selected_original'])==job['sha256'],job['id']
            for rel in job.get('input_files',[])+job.get('prompt_files',[]):
                assert (root/rel).is_file(),rel
        loader=load(folder/'preview/app-loader-validation.json')
        assert loader['ok'] and loader['id']=='custom:'+folder.name and loader['display_name']==manifest['displayName']
        assert loader['spritesheet_sha256']==sha(folder/'spritesheet.webp')
        report={'ok':True,'date':plan['date'],'previous_id':pet['old_id'],'id':folder.name,'display_name':manifest['displayName'],'previous_display_name':pet['previous_display_name'],'spritesheet_sha256':sha(folder/'spritesheet.webp'),'artwork_and_animation_bytes_unchanged':True,'production_originals_unchanged':True,'material_index_paths_verified':True,'current_manifest_loader_verified':True,'installed_names_migrated':False,'application_ui_verified':False,'published':False}
        save(folder/'preview/rename-validation.json',report);inventory.append(report)
    docs=[root/'README.md',root/'PET_NAMES.md',root/'AGENTS.md']+[root/p['new_id']/r for p in pets for r in ['README.md','preview/README.md','source/README.md']]
    for doc in docs:
        text=doc.read_text(encoding='utf-8')
        assert not re.search(r'<img[^>]+src="[^\"]+\.gif',text,re.I)
        for url in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text)+re.findall(r'(?:href|src)="([^\"]+)"',text):
            if re.match(r'[a-zA-Z]+:',url) or url.startswith('#'):continue
            target=unquote(url.strip('<>').split('#')[0]);links+=1
            if target.endswith('maintenance/pet-renaming-2026-10-18/verification.json'):continue
            assert (doc.parent/target).exists(),(str(doc),url)
    report={'ok':True,'date':plan['date'],'pets':inventory,'files_preserved_byte_for_byte':same,'expected_current_metadata_files_changed':changed,'source_index_materials_verified':material_count,'local_links_checked':links,'published_release_files_unchanged':len(before['release_files']),'installed_files_unchanged':len(before['installed_files']),'no_artwork_regenerated':True,'no_release_created':True,'application_ui_verified':False}
    save(audit/'verification.json',report)
    print(json.dumps({k:v for k,v in report.items() if k not in ['pets','expected_current_metadata_files_changed']},ensure_ascii=False))
else: raise SystemExit('Use snapshot, metadata or verify')
