[← 返回宠物合集](../README.md)

# 草薙宁宁 · 新中式礼装

以四星卡「夢をのせたメロディー」特训后造型为原型。

<img src="preview/readme-portrait.png" alt="草薙宁宁新中式礼装Q版静态预览" width="144">

**显示名「宁宁 · 新中式礼装」** · ID `nene_chinoiserie` · 9种动画 · 16个注视方向

- **服饰要素介绍**：蓝紫斜襟礼装、珠饰与腰侧蝴蝶结、不对称纹样外层、黑色及踝开衩长裙、灰色短袜、黑色搭带皮鞋，配蓝色宝石耳饰与黑色颈饰。
- **画风**：Q版日系插画，紧凑头身与短腿比例；克制表情及轻幅动作属于同人演绎。
- **参考卡面**：4星「夢をのせたメロディー」特训后；对应服装「ディグニファイド・ブリリアンス」。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

最终导入文件：[pet.json](pet.json) 与 [spritesheet.webp](spritesheet.webp)。本套包含在[v1.9.0十套完整合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.9.0/nene_codex_pets-v1.9.0.zip)，下载后用同版[SHA256SUMS.txt](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.9.0/SHA256SUMS.txt)核对校验和。历史附件与旧名称见[命名对照](../PET_NAMES.md)及[GitHub Release](https://github.com/scenesuki/nene_codex_pets/releases)。

## 安装

1. 将 `nene_chinoiserie/` 复制到 `~/.codex/pets/`，保留目录顶层的两个导入文件。
2. Windows默认位置为 `%USERPROFILE%\.codex\pets\nene_chinoiserie\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_chinoiserie/`。
3. 在Codex设置 > Pets中刷新并选择「宁宁 · 新中式礼装」，必要时重启应用。

<details>
<summary>规格与验收</summary>

- Codex桌面原生v2，无损RGBA WebP，1536×2288、8列11行、单格192×208，`spriteVersionNumber: 2`。
- [应用规格依据](preview/app-contract-verification.json)为2026-10-18对本机 `OpenAI.Codex_26.1013.4894.0` 的只读检查。
- 九状态为待机、向右移动、向左移动、招手、小跳、失落、等待回应、专注处理中、审视，帧数6/8/8/4/5/8/6/6/6。
- 后两行从000°正上方起顺时针每22.5°一个，共16个注视方向；正下方保持睁眼与向下视线。左右移动单独绘制，保留服装不对称细节。
- 跳跃采用轻幅小跳，鞋底离地0/4/8/4/0px，见[定位记录](preview/jump-placement.json)。
- 细微限制：向右移动有两帧抬膝稍高；小跳为留出安全边距，人物最大高度188px，其他状态约198px。独立原尺寸复核未发现断肢、破衣或显著缩放突变，详见标准动作验收。
- [图集校验](validation.json)、[标准动作验收](preview/standard-visual-qa.json)、[最终视觉验收](preview/final-visual-qa.json)、[方向盲审](preview/direction-blind-validation.json)、[逐方向语义](preview/direction-semantics.json)及[连续性记录](preview/look-continuity.json)保留实际依据。无方向硬性错误。部分中间角度的视线较细微，详见逐方向语义与盲审记录。
- [加载算法检查](preview/app-loader-validation.json)重放本机实际应用的图片、版本与路径验证函数。2026-10-19已将两个导入文件安装到默认宠物目录，逐字节比对及本机加载校验通过，见[安装记录](installed-validation.json)；未切换当前宠物，应用设置及桌面浮动显示尚未实测。
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

使用内置imagegen绘制基准与各状态，确定性脚本负责分格和组装；有效原素材、实际输入及提示词保存在 `source/`，由 `source/materials-index.json` 记录哈希。本套纳入v1.9.0十套合集；制作时的验收记录保留当时状态，当前安装状态见上方安装记录。权利说明见[NOTICE.md](NOTICE.md)。

</details>
