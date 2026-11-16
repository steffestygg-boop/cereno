# Cereno Scientific – oberoende investeraröversikt

Statisk investerarsida på svenska inspirerad av [SynAct-sidan](https://steffestygg-boop.github.io/synact/) med mörkt responsivt gränssnitt, finansieringskalkyler, emissionsbarometer, klickbara kvartalsmilstolpar, värderingsscenario och nyhetsflöde.

**Webbadress efter aktiverad GitHub Pages:** https://steffestygg-boop.github.io/cereno/

Om publicering inte sker automatiskt: öppna **Settings → Pages → Build and deployment → Source = GitHub Actions** och kontrollera Actions-loggar.

## Det som ingår
- **Aktien:** extern TradingView-widget. Rapporterat antal aktier och kassa är historiska och tydligt daterade.
- **Pipeline:** CS1/EPIMODE (PAH), CS014 (PH-ILD), CS585 (APS).
- **Finansiering:** planerad 400 Mkr-unitsemission; skillnad mellan brutto och verklig kassa; Fenjas 70 Mkr-kvittning och kontant återbetalning som en varierbar simulator.
- **Utspädning:** antagen teckningskurs, nya aktier och utspädningskvot, utan att gissa kommande faktiska emissionsvillkor.
- **Emissionsavsnitt:** konkreta kända villkor för aviserad 400 Mkr-emission, teckningskurs när den beslutas och Fenja/utspädningssimulator.
- **Konkursbarometer:** riskbedömning för betalningsförmåga, villkorad emissionsfinansiering och skuld; två tydligt åtskilda lägen (aktuellt respektive scenario), utan fabricerade konkursprocentsatser.
- **Varningssignaler:** källänkade, datumstämplade observationer. Informationsdatum i datafilen ska uppdateras redaktionellt efter nya finansbesked.
- **Milstolpar:** kvartalsbaserad klickbar tidslinje med filtrering och orange förseningsmarkering. Q1→Q3 2027 för CS014 är källstyrkt; FPI försenat, men utan påhittat antal kvartal.
- **Värderingsgraf:** klickbara hypotetiska bolagsvärden och härledd kurs per aktie före/efter ett illustrativt emissionsscenario. Inga fabricerade analytikerriktkurser.
- **Nyheter:** fast verifierat grundurval och daglig RSS-hämtning via Actions.
- **Beräkningsrutor:** klicka ∑ eller ⓘ för formel, insatta värden, förutsättningar och källor.

## Källor & viktig säkerhetsregel
- [Cerenos emission & Fenja, 12 nov 2026](https://mfn.se/a/cereno-scientific/cereno-scientific-avser-genomfora-en-foretradesemission-av-units-om-cirka-400-msek-med-fokus-pa-den-globala-fas-iib-studien-epimode-och-erhaller-forlangd-lanefinansiering-om-upp-till-175-msek)
- [Cerenos Q3 2026-rapport](https://www.cerenoscientific.com/~/media/Files/C/cereno-scientific/corp/results-and-presentations/2026/Cereno%20Scientific%20Delarsrapport%20Q3%202026.pdf)
- [Cerenos Q3-kommentar och kliniska tidplan](https://www.cerenoscientific.com/sv/nyhetsrum/pressmeddelanden?slug=cereno-scientific-publicerar-delarsrapport-for-tredje-kvartal-2026)
- [EPIMODE-uppdateringen, 8 oktober 2026](https://view.news.eu.nasdaq.com/view?id=bac2b3efd349cf90706b8cf56dc46c45d&lang=en&src=micro)
- [CS014-produktsidan – äldre Q1-uppgift](https://www.cerenoscientific.com/sv/vetenskap-pipeline/cs014)

Automatiken ändrar **inte** kassa, lån, kliniska data, emissionsvillkor eller tidplaner från osäkra nyhetsrubriker. Dessa ändras manuellt efter originalkällans faktiska besked. Aktiekurswidgeten kan vara fördröjd. Webbplatsen är varken officiell eller finansiell rådgivning.

## Filer
`index.html` – allt UI och beräkningar i en självbärande statisk HTML.
`data/milestones.json` – källanknutna kliniska och finansiella händelser.
`data/financing_model.json` – granskade finansvillkor och antaganden.
`data/financing.json` – varningssignaler och daterad finansieringsstatus.
`data/news.json` – nyheter och rubriker.
`scripts/update_news.py` – Google News RSS-inläsning.
`.github/workflows/` – daglig nyhetshämtning och Pages-publicering.

Senaste redaktionella kontroll: 15 november 2026.

## Uppdatering 15 november 2026: konkursbarometer

Emissionsbarometern har ersatts av två delar: den aviserade företrädesemissionen och Konkursbarometern. Emissionsvillkoren är ännu inte formellt beslutade per 15 november 2026; extra bolagsstämma väntas 15 december och styrelsebeslut omkring 17–18 december. Konkursbarometern bygger på rapporterad Q3-kassa och historiskt kassaflöde, plus scenarier för teckning och Fenja-reglering; poäng 1–10 är ett illustrativt index och **inte** statistisk konkurssannolikhet. Finansieringsmisslyckande innebär inte automatiskt juridisk konkurs. Ingen automatisk RSS-rubrik ändrar verifierade kassasiffror eller risknivåer utan manuell kontroll.

Källor: [Cerenos regulatoriska emissionserbjudande](https://www.cerenoscientific.com/sv/nyhetsrum/pressmeddelanden?slug=cereno-scientific-avser-genomfora-en-foretradesemission-av-units-om-cirka-400-msek-med-fokus-pa-den-globala-fas-iib-studien-epimode-och-erhaller-forlangd-lanefinansiering-om-upp-till-175-msek), [Cerenos Q3-rapport](https://www.cerenoscientific.com/sv/nyhetsrum/pressmeddelanden?slug=cereno-scientific-publicerar-delarsrapport-for-tredje-kvartal-2026).


## Veckans nyheter – söndagsarkiv

Avsnittet **Veckans nyheter** ligger direkt efter **Aktien** och hämtar `data/weekly_news.json`. Den senaste sammanställda ISO-veckan visas direkt; äldre veckor ligger hopfällda i ett arkiv med **år, veckonummer och datumintervall**.

- **Söndag kl. 19:30 UTC:** `.github/workflows/weekly-news.yml` kör `scripts/update_weekly_news.py`. Det motsvarar **20:30 svensk vintertid eller 21:30 svensk sommartid**.
- **Måndag kl. 09:30 UTC:** En kompletterande körning fångar sena söndagsnyheter och den ordinarie finansiella veckouppdateringen. Även manuella körningar kan startas i GitHub Actions.
- **Nyhetsunderlag:** publicerade, daterade nyhetsrubriker via Google News RSS; `data/news.json`; redan dokumenterade milstolpar; tillgängliga risk-/emissionsdata i `data/financing.json` och `data/financing_model.json`.
- **Analysförändringar:** veckans sparade modellvärden, nya finansieringsvarningar, emissionsstatus och ändrade milstolpar jämförs mot föregående veckoutgåvas ögonblicksbild. För Cereno innebär detta emissionsstatus och ändringar i konkurs-/finansieringsmodellen, inte en påhittad emissionssannolikhet.
- **Källskillnad:** händelser från tidigare källgranskade dataposter märks som sådana. RSS-rubriker märks tydligt som **inte fulltextgranskade**; systemet drar inte egna slutsatser om klinisk effekt eller kassaförändringar utifrån rubriktext.
- **Historik:** äldre veckor bevaras i samma JSON-fil, inte som en ny uppsättning som skriver över förra veckan. De inledande veckorna är 2026-W45 och 2026-W46. Veckor som rekonstrueras i efterhand får inte tilldelas finansieringsdata som först blev kända en senare vecka.
- **Tester:** `python -m unittest discover -s tests -p 'test_weekly_news.py'` kontrollerar ISO-veckor, veckogränser, proveniens, daterade milstolpar och att äldre veckor inte får senare emissionsvärden.

**Begränsning:** GitHub Actions är en schemalagd best-effort-körning och RSS-sökning är inte heltäckande. Ett automatiskt skript kan inte i sig analysera hela innehållet i alla artiklar. Avsnittet ger källanknutna, korta händelseöversikter, inte garanterat varje relevant uppgift eller en självständig faktagranskad fulltextsanalys. Vid otillgängliga RSS-källor används även de redan sparade lokala källorna.
