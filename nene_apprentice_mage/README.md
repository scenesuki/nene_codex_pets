[← 返回宠物合集](../README.md)

# 宁宁 · 见习魔导师

<img src="preview/readme-portrait.png" alt="草薙宁宁见习魔导师静态预览" width="144">

**宁宁 · 见习魔导师** · ID `nene_apprentice_mage` · 9种状态 · 16个注视方向

- **服饰要素介绍**：蓝青尖顶宽檐帽、金边外套与黄色袖口，白色百褶短裙、黑色胸前结、棕色斜挎药剂带，黑口白长袜与棕色系带短靴。
- **画风**：Q版日系插画，约3头身，紧凑身体与短腿，轻幅动作。
- **参考卡面**：4星「悲しみも全部」特训后；衣装「見習い魔導士のワンピース」。

## 动画与下载

[九状态动画总览](preview/animation-overview.gif) · [十六方向循环](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

导入文件：[pet.json](pet.json) · [spritesheet.webp](spritesheet.webp)。

[下载 v2.0.0 十九套合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/nene_codex_pets-v2.0.0.zip) · [SHA-256 校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/SHA256SUMS.txt)。本套已收录于该版本；历史名称见[命名对照](../PET_NAMES.md)。

## 安装

1. 将 `nene_apprentice_mage/` 复制到 `~/.codex/pets/`，保留顶层两个导入文件。
2. Windows默认目录为 `%USERPROFILE%\.codex\pets\nene_apprentice_mage\`；自定义 `CODEX_HOME` 时使用其下 `pets/nene_apprentice_mage/`。
3. 在设置的Pets中刷新并选择；当前应用若使用云端宠物库，还需要通过宠物上传流程加入列表。制作完成不代表已经安装。

<details>
<summary>规格与验收</summary>

- 原生v2，无损RGBA WebP，1536×2288、8列11行、192×208单格，`spriteVersionNumber: 2`。
- [规格依据](preview/app-contract-verification.json)记录 Codex 26.1016.8120.0 应用代码及图集格式的检查结果；本套已通过[原生加载校验](preview/app-loader-validation.json)。加载校验不等同于应用内显示验证。
- 九状态：待机、向右慢走、向左慢走、招手、轻跳、失落、等待回应、专注检查、审视；帧数6/8/8/4/5/8/6/6/6。两向步态分别生成以保留衣装不对称细节。
- 动作统一单行缩放、脚底基线与轻跳定位，见[定位记录](preview/standard-registration.json)；人物像素仅做裁切、一次缩放与组装，没有程序绘制角色。
- 注视000°为上，090°为屏幕右，180°为下，270°为屏幕左；眼睑、眼神与头颈共同表现，固定双脚与药剂带，检查16方向及跨行循环。
- [图集校验](validation.json)、[标准动作](preview/standard-visual-qa.json)、[最终视觉](preview/final-visual-qa.json)、[方向语义](preview/direction-semantics.json)、[方向盲审](preview/direction-blind-validation.json)及[连续性](preview/look-continuity.json)记录实际结果。
- 已接受的细微限制：左向移动的过渡帧后膝较弯，略带Q版夸张。；部分右上仰角接近，112.5°的向下分量在盲审中不够明显；按有标注循环复核后接受。；个别注视转折的头帽变化幅度略不均匀，未发现重大衔接或定位问题。
- 应用内实际选择、列表渲染与桌面浮动显示尚未实测。

</details>

<details>
<summary>参考与制作记录</summary>

- [卡面、原色全身模型及配饰](https://game8.jp/pjsekai/546568)
- [2023-08-21卡池报道：卡面与衣装对应](https://gameo.jp/pjsekai/15817)
- [卡面数据库条目](https://pjsk.moe/ja-jp/cards/701/)
- [官方草薙宁宁角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)

原色全身模型显示完整裙摆、白色长袜与棕色短靴，因此下半身均有视觉依据；没有把特训后卡面的暖色场景光当作服装原色。独立配饰资料未作为任意新增饰品，固定造型以卡面和原色模型为准。没有添加魔法书、手杖、其他角色或场景光效。

「见习魔导师」为本项目按服装特点命名。官方资料中的音乐剧志向、歌唱特长、认真和对人群的拘谨，被创作演绎为安静待机、含蓄招手、轻步、仔细检查已有药剂带、询问与审视；这些动画并非官方新增技能设定。

人物画面由 ImageGen 生成；处理脚本复用自[紫夜哥特](../nene_gothic_couture/README.md)，仅修改本套副本的色键和流程配置，未借用其他宠物的人物画面。制作原素材不随仓库或安装包分发。权利说明见 [NOTICE.md](NOTICE.md)。

</details>
