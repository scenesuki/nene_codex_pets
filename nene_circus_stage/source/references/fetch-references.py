from pathlib import Path
import urllib.request,json,hashlib
root=Path(__file__).resolve().parent
sources=[]
def fetch(name,url):
 with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"}),timeout=50) as stream:data=stream.read()
 (root/name).write_bytes(data)
 sources.append({"file":name,"url":url,"sha256":hashlib.sha256(data).hexdigest()})
 return data
fetch("official-event-card.jpg","https://prtimes.jp/i/5397/3548/resize/d5397-3548-933937-2.jpg")
fetch("official-profile.html","https://pjsekai.sega.jp/character/unite04/nene/index.html")
url="https://raw.githubusercontent.com/Sekai-World/sekai-master-db-diff/main/cards.json"
with urllib.request.urlopen(url,timeout=60) as stream:data=stream.read()
card=next(c for c in json.loads(data) if c.get("prefix")=="ワンダーステッキ" and c.get("characterId")==15)
assert card["cardRarityType"]=="rarity_2"
keep={k:v for k,v in card.items() if k not in ["cardParameters","specialTrainingCosts","masterLessonAchieveResources"]}
(root/"wand-card-game-data.json").write_text(json.dumps({"source":url,"database_sha256":hashlib.sha256(data).hexdigest(),"card":keep},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
sources.append({"file":"wand-card-game-data.json","url":url,"database_sha256":hashlib.sha256(data).hexdigest(),"status":"non-official game-data mirror"})
(root/"sources.json").write_text(json.dumps(sources,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(keep,ensure_ascii=False,indent=2))
