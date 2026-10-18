"""Read the installed Codex pet contract without modifying the application."""
import hashlib
import json
import struct
from pathlib import Path

root = Path(__file__).resolve().parents[2]
archive = Path(r"C:\Program Files\WindowsApps\OpenAI.Codex_26.1007.2314.0_x64__2p2nqsd0c76g0\app\resources\app.asar")
with archive.open("rb") as stream:
    sizes = struct.unpack("<4I", stream.read(16))
    directory = json.loads(stream.read(sizes[3]))
    entries = {}
    for name, markers in {
        "webview/assets/app-initial-b8e1c8014bb4.js": ["version:2,width:1536", "slo={failed:", "function _lo"],
        ".vite/build/src-BJv5Mk7n.js": ["GK=1536", "async function XK", "function QK", "async function tq"],
    }.items():
        node = directory
        for part in name.split("/"):
            node = node["files"][part]
        stream.seek(8 + sizes[1] + int(node["offset"]))
        data = stream.read(node["size"])
        text = data.decode("utf-8")
        snippets = {}
        for marker in markers:
            index = text.find(marker)
            if index < 0:
                raise ValueError(f"Missing contract marker: {marker}")
            snippets[marker] = text[max(0, index - 50):index + 1300]
        entries[name] = {"sha256": hashlib.sha256(data).hexdigest(), "excerpts": snippets}

result = {"checked_on": "2026-10-13", "archive": str(archive), "entries": entries}
output = root / "source/references/app-contract-verification.json"
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(output)
