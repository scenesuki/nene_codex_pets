"""Fetch public game-data grounding and card art without modifying other pets."""
import hashlib
import json
from pathlib import Path
import urllib.request

root = Path(__file__).resolve().parent
url = 'https://raw.githubusercontent.com/Sekai-World/sekai-master-db-diff/main/cards.json'
data = urllib.request.urlopen(url, timeout=45).read()
cards = [c for c in json.loads(data) if c.get('characterId') == 15 and 'movie' in c.get('prefix', '').lower()]
assert len(cards) == 1, [(c['id'], c['prefix']) for c in cards]
card = cards[0]
(root / 'movie-card-game-data.json').write_text(json.dumps({'source': url, 'database_sha256': hashlib.sha256(data).hexdigest(), 'card': card}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
asset = card['assetbundleName']
records = []
for name, source in [
    ('movie-card.png', f'https://storage.sekai.best/sekai-jp-assets/character/member/{asset}_rip/card_normal.png'),
    ('movie-cutout.png', f'https://storage.sekai.best/sekai-jp-assets/character/member/{asset}_rip/normal.png'),
    ('official-profile.html', 'https://pjsekai.sega.jp/character/unite04/nene/index.html'),
]:
    try:
        content = urllib.request.urlopen(source, timeout=45).read()
        (root / name).write_bytes(content)
        records.append({'file': name, 'url': source, 'sha256': hashlib.sha256(content).hexdigest()})
    except Exception as error:
        records.append({'file': name, 'url': source, 'error': str(error)})
(root / 'sources.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k:card.get(k) for k in ['id','characterId','cardRarityType','attr','prefix','assetbundleName','releaseAt']},ensure_ascii=False))
print(json.dumps(records,ensure_ascii=False))
