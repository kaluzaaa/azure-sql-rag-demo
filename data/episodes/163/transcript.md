# 163.mp3

[00:00:00.050] **Łukasz Kałużny:** Jeżeli coś jest niepotrzebne, to nie powinno być wystawiane. Więc o MCP można pomyśleć jako API Gateway'u, ale to nie jest API Gateway w tym rozumieniu, w którym go używaliśmy. Pierwsza rzecz, o której powiem, za dużo narzędzi, za dużo zwracamy i przez to mamy albo wyczerpanie okna kontekstowego w LLM-ie, albo problemy z trzymaniem się, bo jest za dużo kontekstu.

[00:00:24.590] **Szymon Warda:** Warto być leniwym. Tak, zdecydowanie, bo te opisy, które są generowane, są generowane naprawdę dobrze i są generowane w taki sposób, w jaki LLM to ładnie zrozumie.

[00:00:33.380] **Łukasz Kałużny:** Dobra, tu jest duży problem i podam to na przykładzie MCP od Jiry. Cześć, słuchacie Patoarchitektów. Prowadzą Łukasz Kałużny...

[00:00:54.230] **Szymon Warda:** I Szymon Warda. Wszystkie linki do tego odcinka o dziwo, jak zwykle Patoarchitekci.io. Wygooglacie, wyczatujecie, znacie. Dobrze. Dzisiaj fajny odcinek, bo dzisiaj znowu odcinek merytoryczny będzie. O czym będziemy, bo dzisiaj dyskutowiec.

[00:01:10.250] **Łukasz Kałużny:** Dobra, Model Context Protocol, czyli przejdziemy merytorycznie, wytłumaczymy czym jest bez zbędnego szamaństwa i memów, które mogły być. Dzisiaj przed tym jak nagrywamy był świetny mem, który jak widzicie, zaraz go zobaczycie na ekranie, więcej jest osób budujących MCP Servery niż ich faktycznych użytkowników.

[00:01:37.940] **Szymon Warda:** Tak samo jak z pakietami różnymi do node'a i tak dalej. Teraz jest hype. Dobrze Łukaszu, żeby tak to uprościć tak naprawdę, to czym jest właściwie MCP? Jakbyś miał tłumaczyć czterolatkowi.

[00:01:50.990] **Łukasz Kałużny:** Dobra, MCP, może nie czterolatkowi, nie dziesięciolatkowi, to jest dynamiczne rozszerzenie function calling, które mamy w LLM-ach. Czyli LLM może nam, w zależności jak tam model jest zbudowany, może nam zwrócić odpowiedź, że prosi o wywołanie jakiegoś narzędzia z parametrami i my w swoim kodzie to możemy obsłużyć i wywołać jakieś API Restowe. A...

[00:02:15.480] **Szymon Warda:** Nie tylko narzędzia. Może też dopytać się o co nam właściwie chodzi.

[00:02:19.590] **Łukasz Kałużny:** Tak, ale tutaj function calling to są narzędzia, czyli odpalenie czegoś konkretnego u nas i to obsługujemy ze swojej strony kodu. Możemy wziąć, tak jak wszyscy, w samplach zrobić kalkulator albo odpytać się dynamicznie od pogody jakiegoś Restowego API. A tutaj chodziło o to, żeby zrobić decoupling, odseparować function calling od naszego kodu aplikacji agenta i pozwolić na uniwersalne używanie tego. I w istocie MCP jeżeli popatrzymy, to jest wystandaryzowany protokół, który pozwala nam dostarczyć nakładkę na function calling, jak na to popatrzymy, żeby dynamicznie wykrywać narzędzia i zasoby, które są do wykorzystania i potem je wywoływać. Ja bym tak na to popatrzył. Czyli że to jest otwarty protokół.

[00:03:10.370] **Szymon Warda:** Czyli upraszczając, to jest protokół, który umożliwia nam dwojako. To, żeby model dowiedział się, co właściwie klient może zrobić, a żeby klient dowiedział się, co właściwie model może zrobić i żeby nawzajem mogli wywołać, i konkretne wywołania obsługiwać.

[00:03:23.090] **Łukasz Kałużny:** I to jest tak, to jest istotny element. Jak tam popatrzymy historycznie, założenie jest, ma prawie rok, więc jest jak wszystkie rzeczy świeżynka. Został zapoczątkowany przez Anthropica i wszyscy duzi od modeli do tego kontrybuują. I stało się takim właśnie, jak można już popatrzeć na ten model, powiedzieć wprost, to jest standard dostarczania narzędzi do LLM-ów, jeżeli budujemy agenta, asystenta, jakiś kod AI-owy. Tak na to popatrzmy.

[00:03:54.200] **Szymon Warda:** Jeszcze co ważne, bo to mówi, że to powstało rok temu. W zupełności zgadzamy się, ale to nie standard, który powstał rok temu i leży. On się cały czas tam, drobne rozwoje są, wersje wychodzą i tak dalej.

[00:04:05.930] **Łukasz Kałużny:** Tak, to jest, cały czas się rozwija. Raczej zbliża się do jakiejś stabilności. O tak, to możemy ładnie określić, że zaczyna wchodzić w fazę stabilności, jeżeli można nazwać rok czasu rozwoju produktu, standardu.

[00:04:23.570] **Szymon Warda:** Jeżeli teraz mówimy o standardzie, to w takim razie musimy dowiedzieć się, co właściwie ten standard standaryzuje.

[00:04:28.340] **Łukasz Kałużny:** Czyli architektura. I to jest MCP Client. Czyli jak nasz kod LLM, jak możemy do LLM-a podłączyć to MCP i potem MCP Server, czyli coś, co już faktycznie wykonuje tę akcję i nam dostarcza. Czyli tam leży ta cała integracja, która jest potrzebna. I w sumie to jest chyba najważniejsze do powiedzenia.

[00:04:51.080] **Szymon Warda:** ... nazywasz. Dobra, to co jeszcze mamy? Mam jeszcze transporter.

[00:04:58.880] **Łukasz Kałużny:** Dobra, całość jest zbudowana na starym dobrym JSON RPC pod spodem, czyli komunikacja leci, całość standaryzowana jest w JSON RPC. Czy jest to dobre czy złe? Można dyskutować. Uważam, że jest good enough, o tak. I potem mamy transport, czyli pierwsze dla lokalnych rzeczy jak odpalamy, to jest po prostu standard IO, czyli po prostu komunikacja przez konsolę. I pozostawmy to bez komentarza, potem jeszcze do tego przejdziemy. A drugie, to jest Streamabel HTTP, czyli po prostu po HTTP2.

[00:05:35.780] **Szymon Warda:** Do negocjacji protokołu. Jest to opisane dość dokładnie w dokumentacji, tego już tu nie będziemy wchodzić.

[00:05:43.580] **Łukasz Kałużny:** Ważne jest, że są negocjacje co dostarcza serwer. Czyli jeżeli mamy klienta z dowolnego SDK, to on może odpytać serwer w jakiej wersji działa i co on dostarcza. I to jest dobry element.

[00:05:57.630] **Szymon Warda:** Protokół, który jest taki, widać, że jest przemyślany pod kątem tego, że te serwery powstaną i może nie będą rozwijane. Więc żeby były negocjacje, co klient umie obsługiwać, co serwer może obsługiwać i tak dalej. Całkiem niezły mechanizm w fallbacku tam wpisane, jest to ustandaryzowane. Oczywiście, żebyśmy się słuchali tego jak to powinno być zrobione. Dobra, to teraz idziemy. Ok, wiemy co mamy właściwie jeżeli chodzi co to robi. To teraz pytanie kolejne, do czego będziemy używali?

[00:06:25.320] **Łukasz Kałużny:** I rozdzielmy świat, bo powiedziałbym mamy szamanów z AI-a, którzy mówią, influencerów czy ludzi podających się za programistów, a tak naprawdę nie potrafiących kodować, bo robią to tylko dzięki vibe codingowi. I trzeba rozdzielić dwa elementy, teraz już na poważnie. Pierwszy scenariusz, który jest szerzej omawiany ciągle, to jest lokalna produktywność. Czyli do mojego Claude chata, VSCode'a, Cursora, Claude Code'a czy tam innych narzędzi, dostarczam właśnie różne wystandaryzowane narzędzia, które są zazwyczaj lokalnie odpalane, ale może też zdalnie. Ja zostawiam tutaj taką listę z tego, co ja na przykład u siebie używam. Jednym z takich przykładów chyba, które mogę polecić, to jest Context 7. I jak się opisują: up to date documentation for LLM's and AI code editors. Czyli żeby LLM mógł sobie ściągnąć aktualną dokumentację do jakiejś biblioteki.

[00:07:26.190] **Szymon Warda:** Bo to jest w ogóle, jak już zatrzymaliśmy się przy tym, bardziej ruszyliśmy, to jest bardzo ważne, żeby nakierować jak to wykorzystanie właśnie MCP wygląda, szczególnie lokalnie. Bo to jest tak, że stawiamy sobie często bardzo małe, drobne serwerki MCP, czyli rzeczy, które programy właściwie, które umożliwiają nam jakieś dodatkowe możliwości, które może LLM wykorzystać i to nam umożliwia dostęp do plików, kalendarza, jak Ty mówiłeś właśnie do dokumentacji i tak dalej. Bo idea jest taka, że LLM nie będzie tego wykonywać, nie będzie sięgał, on jest tylko tym statystycznym mechanizmem, który wylicza nam to wszystko, ale dzięki temu właśnie dajemy dodatkowe możliwości, możemy go ładnie rozszerzyć. I to jest właśnie ten cały clue tego gdzie MCP będzie używane.

[00:08:07.680] **Łukasz Kałużny:** Tak i dobrze, że wspomniałeś lokalnie, bo zazwyczaj te lokalnie oznacza trzy ścieżki, jak odpalamy lokalnie. Pierwsza ścieżka to jest odpal coś NPX-em, czyli kawałek source kodu node'owego, albo zaciągnij paczkę i ją odpal i dostań się do niej przez stdio. Druga, to odpal, zainstaluj coś z pip'a, ściągnij jakąś paczkę pip'ową. Trzecia, taka kulturalna to nazwijmy, odpal Dockera. To są trzy takie rzeczy, które się najczęściej z tym kodem dzieją i 99% przypadków to jest odpalanie stdio.

[00:08:48.970] **Szymon Warda:** Czasami pytamy się jakiś model, czy sobie chatujemy z nim, żeby coś zrobił, to on nam mówi: ok, ja tego nie umiem zrobić, ale umiem napisać program w Pythonie, który to obliczy, uruchomi, zwróci mi wynik. I to właśnie ten jest moment, kiedy na tym MCP ..., bo znaczy dajemy możliwość uruchomienia jakiegoś Pythona, dajemy możliwość dostępu do plików. Oczywiście polecamy limitować generalnie do których katalogów mają, bo to może skończyć się źle, ale o tym jeszcze powiemy sobie. Tak że tak, to daje naprawdę bardzo dużo możliwości. To nie jest tylko w tym momencie pytanie - odpowiedź.

[00:09:20.350] **Łukasz Kałużny:** I z takich elementów jeszcze tylko dorzucę, że można się zastanowić, bo troszeczkę przy tym stdio inaczej to działa. Jak już jesteśmy przy dockerach, ja zostawię jeszcze Wam linka, na przykład taki Docker Desktop, z czego ja tam gdzieś z boku też trochę korzystam, wrzucił sobie lokalnie MCP catalog, żeby odpalać to w dockerach. Taka ciekawa ewentualność i wtedy do LLM-a podpinamy tak jeden MCP Server, którym jest właśnie ten gateway na standard IO, a reszta przelatuje mu dynamicznie z tego co wrzuciliśmy w naszą konfigurację Docker Desktopa.

[00:10:01.380] **Szymon Warda:** Teraz nieco podnosimy temperatury szamaństwa, nie za bardzo, ale odrobinę i przechodzimy do ustawienia korporacyjne.

[00:10:07.410] **Łukasz Kałużny:** Dobra i korpo zastosowania, to są różnego rodzaju dostarczenie narzędzi w sposób wystandaryzowany. Bo MCP z założenia ma dać nam dostęp do danych, jakieś akcje i inne rzeczy. I chodzi tutaj prosto, że raczej już w formie zdalnej, czyli wykorzystując protokół po HTTP wystawiamy w firmie jakieś narzędzia, które mogą być wykorzystywane z Copilotem. Jeden przykład ze stosu Microsoftu, Copilot Studio, czyli te boty do Teams'ów, które są low code'owe, nocode'owe, można dostarczyć do nich akcję właśnie w postaci takiego MCP zdalnego. Czyli podłączamy się do serwera i infrastruktura na przykład Microsoftu azure'owa, teraz Logic Appsy mogą być wystawiane jako MCP, Azure API Gateway pozwala Rest API zamienić w MCP, czyli możemy to wystawić, takie akcje, plus inne cloudy też z tego korzystają. I teraz co jest ważne do powiedzenia? Raz takie wystawione rozwiązanie na takim API Gateway'u, Logic Appsach czy innym open source, jak na to popatrzymy i zbudowane takie integracje, pozwalają nam wykorzystać to MCP przez wiele różnych zastosowań. Czyli może wykorzystać wielu różnych agentów, na przykład których sobie napiszemy, może z tego skorzystać.

[00:11:25.480] **Szymon Warda:** To jest jeszcze jedna rzecz, ważna rzecz, o której nie powiedzieliśmy, ale generalnie mówimy, że może wykorzystać. To pytanie powstaje, w jaki sposób są serwery MCP wykrywane, deklarowane i tak dalej? Musimy jej jawnie powiedzieć, modelowi, że: ok, to jest serwer MCP, on ma takie możliwości, tak, możesz z nich korzystać i to ładnie opisujemy, tak żeby rozwiać wątpliwości tego i jak ta magia działa. Bo tam magii w sumie nie ma do końca.

[00:11:49.500] **Łukasz Kałużny:** I wiesz co, chyba to jest dobry moment, żeby sobie powiedzieć, co tak naprawdę wystawia MCP, jego podstawowe elementy, te primitives, które są wystawione.

[00:12:02.700] **Szymon Warda:** Taki schemat, można powiedzieć.

[00:12:04.740] **Łukasz Kałużny:** Dobra, i pierwszym to jest, chyba będzie najbardziej popularne, reszta jest zbędna, jeżeli popatrzymy na to, co się dzieje, to są toolsy, czyli narzędzia. I LLM sobie robi tam toollist, ma toollist, czyli sprawdzenie, klient sobie pobiera całą listę i mamy potem toolscall, czyli wywołania. I teraz jak sobie popatrzymy, to jest po prostu function calling, czyli to co dostaje LLM, to jest function calling. I tu wchodzimy w całość, w piękno jak i zło. Modele LLM mają swoją długość kontekstu, który obsługują. Powyżej pewnych, mimo, że możemy wprowadzić nie wiadomo ile, to się gubią, źle wybierają narzędzia. Ponieważ ten...

[00:12:50.320] **Szymon Warda:** ... więc gdzieś go ukryjemy, albo w toolsach, albo w naszych promptach, albo w historii i tak dalej, że gdzieś wsadzimy, to gdzieś będziemy mieli mniej.

[00:12:57.820] **Łukasz Kałużny:** Tak. Im więcej wsadzimy. I teraz o co chodzi? Toole wystawiają nam, pokazują się do LLM-a po prostu jako jakiś format JSON-a, jakbyśmy sobie popatrzyli w jaki sposób jest to wysyłane pod spodem. I w tych toolach, to co znajdziemy, to jest nazwa toola, tam jego ID, ale to pomijamy teraz, nazwa toola, description i input z SCIM-a w JSON-ie. Czyli pierwsze, jak się nazywa narzędzie, opis do czego służy i jaki ma input. I na podstawie tego LLM będzie musiał podjąć decyzję, jeżeli mu jawnie nie powiemy, że skorzystaj z tego narzędzia, to LLM będzie musiał dynamicznie na podstawie tego spróbować wykorzystać to do tego, żeby wywołać jakąś akcję i rozszerzyć nam funkcjonalności. I tutaj od razu taka ważna rzecz z naszej praktyki, description warto generować i opisy do input SCIM-y warto generować również LLM-em po angielsku, żeby były zrozumiałe dla LLM-a.

[00:14:01.390] **Szymon Warda:** Warto być leniwym, tak, zdecydowanie, bo te opisy, które są generowane, są generowane naprawdę dobrze i są generowane w taki sposób, w jaki LLM to ładnie zrozumie. Nie ma co tutaj się wysilać, że ja zrobię to lepiej. Nie, nie ma to sensu. Może jakieś małe tweakowanie, ale wtedy to jest bardziej oznaka tego, że coś jest niezrozumiałe. Jedna jeszcze ważna rzecz, bo to jest coś, co będzie się powtarzało przy pozostałych w tych elementach, mianowicie, że większość tych resource'u, większość tych podstawowych elementów mają też element odświeżania. Czyli, że może być poinformowany, że ok, jest coś nowego, coś się zmieniło i tak dalej. W toolsach może ma zastosowanie, ale będzie miało dużo ważniejsze, większe zastosowanie w kontekście resource'ów. Ale trochę wyprzedzam.

[00:14:45.630] **Łukasz Kałużny:** Tak i właśnie jak wyprzedzasz resourcesy, to kolejny zestaw. Tak, czyli to są, można powiedzieć, że resource'y to są dane bez logiki. Czyli tak jak toolsy, to jest wywoływanie, jeżeli popatrzymy, wywoływanie jakichś akcji, modyfikacja, pobieranie, to resource'y to jest po prostu dane bez logiki. Czyli zwróć mi jakiś API response, jakiś kawałek pliku, ewentualnie to są trochę dynamiczne źródła danych, czyli mają jakiegoś where'a, na przykład zwróć mi dane dla użytkownika po ID. Ale to są rzeczy, które szybko zwracają dane i są lekkie w obrobieniu.

[00:15:26.910] **Szymon Warda:** Tak, to najczęściej kończy się, że to są po prostu pliki, tak w wiekszości przypadków można powiedzieć. Dobrze, to mieliśmy takie dwa trochę bardziej namacalne. Teraz wchodzimy w promptsy, które są już proste jak nie wiem co, bo są jak konsola w Quake'u generalnie z konkretnymi wywołaniami komend tak naprawdę.

[00:15:46.770] **Łukasz Kałużny:** Raczej czy wiesz co, komend, to są predefiniowane snippety, szablony promptów. Czyli weźmy zrobię slash review code i wykona mi albo w zależności jak jest zaimplementowany nasz UI, UX, to model dostanie gotowego prompta do użycia, albo po prostu ten prompt wyświetli nam się i rozwinie w naszej konsoli, gdzie wprowadzamy. Czyli gotowe komendy, które pod spodem są predefiniowanym po prostu szablonem prompta. Nic więcej.

[00:16:14.820] **Szymon Warda:** Tak, żeby być pewnym, że model doskonale nas zrozumie. Dobra, to mamy coś, co powiedzieliśmy wcześniej trochę, mianowicie sampling, coś co weszło relatywnie można powiedzieć nie dawno.

[00:16:26.460] **Łukasz Kałużny:** Wiesz co, on jest od początku, to może tak, jest od początku. Założenie jest takie, że... Ciągle jest walka z UI-em i użyciem tego prawidłowo. To jest chyba dobre określenie, bo jeżeli zobaczymy na sampling, jak są klienci, wyglądają gotowi, to z gotowych narzędzi wszystko jest czerwone, nawet Claude ten Chat Desktop, desktopowa apka Cloude'a też tego w ogóle w żaden sposób nie wspiera i to jest istotne. Ale założenie jest takie, że serwer może poprosić klienta właśnie o taki human in the loop i całą wymianę, czyli co będzie wysłane, cała kontrola, co będzie wysłane do LLM-a albo co LLM wykona. Czyli mamy taki cały proces właśnie akceptacji, samplowania, co się zadzieje, co będzie zrobione, co będzie przekazane, to można tak bardzo w tym momencie skrócić. I tutaj bym chyba powiedział, że to jest ten moment MCP, gdzie on gdzieś jest, ale nie jest określany nawet już jako core feature, jak sobie popatrzymy tam od strony serwerów. I całość ma polegać na tym, że pozwolimy serwerowi poprosić o coś, serwer będzie mógł poprosić klienta o coś, żeby LLM coś rozszerzył na przykład i też pozwolić w którymś miejscu na akceptowanie.

[00:18:04.310] **Szymon Warda:** Dobra, to idziemy. Ostatni - roots.

[00:18:07.190] **Łukasz Kałużny:** Dobra. I to jest taka rzecz od strony klienta, czyli jakie zasoby, jakie ścieżki dyskowe mogą być obsługiwane na przykład lokalnie.

[00:18:17.810] **Szymon Warda:** Proste. Dobra.

[00:18:19.640] **Łukasz Kałużny:** Albo jeszcze inny przykład, potem zaawansowany, daj dostęp do kalendarza czy do czegoś. To już takie inne elementy, które mogą się pojawić.

[00:18:29.570] **Szymon Warda:** Dobra, to idźmy kawałek dalej, bo mamy sobie element w MCP jeżeli chodzi o schemat, mamy odnośnie transportu. I jeszcze jest kolejny ważny element, mianowicie tego, jak wygląda uwierzytelnianie, bo to są zasoby lokalne, może nie są takie ważne, ale zdalne to już musimy wiedzieć, jak się ma to wszystko uwierzytelnić. Więc jak to śmiga? Bo śmiga całkiem nieźle.

[00:18:52.480] **Łukasz Kałużny:** Czy wiesz co, będziemy łączyć teorię z praktyką w tym momencie. Czyli mamy, tak jak powiedziałeś, stdio lokalnie, krzyżyk na drogę. I teraz zło, które trzeba powiedzieć od strony bezpieczeństwa, że bardzo tam często tokeny latają pod spodem. Czyli przy wywołaniu tego lokalnego toola w configu na przykład jawnie deklarujemy clear tekstem. Leży sobie na przykład token, uwielbiam taki przykład MCP Servera do Stripe'a, do obsługi płatności i innych rzeczy, gdzie leży token admina? Tak po prostu leży sobie goły i wesoły token admina, więc to jest pierwszy przypadek i tutaj żebyśmy wiedzieli. A kiedy już pójdziemy w te scenariusze bardziej zaawansowane, gdzie mamy tą autoryzację, to tu teraz jest prosto i odpowiedź brzmi OAuth i OpenID Connect.

[00:19:42.910] **Szymon Warda:** Standard, który wykorzystuje kolejny standard można powiedzieć, nic nowego.

[00:19:46.540] **Łukasz Kałużny:** To nic nowego. Daje nam to gdzieś single sign-on'y, znany już UX, który można wpasować potem w naszą aplikację, czyli na przykład zarequest'ować się o zalogowanie do jakiejś usługi. Weźmy do GitHuba, Office 365, Google Workspace, SAP-a czy innych. Czyli można kombinować ze scenariuszami single sign-on, bądź poproszenia użytkownika o zalogowanie się. Więc od tej strony nic nie zostało takiego wymyślonego. Przy czym sample, jeżeli chodzi na przykład o TypeScript SDK, Python SDK leżą i kwiczą, o tak, jeżeli popatrzymy. Za to widać, że Microsoft jest korporacyjny, bo tam z samplami do OAutha jest o wiele lepiej i Entry.

[00:20:33.160] **Szymon Warda:** Z dokumentacją i rzeczami dla developerów sobie radził całkiem fajnie. Dobra, ale to idziemy kawałek dalej, bo bezpieczeństwo nie kończy się właściwie tylko na tym, co się właściwie dzieje, jeżeli chodzi o uwierzytelnianie. Ale mamy cały temat prompt injection, który jest potencjalną dziurą, bo mamy dwa obszary- to, co użytkownik wysyła i to, co model odpowiada niejako. Czyli mamy prompt shielda i content protection. I o co w tej bajce chodzi?

[00:20:58.420] **Łukasz Kałużny:** Dobra, to pierwsze zajmijmy się tym content protection, o który trzeba sobie zadbać. To jest pytanie, co my wyślemy do LLM-a tak naprawdę z naszych danych? I to jest teraz długa dyskusja, ona wychodzi tak naprawdę poza MCP Szymon. Bo jak popatrzysz sobie, to jest temat DLP i to jest powiedzenie czy narzędzie możemy wykorzystywać na przykład do danych medycznych czy innych, w zależności, w jakiej firmie pracujemy i co możemy wysyłać. I to jest taki pierwszy problem, który się znajduje. I to jest trudne powiedzenie w tym momencie, tak jawnie, jak to zaimplementować, jak zrobić do tego compliance. Czyli jako rynek, w tym momencie, jak nagrywamy, czyli wrzesień 2025 roku, mamy problem, że jako rynkowo coś rozmawiamy, ktoś coś ciągle proponuje, ale nie ma nic takiego jawnie powiedzianego, czym to tak naprawdę powinno być.

[00:21:56.500] **Szymon Warda:** Teraz wyjaśnię jak to w ogóle działa. To działa tak, że zanim otrzymamy kawałek kodu, który zanim przekażemy do modelu sprawdza na przykład czy tam nie ma zdania typu: weź, zignoruj wszystkie swoje zakładki bezpieczeństwa i zrób to, co ja chcę. Czyli tak naprawdę czy nasz produkt...

[00:22:12.310] **Łukasz Kałużny:** Mówisz o content, mówisz o content protection, czyli mówimy o DLP? Bo ja zacząłem od prostszego, czyli DLP data + prevention, czyli czy dane do LLM-a są wysyłane jakieś z naszego MCP, które jednak nie powinny być wysyłane. A prompt shield to jest to, co powiedziałeś, sprawdzenie czy nie mamy prompt injection.

[00:22:38.620] **Szymon Warda:** Możliwe, nie będę się upierał. Tak, jedno sprawdzanie tego, co jest wysyłane, a drugie to jest to, czy model w odpowiedzi nie wysyła czegoś, co nie powinien. To jest przypadek, który możecie gadać sobie z chatem co chcecie, żeby on zrobił. I tu się w ogóle nic nie zmieniło i on Wam myśli, myśli, a na koniec mówi: sorry, nie mogę Ci powiedzieć, bo to by łamało jakieś prawa albo robiłoby coś, co jest nielegalne.

[00:23:02.440] **Łukasz Kałużny:** Wiesz co, a z drugiej strony taki przypadek tych podatności, jeżeli nie mamy kontroli nad danymi. Czyli przykładowo powiemy sobie, żeby MCP pobrało coś, to jest sławetny atak na MCP GitHuba, czyli ten cały prompt injection, który jest. Czyli że ściągamy sobie z publicznych źródeł issue'sa, a tam było żeby issue zleakował, była instrukcja, żeby zleakować wszystkie secrety i odpowiedzieć nimi na przykład w issue, do issue githubowego wpisać swoje wszystkie secrety i prywatne repa, do których jest dostęp. To będzie taki przykład. Czyli założenie jest takie, że cały ten prompt shield, który mamy, powinniśmy weryfikować te dane, które jeżeli są one ze źródeł publicznych gdzieś ściągane albo pochodzą z nie zaufanych źródeł, to one powinny być weryfikowane. I jak to się w niektórych określeniach mówi, że ten payload powinien być wysadzany i sprawdzany. I tutaj idąc z naszej działki najbardziej Azure, na przykład Microsoft ma usługę taką po API Restowym, która się nazywa Azure AI Safety. Dobra, chyba albo content safety, już coś z tym, coś z bezpieczeństwem w nazwie. Zostawię linka poprawnego. I całość polega, że możecie wysłać tam na przykład dokument, który wsadzacie do LLM-a albo MCP będzie pobierać i coś z nim robić i przekazywać do LLM-a, żeby sprawdzić, czy na przykład nie ma tam jakichś szkodliwych instrukcji, które pozwolą to coś ominąć.

[00:24:37.660] **Szymon Warda:** Dobra, to to mamy to wróćmy w takim razie do naszego tematu, jak ten MCP w ogóle ułożyć? Czyli jak zrobić, żeby on działał dobrze? Czyli MCP i API Gateway. Bo o tym trochę wspomnieliśmy, ale trochę może temat rozwińmy.

[00:24:53.620] **Łukasz Kałużny:** Dobra, tu jest duży problem i podam to na przykładzie MCP Jiry. MCP od Jiry, tej cloudowej, jeżeli się do niego podepniemy, po prostu zwraca słuchajcie as is restowe API. Czyli po prostu wyrzuca kupę nieudokumentowanych pól, niezrozumiałych opisów i innych rzeczy. Po prostu tak jakbyście ściągnęli sobie Postmanem coś z Jiry, to wystawia to do LLM-a i LLM gówno tego nie rozumie, przepraszam za to określenie. Albo ilość, co teraz jest jeszcze gorsza, większym wyzwaniem, o czym sobie powiemy, albo ilość tokenów, które zwraca jest za duża i wykorzystujemy limit okna naszego kontekstu input tokenów na to, żeby wrzucić syf. I tutaj jeżeli mówimy, że jest to API Gateway, to jest to API Gateway dla LLM-ów i musi być dostosowany, to co będzie MCP zwracało, musi być dostosowane do LLM-ów. I to jest taka rzecz kluczowa do zrozumienia. I ja w tym miejscu, słuchajcie to co mogę Wam polecić, jak rozmawiałem z klientami z naszej praktyki, że to co wystawiamy do LLM-a, to nie jest nasz CRUD z systemu biznesowego czy jak to tam ładnie nazwiecie swoje API, które wystawiacie, tylko przemapowanie tego na faktyczne funkcje biznesowe. Jeżeli coś jest niepotrzebne, to nie powinno być wystawiane w tym. Więc o MCP można pomyśleć jako API Gateway. Ale to nie jest API Gateway w tym rozumieniu, w którym go używaliśmy.

[00:26:36.710] **Szymon Warda:** Parafrazując to, co powiedziałeś, to musi być API, które będzie realnie używalne i które będzie dostarczało jakąś wartość, że model może coś tam zrobić, a nie na zasadzie jak CRUD-a, że zrób to, zrób to, zrób to, bo w tym momencie, jeżeli to byłby taki prosty CRUD, to nie przekładamy na model całą logikę naszą biznesową, której on oczywiście nie ma tak naprawdę. ... i tyle.

[00:26:59.240] **Łukasz Kałużny:** Albo co ważne i najgorsze może się okazać, że model nie trzyma się instrukcji i naszej logiki biznesowej, którą sobie wymyśliliśmy w API, którą na przykład frontend trzyma się doskonale, bo go tam zakodowaliśmy, jest deterministyczne, ale model nie ma ochoty na to.

[00:27:18.120] **Szymon Warda:** Model będzie się coraz mniej trzymał tej logiki im dłuższy jest chat, im dłuższy kontekst ma i tak to będzie wyglądało. Nie uciekniemy przed tym. Dobra, czyli powiedzieliśmy sobie. Mamy jeszcze dwie ważne rzeczy. Mamy jeszcze izolację i rate limiting.

[00:27:33.120] **Łukasz Kałużny:** Dobra rate limiting chyba...

[00:27:35.460] **Szymon Warda:** Prosta opcja. Ogólnie badamy to, żeby jeden klient nam nie utłukł całego systemu i musimy mieć jakieś miejsce, gdzie będziemy mówili kto, co, ile zasobów zużywa. Co jest super ważne w kontekście tego jak my pracujemy, to jest to, żeby na przykład postawić APIM-a po drodze, żeby dokładnie wiedzieć kto z czego korzysta, jak to wygląda i żeby ten ruch móc jakoś śledzić mówiąc bardzo prosto. Bo potem przyjdzie rachunek i okaże się, że sorry, ale nie wiemy kto tyle zużył.

[00:28:01.410] **Łukasz Kałużny:** Dobra. I teraz ten sampling request, ta izolacja od tej strony. Jeżeli popatrzymy. I tutaj zróbmy to na przykładzie tego, co jest w dokumentacji od MCP, jak ta izolacja działa i sampling. Czyli przykładowo serwer ma listę na przykład lotów dostępną, przesyła je do użytkownika i użytkownik na przykład akceptuje, czy przekazać to potem w ogóle do LLM-a czy nie. To jest jeden taki human in the loop, jeżeli teraz popatrzymy, na tym samplingu. To jest założenie, że klient w którymś miejscu ma tą interakcję i taką jawnie powiedzianą. Dla mnie, jeżeli ktoś z Was vibe code'uje czy użył Copilota, Cursora, Claude Code, to jest na przykład taka rzecz, którą widzimy, że ja chcę wywołać jakieś narzędzie albo zedytować plik. I to jest chyba tak od strony developerskiej do pokazania, to, że mamy gdzieś jawne interakcje, gdzie akceptujemy coś, a potem jest to kończone tak naprawdę w tym. I teraz jest też rozwalenie, bo tam się pojawia właśnie nie tylko sampling, ale leak... Wywołania, o tak, po polsku będzie lepiej, nie będę się męczył z moim sposobem wymowy. Więc pojawiają się jeszcze, oprócz samplingu pojawiają się wywołania, czyli założenie docelowo w MCP będzie, że samplign będzie jednym, wywołania będą drugim. Ale to już zostawmy w tym momencie drafty w spokoju.

[00:29:38.130] **Szymon Warda:** Łukasz mówi o elicitation. Dla tych, którzy chcieliby wygooglać o co chodzi. Dobra, czyli co, to mamy zamknięte. To teraz ok, kupiliśmy czym jest MCP, kupiliśmy, jak korzystać, do czego jest i tak dalej. To jak teraz w ogóle zacząć używać? Czy to jest na zasadzie zaczynamy od zera czy...

[00:29:59.640] **Łukasz Kałużny:** Dobra.

[00:30:01.290] **Szymon Warda:** Jak to monitorować? Jak debugować?

[00:30:03.150] **Łukasz Kałużny:** Dobra, mamy dwa podejścia. Po pierwsze YOLO, czyli vibe code'ujemy i to zostawmy. A na poważnie to jest pytanie, czy my kodujemy własne MCP Server? To jest od strony, bo zazwyczaj...

[00:30:20.220] **Szymon Warda:** Wątpliwy sens.

[00:30:20.470] **Łukasz Kałużny:** Tak. Czy wiesz co, wątpliwy w niektórych momentach będzie. Jeżeli na przykład robisz produkt i inne rzeczy to nie przeskoczysz.

[00:30:27.060] **Szymon Warda:** Może tak. Pytanie jak od zera, bo są biblioteki, które już dają, są tą bazą, Serverem MCP i od tego można zacząć.

[00:30:35.130] **Łukasz Kałużny:** Tak, czyli inaczej, nie kodujemy tego od zera, tylko bierzemy SDK i lecimy z SDK w języku, który preferujemy w firmie.

[00:30:46.680] **Szymon Warda:** Tak, tam są czasem takie drobne rzeczy typu właśnie jak są outy ustawione jakieś, jak są standardy spełniane i tak dalej. To nie jest tak, że tworzymy nowy serwer HTTP i lecimy od zera. Nie, to nie jest, nie ta droga.

[00:30:59.010] **Łukasz Kałużny:** Bierzemy SDK i wpinamy się i to będzie budowało nam. W sumie w wielu przypadkach będzie to po prostu jakaś nakładka i kolejne proxy. I tutaj pójdę w tą stronę, idąc, odwołując się do części azure'owej. Azure API Management, który jest takim bardzo dużym gatewayem, daje na przykład możliwość wystawienia polityk właśnie tych rzeczy, które już opublikowaliśmy, republikację jako MCP. I to jest taka rzecz, której bym się zastanowił teraz, jeżeli na przykład korzystam z Azure'a czy z innych rzeczy, bo też sobie researchowałem, jest parę innych, też open source'owych już takich narzędzi, czy ja nie wystawię po prostu czegoś istniejącego z drobną zmianą logiki na takim proxy API Gateway, żeby dostosować to pod LLM-a. Czyli taki kierunek teraz zawodowy, jak popatrzymy i doświadczenie mówi, że pojawią się teraz produkty i trzy razy bym się zastanowił, czy nie wykorzystam gotowego kawałka usługi albo rozwiązania softwareowego, które pozwoli nam zrobić przemapowanie, niż pisać coś od zera.

[00:32:12.500] **Szymon Warda:** Tak, tylko tu jest jedna rzecz ważna, to jest to, o czym mówiliśmy, trzeba trochę podkreślić to, co mówiliśmy wcześniej. To nie jest przemapowanie do jednego. Tam dalej musi być filtracja, dalej musi być zerknięcie co, jak, gdzie i co nam to wypluje. Bo wejdzie masę narzędzi, które powiem, że jak z każdą technologią: użyj naszego narzędzia i już w ogóle robota zakończona. To tak nie do końca działa. One ułatwiają pracę, ale dalej po naszej stronie musi przejść filtracja, jak to w ogóle wygląda i jak to będzie wykorzystywane.

[00:32:39.740] **Łukasz Kałużny:** Inaczej, do dużej ilości scenariuszy, na przykład od strony Azure'a, można zaprząc połączenie Azure API Management + Logic Appsy tam, gdzie potrzebujemy trochę logiki. Ale jak zaczynamy kończyć z workflowem i ifologią i innymi rzeczami, zaczynamy budować coś, co nie przypomina prostej rzeczy: zbierz mi z kilku endpointów na przykład po kolei logikę, tylko zaczynamy robić drzewo grafów i wygląda to jak klasyczny kod, to lepiej odpalić i samodzielnie napisać taki serwer, a potem można go przeproxować przez taki API Management. Bo na to API Management pozwala, żeby robić też reverse proxy do innych MCP, więc to jest spoko i trzeba znaleźć. Jeżeli nie mamy super skomplikowanej logiki, lepiej pójść w niskokodowe rozwiązania. Ale jeżeli zaczynamy robić za dużo, to już warto podejść do tego. I teraz co trzeba sobie powiedzieć o tych funkcjonalnościach API Gateway'ów? To będzie istotne. One zakładają użycie toolsów, jeżeli popatrzymy. To jest istotny element, że one nastawiają się na toolsy głównie, trochę resource'y. A jeżeli będziemy chcieli wykorzystać większe możliwości, to prawdopodobnie i tak będziemy musieli skończyć z samodzielnym odpaleniem serwera MCP.

[00:34:05.210] **Szymon Warda:** Własnego serwera albo jakieś przejściówki. Dokładnie tak. Dobra, to co tam jeszcze mamy?

[00:34:11.630] **Łukasz Kałużny:** Debugger. Debugger, MCP Inspector.

[00:34:15.290] **Szymon Warda:** Przydatny.

[00:34:17.570] **Łukasz Kałużny:** Szymon, inaczej, dopracowany. To jest w ogóle piękna rzecz.

[00:34:22.610] **Szymon Warda:** I żeby to było jasne, bo w ogóle MCP Inspector to nie jest jakiś taki side project, że tak powiem, tylko to faktycznie jest wpisane w dokumentacji jako jedno z narzędzi, które są preferowane. Więc to jest ładnie rozwijane i faktycznie zachowuje się i wygląda dobrze. Tam nie ma popeliny.

[00:34:36.950] **Łukasz Kałużny:** Jest przyjemny, działający UI, wspiera uwierzytelnianie. Uwierzytelnianie do serwera, czyli na przykład jak debugujemy lokalnie możemy przejść sobie cały flow oauthowy, dostarczyć swoją tożsamość i to jest mega dla mnie istotne. Bo na przykład możemy sprawdzić czy wykorzystujemy poprawnie context usera.

[00:34:58.460] **Szymon Warda:** Dobra, to co, lecimy dalej, bo tam jeszcze jest parę rzeczy generalnie. Są jeszcze narzędzia do przeglądania, do debugowania całego JSON-a i takie bardziej niskopoziomowe rzeczy. Ale większość sytuacji nasz MCP Inspector wystarczy. Czy coś jeszcze?

[00:35:19.070] **Łukasz Kałużny:** Wiesz co, nie, to bym zostawił, ale poszedłbym do trochę wyzwań praktycznych, które będą.

[00:35:24.830] **Szymon Warda:** No to lecimy w takim razie.

[00:35:25.850] **Łukasz Kałużny:** Czyli z doświadczenia. I pierwsza rzecz, o której powiem, za dużo narzędzi, za dużo zwracamy i przez to mamy albo wyczerpanie okna kontekstowego w LLM-ie, albo problemy z trzymaniem się, bo jest za dużo kontekstu. I to jest chyba rzecz, którą okej, jak tam mamy, to patrzę na tą sraczkę jak nawalimy za dużo extension'ów do IDE, żeby mieć super piękne albo do konsoli, nie wiemy co się dzieje, to tutaj będzie podobnie.

[00:35:56.780] **Szymon Warda:** Bo to jest znowu taki akt balansowania, bo też można walnąć jeden obiekt, jedno wielkie narzędzie z absurdalnym i bardzo skomplikowanym API. To też nie zadziała do końca.

[00:36:08.540] **Łukasz Kałużny:** Tak, dlatego mówię, że bardziej mówię, żeby nie było w tym na przykład tak... Jak tworzymy agenta, to weźmy przypadek korporacyjny, najczęstszy, tworzymy agenta, to on tych MCP nie powinien mieć nawalone, że zrobi nam wszystko na raz, tylko może nad nim jest jakiś agent orchestrator, który woła małego agenta, który ma podpięte małe MCP, wykorzystane ileś tam akcji, a nie jeden wielki agent do zbawienia całego świata.

[00:36:38.540] **Szymon Warda:** Dobra, to jeszcze jakie mam praktyki dobre, jeżeli chodzi o budowanie samych narzędzi?

[00:36:43.550] **Łukasz Kałużny:** Dobra, kolejna rzecz, żeby pamiętać o SCIM-ie Validation na inpucie i dobrym opisie SCIM-y inputowej i outputowej. To chyba jest w ogóle najbardziej istotny element całości.

[00:36:58.940] **Szymon Warda:** Bo model musi wiedzieć, co właściwie produkuje, co przyjmuje, czego może użyć i co ma zwrócić tak naprawdę.

[00:37:05.030] **Łukasz Kałużny:** Tak. Kolejna rzecz to content, żeby wspierać obsługę różnych formatów. I to jest dyskusyjna rzecz, o tak, w jaki sposób do tego podchodzimy. Ale z założenia możemy wrzucić tam i tekst i binarki, imige, więc jest ileś takich możliwości tutaj.

[00:37:26.900] **Szymon Warda:** Tak, idziemy dalej. To, o czym mówiliśmy, czyli notyfikacja. Mówiliśmy, że te rzeczy właśnie jak toolsy, utilities i tak dalej, one mogą się zmieniać, że to jest szczególnie ważne przy plikach w kontekście załóżmy jak pracujemy, nawet jakąś ideę i tak dalej, żeby model był notyfikowany o tym, że coś się zmieniło. To też jest dobre w kontekście bycia, żeby ten model był bardziej proaktywny, żeby tam coś się działo.

[00:37:47.870] **Łukasz Kałużny:** Raczej to wiesz, też mówimy nie model a klient. Czyli że jak idzie następny request, to że dzieją się nowe rzeczy. I druga sprawa, która jest w wyzwaniach praktycznych. Jeżeli mamy long running joby, to serwer powinien odsyłać progres. Czyli jest tam w tym trzymana sesja, jest odsyłany progres. Bo są ciekawe przypadki, ja nauczyłem się tego w praktyce, jak mi model zaczął halucynować, jak zaczęło się pobieranie, obrabianie jakiegoś tekstu związanego właśnie z podcastem. I on na podstawie tytułu, słuchaj Szymon, wymyślił nam, zsumaryzował nam odcinek, do którego nie miał transkryptu.

[00:38:30.600] **Szymon Warda:** Słuchaj, ja dałem modelowi ostatnio, opcję chatowi, żeby zrobił OCR-a. Bardzo ładnie, zupełnie innymi słowami opisał co jest, co tam na stronie zobaczył. Nie miało to nic wspólnego z tym, co właściwie tam się działo.

[00:38:42.270] **Łukasz Kałużny:** I nie miał tej strony.

[00:38:44.580] **Szymon Warda:** Tak, w ogóle, nie wyszło mu to kompletnie. Dobrze, to teraz wracamy na chwilę od naszych odskoczni. Odnośnie czy dane, które wysyłamy, to pamiętajmy też o takich rzeczach typu właśnie, że mamy tam jeszcze paginacja albo jeszcze inne rzeczy, więc zwracanie tych danych też może odbywać się w etapach, nie ma co też wysyłać. Dobre praktyki developerskie są też mile widziane wszędzie. Dobrze, workspace bundories.

[00:39:11.040] **Łukasz Kałużny:** Czyli właśnie te rooty. Tylko one... Inaczej, znowu pójdę teraz, rooty są wspaniałą rzeczą. Zwrócę się teraz z powrotem Szymon do client feature'ów co i jak jest supportowane i pozostawmy to tym minutą, zróbmy tutaj minutę ciszy na temat tego feature'a. Czyli on jest, ale jest to implementowane zazwyczaj już w samym agencie, narzędziu, a nie w tych gotowcach.

[00:39:43.620] **Szymon Warda:** To wchodzimy na, jeszcze poruszymy temat jeden, czyli autonomiczni agenci, czyli poziom szamański bardzo wysoki, ale to trzeba powiedzieć.

[00:39:52.380] **Łukasz Kałużny:** Dobra, autonomiczny agent to oznacza, że cron, event albo request go wywołał. To jest autonomiczny agent. On tam nie siedzi i nie myśli, więc zostawmy. Problem przy autonomicznych będzie jeden wielki.

[00:40:11.970] **Szymon Warda:** Monitorowanie.

[00:40:12.360] **Łukasz Kałużny:** Ale z drugiej strony, monitorowanie tego, wykorzystania tych MCP. I znowu wrócę do samego początku wyzwań, czyli żeby miał mało narzędzi, ograniczony scope i nie musiał on rozumieć pokrętnej logiki biznesowej, jeżeli taka występuje, tylko żeby miał jak krowie na rowie podane. I druga rzecz, która nam wychodzi z tego, to bardzo ładnie, nawet jak jest autonomiczny, automagiczny, samodzielny, to na koniec dnia powinien być zaimplementowany człowiek. Przykładowo, że modyfikacja w systemie to być może jest przygotowanie draftu, wysłany mail z akceptacją, że ma zostać coś zedytowane, czy propozycje na przykład update'ów w systemie, które człowiek zaakceptuje.

[00:41:04.300] **Szymon Warda:** Tak, to co ruszyłeś jest bardzo ważne, bo to nie jest tak, że możemy podłączyć się, że powinniśmy móc to, bo nie możemy naszych agentów MCP wystawić z jakichś systemów, na przykład korporacyjnych, księgowych i tak dalej, one będą sobie tam śmigały, bo automagicznie wyczają co tam powinno się dziać. To jest coś, co powinno być na chwilę obecną jeszcze weryfikowane i sprawdzane, czy tam człowiek, odpowiedzialność jest po stronie człowieka.

[00:41:28.630] **Łukasz Kałużny:** Tak, ja tutaj zostawię bardzo ważne, przypomnę, bo to omawialiśmy, wydaje mi, się przed wakacjami. To była luka Zero-Click w Copilocie. Ten atak był chyba nazwany EchoLeak, jak dobrze pamiętam. I tutaj macie wspaniały przykład, że twórcy technologii sobie z tym nie radzą, a co dopiero narzeźbiony kawałek agenta modnym frameworkiem LLM-owym.

[00:42:02.170] **Szymon Warda:** Chcąc być uczciwym, to ta sekcja odnośnie płatności i w dokumentacji się rozwija i tam jest coraz więcej. I te opisy jak płatności wyglądają są już całkiem niezłe. Więc podchodzą do tego zdecydowanie poważnie. To nie jest takie: wyczaicie sobie sami. Dobra, czy mamy coś jeszcze właściwie, czy kończymy ten odcinek?

[00:42:22.900] **Łukasz Kałużny:** Kończymy, bo chyba można powiedzieć, że bierzcie i testujcie. A jak potrzebujecie pomocy w firmie, to zgłoście się, bo robimy też to na co dzień.

[00:42:35.830] **Szymon Warda:** Dokładnie tak. Dobra, to co? Tyle, na razie. Heja.

[00:42:40.060] **Łukasz Kałużny:** Hej!

