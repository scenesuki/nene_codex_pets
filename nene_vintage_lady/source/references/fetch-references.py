from pathlib import Path
import urllib.request,json,hashlib
root=Path(__file__).resolve().parent
sources=[]
def get(name,url):
 with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"}),timeout=45) as r:data=r.read()
 (root/name).write_bytes(data)
 sources.append({"file":name,"url":url,"sha256":hashlib.sha256(data).hexdigest()})
 return data
get("edo-card-wallpaper.jpg","https://anihonetwallpaper.com/image/2024/07/202401166-ProjectSEKAI-KusanagiNene.jpg")
get("official-event-card.jpg","https://prcdn.freetls.fastly.net/release_image/5397/5855/5397-5855-e2e538912f06afa4d632d0d3728264d9-600x338.jpg")
get("official-profile.html","https://pjsekai.sega.jp/character/unite04/nene/index.html")
url="https://raw.githubusercontent.com/Sekai-World/sekai-master-db-diff/main/cards.json"
with urllib.request.urlopen(url,timeout=60) as r:data=r.read()
cards=json.loads(data)
card=next(c for c in cards if c.get("prefix")=="江戸の町並みに飲まれて")
assert card["characterId"]==15 and card["cardRarityType"]=="rarity_2"
keep={k:v for k,v in card.items() if k not in ["cardParameters","specialTrainingCosts","masterLessonAchieveResources"]}
(root/"edo-card-game-data.json").write_text(json.dumps({"source":url,"database_sha256":hashlib.sha256(data).hexdigest(),"card":keep},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
sources.append({"file":"edo-card-game-data.json","url":url,"database_sha256":hashlib.sha256(data).hexdigest(),"status":"non-official game-data mirror"})
(root/"sources.json").write_text(json.dumps(sources,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(keep,ensure_ascii=False,indent=2))
