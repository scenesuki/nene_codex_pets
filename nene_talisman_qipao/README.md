[← 返回宠物合集](../README.md)

# 宁宁 · 符饰旗袍

<img src="preview/readme-portrait.png" alt="草薙宁宁符饰旗袍Q版预览" width="144">

**宁宁 · 符饰旗袍** · ID `nene_talisman_qipao` · 9种动画 · 16个注视方向

- **服饰要素**：灰绿双丸子头、细辫与短卷发，深蓝金边发饰，符饰项链；玫红盘扣长上衣配浅绿滚边、白色侧拼片、深蓝领片及紫色荷叶边喇叭袖；藏蓝金边短裤、单侧腿环、紫色鞋帮与金底系带圆头鞋。
- **画风**：Q版日系插画，紧凑头身、短腿与轻幅动作。
- **参考卡面**：4星「口には出せないこの気持ち」特训后；原色衣装「躍るは宴者」。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

导入文件：[pet.json](pet.json) · [spritesheet.webp](spritesheet.webp)。

[下载 v2.0.0 十九套合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/nene_codex_pets-v2.0.0.zip) · [SHA-256 校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/SHA256SUMS.txt)。本套已收录于该版本；历史名称见[命名对照](../PET_NAMES.md)。

## 安装

1. 将 `nene_talisman_qipao/` 复制至 `~/.codex/pets/`，保留顶层两个导入文件。
2. Windows 默认路径为 `%USERPROFILE%\.codex\pets\nene_talisman_qipao\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_talisman_qipao/`。
3. 在 **Codex 设置 > Pets** 中刷新并选择「宁宁 · 符饰旗袍」，必要时重启应用。

<details>
<summary>规格与验收</summary>

**验证范围**：文件及预览检查已有记录；Codex 设置识别、桌面浮动显示与应用内动态播放尚未实测。兼容依据和已知限制如下。

- Codex原生v2，无损RGBA WebP，1536×2288、8列11行、单格192×208，`spriteVersionNumber: 2`。
- [应用规格依据](preview/app-contract-verification.json)：2026-10-21只读核对 `OpenAI.Codex_26.1013.4894.0` 实际安装包。
- 九状态：待机、向右移动、向左移动、招手、小跳、失落、等待回应、专注处理中、审视；帧数6/8/8/4/5/8/6/6/6。
- 各动作从原始生成图一次裁切缩放，每行统一比例，最大人物高度190px、落地基线203px；小跳离地0/4/8/4/0px。见[动作定位记录](preview/standard-registration.json)。左右移动分别生成，保留白色侧拼片、袖口与单侧腿环，不使用镜像替代。
- 两行注视从000°正上方开始，每22.5°顺时针变化；090°屏幕右、180°下、270°屏幕左。部分中间方向的斜向分量细微，已通过带标签循环复核，具体限制见最终视觉和方向记录。
- [图集校验](validation.json)、[标准动作验收](preview/standard-visual-qa.json)、[最终视觉验收](preview/final-visual-qa.json)、[方向盲审](preview/direction-blind-validation.json)、[逐方向语义](preview/direction-semantics.json)与[连续性](preview/look-continuity.json)记录实际检查结果。
- 已接受的细微限制：方向第10行的头发轮廓比第9行高约8–10px，两个跨行接缝可见，但身体与脚位稳定；022.5与045的角度差异偏弱，均保持正确右上象限；315与337.5的水平差异较弱，向上程度仍有递进；waiting末首歪头方向反转，属于局部循环接缝；向右移动比向左移动更正面，但目光方向及相反靴子交替足以辨认；少量手指、袖褶和配饰细节存在帧间变化。
- [加载算法检查](preview/app-loader-validation.json)重放对应版本应用的图片、版本与路径验证函数；[预览文件检查](preview/preview-files-check.json)逐帧解码全部GIF，静态小图逐像素来自最终待机首帧。
- [README排版检查](preview/readme-layout-check.json)：首页与本页在1280px桌面和390px窄屏下的静态图、页面宽度及折叠交互已有验证记录；尚未核对GitHub线上渲染。

</details>

<details>
<summary>参考与制作记录</summary>

- [卡面、对应衣装与原色全身模型](https://game8.jp/pjsekai/775312)：资料站展示的游戏原图及模型，核对完整着装。
- [特训后卡面原图](https://img.game8.jp/12435827/7489248c38558c85aaabd5a86fc9900f.webp/original)
- [原色全身服装图](https://img.game8.jp/12435830/13bc946950e981c61a2410072a2dd5dc.webp/original)
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)

卡面与完整模型共同确认发髻、细辫、领片、符饰、盘扣、喇叭袖、短裤、腿环、踝部鞋帮及鞋履；下半身已有可靠全身图，无需自行设计。保留特训后双丸子发型，发色按模型校正卡面彩光。常态为紫色睁眼，眨眼只作为动画表情。卡面幽灵、舞台布景、漂浮光效不纳入宠物。

「符饰旗袍」是本项目按服饰特点起的名称，非官方固定译名。官方角色资料中的游戏、音乐剧喜好及宁宁面对人群的拘谨，转化为安静待机、含蓄招手、短暂懊恼后恢复、认真思考和审视等动画；这些动作属于创作演绎。符纸保留不可读的红色装饰纹样。

角色与动画使用 ImageGen 制作，图集经分格、定位和组装导出。制作原素材不随仓库或安装包分发；安装以本页列出的两个导入文件为准。权利说明见 [NOTICE.md](NOTICE.md)。

</details>
