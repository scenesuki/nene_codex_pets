[← 返回宠物合集](../README.md)

# 宁宁 · 青柠休闲装

<img src="preview/readme-portrait.png" alt="草薙宁宁青柠休闲装Q版静态预览" width="144">

**宁宁 · 青柠休闲装** · ID `nene_kuchipatchi_casual` · 9种动画 · 16个注视方向

- **参考卡面**：四星「大特訓大会の成果！」特训后；原色衣装「くちぱっち風ゆったりコーデ」。
- **服饰要素**：叶饰耳机与灰绿长发、青柠蓬袖短外套、白色花边短裙、蓝挂绳及粉色拓麻歌子挂件；荧绿连袜裤、右腿蓝色饰件、白色堆堆袜和绿绒拖鞋。
- **画风**：细线与柔和赛璐璐上色的Q版日系插画，脸型、头肩关系和紧凑身体以复古淑女造型的 Q 版比例为基准。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [静态全帧](preview/contact-sheet.png) · [全部预览](preview/README.md)

导入文件：[pet.json](pet.json) · [spritesheet.webp](spritesheet.webp)。

[下载 v2.0.0 十九套合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/nene_codex_pets-v2.0.0.zip) · [SHA-256 校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/SHA256SUMS.txt)。本套已收录于该版本；历史名称见[命名对照](../PET_NAMES.md)。

## 安装

1. 将 `nene_kuchipatchi_casual/` 复制至 `~/.codex/pets/`，保留顶层 `pet.json` 与 `spritesheet.webp`。
2. Windows 默认路径为 `%USERPROFILE%\.codex\pets\nene_kuchipatchi_casual\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_kuchipatchi_casual/`。
3. 在 **Codex 设置 > Pets** 中刷新并选择「宁宁 · 青柠休闲装」，必要时重启应用。

<details>
<summary>规格与验收</summary>

**验证范围**：文件及预览检查已有记录；Codex 设置识别、桌面浮动显示与应用内动态播放尚未实测。兼容依据和已知限制如下。

- 原生v2图集：无损RGBA WebP、1536×2288、8列11行、单格192×208，`spriteVersionNumber: 2`。
- [格式复核](preview/production-contract-check.json)对照应用前后端实现，结果与[原规格依据](preview/app-contract-verification.json)一致。
- 前九行是待机、向右移动、向左移动、招手、小跳、失落、等待回应、专注处理中和审视，帧数6/8/8/4/5/8/6/6/6。后两行是16个注视方向：000°上、090°右、180°下、270°左，每22.5°顺时针排列。
- 左右移动分别生成，每侧4个交替步态关键姿势重复两次，填充应用8帧行，不以镜像替代。小跳的脚底离地为0/2/7/2/0px；各行统一缩放和脚底基线，见[定位记录](preview/registration.json)。另填入第0行第6列的中性姿势以兼容现有图集校验工具。
- [图集检查](validation.json)验证格式、透明度、有效格、空格与透明像素隐藏RGB；[几何与无损检查](preview/atlas-geometry-check.json)确认边距、WebP逐像素回读和静态展示图与最终待机首帧一致。
- [加载算法检查](preview/app-loader-validation.json)重放实际应用的图片、版本及路径校验函数；[预览文件检查](preview/preview-files-check.json)逐帧解码全部GIF并核对帧数、时长、链接和素材哈希。
- [实际尺寸播放检查](preview/animation-playback-check.json)在Chromium中按192×208单格播放九状态，验证帧推进并人工查看连续快照；该检查不等同于Codex应用内播放。GIF便于快速查看循环，实际待机节奏由应用控制。
- [最终视觉验收](preview/final-visual-qa.json)与[逐方向语义](preview/direction-semantics.json)记录实际复核。已接受的细微限制：部分相邻斜向视线的分量差异较细；抬头修正帧与相邻帧的发丝、头部轮廓略有变化；少量衣褶、发丝与挂件细节随帧变化，GIF调色板边缘略有颗粒。
- [README排版检查](preview/readme-layout-check.json)覆盖1280px桌面和390px窄屏的静态图、页面宽度与折叠交互。GitHub线上渲染尚未核对。

</details>

<details>
<summary>参考与制作记录</summary>

- [SEGA官方联动公告与卡面](https://www.sega.jp/topics/detail/250919_3/)：确认卡名、衣装名和拓麻歌子联动关系。
- [卡面与原色全身服装模型](https://game8.jp/pjsekai/713025)：补齐裙摆、腿饰、袜子和拖鞋；未使用另三款配色。
- [特训后原图](https://img.game8.jp/11796108/49d0ea113227b2d45b459e6dacf1692e.webp/original) · [原色全身模型](https://img.game8.jp/11796170/d47bede0216dc01d6c96fe0f559ddf60.webp/original)
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)：游戏、音乐剧爱好以及谨慎而努力的性格，用于动作构思。
- 比例参考为原ID `nene_edo`、现名[宁宁 · 复古淑女](../nene_vintage_lady/README.md)。仅借鉴头身比例，未借用其帽子、折扇、手套、长裙或靴子。

「青柠休闲装」为本项目按配色、蓬袖和绒拖鞋起的名称，并非官方译名。安静眨眼、含蓄招手、轻跳、失落后恢复、等待、认真操作挂件和审视属于同人创作演绎；卡面食品、场景及独立吉祥物未纳入宠物。

角色与动画使用 ImageGen 制作，图集经分格、定位和组装导出。制作原素材不随仓库或安装包分发；安装以本页列出的两个导入文件为准。权利说明见 [NOTICE.md](NOTICE.md)。

</details>

