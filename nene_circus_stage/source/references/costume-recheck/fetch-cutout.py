"""Retrieve complete game-art cutouts rather than rectangular card crops."""
import concurrent.futures
import hashlib
import io
import json
from pathlib import Path
import urllib.request
from PIL import Image

folder = Path(__file__).resolve().parent
sources = [
    ("wand-cutout-en.png", "https://storage.sekai.best/sekai-en-assets/character/member_cutout_trm/res015_no005/normal.png"),
    ("wand-cutout-tw.png", "https://storage.sekai.best/sekai-tc-assets/character/member_cutout_trm/res015_no005/normal.png"),
    ("wand-cutout-kr.png", "https://storage.sekai.best/sekai-kr-assets/character/member_cutout_trm/res015_no005/normal.png"),
]
def fetch(entry):
    name, url = entry
    try:
        destination = folder / name
        if destination.exists():
            data = destination.read_bytes()
        else:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=25) as response:
                data = response.read()
            Image.open(io.BytesIO(data)).verify()
            destination.write_bytes(data)
        image = Image.open(io.BytesIO(data))
        return {"file": name, "url": url, "size": list(image.size), "mode": image.mode,
                "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
                "source_status": "community game-art mirror; visual completeness must be inspected"}
    except Exception as error:
        return {"file": name, "url": url, "error": str(error)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch, sources))
(folder / "regional-cutout-download-record.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(results, ensure_ascii=False, indent=2))
