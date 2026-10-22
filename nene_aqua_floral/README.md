[← 返回宠物合集](../README.md)

# 宁宁 · 水蓝花饰礼裙

<img src="preview/readme-portrait.png" alt="草薙宁宁水蓝花饰礼裙Q版预览" width="144">

**宁宁 · 水蓝花饰礼裙** · ID `nene_aqua_floral` · 9种动画 · 16个注视方向

- **服饰要素**：灰绿长发、珍珠发箍与绿白花海星蓝坠，白色长灯笼袖与浅绿镶边尖领，金扣、金链及腰侧花饰，白色花边内裙叠水蓝不对称外裙，裸腿配浅绿系带白色礼鞋。
- **画风**：Q版日系插画，紧凑头身、短腿与轻幅动作。
- **参考卡面**：4星「抱く焦燥」特训后；原色衣装「レーヴ・デ・トナリティ」。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

导入文件：[pet.json](pet.json) · [spritesheet.webp](spritesheet.webp)。

[下载 v2.0.0 十九套合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/nene_codex_pets-v2.0.0.zip) · [SHA-256 校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/SHA256SUMS.txt)。本套已收录于该版本；历史名称见[命名对照](../PET_NAMES.md)。

## 安装

1. 将 `nene_aqua_floral/` 复制至 `~/.codex/pets/`，保留顶层两个导入文件。
2. Windows 默认路径为 `%USERPROFILE%\.codex\pets\nene_aqua_floral\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_aqua_floral/`。
3. 在 **Codex 设置 > Pets** 中刷新并选择「宁宁 · 水蓝花饰礼裙」，必要时重启应用。

<details>
<summary>规格与验收</summary>

**验证范围**：文件及预览检查已有记录；Codex 设置识别、桌面浮动显示与应用内动态播放尚未实测。兼容依据和已知限制如下。

- Codex原生v2，无损RGBA WebP，1536×2288、8列11行、单格192×208，`spriteVersionNumber: 2`。
- [应用规格依据](preview/app-contract-verification.json)：2026-10-20只读核对 `OpenAI.Codex_26.1013.4894.0`。
- 九状态：待机、向右移动、向左移动、招手、小跳、失落、等待回应、专注处理中、审视；帧数6/8/8/4/5/8/6/6/6。
- 标准动作从各行原始生成图一次裁切缩放，每行使用统一比例，最大人物高度190px、落地基线203px；小跳仅0/4/8/4/0px。见[动作定位记录](preview/standard-registration.json)。左右动作独立生成，保持头侧花饰、腰花与裙摆原侧别。
- 左右移动呈节奏略不均的轻快碎步，失落后的起身恢复略快；小跳峰值姿态有轻微伸展。上述细微限制已按原尺寸逐帧复核接受，详见最终视觉验收。
- 后两行为从000°正上方开始、每22.5°顺时针变化的16方向，180°保持睁眼低头。十六方向均通过语义复核。
- 后八方向的头顶和发量略大，跨行转头有轻微差异；独立原尺寸复核未见明显全身缩放或手脚跳位。连续性程序在裙下标出的孔洞候选为正常腿侧、两腿间开放区域。
- [图集校验](validation.json)、[标准动作验收](preview/standard-visual-qa.json)、[最终视觉验收](preview/final-visual-qa.json)、[方向盲审](preview/direction-blind-validation.json)、[逐方向语义](preview/direction-semantics.json)与[连续性](preview/look-continuity.json)记录实际结果及细微限制。
- [加载算法检查](preview/app-loader-validation.json)重放对应版本应用的图片、版本与路径验证函数；[预览文件检查](preview/preview-files-check.json)逐帧解码全部GIF，静态小图逐像素来自最终待机首帧。

</details>

<details>
<summary>参考与制作记录</summary>

- [SEGA官方公告：卡面与衣装对应](https://prtimes.jp/main/html/rd/p/000006490.000005397.html)
- [原色全身服装与配饰](https://game8.jp/pjsekai/687172)
- [完整高清特训后卡面](https://pjsekai.gamedbs.jp/chara/show/7/1149)
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)

完整卡面与原色全身模型共同确认发饰、尖领、腰花、链饰、长短裙层、裸腿及鞋履。白色内裙前部约及膝，水蓝侧后外裙更长；不是裤装，也不添加长袜或靴子。发色按模型校正卡面暖光，保留灰绿长发及前侧收束发尾，不新增帽子。没有专属解锁发型，不借用其他卡面的短发。

「水蓝花饰礼裙」是根据本套服饰特征命名，非官方衣装名称的固定译法。卡面的闭目表情用于眨眼、失落或专注表现；常态采用模型紫眼。宁宁的音乐剧、游戏喜好和不擅长人多场所来自角色资料；含蓄招手、轻步、思考及小跳是本项目动画演绎。小鸟、鸟笼、椅子、留声机及贝壳场景不纳入宠物。

角色与动画使用 ImageGen 制作，图集经分格、定位和组装导出。制作原素材不随仓库或安装包分发；安装以本页列出的两个导入文件为准。权利说明见 [NOTICE.md](NOTICE.md)。

</details>
