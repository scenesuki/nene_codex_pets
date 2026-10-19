[← 返回宠物合集](../README.md)

# 宁宁 · 马戏团礼装

<img src="preview/readme-portrait.png" alt="宁宁 · 马戏团礼装静态预览" width="144">

**宁宁 · 马戏团礼装** · ID `nene_circus_stage` · 9种动画 · 16个注视方向

- **服饰要素介绍**：红色短外套、黑蓝金条纹膝上短裙、红金裙边与红色小腿袜，膝盖露出；鞋履带红色拼片及金色踝蝴蝶结，裸手持金色槽纹杖头的黑色手杖。
- **画风**：Q版日系插画
- **参考卡面**：2星卡「ワンダーステッキ」。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

最终导入文件：[pet.json](pet.json) 与 [spritesheet.webp](spritesheet.webp)。本套包含在[v1.9.0十套完整合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.9.0/nene_codex_pets-v1.9.0.zip)，下载后用同版[SHA256SUMS.txt](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.9.0/SHA256SUMS.txt)核对校验和。历史附件与旧名称见[命名对照](../PET_NAMES.md)及[GitHub Release](https://github.com/scenesuki/nene_codex_pets/releases)。

## 安装

1. 解压本版合集，将 `nene_circus_stage/` 复制至 `~/.codex/pets/`，保留顶层的 `pet.json` 与 `spritesheet.webp`。
2. Windows默认目录为 `%USERPROFILE%\.codex\pets\nene_circus_stage\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_circus_stage/`。
3. 在Codex设置 > Pets中刷新并选择「宁宁 · 马戏团礼装」，必要时重启应用。

本套当前名称尚未安装；本次未执行安装或切换。

<details>
<summary>规格与验收</summary>

- [更名校验](preview/rename-validation.json)记录当前名称及成品哈希；图片、动画和有效制作原素材保持原字节。历史制作与安装记录保留当时标识，当前名称见[命名对照](../PET_NAMES.md)。

- 原生Codex v2，无损RGBA WebP，1536×2288，8列11行，单格192×208，`spriteVersionNumber: 2`。[应用规格依据](preview/app-contract-verification.json)来自制作时对本机实际应用的只读检查。
- 九状态为待机、左右移动、招手、跳跃、失落、等待回应、思考处理中、审视，帧数6/8/8/4/5/8/6/6/6；后两行从正上方000°开始顺时针每22.5°一个，共16方向。`running`表示站定处理任务，左右移动由两条方向状态承担。
- [当前图集校验](validation.json)通过：尺寸、布局、必需格、透明空格及透明像素隐藏RGB符合要求。[原视觉验收摘要](preview/visual-qa.json)保留最终接受结论。
- [逐方向记录](preview/direction-semantics.json)与[独立盲审汇总](preview/direction-blind-validation.json)保留当前视线的验收依据。已接受的细微限制：045°、112.5°、202.5°、225°、292.5°的部分视线分量较细；两行交界存在轻微换姿，带标签复核未见错象限、反转或明显跳变。
- [GIF文件检查](preview/preview-files-check.json)已解码全部11个GIF，核对数量、尺寸与时长，总览为1680ms。[加载算法检查](preview/app-loader-validation.json)已核对更名后的工作区清单、图片及路径；未执行应用UI显示测试。
- 静态图为最终待机首帧192×208原始RGBA裁切。实际播放器动态播放、应用内显示、README桌面/窄屏显示及折叠交互尚未实测。

</details>

<details>
<summary>参考与制作记录</summary>

- [SEGA官方公告](https://prtimes.jp/main/html/rd/p/000003548.000005397.html)
- [社区转载的角色设计资料页](https://www.bilibili.com/opus/854907901648568377)
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)

完整衣装以社区转载的角色设计资料核对，未核实官方直链；可见膝上短裙、露膝、红袜、鞋饰及手杖全长。双脚站立属于桌面动作演绎。

原作角色资料与卡面用于外观和性格依据；转绘、站立姿态和安静眨眼、克制招手、期待回应、思考及审视动作均为创作演绎，不宣称为官方原动画。

正式成果由当前导入文件、正式预览、来源说明与最终验收记录组成。当前成果选用的原始生成图、有效参考图、实际生成输入和提示词仅保留在本地本套 `source/`，索引为本地 `source/materials-index.json`；原素材不随 GitHub 仓库或安装ZIP分发。未采用废案、重复制作缓存及旧本地包按授权清理，图集和动画像素保持原样。权利说明见[NOTICE.md](NOTICE.md)。部分验收JSON内的制作路径是历史元数据，当前使用入口以本页和顶层导入文件为准。

</details>
