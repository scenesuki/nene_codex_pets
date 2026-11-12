[← 返回宠物合集](../README.md)

# 宁宁机器人

<img src="preview/readme-portrait.png" alt="宁宁机器人静态预览" width="144">

**宁宁机器人** · ID `nene_robo` · 9种动画 · 16个注视方向

> **视线跟随提示（2026-11-06）**：当前已核验的 Codex 官方版本尚未正常支持宠物跟随日常鼠标移动。本项目已提供 16 个注视方向素材，但不代表实际使用时会自动跟随鼠标；该问题位于应用端，并非素材缺失。详见[官方仓库反馈 #33224](https://github.com/openai/codex/issues/33224)。

2026-11-06 优化：原跳跃槽位改为站定抬手问好，五帧全程睁眼，第三帧保持紫色机械眼睛。已按用户要求卸载本机旧版、删除两条同名云端旧记录，再安装当前优化版并重建一条云端宠物，恢复使用宁宁机器人；见[当前安装记录](preview/current-installation-validation.json)。用户已于2026-11-06确认当前优化版审查通过。下方 v2.0.0 下载对应优化前版本，本次尚未上传 GitHub 或发布 Release。

- **服饰要素**：原始黄裙演出服，搭配青绿马甲、粉色蝴蝶结、蝶饰与机械四肢。
- **画风**：贴近游戏原画
- **参考卡面**：无独立参考卡面；参考官方宁宁机器人原始造型。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

导入文件：[pet.json](pet.json) · [spritesheet.webp](spritesheet.webp)。

[下载 v2.0.1 十九套合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.1/nene_codex_pets-v2.0.1.zip) · [SHA-256 校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.1/SHA256SUMS.txt)。

## 安装

1. 解压本版合集，将 `nene_robo/` 复制至 `~/.codex/pets/`，保留顶层的 `pet.json` 与 `spritesheet.webp`。
2. Windows 默认目录为 `%USERPROFILE%\.codex\pets\nene_robo\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_robo/`。
3. 在 **Codex 设置 > Pets** 中刷新并选择「宁宁机器人」，必要时重启应用。

<details>
<summary>规格与验收</summary>

**验证范围**：文件及预览检查已有记录；Codex 设置识别、桌面浮动显示与应用内动态播放尚未实测。兼容依据和已知限制如下。

- [更名校验](preview/rename-validation.json)保留更名时的名称及成品哈希；该记录对应本次优化前版本。历史记录保留当时标识。

- 原生Codex v2，无损RGBA WebP，1536×2288，8列11行，单格192×208，`spriteVersionNumber: 2`。[应用规格依据](preview/app-contract-verification.json)来自制作时对对应版本应用的只读检查。
- 九状态为待机、左右移动、招手、问好、失落、等待回应、思考处理中、审视，帧数6/8/8/4/5/8/6/6/6；问好保留原 `jumping` 标识、第4行（从0计）及5帧布局，时长为140/140/140/140/280ms。后两行从正上方000°开始顺时针每22.5°一个，共16方向。`running`表示站定处理任务，左右移动由两条方向状态承担。
- [当前图集校验](validation.json)通过：尺寸、布局、必需格、透明空格及透明像素隐藏RGB符合要求。[原视觉验收摘要](preview/visual-qa.json)保留最终接受结论。
- [逐方向记录](preview/direction-semantics.json)与[独立盲审汇总](preview/direction-blind-validation.json)保留当前视线的验收依据。已接受的细微限制：157.5°、202.5°横向和067.5°、112.5°纵向分量较细；045°、315°同邻格差别较小，337.5°回正稍明显，完整循环复核未见明显跳变。
- [GIF文件检查](preview/preview-files-check.json)记录当前11个GIF的逐帧解码、数量、尺寸与时长，总览为1680ms。[原加载算法检查](preview/app-loader-validation.json)对应优化前图集；本次未重放应用加载算法或执行应用UI显示测试。
- [问好动作修订校验](preview/greeting-validation.json)记录本次成品哈希、五帧布局、首尾与待机衔接及其他状态不变检查。[五帧静态图](preview/greeting-frames.png)与[问好动画](preview/jumping.gif)用于审查。当前环境无法访问既有记录中的应用归档，沿用[已核实的v2规格](preview/app-contract-verification.json)；当前应用版本兼容性待实测。本地浏览器策略禁止打开文件URL，未完成实际播放器动态播放检查，已执行逐帧静态检查与GIF解码、时长检查。
- 静态图为最终待机首帧192×208原始RGBA裁切。实际播放器动态播放及 Codex 应用内显示尚未实测。

</details>

<details>
<summary>参考与制作记录</summary>

- [日文官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)
- [英文官方资料](https://www.colorfulstage.com/characters/wonderlands-showtime/nene/index.html?year=past)
- [游戏剧情截图整理](https://game-question.com/qa/project_sekai/1347c27f-3404-473b-a2b9-3167a065d192)
- [官方商品包装照片（第三方卖家）](https://www.ebay.com/itm/405696609821)
- [游戏一格漫画整理](https://gameo.jp/pjsekai/494)

原始机器人外观以剧情截图和商品包装插画交叉核对；第三方整理页与卖家照片并非官方直接下载。

原作角色资料与卡面用于外观和性格依据；转绘、站立姿态和安静眨眼、克制招手、期待回应、思考及审视动作均为创作演绎，不宣称为官方原动画。

本次问好为创作演绎：双脚站定，画面右侧机械手抬起示意并轻轻点头，再放下回到待机；按用户要求，第三帧改为睁眼微笑，问好五帧均保持睁眼。仅替换原跳跃槽位，其他状态（包括已有表情）保持原样。

角色与动画使用 ImageGen 制作，图集经分格、定位和组装导出。制作原素材不随仓库或安装包分发；安装以本页列出的两个导入文件为准。权利说明见 [NOTICE.md](NOTICE.md)。

</details>
