"""Read the installed Codex pet contract without modifying the application."""
import hashlib
import json
import struct
from pathlib import Path

root = Path(__file__).resolve().parents[1]
archive = Path(r"C:\Program Files\WindowsApps\OpenAI.Codex_26.1013.4894.0_x64__2p2nqsd0c76g0\app\resources\app.asar")
with archive.open("rb") as stream:
    sizes = struct.unpack("<4I", stream.read(16))
    directory = json.loads(stream.read(sizes[3]))
    entries = {}
    def paths(node, prefix=""):
        for key, value in node.get("files", {}).items():
            name = prefix + key
            if "files" in value:
                yield from paths(value, name + "/")
            else:
                yield name, value
    for name, node in paths(directory):
        if not (name.startswith("webview/assets/app-initial-") or name.startswith(".vite/build/src-")) or not name.endswith(".js"):
            continue
        stream.seek(8 + sizes[1] + int(node["offset"]))
        data = stream.read(node["size"])
        text = data.decode("utf-8")
        snippets = {}
        markers = ["version:2,width:1536", "nlo={failed:", "GK=1536", "spriteVersionNumber", "spritesheetPath"]
        for marker in markers:
            index = text.find(marker)
            if index < 0:
                continue
            snippets[marker] = text[max(0, index - 50):index + 1300]
        if "version:2,width:1536" in snippets or "spritesheetPath" in snippets:
            entries[name] = {"sha256": hashlib.sha256(data).hexdigest(), "excerpts": snippets}
assert any("version:2,width:1536" in entry["excerpts"] for entry in entries.values())

result = {"checked_on": "2026-10-18", "archive": str(archive), "entries": entries}
output = root / "references/app-contract-verification.json"
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(output)
