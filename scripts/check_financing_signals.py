"""Bevaka nya Cereno-finansieringsrubriker; ändra ALDRIG verifierade belopp automatiskt."""
import datetime as dt
import email.utils
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILE = ROOT / "data" / "financing.json"
QUERY = '"Cereno Scientific" (emission OR teckning OR konvertibel OR Fenja OR handelsstopp OR finansiering OR kapitalbehov OR partner) when:35d'
URL = "https://news.google.com/rss/search?" + urllib.parse.urlencode(
    {"q": QUERY, "hl": "sv", "gl": "SE", "ceid": "SE:sv"}
)
data = json.loads(FILE.read_text(encoding="utf-8"))
base = [a for a in data.get("alerts", []) if not a.get("auto_id")]
now = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
reviews = []
try:
    request = urllib.request.Request(URL, headers={"User-Agent": "CerenoRiskWatch/1.0"})
    with urllib.request.urlopen(request, timeout=25) as response:
        root = ET.fromstring(response.read())
    seen = set()
    for item in root.findall("./channel/item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if not link or "cereno" not in title.casefold() or link in seen:
            continue
        if not re.search(r"emission|teckningskurs|konvertib|fenja|handelsstopp|finansier|kapitalbehov|likviditet|studieförsening|försenad|skulder|betalningsanstånd|partneravtal", title, re.I):
            continue
        seen.add(link)
        pub = (item.findtext("pubDate") or "").strip()
        try:
            published = email.utils.parsedate_to_datetime(pub).date().isoformat()
        except (ValueError, TypeError, IndexError):
            published = ""
        reviews.append({
            "auto_id": link,
            "level": "bevakning",
            "title": "Rubrik kräver faktagranskning: " + title[:135],
            "detail": "Automatiskt hittad rubrik. Ingen självständig verifiering av belopp, avtal, kursrörelse eller faktisk nyemission.",
            "status": "Obekräftad RSS-träff",
            "date": published,
            "source": link,
            "next_step": "Öppna bolagets originalmeddelande och verifiera innehållet innan grunddata ändras."
        })
        if len(reviews) >= 6:
            break
    data["coverage_status"] = "RSS-genomsökt; rubriker kräver manuell granskning"
    data["automated_checked"] = True
    data["failed_sources"] = []
except (OSError, ValueError, ET.ParseError) as error:
    data["coverage_status"] = "Begränsad täckning: RSS misslyckades"
    data["automated_checked"] = False
    data["failed_sources"] = [str(error)[:140]]
    # Bevara föregående rubrikträffar om nätverket är otillgängligt.
    reviews = [a for a in data.get("alerts", []) if a.get("auto_id")][:6]
data["alerts"] = base + reviews
data["automated_checked_at"] = now
data["review_needed"] = [
    {"date": a["date"], "title": a["title"], "source": a["source"]}
    for a in reviews
]
if "--weekly" in sys.argv:
    data["weekly_checked_at"] = now
    data["weekly_note"] = (
        "Nya rubriker sökta; verifierade finansfakta och användarstyrt "
        "sannolikhetsscenario är oförändrade utan originalkällor."
    )
FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8")
print(data["coverage_status"], "Rubrikträffar:", len(reviews))
