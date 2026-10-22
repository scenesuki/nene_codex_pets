[← 返回宠物合集](../README.md)

# 宁宁 · 维多利亚洛丽塔 · 花边洋伞

<img src="preview/readme-portrait.png" alt="宁宁 · 维多利亚洛丽塔 · 花边洋伞静态预览" width="144">

**宁宁 · 维多利亚洛丽塔 · 花边洋伞** · ID `nene_victorian_lolita` · 9种动画 · 16个注视方向

- **服饰要素**：藏蓝圆帽与短披肩、青绿色蓬裙、棕色束腰、中筒靴和白手套，配颊侧短卷发；右手持展开的藏蓝条纹花边伞。画框外伞缘按已展示的花纹补全，并适当缩小以完整显示。
- **画风**：Q版日系插画
- **参考卡面**：4星卡「きらびやかな夢の舞台」特训后；服装「スパカリバルーンドレス」。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

导入文件：[pet.json](pet.json) · [spritesheet.webp](spritesheet.webp)。

[下载 v2.0.0 十九套合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/nene_codex_pets-v2.0.0.zip) · [SHA-256 校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/SHA256SUMS.txt)。本套已收录于该版本；历史名称见[命名对照](../PET_NAMES.md)。

## 安装

1. 解压本版合集，将 `nene_victorian_lolita/` 复制至 `~/.codex/pets/`，保留顶层的 `pet.json` 与 `spritesheet.webp`。
2. Windows 默认目录为 `%USERPROFILE%\.codex\pets\nene_victorian_lolita\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_victorian_lolita/`。
3. 在 **Codex 设置 > Pets** 中刷新并选择「宁宁 · 维多利亚洛丽塔 · 花边洋伞」，必要时重启应用。

<details>
<summary>规格与验收</summary>

**验证范围**：文件及预览检查已有记录；Codex 设置识别、桌面浮动显示与应用内动态播放尚未实测。兼容依据和已知限制如下。

- [更名校验](preview/rename-validation.json)记录当前名称及成品哈希；图片、动画和有效制作原素材保持原字节。历史记录保留当时标识，当前名称见[命名对照](../PET_NAMES.md)。

- 原生Codex v2，无损RGBA WebP，1536×2288，8列11行，单格192×208，`spriteVersionNumber: 2`。[应用规格依据](preview/app-contract-verification.json)来自制作时对对应版本应用的只读检查。
- 九状态为待机、左右移动、招手、跳跃、失落、等待回应、思考处理中、审视，帧数6/8/8/4/5/8/6/6/6；后两行从正上方000°开始顺时针每22.5°一个，共16方向。`running`表示站定处理任务，左右移动由两条方向状态承担。
- [当前图集校验](validation.json)通过：尺寸、布局、必需格、透明空格及透明像素隐藏RGB符合要求。[原视觉验收摘要](preview/visual-qa.json)保留最终接受结论。
- [逐方向记录](preview/direction-semantics.json)与[独立盲审汇总](preview/direction-blind-validation.json)保留当前视线的验收依据。已接受的细微限制：135°、157.5°、202.5°、225°、247.5°横向提示较细，顺序复核未见错象限或反转。当前跳跃为8px离地、伞顶起伏12px的小跳。
- [GIF文件检查](preview/preview-files-check.json)已解码全部11个GIF，核对数量、尺寸与时长，总览为1680ms。[加载算法检查](preview/app-loader-validation.json)已核对更名后的工作区清单、图片及路径；未执行应用UI显示测试。
- 静态图为最终待机首帧192×208原始RGBA裁切。实际播放器动态播放及 Codex 应用内显示尚未实测。

</details>

<details>
<summary>参考与制作记录</summary>

- [SEGA发布稿转载](https://www.4gamer.net/games/476/G047609/20211228045/)
- [服装模型资料](https://pjsekai.gamedbs.jp/chara/model3d?c=7&q=%E3%82%B9%E3%83%91%E3%82%AB%E3%83%AA%E3%83%90%E3%83%AB%E3%83%BC%E3%83%B3%E3%83%89%E3%83%AC%E3%82%B9)
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)

服装名为「スパカリバルーンドレス」；模型截图仅补充衣裙与鞋履，短卷发以特训后卡面为准。画框外的展开伞缘按创作方案补全并缩小。

原作角色资料与卡面用于外观和性格依据；转绘、站立姿态和安静眨眼、克制招手、期待回应、思考及审视动作均为创作演绎，不宣称为官方原动画。

角色与动画使用 ImageGen 制作，图集经分格、定位和组装导出。制作原素材不随仓库或安装包分发；安装以本页列出的两个导入文件为准。权利说明见 [NOTICE.md](NOTICE.md)。

</details>
