"""Preserve the discovered character design-sheet scan as secondary evidence."""
import hashlib
import io
import json
from pathlib import Path
import urllib.request
from PIL import Image

folder = Path(__file__).resolve().parent
url = "https://i0.hdslb.com/bfs/article/0742c9502aa7fff9675ecb02c548dd98298252208.jpg"
request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Referer": "https://www.bilibili.com/"})
with urllib.request.urlopen(request, timeout=25) as response:
    data = response.read()
image = Image.open(io.BytesIO(data))
image.verify()
destination = folder / "nene-design-sheet-scan.jpg"
assert not destination.exists()
destination.write_bytes(data)
record = {"file": destination.name, "url": url,
          "source_page": "https://www.bilibili.com/opus/854907901648568377",
          "size": list(Image.open(io.BytesIO(data)).size),
          "sha256": hashlib.sha256(data).hexdigest(),
          "status": "community-hosted design-sheet scan; verify visible outfit and page context before use"}
(folder / "design-sheet-download-record.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record, indent=2))
