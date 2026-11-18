# Cereno Scientific – oberoende investeraröversikt

Arbetsregler för alla uppdateringar: läs [AGENTS.md](AGENTS.md), följ varje följdändring tills inget återstår och kontrollera därefter de andra aktiesidorna.

Statisk investerarsida på svenska inspirerad av [SynAct-sidan](https://steffestygg-boop.github.io/synact/) med mörkt responsivt gränssnitt, finansieringskalkyler, aviserad emission och konkursbarometer, klickbara kvartalsmilstolpar, värderingsscenario och nyhetsflöde.

**Webbadress efter aktiverad GitHub Pages:** https://steffestygg-boop.github.io/cereno/

Om publicering inte sker automatiskt: öppna **Settings → Pages → Build and deployment → Source = GitHub Actions** och kontrollera Actions-loggar.


## Big Pharma-due diligence och riskbarometrar (17 november 2026)

Ramverk: [Vision Lifesciences – Pharma Due Diligence Checklist](https://visionlifesciences.com/insights/pharma-due-diligence-checklist). `data/financing_model.json → partner_due_diligence` innehåller den **manuellt granskade** bedömningen för sju områden: klinik, patent/IP, regulatoriskt, kommersiellt, finansiellt, tillverkning/CMC och juridik/avtal. Den visar också nästa tänkbara beslutströskel hos en köpare, kapitaltiming, tre finansieringsscenarier och okända faktorer. Sidan läser detta underlag direkt från JSON.

**Princip:** Klinisk/långsiktig potential, sannolikhet och **timing** för ett Big Pharma-avtal samt bolagets finansieringsbehov är olika frågor. Ett uteblivet avtal är inte bevis på en avvisad tillgång. Antag inga garanterade framtida upfrontbetalningar eller optionslikvider som kassa. Skilj verifierade rapportuppgifter från subjektiva DD-bedömningar och undvik att dubbelräkna risk.

Cerenos redan **aviserade** företrädesemission visas separat från konkursbarometern. Konkursskalan är ett subjektivt **stressindex**, inte en konkurssannolikhet. Efter en antagen emission får osäker partner-timing en extra analytisk poäng i stresscenariot; dagens ej fullföljda emission behåller sin separata risknivå.


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

### Klickbara fördjupningar till Veckans nyheter – november 2026

- Varje händelse i **Händelser under veckan** är nu en **helklickbar, tangentbordsstyrd knapp**, som öppnar en informationsruta med rubrik, en konkret sammanfattning, viktiga siffror, bakgrund, ekonomisk/klinisk betydelse och länk till den granskade originalkällan. Stäng med **Escape**, stängknappen eller klick på bakgrunden; fokus återgår till händelsen.
- De korta händelsekorten visar också fakta och siffror **utan att man behöver klicka**. Exempelvis får analytikeruppdateringar tydliga tidigare och nya värden (ABG 1,80 → 2,10 kr), studier får antal patienter och finansieringsbesked får villkor och belopp.
- Generiska innehållstexter som `Rapporterad kassa och historiskt kassaflöde är inte en dagsaktuell finansieringsprognos` har tagits bort från händelsekorten. Om en obekräftad RSS-rubrik saknar tillräcklig information används **inte** en påhittad förklaring; källan kan öppnas från informationsrutan.
- `data/weekly_event_details.json` innehåller **källgranskade** fördjupningar för viktiga händelser. Söndagsjobbet använder dessa plus `body`/`meaning` från redan dokumenterade milstolpar när det skapar `data/weekly_news.json`, så att tidigare manuellt förtydligade nyheter inte skrivs över med generiskt standardinnehåll.
- Källgranskade uppgifter hålls åtskilda från automatiskt inlästa rubriker. Källgranskade analysscenarier är fortfarande inte traditionella garanterade kursmål.

## Aktiekurs – automatisk och tidsstämplad (november 2026)

Under **Aktien** visas nu kursen med samma utformning som på SynAct-sidan: stor kurs i kronor, källa och den **faktiska kurstidpunkten**. TradingViews separata inbäddade kursruta har ersatts med en direktläst kursruta; en länk till TradingView finns kvar för jämförelse. Kursen kan vara fördröjd.

- `scripts/update_stock_quote.py` hämtar Cereno Scientific B (Yahoo-symbol `CRNO-B.ST`) från Yahoo Finances chart-endpoint och kontrollerar bolagssymbol, SEK, positivt kursvärde och tidsstämpel. Hämtningen sker automatiskt via `.github/workflows/refresh-stock-quote.yml` ungefär var 20:e minut på vardagar, med hänsyn till att GitHub Actions kan fördröjas och den externa kurskällan ibland kan vara otillgänglig.
- Kursen sparas i `data/stock_quote.json`. Webbplatsen hämtar filen vid öppning och kontrollerar om den ändrats varannan minut. Om kursen är från föregående handelsdag ska **detta datum synas**, inte klockslaget då GitHub Actions senast körde.
- Kurser under en krona behåller fler decimaler för att inte förlora meningsfull prisprecision. Kurserna har ingen automatisk påverkan på analysens emissionsrisk, milstolpar eller andra finansieringsantaganden.
- Källa och tidsstämpel visas intill kursen. Vid fel i kursleverantören behålls senast verifierade kurs och den ska inte presenteras som dagens livekurs. Regressionstester i `tests/test_stock_quote.py` kontrollerar kursvalidering och kursrutan.


### Kontrollerad daglig nyhetsbevakning – november 2026

**09.00 svensk tid varje dag:** `.github/workflows/weekly-news.yml` startar två alternativa UTC-tidpunkter (07 eller 08 UTC). Skriptet väljer rätt starttid efter sommar-/vintertid med hjälp av **vilket cron-uttryck som utlöste körningen**, inte vilken minut GitHub Actions råkar starta jobbet. En giltig körning får därför inte falla bort om GitHub blir försenat. Manuell omkörning fungerar oavsett klockslag.

**Eftermiddagskontroll på vardagar:** ytterligare körning kl. 14.00 UTC (15.00 på vintern / 16.00 på sommaren) fångar nyheter som publiceras senare än morgonsökningen.

**Flera oberoende nyhetskällor:** systemet söker direkt i respektive bolags MFN-lista över originalpressmeddelanden, kompletterat med breda Google News-frågor och mer riktade sökningar mot bl.a. BioStock, Börsvärlden samt analysfirmornas publiceringsplattformar. Såväl kliniska nyheter som finansiering, VD-förändringar, styrelsebeslut, aktieköp och analytikeruppdateringar bevakas.

**Veckogränser och dubbletter:** innehållet för innevarande vecka avser måndag till dagens datum. Händelser som hör till en tidigare ISO-vecka flyttas inte av misstag till en ny vecka. Ursprungliga bolagsmeddelanden prioriteras framför sekundära rubriksammanfattningar och dubbla MFN-återgivningar filtreras. Tidigare veckors arkiv förblir läsbart.

**Källkvalitet:** automatiskt insamlade rubriker märks som sådana och får inte påhittade sammanfattningar. Källgranskade fördjupningar med verifierade nyckeltal i `data/weekly_event_details.json` visas som klickbara informationsrutor. GitHub Actions och Google News ger ingen absolut garanti för start exakt 09.00 eller att samtliga nyheter indexeras omedelbart.

**Separata analyser:** kursrutan kan uppdateras ungefär var 20:e minut på handelsdagar. Emissions-/finansieringsrisken samt kliniska milstolpar har andra egna datakällor och uppdateringsrutiner; den dagliga nyhetssökningen innebär inte att varje risk- eller milstolpsantagande automatiskt skrivs om utan underlag.
