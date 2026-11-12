[← 返回宠物合集](../README.md)

# 宁宁 · 紫夜哥特

<img src="preview/readme-portrait.png" alt="草薙宁宁紫夜哥特Q版静态预览" width="144">

**宁宁 · 紫夜哥特** · ID `nene_gothic_couture` · 9种动画 · 16个注视方向

> **视线跟随提示（2026-11-06）**：当前已核验的 Codex 官方版本尚未正常支持宠物跟随日常鼠标移动。本项目已提供 16 个注视方向素材，但不代表实际使用时会自动跟随鼠标；该问题位于应用端，并非素材缺失。详见[官方仓库反馈 #33224](https://github.com/openai/codex/issues/33224)。

- **服饰要素**：紫黑荷叶发箍与玫瑰结饰、灰绿长发与系带前发；黑色领饰与手套、紫色泡肩长袖收腰上衣、细腰带与背后蝴蝶结；藏蓝竖纹中央裙片、紫色卷纹侧片、星形垂链、灰色下裙边和黑蕾丝；灰色长袜与紫色T字系带低跟礼鞋。
- **画风**：Q版日系插画，紧凑头身、短腿比例与轻幅动作。
- **参考卡面**：4星「ステップに想いをのせて」特训后；原色衣装「シェリール・オートクチュール」。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

导入文件：[pet.json](pet.json) · [spritesheet.webp](spritesheet.webp)。

2026-11-12 整套重绘。以特训后卡面的温柔神态和原色衣装模型为依据，重画角色、九种动作和十六方向注视。站姿恢复睁眼浅笑，收腰与钟形裙层次更清楚。等待用伸掌邀请，专注用指尖轻点手心，审视用扶下巴偏头区分。 [重绘记录](preview/redesign-validation.json)

根据用户反馈，左右走路的全部帧已重绘为小幅步态，双脚靠近身体，脚跟轻抬，手臂在身侧轻摆。当前成品待用户确认。 [步态修订校验](preview/quiet-walk-validation.json)

[下载 v2.0.1 十九套合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.1/nene_codex_pets-v2.0.1.zip) · [SHA-256 校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.1/SHA256SUMS.txt)。

2026-11-12 已核对本机文件与云端图集均为当前成品，云端保留一条。 [当前安装记录](preview/current-installation-validation.json)

## 安装

1. 将 `nene_gothic_couture/` 复制至 `~/.codex/pets/`，保留顶层两个导入文件。
2. Windows 默认目录为 `%USERPROFILE%\.codex\pets\nene_gothic_couture\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_gothic_couture/`。
3. 在 **Codex 设置 > Pets** 中刷新并选择「宁宁 · 紫夜哥特」，必要时重启应用。

<details>
<summary>规格与验收</summary>

- 重绘校验覆盖全部73个必需格及额外待机参考格。小幅步态重绘后已复核16个替换格、原尺寸留边和12个GIF。此前文件及安装记录对应各自版本。 [当前校验](preview/quiet-walk-validation.json)

**验证范围**：文件及预览检查已有记录；Codex 设置识别、桌面浮动显示与应用内动态播放尚未实测。兼容依据和已知限制如下。

- Codex原生v2，无损RGBA WebP，1536×2288、8列11行、单格192×208，`spriteVersionNumber: 2`。
- [应用规格依据](preview/app-contract-verification.json)：2026-10-21只读核对Codex 26.1016.6573.0实际安装包的加载与渲染代码。
- 九状态：待机、向右移动、向左移动、招手、小跳、失落、等待回应、专注处理中、审视；帧数6/8/8/4/5/8/6/6/6。
- 按原始素材组等比缩放，站姿鞋底定位在同一高度。左右移动各有四个步态姿势，重复组成八格。小跳首尾复用新待机首帧，最高点鞋底上移8px。 [跳跃衔接](preview/jump-transition.gif)
- 注视从000°正上方开始，每22.5°顺时针变化，090°屏幕右、180°下、270°屏幕左。正上方单独重绘，正下方保持睁眼。部分相邻方向差异较细，正上方抬眼幅度较明显，衔接观感待确认。 [方向检查图](preview/look-directions.png) · [应用映射依据](preview/current-look-runtime-verification.json)
- 文件校验与原尺寸静态序列检查已完成。左右移动的循环节奏和注视切换待应用内验收。 [图集校验](validation.json)
- 重绘前记录包括[左移修订](preview/refinement-validation.json)、[画风修订](preview/style-fix-validation.json)、[原视觉验收](preview/final-visual-qa.json)和[原加载检查](preview/app-loader-validation.json)。

- 制作时的 [README 排版检查](preview/readme-layout-check.json)记录桌面与窄屏检查结果。

</details>

<details>
<summary>参考与制作记录</summary>

- [SEGA官方公告：卡面与衣装对应](https://prtimes.jp/main/html/rd/p/000006449.000005397.html)
- [原色全身模型与头饰](https://game8.jp/pjsekai/684202)
- [高清完整特训后卡面](https://pjsekai.gamedbs.jp/chara/show/7/1136)
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)

完整原色全身模型已显示裙摆、灰袜和紫色T字系带礼鞋，无需猜测下半身；卡面补充头饰、领饰、裙片与链饰细节，未采用场景光照造成的粉色偏色。卡面中的花束与发光蝴蝶属于场景元素，本套未作为固定持物。

「紫夜哥特」是本项目按服饰特点起的名称，非官方译名。官方资料中的音乐剧志向、歌唱与游戏爱好及面对人群的拘谨，转化为安静待机、含蓄招手、轻步、认真思考与审视；这些动作属于创作演绎。

制作流程复用了猫耳旅装的处理脚本并按本套适配，未借用其他宠物的角色图片。角色与动画使用 ImageGen 制作，图集经分格、定位和组装导出。制作原素材不随仓库或安装包分发；安装以本页列出的两个导入文件为准。权利说明见 [NOTICE.md](NOTICE.md)。

</details>
