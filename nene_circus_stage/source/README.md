# nene_circus_stage · 制作原素材

当前导入入口为宠物目录顶层的 `pet.json`、`spritesheet.webp`，正式预览与最终验收位于 `../preview/`。

- [素材索引](materials-index.json)记录当前成果选用的原始生成图、实际输入、有效提示词及SHA-256。
- 原始生成图、参考原图和提示词保留原有字节；历史生成清单中的旧路径仅作原始记录，现存文件以素材索引为准。
- 少量实际输入来自先前候选，其有效输入副本保存在 `references/selected-inputs/` 并列入索引，其余未采用候选已清理。
- 分格帧、重复组装图集和诊断预览属于可重建缓存；不作为安装入口，也不纳入合集ZIP。有效参考依据与创作补全见[本套说明](../README.md)。

当前选用素材位于 `costume-correction-20261016/`；完整卡面核对图保留在 `references/costume-recheck/`。

| 生成任务 | 选用的原始生成图 |
| --- | --- |
| `base` | [costume-correction-20261016/decoded/base.png](costume-correction-20261016/decoded/base.png) |
| `idle` | [costume-correction-20261016/decoded/idle.png](costume-correction-20261016/decoded/idle.png) |
| `running-right` | [costume-correction-20261016/decoded/running-right.png](costume-correction-20261016/decoded/running-right.png) |
| `running-left` | [costume-correction-20261016/decoded/running-left.png](costume-correction-20261016/decoded/running-left.png) |
| `waving` | [costume-correction-20261016/decoded/waving.png](costume-correction-20261016/decoded/waving.png) |
| `jumping` | [costume-correction-20261016/decoded/jumping.png](costume-correction-20261016/decoded/jumping.png) |
| `failed` | [costume-correction-20261016/decoded/failed.png](costume-correction-20261016/decoded/failed.png) |
| `waiting` | [costume-correction-20261016/decoded/waiting.png](costume-correction-20261016/decoded/waiting.png) |
| `running` | [costume-correction-20261016/decoded/running.png](costume-correction-20261016/decoded/running.png) |
| `review` | [costume-correction-20261016/decoded/review.png](costume-correction-20261016/decoded/review.png) |
| `look-cardinals` | [costume-correction-20261016/decoded/look-cardinals.png](costume-correction-20261016/decoded/look-cardinals.png) |
| `look-row-9` | [costume-correction-20261016/decoded/look-row-9.png](costume-correction-20261016/decoded/look-row-9.png) |
| `look-row-10` | [costume-correction-20261016/decoded/look-row-10.png](costume-correction-20261016/decoded/look-row-10.png) |

本次仅迁移外层目录与素材索引路径；生成清单、提示词、原始验收及制作脚本保留制作时的名称和字节。当前路径以素材索引为准，名称对应见[命名对照](../../PET_NAMES.md)。
