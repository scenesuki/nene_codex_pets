# nene_victorian_lolita · 制作原素材

当前导入入口为宠物目录顶层的 `pet.json`、`spritesheet.webp`，正式预览与最终验收位于 `../preview/`。

- [素材索引](materials-index.json)记录当前成果选用的原始生成图、实际输入、有效提示词及SHA-256。
- 原始生成图、参考原图和提示词保留原有字节；历史生成清单中的旧路径仅作原始记录，现存文件以素材索引为准。
- 少量实际输入来自先前候选，其有效输入副本保存在 `references/selected-inputs/` 并列入索引，其余未采用候选已清理。
- 分格帧、重复组装图集和诊断预览属于可重建缓存；不作为安装入口，也不纳入合集ZIP。有效参考依据与创作补全见[本套说明](../README.md)。

跳跃原素材位于 `jump-refinement-20261016/`，其余状态采用本目录选定原图；素材索引对应当前成品。

| 生成任务 | 选用的原始生成图 |
| --- | --- |
| `base` | [decoded/base.png](decoded/base.png) |
| `idle` | [decoded/idle.png](decoded/idle.png) |
| `running-right` | [decoded/running-right.png](decoded/running-right.png) |
| `running-left` | [decoded/running-left.png](decoded/running-left.png) |
| `waving` | [decoded/waving.png](decoded/waving.png) |
| `failed` | [decoded/failed.png](decoded/failed.png) |
| `waiting` | [decoded/waiting.png](decoded/waiting.png) |
| `running` | [decoded/running.png](decoded/running.png) |
| `review` | [decoded/review.png](decoded/review.png) |
| `look-cardinals` | [decoded/look-cardinals.png](decoded/look-cardinals.png) |
| `look-row-9` | [decoded/look-row-9.png](decoded/look-row-9.png) |
| `look-row-10` | [decoded/look-row-10.png](decoded/look-row-10.png) |
| `jumping` | [jump-refinement-20261016/decoded/jumping.png](jump-refinement-20261016/decoded/jumping.png) |

本次仅迁移外层目录与素材索引路径；生成清单、提示词、原始验收及制作脚本保留制作时的名称和字节。当前路径以素材索引为准，名称对应见[命名对照](../../PET_NAMES.md)。
