"""Collect this pet's accepted images, provenance and documentation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
from PIL import Image

run = Path(__file__).resolve().parents[1]
pet = run.parent
root = pet.parent
load = lambda p: json.loads(p.read_text(encoding='utf-8'))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

assert load(run/'qa/final-visual-qa.json')['visual_qa'] == 'pass'
assert load(run/'final/validation-extended.json')['ok']
assert load(run/'qa/direction-blind-validation.json')['ok']
semantics = load(run/'qa/direction-semantics.json')
assert semantics['ok'] and all(d['status'] != 'fail' for d in semantics['directions'])
preview = pet/'preview'
preview.mkdir(exist_ok=True)
shutil.copy2(run/'final/spritesheet-extended.webp', pet/'spritesheet.webp')
shutil.copy2(run/'final/validation-extended.json', pet/'validation.json')
save(pet/'pet.json', {'id':pet.name, 'displayName':'宁宁 · 新中式礼装', 'description':'草薙宁宁「夢をのせたメロディー」特训后新中式礼装，Q版日系插画。', 'spriteVersionNumber':2, 'spritesheetPath':'spritesheet.webp'})
for name in ['standard-visual-qa.json','final-visual-qa.json','direction-semantics.json','direction-blind-validation.json','direction-blind-verdicts.json','look-continuity.json','chroma-despill-extended.json','jump-placement.json','blind-review-resolution.json']:
    if (run/'qa'/name).exists():
        shutil.copy2(run/'qa'/name, preview/name)
shutil.copy2(run/'references/app-contract-verification.json', preview/'app-contract-verification.json')
with Image.open(pet/'spritesheet.webp') as atlas:
    atlas.crop((0,0,192,208)).save(preview/'readme-portrait.png')
shutil.copy2(root/'nene_classical_lolita/NOTICE.md', pet/'NOTICE.md')

materials = {}
jobs = []
manifest = load(run/'imagegen-jobs.json')
for job in manifest['jobs']:
    assert job['status'] == 'complete', job['id']
    original = run/job['output_path']
    assert sha(original) == job['source_sha256']
    inputs = []
    for item in job.get('input_images', []):
        p = run/item['path']
        assert p.exists(), p
        materials[p] = 'actual generation input'
        inputs.append(str(p.relative_to(root)))
    prompts = []
    for key in ['prompt_file','executed_prompt_file','look_mechanics_file']:
        if job.get(key):
            p = run/job[key]
            assert p.exists(), p
            materials[p] = 'production prompt or look mechanics'
            prompts.append(str(p.relative_to(root)))
    for attempt in job.get('previous_attempts', []):
        if attempt.get('used_as_input'):
            materials[run/attempt['preserved_output']] = 'preserved actual edit input'
    materials[original] = 'selected original generated image'
    if job.get('input_provenance'):
        materials[run/job['input_provenance']] = 'actual generation input audit'
    jobs.append({'id':job['id'], 'selected_original':str(original.relative_to(root)), 'sha256':sha(original), 'input_files':inputs, 'prompt_files':prompts})
for folder in ['references','prompts']:
    for p in (run/folder).rglob('*'):
        if p.is_file():
            materials.setdefault(p, 'reference or prompt record')
for name in ['imagegen-jobs.json','pet_request.json']:
    materials[run/name] = 'generation manifest'
for p in (run/'qa').iterdir():
    if p.suffix in ['.py','.mjs']:
        materials[p] = 'deterministic processing or verification script'
save(run/'materials-index.json', {'pet_id':pet.name, 'current_atlas_sha256':sha(pet/'spritesheet.webp'), 'jobs':jobs, 'retained_materials':[{'path':str(p.relative_to(root)), 'sha256':sha(p), 'roles':[role]} for p,role in sorted(materials.items())], 'note':'Selected originals and actual inputs are retained byte for byte. Installation uses only the pet directory top-level files.'})
(run/'README.md').write_text('''# nene_chinoiserie · 制作原素材

- [素材索引](materials-index.json)记录选用原始生成图、实际输入、提示词、用途和SHA-256。
- `decoded/`保留选用原图；`references/`保留完整卡面、原色全身模型及实际输入；`prompts/`保留制作提示词。
- `frames/`、`final/`、`qa/`保留本套分格、组装及检查记录；安装入口为宠物目录顶层文件。
- 人物画面通过内置imagegen生成；脚本只负责分格、定位、组装和一次边缘处理。未借用其他宠物的角色画面。
- 造型核对见[研究记录](references/research.md)，最终状态见[本套说明](../README.md)。
''', encoding='utf-8')
warnings = [d for d in semantics['directions'] if d['status']=='warning']
warning_text = '无方向硬性错误。' + ('部分中间角度的视线较细微，详见逐方向语义与盲审记录。' if warnings else '十六方向通过语义检查。')
(pet/'README.md').write_text(f'''[← 返回宠物合集](../README.md)

# 草薙宁宁 · 新中式礼装

以四星卡「夢をのせたメロディー」特训后造型为原型。

<img src="preview/readme-portrait.png" alt="草薙宁宁新中式礼装Q版静态预览" width="144">

**显示名「宁宁 · 新中式礼装」** · ID `nene_chinoiserie` · 9种动画 · 16个注视方向

- **服饰要素介绍**：蓝紫斜襟礼装、珠饰与腰侧蝴蝶结、不对称纹样外层、黑色及踝开衩长裙、灰色短袜、黑色搭带皮鞋，配蓝色宝石耳饰与黑色颈饰。
- **画风**：Q版日系插画，紧凑头身与短腿比例；克制表情及轻幅动作属于同人演绎。
- **参考卡面**：4星「夢をのせたメロディー」特训后；对应服装「ディグニファイド・ブリリアンス」。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

最终导入文件：[pet.json](pet.json) 与 [spritesheet.webp](spritesheet.webp)。本套已在本地制作，尚未安装、上传或发布；已发布v1.8.0仍为此前九套合集，不包含本套。

## 安装

1. 将 `nene_chinoiserie/` 复制到 `~/.codex/pets/`，保留目录顶层的两个导入文件。
2. Windows默认位置为 `%USERPROFILE%\\.codex\\pets\\nene_chinoiserie\\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_chinoiserie/`。
3. 在Codex设置 > Pets中刷新并选择「宁宁 · 新中式礼装」，必要时重启应用。

<details>
<summary>规格与验收</summary>

- Codex桌面原生v2，无损RGBA WebP，1536×2288、8列11行、单格192×208，`spriteVersionNumber: 2`。
- [应用规格依据](preview/app-contract-verification.json)为2026-10-18对本机 `OpenAI.Codex_26.1013.4894.0` 的只读检查。
- 九状态为待机、向右移动、向左移动、招手、小跳、失落、等待回应、专注处理中、审视，帧数6/8/8/4/5/8/6/6/6。
- 后两行从000°正上方起顺时针每22.5°一个，共16个注视方向；正下方保持睁眼与向下视线。左右移动单独绘制，保留服装不对称细节。
- 跳跃采用轻幅小跳，鞋底离地0/4/8/4/0px，见[定位记录](preview/jump-placement.json)。
- 细微限制：向右移动有两帧抬膝稍高；小跳为留出安全边距，人物最大高度188px，其他状态约198px。独立原尺寸复核未发现断肢、破衣或显著缩放突变，详见标准动作验收。
- [图集校验](validation.json)、[标准动作验收](preview/standard-visual-qa.json)、[最终视觉验收](preview/final-visual-qa.json)、[方向盲审](preview/direction-blind-validation.json)、[逐方向语义](preview/direction-semantics.json)及[连续性记录](preview/look-continuity.json)保留实际依据。{warning_text}
- [加载算法检查](preview/app-loader-validation.json)重放本机实际应用的图片、版本与路径验证函数；未安装、切换或测试应用设置及桌面浮动显示。
- [预览文件检查](preview/preview-files-check.json)逐帧解码11份GIF。首屏静态图逐像素提取最终图集待机首帧。README窄屏显示与实际播放器交互尚未实测。

</details>

<details>
<summary>参考与制作记录</summary>

- [世嘉官方公告：卡面与服装对应](https://prtimes.jp/main/html/rd/p/000006017.000005397.html)
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)
- [完整特训后卡面素材镜像](https://storage.sekai.best/sekai-jp-assets/character/member/res015_no038/card_after_training.png)
- [原色全身服装模型](https://appmedia.jp/pjsekai/78185441)与[另一角度核对](https://game8.jp/pjsekai/641360)
- [游戏卡面主数据镜像](https://github.com/Sekai-World/sekai-master-db-diff/blob/main/cards.json)

按标题匹配的游戏卡ID为1005，角色ID15，资源名 `res015_no038`。完整卡面用于发型、服色、袖口和配饰；同套原色全身模型用于裙摆、开衩、短袜袜口和鞋履。下半身要素有图像依据，无自行补全；模型默认发型不替代卡面发型。

“新中式礼装”是依据斜襟与不对称叠穿作出的项目命名，并非官方服装分类。官方设定提供宁宁喜爱游戏与音乐剧、认真追逐舞台梦想的性格依据；轻微招呼、思考、等待回应和失落恢复为创作演绎。未纳入卡面场景、花盆、窗饰或鸟。

使用内置imagegen绘制基准与各状态，确定性脚本负责分格和组装；有效原素材、实际输入及提示词保存在 `source/`，由 `source/materials-index.json` 记录哈希。未安装、上传或创建新Release。权利说明见[NOTICE.md](NOTICE.md)。

</details>
''', encoding='utf-8')
states = ['idle','running-right','running-left','waving','jumping','failed','waiting','running','review']
labels = ['待机','向右移动','向左移动','招手','小跳','失落','等待回应','专注处理中','审视']
(preview/'README.md').write_text('[← 返回本套说明](../README.md)\n\n# 宁宁 · 新中式礼装 · 动画预览\n\n[九状态总览](animation-overview.gif) · [十六方向循环](look-directions.gif) · [静态全帧](contact-sheet.png) · [方向检查图](look-directions.png)\n\n| 动作 | 预览 |\n| --- | --- |\n'+'\n'.join(f'| {label} | [查看动画]({state}.gif) |' for state,label in zip(states,labels))+'\n\n全部预览来自本套最终图集。\n', encoding='utf-8')
(run/'progress.md').write_text('# 制作进度\n\n- [x] 准备与服饰核对\n- [x] 角色基准\n- [x] 九状态与十六方向\n- [x] 组装、验收与工作区交付\n\n尚未安装、上传或发布。\n', encoding='utf-8')
save(run/'qa/run-summary.json', {'ok':True,'completed_at':datetime.now(timezone.utc).isoformat(),'pet_id':pet.name,'display_name':'宁宁 · 新中式礼装','spritesheet_sha256':sha(pet/'spritesheet.webp'),'source_index':'source/materials-index.json','direction_warning_angles':[d['angle'] for d in warnings],'installed':False,'uploaded':False,'published':False})
print(json.dumps({'pet_id':pet.name,'material_count':len(materials),'selected_jobs':len(jobs)},ensure_ascii=False))
