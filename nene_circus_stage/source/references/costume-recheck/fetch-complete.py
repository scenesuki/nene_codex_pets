"""Preserve uncropped card references for the user's costume correction."""
import concurrent.futures
import hashlib
import io
import json
from pathlib import Path
import urllib.request
from PIL import Image

folder = Path(__file__).resolve().parent
sources = [
    ("card-full.png", "https://static.wikia.nocookie.net/projectsekai/images/b/b9/Wonder_Wand.png/revision/latest?cb=20201106094320"),
    ("card-transparent.png", "https://static.wikia.nocookie.net/projectsekai/images/7/7b/Wonder_Wand_transparent.png/revision/latest?cb=20201116211857"),
    ("gallery-card.webp", "https://pjsekai.gamedbs.jp/image/chara/member/1608018546125_zkgqiy21.webp"),
    ("gallery-transparent.webp", "https://pjsekai.gamedbs.jp/image/chara/member_trm/1608020246057_vlofx0t5.webp"),
]
def fetch(entry):
    name, url = entry
    destination = folder / name
    try:
        if destination.exists():
            data = destination.read_bytes()
        else:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=25) as response:
                data = response.read()
            image = Image.open(io.BytesIO(data))
            image.verify()
            destination.write_bytes(data)
        image = Image.open(io.BytesIO(data))
        return {"file": name, "url": url, "size": list(image.size), "mode": image.mode,
                "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
                "source_status": "community mirror of game artwork; cross-check with official cropped announcement"}
    except Exception as error:
        return {"file": name, "url": url, "error": str(error)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(fetch, sources))
(folder / "download-record.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(results, ensure_ascii=False, indent=2))
assert any("size" in item for item in results), "No complete card image obtained"
