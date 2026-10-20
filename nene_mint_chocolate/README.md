[← 返回宠物合集](../README.md)

# 宁宁 · 薄荷巧克力

<img src="preview/readme-portrait.png" alt="宁宁薄荷巧克力Q版静态预览" width="144">

**宁宁 · 薄荷巧克力** · ID `nene_mint_chocolate` · 9种动画 · 16个注视方向

- **服饰要素介绍**：灰绿短波波头、巧克力褶花与薄荷绿发结，方领褐色花纹长袖、束腰、高腰格纹短裤、单侧蕾丝腿环与薄荷绿系带棕色及膝靴。
- **画风**：Q版日系插画，紧凑头身与短腿比例，采用含蓄表情和轻幅动作。
- **参考卡面**：4星「相手をイメージして」特训后；对应衣装「メルティペパーミント」。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

最终导入文件：[pet.json](pet.json) 与 [spritesheet.webp](spritesheet.webp)。本套已纳入[v1.10.0十三套完整合集](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.10.0)。

## 安装

1. 将 `nene_mint_chocolate/` 复制至 `~/.codex/pets/`，保留顶层两个导入文件。
2. Windows默认目录为 `%USERPROFILE%\.codex\pets\nene_mint_chocolate\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_mint_chocolate/`。
3. 在Codex设置 > Pets中刷新并选择「宁宁 · 薄荷巧克力」，必要时重启应用。

<details>
<summary>规格与验收</summary>

- Codex原生v2，无损RGBA WebP，1536×2288、8列11行、单格192×208，`spriteVersionNumber: 2`。
- [应用规格依据](preview/app-contract-verification.json)为2026-10-19只读核对本机 `OpenAI.Codex_26.1013.4894.0` 的结果。
- 九状态：待机、向右移动、向左移动、招手、小跳、失落、等待回应、专注处理中、审视；帧数6/8/8/4/5/8/6/6/6。左右移动分别绘制，保持单侧头饰与腿环的位置。
- 移动采用低幅交替行走；小跳鞋底离地0/4/8/4/0px，见[定位记录](preview/jump-placement.json)。为留足小跳边距，该状态最大人物高度188px，其他状态约198px；独立原尺寸检查将约5%的尺度差记录为轻微限制，未发现明显突跳。
- 后两行从000°正上方开始，每22.5°顺时针一个，共16方向；180°低头保持睁眼。部分中间方向的视线较细微，已结合带标签顺序与连续性复核接受，详见方向记录。
- [图集校验](validation.json)、[标准动作验收](preview/standard-visual-qa.json)、[最终视觉验收](preview/final-visual-qa.json)、[方向盲审](preview/direction-blind-validation.json)、[逐方向语义](preview/direction-semantics.json)与[连续性](preview/look-continuity.json)记录实际验收与细微限制。
- [加载算法检查](preview/app-loader-validation.json)重放本机实际应用的图片、版本及路径验证函数；[预览文件检查](preview/preview-files-check.json)逐帧解码全部GIF，静态小图逐像素取自最终待机首帧。
- 尚未安装、切换或进行应用设置识别、桌面浮动显示测试；未测试README窄屏交互与实际播放器动态播放。

</details>

<details>
<summary>参考与制作记录</summary>

- [SEGA官方公告：卡面与衣装对应](https://prtimes.jp/main/html/rd/p/000004959.000005397.html)
- [特训后卡面与原色全身模型](https://game8.jp/pjsekai/594154)
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)

完整原色试穿模型已展示短裤、单侧腿环、长靴系带、鞋尖及靴底，关键下半身要素齐全；以模型原色校正卡面暖光。短发与头饰以特训后卡面为准。未显示的背面不新增装饰，本套不含纯背面动作。

“薄荷巧克力”为依据巧克力棕与薄荷绿配色作出的项目命名，并非官方衣装名的固定译法。官方资料提供宁宁喜爱游戏、音乐剧及不擅长人多场所等性格依据；含蓄招手、专注思考、失落恢复与小跳属于桌面动画演绎。未纳入卡面抱枕、甜点、床椅或场景。

使用内置imagegen绘制；有效原素材、实际输入、提示词及索引仅在本地 `source/` 保留。制作完成时的验收记录保留原状态；当前发布版本为v1.10.0。权利说明见[NOTICE.md](NOTICE.md)。

</details>
