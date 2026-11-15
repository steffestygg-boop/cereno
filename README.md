# Cereno Scientific – oberoende investeraröversikt

Statisk investerarsida på svenska inspirerad av [SynAct-sidan](https://steffestygg-boop.github.io/synact/) med mörkt responsivt gränssnitt, finansieringskalkyler, emissionsbarometer, klickbara kvartalsmilstolpar, värderingsscenario och nyhetsflöde.

**Webbadress efter aktiverad GitHub Pages:** https://steffestygg-boop.github.io/cereno/

Om publicering inte sker automatiskt: öppna **Settings → Pages → Build and deployment → Source = GitHub Actions** och kontrollera Actions-loggar.

## Det som ingår
- **Aktien:** extern TradingView-widget. Rapporterat antal aktier och kassa är historiska och tydligt daterade.
- **Pipeline:** CS1/EPIMODE (PAH), CS014 (PH-ILD), CS585 (APS).
- **Finansiering:** planerad 400 Mkr-unitsemission; skillnad mellan brutto och verklig kassa; Fenjas 70 Mkr-kvittning och kontant återbetalning som en varierbar simulator.
- **Utspädning:** antagen teckningskurs, nya aktier och utspädningskvot, utan att gissa kommande faktiska emissionsvillkor.
- **Emissionsbarometer:** den nuvarande emissionen är redan aviserad, varför den inte hanteras som en ny framtida riskhändelse. För ytterligare framtida emissioner finns ett **subjektivt, explicit villkorat scenario** med 3/6/12 månader; användaren kan ändra basantagandet och klicka på ∑ för uträkning och känslighet.
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
