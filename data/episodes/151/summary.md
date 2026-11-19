## 1. Omówienie Technology Radar Volume 32 od Thoughtworks
Summary: Prowadzący omawiają najnowszą edycję Technology Radar od firmy Thoughtworks. Wyjaśniają, że jest to cykliczna publikacja zawierająca rekomendacje dotyczące technologii, podzielona na cztery obszary oraz cztery poziomy adopcji: adopt, trial, assess i hold.

Speaker summaries:
- Łukasz Kałużny: Wyjaśnia, że Technology Radar jest opinionated z perspektywy jednej firmy, ale zawiera przydatne informacje i opinie dotyczące różnych technologii.
- Szymon Warda: Tłumaczy strukturę raportu i znaczenie poszczególnych kręgów adopcji, od najbardziej rekomendowanych (adopt) po niezalecane (hold).

Most interesting quotes:
1. Łukasz Kałużny: "Thoughtworks to jest taka duża firma doradcza, choć relatywnie mała w porównaniu do innych firm doradczych, ponieważ zatrudnia około pięciu, sześciu tysięcy konsultantów. Co kilka miesięcy publikują Technology Radar."
2. Szymon Warda: "Każdy z tych elementów podzielony jest na cztery kręgi. Zaczynając od najbardziej wewnętrznego, czyli adopt - to oznacza, że oni rekomendują bezpośrednie wykorzystanie danej technologii."

## 2. Fast Testing w kontekście modeli AI
Summary: Prowadzący dyskutują o Fast Testing, które znalazło się w kategorii adopt w raporcie. Technika ta polega na testowaniu API modeli AI poprzez wysyłanie różnorodnych zapytań w celu sprawdzenia odporności i zachowania.

Speaker summaries:
- Łukasz Kałużny: Wyraża wątpliwości co do użyteczności Fast Testing, wskazując, że lepszym rozwiązaniem jest walidacja schemy przed przekazaniem do serwera aplikacyjnego.
- Szymon Warda: Kwestionuje wartość Fast Testing w językach zarządzanych, sugerując, że technika ta ma ograniczoną przydatność poza wyłapywaniem lepszych komunikatów błędów.

Most interesting quotes:
1. Szymon Warda: "Fast testing koncentruje się na tym, że wszystkie modele AI i LLM są odpytywane w różnej formie przez różne API, co prowadzi do powstania chaosu."
2. Łukasz Kałużny: "Jeżeli walidujecie schemę, przeprowadzacie walidację przed przekazaniem do przetwarzania na waszym serwerze aplikacyjnym, co jest istotne, to schemat powinien być walidowany zanim trafi bezpośrednio do przetwarzania."

## 3. Software Bill of Materials (SBOM)
Summary: Prowadzący omawiają SBOM, który przeszedł z trial do adopt. Podkreślają rosnące znaczenie tego narzędzia ze względu na regulacje prawne oraz korzyści związane z bezpieczeństwem i zarządzaniem licencjami.

Speaker summaries:
- Szymon Warda: Wyjaśnia, że SBOM zyskał na znaczeniu ze względu na regulacje prawne i wymogi bezpieczeństwa, szczególnie w kontekście obrony przed atakami na łańcuch dostaw.
- Łukasz Kałużny: Podkreśla, że oprócz aspektów bezpieczeństwa, SBOM przynosi korzyści w zarządzaniu licencjami oprogramowania.

Most interesting quotes:
1. Szymon Warda: "Skąd to się wzięło? Regulacje prawne. Rząd brytyjski wprowadził AI Cybersecurity Code of Practice i CISA: AI Cybersecurity Collaboration Playbook, które właśnie tego wymagają."
2. Szymon Warda: "Efektem ubocznym posiadania dobrego SBOM-a jest też zarządzanie licencjami."

## 4. Architecture Advice Process
Summary: Prowadzący krytycznie analizują Architecture Advice Process, który znalazł się w kategorii trial. Wyrażają wątpliwości co do zdecentralizowanego podejścia, w którym każdy może podejmować decyzje architektoniczne po konsultacji z ekspertami.

Speaker summaries:
- Łukasz Kałużny: Zgadza się, że każdy powinien mieć możliwość kontrybuowania do architektury, ale uważa, że powinno to przechodzić przez proces review i akceptacji.
- Szymon Warda: Ostrzega, że zbyt duża decentralizacja w dużych organizacjach może prowadzić do chaosu i problemów z utrzymaniem spójności systemów.

Most interesting quotes:
1. Łukasz Kałużny: "Uważam, że taka osoba może zrobić ADR-a i powinien on przejść review i akceptację."
2. Szymon Warda: "Pewien poziom zwinności prowadzi w dłuższej perspektywie do bałaganu, to bardzo proste."
3. Łukasz Kałużny: "Gildia jest miejscem wymiany wiedzy i dyskusji na temat standardów, a nie podejmowania decyzji w kontekście kawałka systemu."

## 5. Just-in-time Privileged Access Management
Summary: Prowadzący omawiają Just-in-time Privileged Access Management, który znalazł się w kategorii trial. Wyrażają zdziwienie, że ta podstawowa praktyka bezpieczeństwa dopiero teraz znalazła się w raporcie.

Speaker summaries:
- Łukasz Kałużny: Wyraża zaskoczenie, że tak podstawowa praktyka bezpieczeństwa dopiero teraz pojawia się w raporcie.
- Szymon Warda: Podkreśla zalety tego podejścia, w tym możliwość audytu, ograniczony czas dostępu i konieczność uzasadnienia potrzeby podwyższonych uprawnień.

Most interesting quotes:
1. Łukasz Kałużny: "Just in Time Privileged Access Management to sytuacja, gdy w jakiejś chmurze czy narzędziu klikacie, aby otrzymać czy podnieść swoje uprawnienia i potwierdzacie to przez MFA."
2. Szymon Warda: "Co ważne, wszystko jest rejestrowane w audycie, musisz uzasadnić dlaczego potrzebujesz tych uprawnień, są one przyznawane na określony czas i jawnie ograniczone."

## 6. Wykorzystanie GenAI do zrozumienia legacy code
Summary: Prowadzący omawiają wykorzystanie modeli AI do analizy i zrozumienia starych baz kodu, które znalazło się w kategorii trial. Wyrażają opinię, że ta technologia ma duży potencjał i dziwią się, że nie znajduje się wyżej w raporcie.

Speaker summaries:
- Szymon Warda: Wyraża zdziwienie, że ta technologia jest tylko w kategorii trial, mimo że już teraz widać jej dużą wartość w praktyce.
- Łukasz Kałużny: Potwierdza, że ta technologia nie jest nowa w raporcie i była już wcześniej wymieniana.

Most interesting quotes:
1. Szymon Warda: "To jest coś, co już się dzieje. W przypadku tego typu zastosowań widzimy bardzo dużą wartość."
2. Szymon Warda: "Przepraszam, ale tutaj czekamy tylko na udoskonalenie narzędzi, które już zaczynają się pojawiać, więc dziwi mnie, że to jest tak nisko sklasyfikowane."

## 7. AI-powered UI Testing
Summary: Prowadzący omawiają testowanie UI wspierane przez AI, które znalazło się w kategorii assess. Szymon Warda podkreśla potencjał tej technologii w rozwiązaniu problemów związanych z kosztownym i niestabilnym testowaniem UI.

Speaker summaries:
- Szymon Warda: Wyjaśnia, że pojawiły się dwa podejścia do AI-powered UI Testing: modele fine-tune'owane na przetwarzanie zdjęć UI oraz połączenie modeli multimodalnych z informacjami o strukturze HTML.
- Łukasz Kałużny: Wyraża zainteresowanie tematem i zgadza się z potencjałem tej technologii.

Most interesting quotes:
1. Szymon Warda: "Testowanie UI jest niewyobrażalnie kosztowne, ciągle się zmienia, jest bardzo niestabilne i stanowi prawdziwą drogę przez mękę dla każdego, kto się tym zajmował."
2. Szymon Warda: "Z całego obszaru testowania, szczególnie elementów UI, to może być naprawdę mała rewolucja, jeśli rozwinie się w formie dobrych narzędzi, a ma na to szansę."

## 8. AI Accelerated Shadow IT na hold
Summary: Prowadzący z zadowoleniem komentują umieszczenie AI Accelerated Shadow IT w kategorii hold. Zgadzają się, że narzędzia AI powinny pozostać w rękach specjalistów IT, a nie być używane przez osoby nietechniczne z biznesu.

Speaker summaries:
- Łukasz Kałużny: Wyraża zadowolenie, że raport zaleca ograniczanie shadow IT w kontekście AI, podkreślając, że osoby nietechniczne często nie rozumieją konsekwencji używania takich narzędzi.
- Szymon Warda: Potwierdza, że takie podejście jest nie do utrzymania w dłuższej perspektywie.

Most interesting quotes:
1. Łukasz Kałużny: "Rozwiązania AI, jeśli chodzi o technologię, generowanie i inne funkcje, powinny pozostać w gestii IT. Osoby będące power userami z biznesu, które nie są z IT, niestety nie mają świadomości konsekwencji swoich działań."
2. Szymon Warda: "To jest nie do utrzymania na dłuższą metę, tak bym to określił."

## 9. Local Coding Assistant na hold
Summary: Prowadzący omawiają umieszczenie lokalnych asystentów kodowania (Local Coding Assistant) w kategorii hold. Zgadzają się z tą decyzją, argumentując, że jakość lokalnych modeli jest niższa, a koszty sprzętowe zbyt wysokie.

Speaker summaries:
- Łukasz Kałużny: Zgadza się z umieszczeniem lokalnych asystentów kodowania w hold, argumentując, że przepala się na to pieniądze i czas bez uzyskania odpowiedniej wartości.
- Szymon Warda: Wyjaśnia, że lokalne modele są zbyt wolne lub zbyt okrojone, a wyposażenie każdego dewelopera w odpowiedni sprzęt byłoby zbyt kosztowne.

Most interesting quotes:
1. Łukasz Kałużny: "Jest słusznie umieszczony w kategorii hold, ponieważ wydaje się na to pieniądze i czas bez uzyskania realnej wartości, gdyż jakość jest wbrew pozorom niższa."
2. Szymon Warda: "Te modele są po prostu zbyt wolne działając na lokalnej maszynie, albo są zbyt okrojone, choć działają szybko. Nie mamy wystarczających środków ani sprzętu, aby wyposażyć komputer każdego developera w odpowiednie karty graficzne."

## 10. SAFe (Scaled Agile Framework) na hold
Summary: Prowadzący z zadowoleniem komentują umieszczenie Scaled Agile Framework (SAFe) w kategorii hold. Krytykują to podejście jako nieefektywne i prowadzące do waterfallowego procesu pod przykrywką Agile.

Speaker summaries:
- Szymon Warda: Wyraża zadowolenie, że raport potwierdza, iż SAFe nie działa, spowalnia pracę i zamienia się w waterfall.
- Łukasz Kałużny: Krytycznie określa SAFe jako próbę zachowania waterfallowego podejścia pod przykrywką Agile.

Most interesting quotes:
1. Szymon Warda: "SAFe jest w kategorii hold, czyli Scaled Agile Framework. Jest w kategorii hold, co potwierdza, że to rozwiązanie w ogóle nie działa."
2. Łukasz Kałużny: "To jest: udawajmy, że stosujemy Agile, ale w rzeczywistości pracujmy w modelu waterfall i zabezpieczajmy się na każdym kroku, jednocześnie twierdząc, że jesteśmy zwinni."
3. Szymon Warda: "Nie znam osoby, która byłaby z tego zadowolona."

## 11. Claude Sonnet w trial
Summary: Prowadzący omawiają Claude Sonnet, który znalazł się w kategorii trial. Obaj wyrażają pozytywne opinie na temat tego modelu AI.

Speaker summaries:
- Szymon Warda: Potwierdza, że korzysta z Claude Sonnet i jest zadowolony z wyników.
- Łukasz Kałużny: Zauważa, że Szymon przekonał się do tego modelu.

Most interesting quotes:
1. Szymon Warda: "Claude Sonnet. Pierwszy raz pojawia się w raporcie. Obaj z niego korzystamy, wyniki są bardzo dobre."
2. Łukasz Kałużny: "Szymon się do niego przekonał."

## 12. Klein CLI and Editor
Summary: Prowadzący omawiają Klein CLI and Editor, wtyczkę do Visual Studio Code, która znalazła się w kategorii trial. Porównują ją do Cursora i dyskutują o jej funkcjonalnościach.

Speaker summaries:
- Szymon Warda: Opisuje funkcjonalności Klein, w tym wsparcie dla dużych baz kodu i Headless Browser Testing.
- Łukasz Kałużny: Wyraża sceptycyzm co do wartości Klein w porównaniu do innych narzędzi, zwłaszcza w kontekście ceny i funkcjonalności.

Most interesting quotes:
1. Szymon Warda: "To jest wtyczka do Visual Studio Code. Stanowi pewnego rodzaju alternatywę dla Cursora."
2. Łukasz Kałużny: "Jedynym naprawdę wartościowym elementem, jaki można z niego wyciągnąć, jest Headless Browser Support."

## 13. Cursor w trial
Summary: Prowadzący omawiają Cursor, narzędzie AI do kodowania, które znalazło się w kategorii trial. Wyrażają bardzo pozytywne opinie na jego temat, podkreślając jego funkcjonalności i efektywność.

Speaker summaries:
- Szymon Warda: Entuzjastycznie opisuje funkcjonalności Cursora, w tym wsparcie dla MCP, odnoszenie się do poprzednich rozmów i przeszukiwanie dokumentacji.
- Łukasz Kałużny: Żartobliwie komentuje entuzjazm Szymona, porównując go do mema z Futuramy.

Most interesting quotes:
1. Szymon Warda: "Jest liderem na rynku. Nie oszukujmy się, oni po prostu dominują w tej kategorii i działa to naprawdę dobrze, mogę to potwierdzić."
2. Łukasz Kałużny: "Szymon zachowywał się jak bohater mema z Futuramy: 'bierzcie moją kartę, bierzcie moje pieniądze', gdy zobaczył jak to działa po ostatnich aktualizacjach."
3. Szymon Warda: "Przypominają mi się czasy kodowania, kiedy uruchamiasz prostą komendę i mówisz, że idziesz coś zrobić, bo właśnie trwa kompilacja, a ona po prostu przetwarza dane."

## 14. D2 jako alternatywa dla Mermaid
Summary: Prowadzący omawiają D2, język do rysowania diagramów, który znalazł się w kategorii trial. Dyskutują o jego zaletach i wadach w porównaniu do Mermaid.

Speaker summaries:
- Szymon Warda: Opisuje D2 jako alternatywę dla Mermaid, z lepszym wyglądem wizualnym i możliwością przechodzenia między poziomami diagramów w studio.
- Łukasz Kałużny: Wyraża sceptycyzm co do wartości D2, szczególnie biorąc pod uwagę cenę studia.

Most interesting quotes:
1. Szymon Warda: "To jest odpowiednik Mermaid, czyli język do rysowania diagramów. I to jest pierwszy raz, gdy pojawia się w kategorii trial."
2. Szymon Warda: "Studio umożliwia przechodzenie między poziomami diagramów, podobnie jak w C4. Klikasz i przechodzisz na głębsze lub wyższe poziomy."
3. Szymon Warda: "Czy wiesz ile kosztuje ich studio? 25 dolarów za użytkownika miesięcznie."

## 15. JSON Crack
Summary: Prowadzący omawiają JSON Crack, narzędzie do wizualizacji struktury JSON i YAML, które znalazło się w kategorii trial. Dyskutują o jego potencjalnych zastosowaniach i użyteczności.

Speaker summaries:
- Szymon Warda: Opisuje JSON Crack jako narzędzie do wizualizacji struktury JSON i YAML, ale wyraża wątpliwości co do jego praktycznej użyteczności.
- Łukasz Kałużny: Widzi potencjalne zastosowania dla JSON Crack przy analizie odpowiedzi API i przeglądaniu skomplikowanych struktur.

Most interesting quotes:
1. Szymon Warda: "To jest narzędzie, które wizualizuje strukturę JSON i YAML. Dzięki niemu możecie zobaczyć przejrzyste reprezentacje dużych plików z ich podsekcjami."
2. Łukasz Kałużny: "Gdy analizuję odpowiedzi z API, rozpoznaję struktury lub muszę przejrzeć skomplikowane formaty czy pliki YAML, do których nie ma schematów, to może być przydatne narzędzie."

## 16. Jujutsu jako alternatywa dla Git
Summary: Prowadzący omawiają Jujutsu, nowy system kontroli wersji kompatybilny z Git, który znalazł się w kategorii assess. Wyrażają sceptycyzm co do potrzeby tworzenia alternatywy dla Git.

Speaker summaries:
- Łukasz Kałużny: Wyraża zdziwienie, że ktoś tworzy alternatywę dla Git, kwestionując potrzebę takiego rozwiązania.
- Szymon Warda: Zauważa, że podstawowe komendy Git są proste i można je obsługiwać przez UI, kwestionując wartość nowego systemu.

Most interesting quotes:
1. Łukasz Kałużny: "Ktoś stworzył nowy system kontroli wersji jako alternatywę dla Gita. Alternatywę dla Gita, nowy rozproszony system kontroli wersji, który jest kompatybilny z Gitem."
2. Szymon Warda: "Reklamują się tym, że są jednocześnie proste i potężne. Prawda jest taka, że jeśli nie zagłębiamy się w zaawansowane komendy gitowe, to wszystkie podstawowe operacje można spokojnie wykonać przez interfejs graficzny."
3. Łukasz Kałużny: "Najtrudniejszą rzeczą, której żadne narzędzie nie rozwiąże, i tak pozostaną operacje merge."

## 17. Kubenetmon do monitoringu sieci
Summary: Prowadzący omawiają Kubenetmon, narzędzie od ClickHouse do monitoringu sieci, które znalazł się w kategorii assess. Widzą potencjał w tym narzędziu do monitorowania przepływu danych między chmurami.

Speaker summaries:
- Łukasz Kałużny: Widzi potencjał w Kubenetmon do monitorowania ruchu sieciowego i tworzenia bardziej dokładnych chargebacków.
- Szymon Warda: Zgadza się z potencjalną wartością narzędzia, szczególnie w kontekście klastrów rozpiętych między chmurami i środowiskiem on-premise.

Most interesting quotes:
1. Łukasz Kałużny: "ClickHouse Kubenetmon służy do monitoringu sieci. Pozwala monitorować przepływ danych i przechowywać logi komunikacyjne w ClickHouse."
2. Szymon Warda: "Monitorujemy ilość danych wchodzących i wychodzących, dzięki czemu wiemy ile zapłacimy i co się faktycznie dzieje w sieci."

## 18. AnythingLLM
Summary: Prowadzący omawiają AnythingLLM, aplikację desktopową łączącą modele komercyjne z lokalnymi dokumentami, która znalazła się w kategorii assess. Szymon Warda przedstawia jej funkcjonalności, ale obaj prowadzący nie są przekonani o jej dużej wartości.

Speaker summaries:
- Szymon Warda: Opisuje AnythingLLM jako aplikację umożliwiającą łączenie modeli komercyjnych z lokalnymi dokumentami, ze wsparciem dla MCP i kreatorami agentów AI.
- Łukasz Kałużny: Wyraża sceptycyzm co do przydatności tego narzędzia.

Most interesting quotes:
1. Szymon Warda: "Aplikacja desktopowa, która łączy modele komercyjne z lokalnymi dokumentami. To jest interesujące rozwiązanie."
2. Szymon Warda: "Obsługuje wiele dokumentów. Ogólnie rzecz biorąc, potrafi importować lokalne pliki i umożliwia zadawanie pytań o ich zawartość przy pomocy AI."

## 19. Hurl - narzędzie do testowania API
Summary: Prowadzący omawiają Hurl, narzędzie do testowania API, które znalazło się w kategorii assess. Szymon Warda opisuje jego funkcjonalności i porównuje je do innych narzędzi, zauważając brak operacji warunkowych.

Speaker summaries:
- Szymon Warda: Opisuje Hurl jako narzędzie do testowania API, które umie parsować odpowiedzi, zapisywać do zmiennych i weryfikować dane, ale brakuje mu operacji warunkowych.
- Łukasz Kałużny: Zastanawia się, czy podobne funkcjonalności oferują inne narzędzia, które już znają.

Most interesting quotes:
1. Szymon Warda: "Potrafi przetwarzać odpowiedzi, zapisywać dane do zmiennych, przeprowadzać weryfikację i oferuje narzędzia do integracji z procesami CI/CD jako testy."
2. Szymon Warda: "Nie obsługuje operacji warunkowych, czyli nie ma instrukcji IF, switch ani żadnych podobnych konstrukcji."

## 20. GitLab CI/CD w adopt
Summary: Prowadzący omawiają GitLab CI/CD, który znalazł się w kategorii adopt. Wyrażają zdziwienie, że narzędzie to nagle awansowało z trial do adopt po trzech latach.

Speaker summaries:
- Szymon Warda: Wyraża zdziwienie nagłym awansem GitLab CI/CD do kategorii adopt po trzech latach w trial.
- Łukasz Kałużny: Docenia funkcjonalności GitLab CI/CD, szczególnie w kontekście CD, ale również jest zaskoczony zmianą kategorii.

Most interesting quotes:
1. Szymon Warda: "Znajdował się w kategorii trial w wersjach 2.0 i 2.2, czyli trzy lata temu, a teraz nagle pojawił się w kategorii adopt."
2. Łukasz Kałużny: "Ta wersja SaaS-owa ma kilka interesujących funkcji, szczególnie w obszarze CD, gdzie oferuje sporo ciekawych elementów."

## 21. Dapr w trial
Summary: Prowadzący omawiają Dapr (Distributed Application Runtime), który znalazł się w kategorii trial. Wyrażają zdziwienie i krytykę wobec tej decyzji, wskazując na problemy z projektem.

Speaker summaries:
- Łukasz Kałużny: Krytycznie opisuje Dapr jako próbę stworzenia agnostycznej nakładki aplikacyjnej, która na papierze wyglądała dobrze, ale w praktyce nie spełniła oczekiwań.
- Szymon Warda: Zauważa, że projekt nie przyjął się na rynku i wyraża zdziwienie jego umieszczeniem w kategorii trial.

Most interesting quotes:
1. Łukasz Kałużny: "Microsoft próbował stworzyć agnostyczną nakładkę aplikacyjną. W zasadzie Service Mesh na poziomie aplikacyjnym, bo tak należy to nazwać."
2. Łukasz Kałużny: "Miał to być serwis, który rozumie komunikację synchroniczną i asynchroniczną, uwierzytelnianie i łatwo integruje się z aplikacjami - przynajmniej w teorii."
3. Łukasz Kałużny: "Co ciekawe, Microsoft już dawno wycofał wszystkich swoich inżynierów z tego projektu open source."

## 22. Grafana i ekosystem Grafany
Summary: Prowadzący omawiają Grafanę i jej ekosystem (Loki, Tempo), które znalazły się w raporcie. Wyrażają pozytywne opinie na temat tych narzędzi do monitorowania i observability.

Speaker summaries:
- Szymon Warda: Chwali narzędzia Grafany jako świetny ekosystem do monitorowania, który wymaga jednak pewnej zmiany myślenia u deweloperów i ops.
- Łukasz Kałużny: Zgadza się z pozytywną oceną i dodaje, że kluczowe jest oduczenie się podejścia opartego na full text search.

Most interesting quotes:
1. Szymon Warda: "Są to bardzo dobre narzędzia, które wymagają pewnej zmiany w sposobie myślenia zarówno deweloperów jak i specjalistów operacyjnych, aby odeszli od wyszukiwania pełnotekstowego."
2. Szymon Warda: "Obecnie wszystkie komponenty współpracują ze sobą doskonale. Na tej bazie można budować świetne platformy monitorujące."

## 23. DeepSeek-1 w raporcie
Summary: Prowadzący omawiają obecność chińskiego modelu AI DeepSeek-1 w raporcie. Zastanawiają się nad powodami umieszczenia go w raporcie i brakiem konkretnych doświadczeń z jego użytkowania.

Speaker summaries:
- Łukasz Kałużny: Wymienia trzy wartościowe aspekty DeepSeek: korektę oczekiwań na giełdzie, pokazanie, że można zrobić to taniej, oraz udostępnienie open source.
- Szymon Warda: Sugeruje, że umieszczenie DeepSeek w raporcie może być ukłonem w stronę rynku chińskiego i próbą pokazania, że firma nie jest nastawiona tylko na modele europejsko-amerykańskie.

Most interesting quotes:
1. Łukasz Kałużny: "DeepSeek miał dwa bardzo istotne elementy. Spowodował korektę oczekiwań na giełdzie i udowodnił, że można stworzyć podobne rozwiązania taniej."
2. Szymon Warda: "Nie przedstawiają żadnych informacji o swoich doświadczeniach z tym modelem. Piszą o DeepSeek bardzo ogólnikowo."

## 24. Deno w assess
Summary: Prowadzący omawiają Deno, runtime dla JavaScript/TypeScript, który znalazł się w kategorii assess. Dyskutują o jego zaletach w porównaniu do Node.js i potencjale rozwoju.

Speaker summaries:
- Szymon Warda: Opisuje Deno jako alternatywę dla Node.js z lepszym sandboxingiem, zarządzaniem zależnościami i wsparciem dla TypeScript.
- Łukasz Kałużny: Wyraża zainteresowanie rozwojem ekosystemu JavaScript/Node.js.

Most interesting quotes:
1. Szymon Warda: "To jest runtime dla JavaScriptu, ale przede wszystkim dla TypeScriptu, stanowiący alternatywę dla Node.js."
2. Szymon Warda: "Oferuje kilka udoskonaleń: lepszy sandboxing, lepsze zarządzanie zależnościami i lepsze wsparcie dla TypeScriptu."

## 25. Model Context Protocol (MCP)
Summary: Prowadzący omawiają Model Context Protocol (MCP) od Anthropic, specyfikację określającą sposób integracji modeli AI z zewnętrznymi narzędziami. Podkreślają jej znaczenie jako wiodącej specyfikacji w tej dziedzinie.

Speaker summaries:
- Łukasz Kałużny: Podkreśla znaczenie MCP jako jedynej wiodącej specyfikacji określającej sposób integracji modeli AI z zewnętrznymi narzędziami.
- Szymon Warda: Zgadza się, że MCP jest obecnie jedynym sensownym wyborem przy tworzeniu integracji z agentami AI.

Most interesting quotes:
1. Łukasz Kałużny: "To jest jedyna rzecz, o której można powiedzieć, że jest wiodącą specyfikacją na rynku, bez żadnych wątpliwości."
2. Szymon Warda: "Czy jest sens implementowania MCP teraz tylko dla samej implementacji? Nie, nie ma. Ale jeśli tworzymy cokolwiek, co ma komunikować się z agentami AI, to mamy jeden oczywisty wybór - MCP."

## 26. Hybrid API Management na hold
Summary: Prowadzący omawiają Hybrid API Management, który znalazł się w kategorii hold. Wyrażają zdziwienie ostrą krytyką zawartą w raporcie, sugerując, że musiały wystąpić poważne problemy z tym rozwiązaniem.

Speaker summaries:
- Szymon Warda: Zwraca uwagę na niezwykle ostrą krytykę Hybrid API Management w raporcie, co jest rzadko spotykane.
- Łukasz Kałużny: Zgadza się, że krytyka jest niezwykle ostra, co sugeruje poważne problemy z tym rozwiązaniem.

Most interesting quotes:
1. Szymon Warda: "Skrytykowali ich niezwykle ostro. Te rozwiązania służą jako platforma do zarządzania wieloma chmurami. Skrytykowali ich za system obsługi zgłoszeń, stabilność i dokumentację."
2. Szymon Warda: "Musieli napotkać poważne problemy albo musiało dojść do jakiegoś konfliktu na poziomie biznesowym, bo tak ostrej krytyki jeszcze nie widzieliśmy w tym raporcie."

## 27. OpenTelemetry w adopt
Summary: Prowadzący omawiają OpenTelemetry, które znalazło się w kategorii adopt. Wyrażają pełne poparcie dla tej technologii, podkreślając jej wartość i łatwość implementacji.

Speaker summaries:
- Szymon Warda: Zdecydowanie popiera umieszczenie OpenTelemetry w kategorii adopt, podkreślając jego przyjęcie na rynku i korzyści z implementacji.
- Łukasz Kałużny: Zgadza się z pozytywną oceną OpenTelemetry.

Most interesting quotes:
1. Szymon Warda: "Tak, zdecydowanie warto korzystać. Bardzo dobrze przyjmuje się na rynku."
2. Szymon Warda: "To rozwiązanie wymaga jedynie dodania kilku bibliotek do projektu, a od razu zaczyna działać. Oferuje duże możliwości i pozwala zaoszczędzić znaczne środki."

## 28. Markprompt - biblioteka Pythonowa od Microsoftu
Summary: Prowadzący omawiają Markprompt, bibliotekę Pythonową od Microsoftu, która znalazła się w kategorii trial. Biblioteka służy do konwersji różnych formatów do Markdown, co jest przydatne w kontekście modeli AI.

Speaker summaries:
- Łukasz Kałużny: Opisuje Markprompt jako bibliotekę do konwersji różnych formatów, w tym formatów Microsoftu, do Markdown.
- Szymon Warda: Zauważa, że biblioteka pochodzi od Microsoftu, co tłumaczy jej dobre wsparcie dla formatów Word.

Most interesting quotes:
1. Łukasz Kałużny: "Biblioteka pythonowa, która konwertuje wiele formatów, w tym formaty Microsoftu, do Markdown, działając jak uniwersalne narzędzie pod LLM-y i pipeline do ładowania danych."
2. Szymon Warda: "Jedna istotna informacja - to narzędzie pochodzi od Microsoftu. Dlatego nie dziwi fakt, że dobrze radzi sobie z formatem Word."

## 29. Aspire od Microsoftu
Summary: Prowadzący krytycznie omawiają Aspire od Microsoftu, projekt umożliwiający definiowanie infrastruktury w kodzie aplikacji. Wyrażają sceptycyzm co do praktycznej użyteczności tego podejścia poza lokalnym środowiskiem deweloperskim.

Speaker summaries:
- Łukasz Kałużny: Krytykuje Aspire jako projekt wynikający z ego osoby, która nigdy nie wdrażała aplikacji na produkcji, podkreślając problemy z podejściem, w którym deweloper definiuje infrastrukturę w kodzie.
- Szymon Warda: Kwestionuje praktyczność podejścia, w którym aplikacja ma uprawnienia do zarządzania infrastrukturą.

Most interesting quotes:
1. Łukasz Kałużny: "Aspire jest projektem wynikającym z ambicji osoby, która tworzyła w Microsofcie interesujące rozwiązania, ale nigdy nie wdrożyła żadnej aplikacji na środowisku produkcyjnym."
2. Szymon Warda: "Dlaczego uważamy, że to jest nietypowe podejście? Ponieważ kto nadałby aplikacji uprawnienia na poziomie kontrybutora dla grupy zasobów."
3. Łukasz Kałużny: "Ma dwie zalety: wbudowany kolektor logów OpenTelemetry do pracy lokalnej oraz lokalny dashboard."

## 30. Browser-use dla modeli AI
Summary: Prowadzący omawiają Browser-use, pythonową bibliotekę umożliwiającą modelom AI dostęp do przeglądarki. Łukasz Kałużny widzi w niej potencjał do rozszerzenia możliwości agentów AI.

Speaker summaries:
- Łukasz Kałużny: Opisuje Browser-use jako bibliotekę, która daje modelom AI dostęp do przeglądarki jako Vision i HTML Extraction.
- Szymon Warda: Zgadza się z potencjalną wartością tego narzędzia.

Most interesting quotes:
1. Łukasz Kałużny: "Pythonowa biblioteka, która umożliwia waszemu modelowi LLM lub agentowi dostęp do przeglądarki z funkcjami Vision i ekstrakcji HTML."

## 31. Node overload na hold
Summary: Prowadzący omawiają "Node overload" (nadmierne wykorzystanie Node.js), które znalazło się w kategorii hold. Dyskutują o problemach związanych z używaniem Node.js w nieodpowiednich kontekstach i o potrzebie powrotu do programowania poliglotycznego.

Speaker summaries:
- Szymon Warda: Popiera ideę powrotu do programowania poliglotycznego i zauważa, że Node.js powoli staje się technologią legacy.
- Łukasz Kałużny: Broni Node.js w kontekście aplikacji biznesowych i startupów, gdzie koszty developmentu i możliwość full-stack developmentu są istotne.

Most interesting quotes:
1. Szymon Warda: "Node rozprzestrzenił się w wielu obszarach, gdzie nie powinien był się znaleźć."
2. Szymon Warda: "Node powoli traci pozycję najbardziej poważanego języka i stopniowo staje się technologią legacy."
3. Łukasz Kałużny: "Z perspektywy kosztów rozwoju, możliwości full-stack developmentu i innych podobnych aspektów, nie jest to najgorsze rozwiązanie."

## 32. Podsumowanie Technology Radar
Summary: Prowadzący podsumowują swoje wrażenia z Technology Radar Volume 32. Oceniają raport jako bardziej ucywilizowany niż poprzednie, z kilkoma komediowymi elementami, ale generalnie zawierający wartościowe informacje.

Speaker summaries:
- Łukasz Kałużny: Ocenia raport jako stabilny, doceniając szczególnie wytknięcie problemu Shadow IT i krytykę niektórych technologii jak Aspire.
- Szymon Warda: Określa raport jako "ucywilizowany", choć zawierający niektóre niezrozumiałe wybory.

Most interesting quotes:
1. Łukasz Kałużny: "Wytknięcie problemu Shadow IT jest godne pochwały."
2. Łukasz Kałużny: "Jak zawsze, nie zawodzi pod względem elementów humorystycznych, takich jak Just in Time Village czy Aspire."
3. Szymon Warda: "Są tam elementy, które jak zwykle budzą pytania. Dlaczego w ogóle znalazły się w tym raporcie? Ale tak już bywa."
