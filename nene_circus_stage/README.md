[← 返回宠物合集](../README.md)

# 宁宁 · 马戏团礼装

<img src="preview/readme-portrait.png" alt="宁宁 · 马戏团礼装静态预览" width="144">

**宁宁 · 马戏团礼装** · ID `nene_circus_stage` · 9种动画 · 16个注视方向

> **视线跟随提示（2026-11-06）**：当前已核验的 Codex 官方版本尚未正常支持宠物跟随日常鼠标移动。本项目已提供 16 个注视方向素材，但不代表实际使用时会自动跟随鼠标；该问题位于应用端，并非素材缺失。详见[官方仓库反馈 #33224](https://github.com/openai/codex/issues/33224)。

- **服饰要素**：红色短外套、黑蓝金条纹膝上短裙、红金裙边与红色小腿袜，膝盖露出；鞋履带红色拼片及金色踝蝴蝶结，裸手持金色槽纹杖头的黑色手杖。
- **画风**：Q版日系插画
- **参考卡面**：2星卡「ワンダーステッキ」。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

导入文件：[pet.json](pet.json) · [spritesheet.webp](spritesheet.webp)。

2026-11-06 连续优化：跳跃中间帧统一浅发色和线条，自由手收回腰侧以连接待机姿态，保持露膝红袜及手杖持握。 [本轮校验](preview/refinement-validation.json)。工作区成品已更新，待用户验收；该轮修订晚于已发布合集。此前跳跃、安装及更名校验为历史记录，以本轮成品哈希为准。

2026-11-06 跳跃衔接修订已更新至工作区成品，待用户验收：[待机→跳跃→待机](preview/jump-transition.gif)。v2.0.0 下载仍为修订前版本。

[下载 v2.0.1 十九套合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.1/nene_codex_pets-v2.0.1.zip) · [SHA-256 校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.1/SHA256SUMS.txt)。

2026-11-12 已核对本机文件与云端图集均为当前成品，云端保留一条。 [当前安装记录](preview/current-installation-validation.json)

## 安装

1. 解压本版合集，将 `nene_circus_stage/` 复制至 `~/.codex/pets/`，保留顶层的 `pet.json` 与 `spritesheet.webp`。
2. Windows 默认目录为 `%USERPROFILE%\.codex\pets\nene_circus_stage\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_circus_stage/`。
3. 在 **Codex 设置 > Pets** 中刷新并选择「宁宁 · 马戏团礼装」，必要时重启应用。

<details>
<summary>规格与验收</summary>

- 2026-11-07–08画风与精细度修订：跳跃中间3帧减少细碎卷线，整理胸饰和袖口，保留手杖与露膝红袜。 [当前修订校验](preview/style-fix-validation.json)记录本轮图集哈希与修改格；旧验收为历史记录。已检查静态帧序列与文件，应用内播放及用户验收待确认。

- [跳跃修订校验](preview/jump-transition-validation.json)：仅修改跳跃5格；首尾与原待机首帧逐像素一致，中间三帧使用统一尺度。其余83格和静态头像不变；已检查逐帧外观、透明边界、GIF解码与时长、有效源素材哈希。用户审查与应用内播放待完成；旧安装、更名和视觉记录保留历史结果，不代表本次修订已安装或验收。

**验证范围**：文件及预览检查已有记录；Codex 设置识别、桌面浮动显示与应用内动态播放尚未实测。兼容依据和已知限制如下。

- [更名校验](preview/rename-validation.json)记录当前名称及成品哈希；图片、动画和有效制作原素材保持原字节。历史记录保留当时标识。

- 原生Codex v2，无损RGBA WebP，1536×2288，8列11行，单格192×208，`spriteVersionNumber: 2`。[应用规格依据](preview/app-contract-verification.json)来自制作时对对应版本应用的只读检查。
- 九状态为待机、左右移动、招手、跳跃、失落、等待回应、思考处理中、审视，帧数6/8/8/4/5/8/6/6/6；后两行从正上方000°开始顺时针每22.5°一个，共16方向。`running`表示站定处理任务，左右移动由两条方向状态承担。
- [当前图集校验](validation.json)通过：尺寸、布局、必需格、透明空格及透明像素隐藏RGB符合要求。[原视觉验收摘要](preview/visual-qa.json)保留最终接受结论。
- [逐方向记录](preview/direction-semantics.json)与[独立盲审汇总](preview/direction-blind-validation.json)保留当前视线的验收依据。已接受的细微限制：045°、112.5°、202.5°、225°、292.5°的部分视线分量较细；两行交界存在轻微换姿，带标签复核未见错象限、反转或明显跳变。
- [GIF文件检查](preview/preview-files-check.json)已解码全部11个GIF，核对数量、尺寸与时长，总览为1680ms。[加载算法检查](preview/app-loader-validation.json)已核对更名后的工作区清单、图片及路径；未执行应用UI显示测试。
- 静态图为最终待机首帧192×208原始RGBA裁切。实际播放器动态播放及 Codex 应用内显示尚未实测。

</details>

<details>
<summary>参考与制作记录</summary>

- [SEGA官方公告](https://prtimes.jp/main/html/rd/p/000003548.000005397.html)
- [社区转载的角色设计资料页](https://www.bilibili.com/opus/854907901648568377)
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)

完整衣装以社区转载的角色设计资料核对，未核实官方直链；可见膝上短裙、露膝、红袜、鞋饰及手杖全长。双脚站立属于桌面动作演绎。

原作角色资料与卡面用于外观和性格依据；转绘、站立姿态和安静眨眼、克制招手、期待回应、思考及审视动作均为创作演绎，不宣称为官方原动画。

角色与动画使用 ImageGen 制作，图集经分格、定位和组装导出。制作原素材不随仓库或安装包分发；安装以本页列出的两个导入文件为准。权利说明见 [NOTICE.md](NOTICE.md)。

</details>
