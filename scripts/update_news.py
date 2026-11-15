"""Hämta Cereno-rubriker utan att skriva över redaktionellt verifierade nyheter."""
import datetime as dt
import email.utils
import json
import pathlib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILE = ROOT / "data" / "news.json"
QUERY = '("Cereno Scientific" OR "Cereno CS1" OR "Cereno CS014") when:90d'
URL = "https://news.google.com/rss/search?" + urllib.parse.urlencode(
    {"q": QUERY, "hl": "sv", "gl": "SE", "ceid": "SE:sv"}
)
request = urllib.request.Request(
    URL, headers={"User-Agent": "Mozilla/5.0 (compatible; CerenoInvestorTracker/1.0)"}
)
with urllib.request.urlopen(request, timeout=30) as response:
    xml = response.read()
root = ET.fromstring(xml)
previous = json.loads(FILE.read_text(encoding="utf-8"))
pinned = [item for item in previous.get("items", []) if item.get("verified")]
items = list(pinned)
seen = {item.get("url") for item in items}
added = 0
for node in root.findall("./channel/item"):
    title = (node.findtext("title") or "").strip()
    url = (node.findtext("link") or "").strip()
    if "cereno" not in title.casefold() or not url or url in seen:
        continue
    published = (node.findtext("pubDate") or "").strip()
    try:
        date = email.utils.parsedate_to_datetime(published).astimezone(
            dt.timezone.utc
        ).date().isoformat()
    except (ValueError, TypeError, IndexError):
        date = ""
    items.append({
        "title": title,
        "url": url,
        "date": date,
        "source": (node.findtext("source") or "").strip(),
        "verified": False
    })
    seen.add(url)
    added += 1
if added == 0:
    raise RuntimeError("Inga nya tillgängliga Cereno-rubriker; bevarar föregående fil")
pinned.sort(key=lambda x: x.get("date", ""), reverse=True)
auto = sorted((x for x in items if not x.get("verified")),
              key=lambda x: x.get("date", ""), reverse=True)[:20]
payload = {
    "updated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
    "feed": "Källkontrollerade notiser + automatiska, obekräftade Google News RSS-rubriker",
    "items": pinned + auto
}
FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8")
print(f"Sparat {len(pinned)} verifierade och {len(auto)} RSS-rubriker")
