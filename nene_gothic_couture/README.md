[← 返回宠物合集](../README.md)

# 宁宁 · 紫夜哥特

<img src="preview/readme-portrait.png" alt="草薙宁宁紫夜哥特Q版静态预览" width="144">

**宁宁 · 紫夜哥特** · ID `nene_gothic_couture` · 9种动画 · 16个注视方向

- **服饰要素**：紫黑荷叶发箍与玫瑰结饰、灰绿长发与系带前发；黑色领饰与手套、紫色泡肩长袖收腰上衣、细腰带与背后蝴蝶结；藏蓝竖纹中央裙片、紫色卷纹侧片、星形垂链、灰色下裙边和黑蕾丝；灰色长袜与紫色T字系带低跟礼鞋。
- **画风**：Q版日系插画，紧凑头身、短腿比例与轻幅动作。
- **参考卡面**：4星「ステップに想いをのせて」特训后；原色衣装「シェリール・オートクチュール」。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

导入文件：[pet.json](pet.json) · [spritesheet.webp](spritesheet.webp)。

[下载 v2.0.0 十九套合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/nene_codex_pets-v2.0.0.zip) · [SHA-256 校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/SHA256SUMS.txt)。本套已收录于该版本；历史名称见[命名对照](../PET_NAMES.md)。

## 安装

1. 将 `nene_gothic_couture/` 复制至 `~/.codex/pets/`，保留顶层两个导入文件。
2. Windows 默认目录为 `%USERPROFILE%\.codex\pets\nene_gothic_couture\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_gothic_couture/`。
3. 在 **Codex 设置 > Pets** 中刷新并选择「宁宁 · 紫夜哥特」，必要时重启应用。

<details>
<summary>规格与验收</summary>

**验证范围**：文件及预览检查已有记录；Codex 设置识别、桌面浮动显示与应用内动态播放尚未实测。兼容依据和已知限制如下。

- Codex原生v2，无损RGBA WebP，1536×2288、8列11行、单格192×208，`spriteVersionNumber: 2`。
- [应用规格依据](preview/app-contract-verification.json)：2026-10-21只读核对Codex 26.1016.6573.0实际安装包的加载与渲染代码。
- 九状态：待机、向右移动、向左移动、招手、小跳、失落、等待回应、专注处理中、审视；帧数6/8/8/4/5/8/6/6/6。
- 从各行原始生成图裁切，同行统一缩放、稳定脚底基线；小跳离地0/4/8/4/0px，见[动作定位记录](preview/standard-registration.json)。左右移动分别生成，保留服饰细节与原有位置。
- 注视从000°正上方开始，每22.5°顺时针变化；090°屏幕右、180°下、270°屏幕左，见[实际映射依据](preview/current-look-runtime-verification.json)。四基准方向、两行逐方向和跨行连续性均经检查。
- 注视定位直接使用待机首帧几何，保持脚底基线一致，见[配准说明](preview/registration-strategy-resolution.json)。
- [图集校验](validation.json)、[标准动作验收](preview/standard-visual-qa.json)、[最终视觉验收](preview/final-visual-qa.json)、[方向盲审](preview/direction-blind-validation.json)、[逐方向语义](preview/direction-semantics.json)与[连续性](preview/look-continuity.json)记录实际检查结果。
- 已接受的细微限制：左移动作为偏侧碎步，实际A／双平／B／双平／B／双平／B／双平，不能描述为均匀交替跑步；接近正上或正下的对角方向水平分量稍强，部分相邻方向变化细微，但全部四正向与对角象限正确；337.5至000的头部转正稍明显，完整循环未出现重大定位或尺度突跳；专注与审视都采用克制站姿，依靠手位和低头区分，实际尺寸下差异较含蓄；细小花边、发丝和链饰在不同姿态略有变化，整体造型与人物比例一致。
- [加载算法检查](preview/app-loader-validation.json)重放当前应用实际图片、版本及路径验证函数；[预览文件检查](preview/preview-files-check.json)逐帧解码全部GIF，静态小图逐像素来自待机首帧。

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
