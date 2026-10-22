[← 返回宠物合集](../README.md)

# 宁宁 · 猫耳旅装

<img src="preview/readme-portrait.png" alt="草薙宁宁猫耳旅装Q版预览" width="144">

**宁宁 · 猫耳旅装** · ID `nene_cat_traveler` · 9种动画 · 16个注视方向

- **服饰要素**：米黄浅绿猫耳贝雷帽、灰绿长发与肩前短辫、侧发卡；蓝紫领结、奶油衬衫、薄荷青短袖披肩夹克及金扣浅绿翻领；浅柠檬绿七分灯笼裤配奶油弧线滚边与城市剪影纹、橙色结和深蓝格纹荷叶裤口；绿色长袜、橙色鞋结与奶油厚底鞋，单侧挎包。
- **画风**：Q版日系插画，紧凑头身、短腿与轻幅动作。
- **参考卡面**：4星「憧れを焼き付けて」特训后；原色衣装「アスピリング・トリッパー」。

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

导入文件：[pet.json](pet.json) · [spritesheet.webp](spritesheet.webp)。

[下载 v2.0.0 十九套合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/nene_codex_pets-v2.0.0.zip) · [SHA-256 校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v2.0.0/SHA256SUMS.txt)。本套已收录于该版本；历史名称见[命名对照](../PET_NAMES.md)。

## 安装

1. 将 `nene_cat_traveler/` 复制至 `~/.codex/pets/`，保留顶层两个导入文件。
2. Windows 默认路径为 `%USERPROFILE%\.codex\pets\nene_cat_traveler\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_cat_traveler/`。
3. 在 **Codex 设置 > Pets** 中刷新并选择「宁宁 · 猫耳旅装」，必要时重启应用。

<details>
<summary>规格与验收</summary>

**验证范围**：文件及预览检查已有记录；Codex 设置识别、桌面浮动显示与应用内动态播放尚未实测。兼容依据和已知限制如下。

- Codex原生v2，无损RGBA WebP，1536×2288、8列11行、单格192×208，`spriteVersionNumber: 2`。
- [应用规格依据](preview/app-contract-verification.json)：2026-10-21只读核对 `OpenAI.Codex_26.1016.6573.0` 实际安装包。
- 九状态：待机、向右移动、向左移动、招手、小跳、失落、等待回应、专注处理中、审视；帧数6/8/8/4/5/8/6/6/6。
- 各动作从原始生成图一次裁切缩放，每行统一比例，最大人物高度190px、落地基线203px；小跳离地0/4/8/4/0px。见[动作定位记录](preview/standard-registration.json)。左右移动分别生成，保留单侧挎包、侧发卡与衣装细节，不使用镜像替代。
- 两行注视从000°正上方开始，每22.5°顺时针变化；090°屏幕右、180°下、270°屏幕左。十六方向均通过语义复核。
- [图集校验](validation.json)、[标准动作验收](preview/standard-visual-qa.json)、[最终视觉验收](preview/final-visual-qa.json)、[方向盲审](preview/direction-blind-validation.json)、[逐方向语义](preview/direction-semantics.json)与[连续性](preview/look-continuity.json)记录实际检查结果。
- 已接受的细微限制：左跑支撑角色为一帧A、三帧B，接触节奏稍不均匀，但确实交换双脚；跨行注视的帽顶及头发轮廓有高度差，属于局部外观变化；身体与脚锚点保持稳定；部分相邻注视角度差异较细微，仍保持正确方向；少量发丝、衣褶细节变化及GIF调色板边缘颗粒不影响角色辨识。
- [加载算法检查](preview/app-loader-validation.json)重放对应版本应用的图片、版本与路径验证函数；[预览文件检查](preview/preview-files-check.json)逐帧解码全部GIF，静态小图逐像素来自最终待机首帧。
- [README排版检查](preview/readme-layout-check.json)：首页与本页在1280px桌面和390px窄屏下的静态图、页面宽度及折叠交互已有验证记录；尚未核对GitHub线上渲染。

</details>

<details>
<summary>参考与制作记录</summary>

- [卡面、对应衣装与原色全身模型](https://game8.jp/pjsekai/816089)：资料站展示的游戏原图及模型，核对完整着装。
- [特训后卡面原图](https://img.game8.jp/13000317/ecd7236d4c2a26dee96d7184e6ff49c9.webp/original)
- [原色全身服装图](https://img.game8.jp/13000055/717ab73fe24b2cbc5f8b15526c838cf3.webp/original)
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)

卡面与完整模型共同确认猫耳帽、长发、短辫、领结、短袖披肩、排扣衬衫、灯笼裤、裤脚结、格纹荷叶裤口、绿色长袜和厚底鞋；下半身已有可靠全身图，无需自行设计。灰绿发色按原色模型校正卡面彩光。帽上的猫耳是服装配饰，不是动物耳朵；裤装保留两条分开的裤腿，不画成长裙。卡面里的魔法猫、飞机、旅行箱、城市布景及漂浮星星不纳入宠物。

「猫耳旅装」是本项目按服饰特点起的名称，非官方固定译名。官方角色资料中的游戏、音乐剧喜好及面对人群的拘谨，转化为安静待机、含蓄招手、短暂懊恼后恢复、认真思考和审视等动画；这些动作属于创作演绎。

角色与动画使用 ImageGen 制作，图集经分格、定位和组装导出。制作原素材不随仓库或安装包分发；安装以本页列出的两个导入文件为准。权利说明见 [NOTICE.md](NOTICE.md)。

</details>
