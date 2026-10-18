"""Find public viewer image path code, without guessing more asset URLs."""
import json
from pathlib import Path
import urllib.request

url = "https://api.github.com/repos/Sekai-World/sekai-viewer/git/trees/dev?recursive=1"
request = urllib.request.Request(url, headers={"User-Agent": "nene-costume-reference-check"})
with urllib.request.urlopen(request, timeout=25) as response:
    tree = json.load(response)
paths = [entry["path"] for entry in tree["tree"] if entry["type"] == "blob"
         and entry["path"].startswith("src/")
         and any(term in entry["path"].lower() for term in ("card", "asset", "config"))]
record = {"source": url, "commit": tree["sha"], "paths": paths}
(Path(__file__).parent / "viewer-source-paths.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print("\n".join(paths))
