[← 返回宠物合集](../README.md)

# 宁宁 · 古典洛丽塔 · 红心皇后

<img src="preview/readme-portrait.png" alt="宁宁 · 古典洛丽塔 · 红心皇后静态预览" width="144">

**宁宁 · 古典洛丽塔 · 红心皇后** · ID `nene_classical_lolita` · 9种动画 · 16个注视方向

- **服饰要素介绍**：红心小王冠、红披肩、深绿蕾丝短裙、黑色连裤袜与白色鞋口绿靴；右手持玫瑰，左手持红心牌。站姿、紧凑头身及互动动作属于创作演绎。
- **画风**：Q版日系插画
- **参考卡面**：4星卡「憧れに向かって」特训后；服装「クイーン・オブ・ハート」。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

最终导入文件：[pet.json](pet.json) 与 [spritesheet.webp](spritesheet.webp)。本套包含在[v1.9.0十套完整合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.9.0/nene_codex_pets-v1.9.0.zip)，下载后用同版[SHA256SUMS.txt](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.9.0/SHA256SUMS.txt)核对校验和。历史附件与旧名称见[命名对照](../PET_NAMES.md)及[GitHub Release](https://github.com/scenesuki/nene_codex_pets/releases)。

## 安装

1. 解压本版合集，将 `nene_classical_lolita/` 复制至 `~/.codex/pets/`，保留顶层的 `pet.json` 与 `spritesheet.webp`。
2. Windows默认目录为 `%USERPROFILE%\.codex\pets\nene_classical_lolita\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_classical_lolita/`。
3. 在Codex设置 > Pets中刷新并选择「宁宁 · 古典洛丽塔 · 红心皇后」，必要时重启应用。

本套当前名称尚未安装；本次未执行安装或切换。

<details>
<summary>规格与验收</summary>

- [更名校验](preview/rename-validation.json)记录当前名称及成品哈希；图片、动画和有效制作原素材保持原字节。历史制作与安装记录保留当时标识，当前名称见[命名对照](../PET_NAMES.md)。

- 原生Codex v2，无损RGBA WebP，1536×2288，8列11行，单格192×208，`spriteVersionNumber: 2`。[应用规格依据](preview/app-contract-verification.json)来自2026-10-17对本机 `OpenAI.Codex_26.1013.3656.0` 的只读检查。
- 九状态为待机、左右移动、招手、跳跃、失落、等待回应、专注处理中、审视，帧数6/8/8/4/5/8/6/6/6。后两行从正上方000°开始顺时针每22.5°一个，共16方向。
- 跳跃靴底离地为0/4/8/4/0px，采用轻幅小跳。[定位记录](preview/jump-placement.json)。
- 双向步态可读，但黑袜下的前后脚身份辨识较细微，已记为次要限制。
- [图集校验](validation.json)、[标准动作视觉验收](preview/standard-visual-qa.json)、[最终视觉验收](preview/final-visual-qa.json)、[方向盲审](preview/direction-blind-validation.json)与[连续性记录](preview/look-continuity.json)保留实际检查依据。
- [逐方向语义记录](preview/direction-semantics.json)：未发现方向硬性错误；中间角度的细微限制见逐方向记录。
- 22.5°、135°、157.5°的横向视线较细微；112.5°→135°及157.5°→180°头部轮廓变化略集中，未发现错误象限、反向或明显整体缩放。[次要限制复核](preview/blind-review-resolution.json)。
- [加载算法检查](preview/app-loader-validation.json)已核对更名后的工作区清单、图片及路径；未执行应用UI显示测试。
- [GIF文件检查](preview/preview-files-check.json)逐帧解码正式预览；静态展示图为最终图集待机首帧的原始RGBA裁切。实际播放器及README桌面/窄屏交互尚未实测。

</details>

<details>
<summary>参考与制作记录</summary>

- [世嘉官方公告：卡名及红心皇后服装](https://prtimes.jp/main/html/rd/p/000005688.000005397.html)
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)
- [完整特训后卡面游戏素材镜像](https://storage.sekai.best/sekai-jp-assets/character/member/res015_no033/card_after_training.png)
- [卡面与原色服装模型核对页](https://appmedia.jp/pjsekai/77662849)
- [游戏数据镜像](https://github.com/Sekai-World/sekai-master-db-diff/blob/main/cards.json)

完整卡面用于核对服装和左右手道具，原色3D服装模型用于站姿、裙摆与鞋履核对。未采用特训前的日常服装，也未将卡面中的椅子、玩偶、鸟或漂浮纸牌加入宠物。

官方资料提供角色身份、认真追逐音乐剧梦想及擅长歌唱的设定依据；克制招手、期待回应、看牌思考和审视动作均为创作演绎。画风与特训阶段由用户明确选择。

本套通过内置imagegen绘制基准图和各状态。有效原素材、实际输入与提示词仅保留在本地本套 `source/`，索引为本地 `source/materials-index.json`，不随 GitHub 仓库分发；制作脚本只复用并修改本套副本，没有借用其他宠物人物画面。原素材和制作缓存不作为安装入口。权利说明见[NOTICE.md](NOTICE.md)。

</details>
