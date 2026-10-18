# 本套方案

- 角色：草薙宁宁。卡886「憧れに向かって」特训后，服装「クイーン・オブ・ハート」。
- 用户选择：Q版日系插画；显示名nene_classical lolita，ID nene_classical_lolita；完整可导入宠物、9状态与16方向、正式预览。
- 外观依据：2520×1440完整卡面优先，250×437游戏服装模型用于核对站立裙摆、连裤袜与鞋履。保留小王冠、灰绿长发、紫眼、红披肩与白毛领、奶油领结、绿金短裙与层叠白蕾丝、黑连裤袜、绿短靴和白色鞋口、红玫瑰与红心牌。
- 同人演绎：将卡面坐姿转为约2.5头身站姿。保留安静、克制的表情；轻幅招手、期待回应、专注思考和细看成品，不采用夸张躁动表演。跳跃限制为轻幅小跳。
- 舍去场景：椅子、玩偶、鸟、漂浮纸牌、花园背景不是宠物附属物。
- 左右手：人物右手持玫瑰，正面时在画面左侧；人物左手持红心牌，在画面右侧。两个移动方向分别绘制，不直接镜像，以保持手持物身份。
- 角色性格依据：https://pjsekai.sega.jp/character/unite04/nene/index.html 。官方资料用于内向、擅长歌唱和认真演出的性格依据；具体九状态动作是创作演绎。
- 服装官方确认：https://prtimes.jp/main/html/rd/p/000005688.000005397.html 。完整卡面为游戏素材公开镜像，记录见reference-downloads.json。
- 当前实际应用：OpenAI.Codex_26.1013.3656.0；已只读检查app.asar，原生v2尺寸1536×2288、8列11行、单格192×208，9状态帧数6/8/8/4/5/8/6/6/6，16方向000°向上起顺时针。结果在app-contract-verification.json。
- 技术代码借用：本套qa/verify-target-contract.py、record-generation.py、assemble-standard.py与render-final-previews.py复制自nene_victorian_lolita并只修改本套副本；没有借用其他套人物画面。
- 制作中，尚未安装、上传或发布。

- 本套同时复用既有的build-v2-qa.py、despill-validator-compatible.py及verify-package-loader.mjs制作与只读校验代码。已知边缘处理适配使选取范围覆盖原生验证器96色距判据；最终仅执行一次全图边缘清理，不更改透明度。
