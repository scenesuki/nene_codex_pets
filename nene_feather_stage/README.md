[← 返回宠物合集](../README.md)

# 宁宁 · 羽饰舞台装

<img src="preview/readme-portrait.png" alt="宁宁 · 羽饰舞台装静态预览" width="144">

**宁宁 · 羽饰舞台装** · ID `nene_feather_stage` · 9种动画 · 16个注视方向

> **视线跟随提示（2026-11-06）**：当前已核验的 Codex 官方版本尚未正常支持宠物跟随日常鼠标移动。本项目已提供 16 个注视方向素材，但不代表实际使用时会自动跟随鼠标；该问题位于应用端，并非素材缺失。详见[官方仓库反馈 #33224](https://github.com/openai/codex/issues/33224)。

- **服饰要素**：羽饰白花、白金短披肩、青绿层叠裙摆与粉色领饰。
- **画风**：Q版日系插画
- **参考卡面**：2星卡「Brand New Style」。

2026-11-06 修订：向左跑动按当前待机与向右跑动的头身、躯干和腿部比例重新制作，减小过宽轮廓与前倾幅度，保留左向头饰位置及8帧节奏。[比例对照](preview/run-proportions.png) · [左跑动画](preview/running-left.gif)。用户已确认左跑动作验收合格；随后仅按右跑配色校正头发及青绿色服饰，保持8帧透明度、轮廓、定位与时长完全一致。[校色对照](preview/left-color-comparison.png) · [校色验证](preview/left-color-validation.json)。用户已于2026-11-06确认校色后的整套宠物审查通过。

**安装状态**：2026-11-06已按用户要求删除本机和云端旧版后重新安装当前校色版，云端仅保留一条并恢复当前使用；本机文件哈希与云端图集全部RGBA像素均已核对，见[当前安装记录](preview/current-installation-validation.json)。v2.0.0下载仍为此前发布版，当前修订尚未上传GitHub或发布Release。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

导入文件：[pet.json](pet.json) · [spritesheet.webp](spritesheet.webp)。

[下载 v2.0.1 十九套合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.1/nene_codex_pets-v2.0.1.zip) · [SHA-256 校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.1/SHA256SUMS.txt)。

## 安装

1. 解压本版合集，将 `nene_feather_stage/` 复制至 `~/.codex/pets/`，保留顶层的 `pet.json` 与 `spritesheet.webp`。
2. Windows 默认目录为 `%USERPROFILE%\.codex\pets\nene_feather_stage\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_feather_stage/`。
3. 在 **Codex 设置 > Pets** 中刷新并选择「宁宁 · 羽饰舞台装」，必要时重启应用。

<details>
<summary>规格与验收</summary>

**验证范围**：文件及预览检查已有记录；Codex 设置识别、桌面浮动显示与应用内动态播放尚未实测。兼容依据和已知限制如下。

- [更名校验](preview/rename-validation.json)保留更名时的名称及修订前成品哈希。历史记录保留当时标识。

- 原生Codex v2，无损RGBA WebP，1536×2288，8列11行，单格192×208，`spriteVersionNumber: 2`。[应用规格依据](preview/app-contract-verification.json)来自制作时对对应版本应用的只读检查。
- 九状态为待机、左右移动、招手、跳跃、失落、等待回应、思考处理中、审视，帧数6/8/8/4/5/8/6/6/6；后两行从正上方000°开始顺时针每22.5°一个，共16方向。`running`表示站定处理任务，左右移动由两条方向状态承担。
- [当前图集校验](validation.json)通过：尺寸、布局、必需格、透明空格及透明像素隐藏RGB符合要求。[原视觉验收摘要](preview/visual-qa.json)保留最终接受结论。
- [逐方向记录](preview/direction-semantics.json)与[独立盲审汇总](preview/direction-blind-validation.json)保留当前视线的验收依据。已接受的细微限制：067.5°上向与135°横向分量较细，审视动作克制；两行视线交界有轻微换姿，原尺寸复核未见明显跳变。
- [GIF文件检查](preview/preview-files-check.json)记录当前11个GIF的解码、尺寸与时长，总览为1680ms。[原加载算法检查](preview/app-loader-validation.json)对应左跑修订前图集；本次未重放当前应用加载算法或执行应用UI显示测试。
- [原左跑比例修订校验](preview/left-run-validation.json)记录校色前的图集哈希与定位检查；[当前校色校验](preview/left-color-validation.json)记录仅RGB变化、透明度及其余80格像素不变、用户动作验收通过及结构预检结果。[左跑全帧](preview/running-left-frames.png)用于原尺寸逐帧审查。辅助 ChatGPT 脚本对比例修订前后均只报告原有待机第6列中性格不透明；该格保持原样，当前校色版Pets服务结构预检通过。当前 Codex 应用版本兼容性及实际动态显示仍待实测。
- 静态图为最终待机首帧192×208原始RGBA裁切。实际播放器动态播放及 Codex 应用内显示尚未实测。

</details>

<details>
<summary>参考与制作记录</summary>

- [官方角色资料与当前舞台服立绘](https://pjsekai.sega.jp/character/unite04/nene/index.html)
- [卡名索引](https://projectsekai.fandom.com/wiki/Brand_New_Style)

服装以官方当前舞台服完整立绘核对；卡名与卡738资料由游戏数据镜像辅助确认。

原作角色资料与卡面用于外观和性格依据；转绘、站立姿态和安静眨眼、克制招手、期待回应、思考及审视动作均为创作演绎，不宣称为官方原动画。

角色与动画使用 ImageGen 制作，图集经分格、定位和组装导出。制作原素材不随仓库或安装包分发；安装以本页列出的两个导入文件为准。权利说明见 [NOTICE.md](NOTICE.md)。

</details>
