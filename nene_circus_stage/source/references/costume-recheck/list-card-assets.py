"""Read the public viewer's documented asset listing for this card only."""
import concurrent.futures
import json
from pathlib import Path
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

base = "https://storage.sekai.best/sekai-jp-assets/"
prefixes = [f"character/{kind}/res015_no005/" for kind in
            ("member", "member_cutout", "member_cutout_trm")]
def listing(prefix):
    url = base + "?" + urllib.parse.urlencode({"list-type": "2", "max-keys": "100", "prefix": prefix})
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=25) as response:
            data = response.read()
        root = ET.fromstring(data)
        entries = [{child.tag.split("}")[-1]: child.text for child in element}
                   for element in root.iter() if element.tag.split("}")[-1] == "Contents"]
        return {"prefix": prefix, "url": url, "entries": entries}
    except Exception as error:
        return {"prefix": prefix, "url": url, "error": str(error)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(listing, prefixes))
(Path(__file__).parent / "card-asset-listing.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
print(json.dumps(results, indent=2))
