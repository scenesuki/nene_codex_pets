"""Add the completed local pet while preserving the published nine-pet release."""
from pathlib import Path
import json

pet = Path(__file__).resolve().parents[2]
root = pet.parent
assert json.loads((pet/'pet.json').read_text(encoding='utf-8'))['id'] == pet.name
assert (pet/'preview/readme-portrait.png').is_file()
p = root/'README.md'
s = p.read_text(encoding='utf-8')
old = '草薙宁宁的 Codex 桌面宠物合集。现有九套造型，各有9种状态动画与16个注视方向。新增「憧れに向かって」特训后红心皇后造型 `nene_classical_lolita`（显示名 `宁宁 · 古典洛丽塔 · 红心皇后`）。'
new = '草薙宁宁的 Codex 桌面宠物合集。工作区现有十套造型，各有9种状态动画与16个注视方向。新增「夢をのせたメロディー」特训后新中式礼装 `nene_chinoiserie`（显示名 `宁宁 · 新中式礼装`），已在本地制作，尚未发布。'
assert old in s
s = s.replace(old,new,1)
s = s.replace('v1.8.0合集包含下列全部九套宠物、统一名称、完整预览和最终校验记录。','v1.8.0合集包含此前九套宠物、统一名称、完整预览和最终校验记录，不包含本地新增的新中式礼装。',1)
a = s.index('| 古典洛丽塔·红心皇后 · 新增 |')
b = s.index('## 三步安装',a)
s = s[:a]+'''| 古典洛丽塔·红心皇后 | 新中式礼装 · 本地新增 |
| :---: | :---: |
| <a href="nene_classical_lolita/README.md"><img src="nene_classical_lolita/preview/readme-portrait.png" alt="Classical Lolita宁宁与红心牌、玫瑰" width="144"></a> | <a href="nene_chinoiserie/README.md"><img src="nene_chinoiserie/preview/readme-portrait.png" alt="草薙宁宁新中式礼装" width="144"></a> |
| **服饰要素介绍**：红心王冠、红披肩、深绿蕾丝裙、玫瑰与红心牌 | **服饰要素介绍**：蓝紫斜襟、腰侧蝴蝶结、黑色开衩长裙、灰短袜与黑搭带鞋 |
| **画风**：Q版日系插画 | **画风**：Q版日系插画 |
| **参考卡面**：4星卡「憧れに向かって」特训后；服装「クイーン・オブ・ハート」 | **参考卡面**：4星卡「夢をのせたメロディー」特训后；服装「ディグニファイド・ブリリアンス」 |
| [造型与说明](nene_classical_lolita/README.md) · [查看动画](nene_classical_lolita/preview/animation-overview.gif) | [造型与本地文件](nene_chinoiserie/README.md) · [查看动画](nene_chinoiserie/preview/animation-overview.gif) |

'''+s[b:]
anchor = '- 本次九套名称已统一'
index = s.index(anchor)
s = s[:index]+'- 本地新增 `nene_chinoiserie` 的九状态、十六方向、图集及加载算法验收见其子页；下半身按原色全身模型核实。尚未安装、上传或发布，应用UI及浮动显示尚未实测。\n'+s[index:]
p.write_text(s,encoding='utf-8')
p = root/'PET_NAMES.md'
s = p.read_text(encoding='utf-8')
anchor = '| `nene_classical_lolita` | `nene_classical_lolita` | 宁宁 · 古典洛丽塔 · 红心皇后 |'
assert anchor in s
s = s.replace(anchor, anchor+'\n| 新建，无旧名称 | `nene_chinoiserie` | 宁宁 · 新中式礼装 |',1)
s = s.replace('v1.8.0合集采用本表的新名称；','v1.8.0合集采用此前九套的新名称；新中式礼装为本地新增，尚未发布。',1)
p.write_text(s,encoding='utf-8')
print('Updated README.md and PET_NAMES.md; published v1.8.0 remains nine pets.')
