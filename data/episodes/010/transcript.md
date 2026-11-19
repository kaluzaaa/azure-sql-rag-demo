# 10.mp3

[00:00:12.800] **Szymon Warda:** Cześć, słuchacie Patoarchitektów. Prowadzą, Szymon Warda...

[00:00:17.210] **Łukasz Kałużny:** I Łukasz Kałużny. Wszystkie linki do tego odcinka znajdziecie na Patoarchitekci.io/10.

[00:00:26.090] **Szymon Warda:** Dobra, to temat, dziś Service Mesh, ale z punktu widzenia CTO i architektów. Zanim do tego głównego tematu przejdziemy, to linki. Łukasz.

[00:00:37.490] **Łukasz Kałużny:** Dobra, to będąc przy tematach wokoło Service Mesha, czyli Kubernetes na serverlessie... Przepraszam, serverless na Kubernetesie. Jest ciekawa decyzja Knative, projektu prowadzonego przez Google'a. Był jeden z pomysłów i chęć community, żeby ten projekt został przeniesiony, darowany do Cloud Native Foundation. I w Google powiedzieli nie.

[00:01:06.150] **Szymon Warda:** Co nie dziwi.

[00:01:06.930] **Łukasz Kałużny:** Tak, co nie dziwi. I żebyście wiedzieli, jaka jest struktura tego, to Komitet Sterujący Knative składa się z siedmiu osób, z czego czterech to pracownicy Google'a.

[00:01:19.620] **Szymon Warda:** Tak często to jest zbudowane, są takie grupy pracownicze.

[00:01:24.030] **Łukasz Kałużny:** Tak i spotkania Komitetu Sterującego, w przeciwieństwie do pewnych innych projektów open source'owych, są robione za zamkniętymi drzwiami. Czyli nie są, nie można zobaczyć streamingu, notatek, można zobaczyć tylko decyzje z tego, co zostało podjęte. Więc jest to dość ciekawy sposób, że ten open source nie jest do końca takim... Fajnie, że są źródła, ale wpływ rozwoju na niego jest często podyktowany warunkami sponsorów i to bardzo mocno. Nie ma takiego mocnego wpływu z zewnątrz, o jakim się mówi.

[00:01:56.910] **Szymon Warda:** Znaczy nie oszukujmy się, ktoś za ten open source, za czas tych ludzi płaci. A tam gdzie są pieniądze, to też są oczekiwania i trzeba być tego świadomym. Dobra, to ode mnie. Ja natomiast w kontekście też C-levelu, ale w kontekście też tak naprawdę bardziej fuckupów, o których mówiliśmy wcześniej. Nie raz zdarzała się taka sytuacja, że jakiś projekt widzimy ewidentnie, że to jest taki death march, czyli że za chwilę to wybuchnie. Z reguły się udaje, ale nie zawsze. Historia banku, gdzie właśnie miało być połączenie dwóch banków, migracja między systemami i tak dalej, czyli sytuacja, którą z reguły widzimy albo uczestniczymy, która się faktycznie nie udała. Nie udała się do tego stopnia, że weszła w Wielkiej Brytanii grupa kontrolująca nadzór finansowy i bank z 200 mln przychodu zaraportował 100-parę mln strat w kolejnym roku. Więc faktycznie całkiem ciekawy link, który opisuje to, jak się może nie udać i że to czasami widzimy, że projekt idzie źle, ale mimo mówimy sobie, że i tak się uda, i tak będzie success. Nie zawsze. Czasami może być spektakularna porażka. Bardzo fajny wpis z kilkoma nauczkami, z prostymi błędami.

[00:03:13.290] **Łukasz Kałużny:** Tak, to zawsze jest fascynujące, bo wiem jak wyglądają, nawet wiem, kiedy są te migracje w bankach. Mniej więcej ta wiedza gdzieś na rynku usługowym, konsultacyjnym istnieje, co się dzieje w branży.

[00:03:25.500] **Szymon Warda:** Ja bym nie ograniczał do banku, dużych instytucji.

[00:03:27.720] **Łukasz Kałużny:** Dużych instytucji, ale mówię o bankach, ponieważ komunikaty o braku płatności, możliwość braku płatności kartą...

[00:03:34.230] **Szymon Warda:** Dostępów i tak dalej.

[00:03:34.950] **Łukasz Kałużny:** Dostępów i innych rzeczy jest to dla nas, dla osób nietechnicznych jest najbardziej widoczne w ogóle, jeżeli sobie popatrzymy. I zawsze mi żal tych ludzi, ile jest tych migracji, jak są rozdrobnione.

[00:03:46.530] **Szymon Warda:** Tak.

[00:03:46.980] **Łukasz Kałużny:** Tak. W szczególności jeden z banków chyba przenosił swoje data center przez jakiś czas i mieli okna, przez ostatnie pół roku bardzo często komunikaty.

[00:03:56.440] **Szymon Warda:** Lepsze to niż jeden z podstawowych błędów, który tu właśnie jest opisywany, to jest to, że niejako czas migracji został odłożony upfront, a potem ludzie techniczni mieli się do tego wyrobić. To tak nie działa.

[00:04:08.920] **Łukasz Kałużny:** No tak, trochę o Agile'u, o którym kiedyś rozmawialiśmy.

[00:04:12.310] **Szymon Warda:** Dokładnie. Dobrze, to przejdźmy do naszego głównego tematu.

[00:04:16.690] **Łukasz Kałużny:** Dobrze, Szymonie. To jako że Ty u siebie na blogu często nawiązywałeś do meshów, nawet pisałeś o zaletach artykułów. Więc klasycznie, czym jest w dwóch zdaniach Service Mesh?

[00:04:28.390] **Szymon Warda:** To będzie trudne, ale jest to nowy sposób na budowanie platformy dla serwisów. I tu użyję tej platformy, którą Ty często używasz, bo tu się wybitnie zgodzę, to jest platforma.

[00:04:39.070] **Łukasz Kałużny:** Dobra. Nie udało Ci się, zbyt lakonicznie. Może uda Ci się kiedyś dojść, tak jak i mi. Dobra, to czym to jest faktycznie?

[00:04:46.900] **Szymon Warda:** Faktycznie, tak naprawdę jest to zaadresowanie problemów świata komunikacji, świata synchronicznego przez warstwę infrastruktury. Czyli wyniesienie wszystkich circuit breakerów, retry'ów, time outów, fallbacków i tak dalej, do poziomu infrastruktury tak naprawdę. Czyli wyrzucenie tego z kodu aplikacyjnego.

[00:05:05.760] **Łukasz Kałużny:** Wiesz co, ale jak sobie popatrzysz, wpiszę teraz w Google Service Mesh czy tam w Binga, to od razu pojawia się Kubernetes. Praktycznie we wszystkim, przy każdym pojęciu Service Mesh znajdziemy Kubernetesa.

[00:05:18.060] **Szymon Warda:** Tak i to się zgadza, ponieważ obecnie Kubernetes już jest wszędzie, to po pierwsze. Ale po drugie, to żeby móc właśnie wynieść te wszystkie odpowiedzialności i dalej zapewnić skalowanie, bo nie chcemy oddawać tego, co nam daje Kubernetes, czyli przenoszenia, skalowania i tak dalej, deploymentów, to ten Service Mesh musi na czymś chodzić. I większość implementacji Service Meshy wykorzystuje z Kubernetesa. Czemu? Bo to jest niejako kolejny poziom w rozwoju naszej infrastruktury.

[00:05:45.600] **Łukasz Kałużny:** Czyli jest to wyżej tak naprawdę, aplikacje przenosimy na jeszcze wyższy poziom.

[00:05:51.730] **Szymon Warda:** Ja to zawsze widzę jako taką galaretkę, w którą wrzucamy nasze serwisy. Ta galaretka zajmuje się wszystkim, co ta aplikacja potrzebuje, logowania i tak dalej. O czym dokładnie też będziemy mówili sobie, ale to już zapewnia wszystkie elementy do życia potrzebne.

[00:06:05.920] **Łukasz Kałużny:** No i chyba jeszcze warto wspomnieć o koncepcji Microsoftu. Tak naprawdę o Meshu od Microsoftu, który był, podchodził do tego poziom wyżej i robił to na czystym cloudzie, pomijając.

[00:06:15.910] **Szymon Warda:** Tak, MS w ogóle, jak to zwykle z MS-em bywa, mieli super pomysł, zbyt wcześnie, (...) poziomem abstrakcji wyżej, ale to już chyb przy konkretnym Service Fabricu będziemy o tym mówili dokładnie, jaki na to pomysł mieli i czemu to miało ręce i miało nogi i czemu się nie udało.

[00:06:32.260] **Łukasz Kałużny:** Dobrze, tytułując mówiliśmy, że mamy to, mamy CTO i mamy architektów w dzisiejszym odcinku. Więc jako architekt w jakim sposobie byś poszedł i rozmawiał ze swoim CTO, że chcesz wdrożyć właśnie i zainteresować go w swojej strategii organizacji Service Meshem?

[00:06:50.700] **Szymon Warda:** I to jest bardzo fajne pytanie i na nie trzeba odpowiedzieć na dwa różne sposoby. Bo jeżeli komunikujemy się z C-levelem, z ludźmi zarządzającymi, to pierwsze musimy wiedzieć, jak ten człowiek myśli w kontekście tego, że ludzie często wychodzą od problemu, czyli staramy się rozwiązywać problemy, albo mają jakieś cele, które realizują. To brzmi podobnie, ale trzeba odpowiednio ująć. I teraz...

[00:07:13.260] **Łukasz Kałużny:** To może zacznijmy od problemu.

[00:07:14.760] **Szymon Warda:** Od problemu, dobrze. Jeden z problemów, który przede wszystkim można rozwiązać i rozwiązuje Service Mesh, to jest, wywala tą integrację pomiędzy systemami tak naprawdę. Czyli jest tego mniej, robi się to łatwiej i po prostu jest. To jest też, działa.

[00:07:33.720] **Łukasz Kałużny:** Co ważne, klasyczną synchroniczną integrację.

[00:07:36.150] **Szymon Warda:** Tak, bo oczywiście Service Meshe mimo, że są pomysły na Service Meshe do komunikacji kolejkowej, co jest bardziej API, ale to jeszcze jest pieśnią przyszłości na chwilę obecną. To na razie o tym nie mówimy, mówimy tylko o komunikacji synchronicznej, która jest głównym sposobem komunikacji między systemami w większości organizacji, bo jest najłatwiejsza. HTTP jest bardzo uniwersalny i wszystko, JSON-a skonsumuje.

[00:07:56.050] **Łukasz Kałużny:** Wspomaga, akceleruje budowę tego, komunikacji pomiędzy różnymi usługami.

[00:08:01.540] **Szymon Warda:** Tak. I kolejny obszar to jest to, że często te usługi, którymi będziemy się integrowali, to są stare usługi, których nikt nie chce dotykać już albo nikt nawet nie wie, jak ich dotknąć. I w tym momencie rozwiązujemy problem, że coś, co jest stare, działa słabo i tak dalej. Wrzucamy w galaretkę, która ogarnia kilka rzeczy i dzięki temu system działa lepiej. Nie rozwiązuje problemów wszystkich, ale zmniejsza tą liczbę problemów. Teraz drugie podejście, jak ktoś jest nastawiony na cele. To jest obniżenie kosztów implementacji nowych systemów. Jak? Bardzo prosto. Jeżeli przychodzi firma z ofertą na implementację czegoś, to mówimy: ok, autoryzacja, autentykacja i tak dalej, tym się nie martwicie, logowanie...

[00:08:41.170] **Łukasz Kałużny:** Przepraszam, uwierzytelnianie.

[00:08:43.210] **Szymon Warda:** Dobrze, faktycznie. Czyli tak naprawdę wywalamy bardzo dużo kodu. I tu specjalnie mówię bardzo dużo, bo jak pozbieramy sobie wyceny systemów, ten kod infrastrukturalny, to jest znaczący koszt często każdego systemu, który się nie zawsze zwraca.

[00:08:58.130] **Łukasz Kałużny:** Czyli ważne, trzeba powiedzieć, mówimy tutaj, jeżeli myślimy o usługach, to myślimy o usługach backendowych, które są tą częścią serwerową.

[00:09:06.140] **Szymon Warda:** Tak, dokładnie. Ale w sumie tak naprawdę moglibyśmy zrobić proxowanie, żeby frontend załóżmy retryował. To też jak najbardziej. Kolejnym plusem jest to, że mamy, ja to trochę nazywam jak takie cloud like features w świecie onpremowym bez vendor lockingu tak naprawdę.

[00:09:23.060] **Łukasz Kałużny:** Dobra, to ja od razu może dorzucę takie ryzyko, które pewnie, ryzyko, pytanie, ryzyko tudzież pytanie, które możemy dodać, bo trzeba to utrzymywać. I teraz co z kompetencjami? Bo któryś, zwykle pewnie jak mówimy o platformie, to zespół operations trzeba spivotować na nowe kompetencje, na nowy sposób. I to też z jednej strony będzie to zaleta, że będziemy chcieli wprowadzić jakąś platformę. Ale wadą, że musimy nabyć nowe kompetencje, jeżeli to nie jest cloud i usługa manage.

[00:09:52.900] **Szymon Warda:** Bardzo dużo nowych kompetencji, powiedzmy sobie szczerze. Z drugiej strony to, co powiedziałeś wcześniej tak naprawdę, że na przykład niektóre Service Meshe są jako platforma w niektórych chmurach. Ten sam kod możemy też odpalać na onpremie bez większych problemów. Pytanie gdzie chcemy pójść? To samo mamy z Kubernetesem. Mamy managed Kubernetes w każdej niemalże chmurze, możemy też odpalić to lokalnie. Ale tak, ważne. Skille, które nagle musi nabyć zespół OPS są bardzo duże.

[00:10:23.380] **Łukasz Kałużny:** Dobrze, to jeszcze powiedzmy o, powiedziałeś cloud like. To jakie właśnie te funkcjonalności cloud like?

[00:10:29.740] **Szymon Warda:** Deployment, coś, co jest dziesiątki, nawet czasami tysiące linii kodu powershella, out of the box. Dla mnie jeszcze tracing, monitoring mamy out of the box. To samo co jest na przykład w serverlessie, po prostu działa, jest, nie martwimy się tym. To jest super. I skalowanie, które w sumie daje nam Kubernetes, ale można też powiedzieć przy meszach, jak najbardziej.

[00:10:50.700] **Łukasz Kałużny:** Tak, a przy deploymencie powyżej Kubernetesa to są te zaawansowane metody z pudełka, czyli Canary, testy A, B, green blue deploymenyt.

[00:11:01.710] **Szymon Warda:** Tak.

[00:11:02.580] **Łukasz Kałużny:** Tak. Ja bym od siebie dorzucił rzecz, o której wspomniałeś, czyli security warstwę. Możemy, platforma może zautomatyzować dostęp do aplikacji, jak i też cały routing aplikacyjny, integracyjny, który może narzucić ten mesh.

[00:11:17.460] **Szymon Warda:** Tak. To stworzenie application map i tak dalej, które na przykład daje nam application insert albo coś innego, nagle to po prostu jest, działa i jest fajne.

[00:11:25.620] **Łukasz Kałużny:** Dobrze, to czemu, bo mieliśmy teraz pójście do CTO, a może teraz odwróćmy pytanie, czyli czemu jako architekt ja miałbym pójść do CTO? Czemu chciałbym tego użyć?

[00:11:40.620] **Szymon Warda:** Argumenty są podobne, jak były przy CTO, tylko patrzymy z innej perspektywy. Przede wszystkim jako architekt, jak mam wycenić ten nowy system, po raz kolejny nie muszę martwić się całym kodem infrastrukturalnym, nie muszę reimplementować, dać uwierzytelnienia, logowania, wysyłania metryk i tak dalej, i tak dalej, i tak dalej, w nowej platformie, w nowym języku i tak dalej, i tak dalej. Ten cały boilerplate wychodzi.

[00:12:05.310] **Łukasz Kałużny:** Czyli tak naprawdę funkcjonalności, które sobie za chwilę wymienimy, przenosimy z kodu aplikacji. W niektórych przypadkach nawet go usuwamy, jeżeli już go posiadamy, bądź... Wyłączony kod powinien być tak naprawdę usunięty, to jest też założenie. I przenosimy te zależności do konfiguracji.

[00:12:26.010] **Szymon Warda:** Tak, do konfiguracji. Realnie przenosimy odpowiedzialność, bo wiemy, że w żadnym systemie IT nie można usunąć złożoności, można tylko przenieść w inne miejsce. Ale jest bardzo duże prawdopodobieństwo, że w tym momencie to już zaimplementowane. Czemu? Bo leci po natywnych protokołach, takich bardziej sieciowych tak naprawdę. Działa. I wracamy do clue. To jest platforma. To nie ma sensu robienia tego w kontekście dla jednego systemiku, może jako proof of concept. Ale docelowo to będzie platforma, bo tego będzie. Jak przeniesiemy odpowiedzialność z aplikacji do infrastruktury, to potem musimy to utrzymywać, więc to dalej istnieje. To trzeba zrobić raz dla wielu systemów.

[00:13:02.240] **Łukasz Kałużny:** Tak, to z tym się zgodzę i bym tutaj dodał jeszcze, żeby nie być, powiedzmy, aż tak sfokusowany, że to musi być wiele systemów, jest to dla wielkich. Jak mówiliśmy przy Kubernetesie, jest tam dużo zalet, ale tylko wtedy, kiedy bierzesz to jako zarządzaną usługę.

[00:13:18.860] **Szymon Warda:** Tak, w kontekście jeżeli to ma być dla jednego systemu czy mniejszego, bierzemy jako zarządzana usługa. Jeżeli się rozrośnie, to w tym momencie będziemy mogli to przenieść na więcej systemów i tak dalej. Ale wchodzenie na onpremie, średnio.

[00:13:32.540] **Łukasz Kałużny:** Dobra, co dalej?

[00:13:34.520] **Szymon Warda:** To co, jeżeli uda nam się usunąć te wszystkie implementacje z aplikacji, to Service Mesh daje nam taką realną i kosztowo i pod względem sensowności możliwość posiadania systemu w wielu technologiach. Czyli na przykład mamy kawałek w Node, Pythonie, .Necie, Javie i tak dalej.

[00:13:52.920] **Łukasz Kałużny:** Wiesz co? I teraz takie, jak to jest realne? Bo mówimy o kolejnej pięknej, utopijnej wizji, którą przepraszam, ale była już przy mikroserwisach, bez żadnych Kubernetesów, bez żadnych Meshy.

[00:14:06.720] **Szymon Warda:** I się nie sprawdziła. Zgadza się, nawet Google generalnie ma określony zbiór języków. I tak, tylko ja w tym momencie bardziej myślę w kontekście dla całej firmy. Czyli nie, że mamy jeden system na przykład księgowy w wielu językach, tylko że nasz system księgowy z reguły gada z jakimś systemem HR-owym, działa z jakimś innym systemem, na przykład raportującym i tak dalej. I te systemy są z reguły w różnych technologiach. I z nich wszystkich można wywalić te właśnie wspólne elementy. Tak naprawdę nasz system, jak wdrażamy w jakiejkolwiek korporacji, firmie, to nie jest to nigdy jeden niezależny system, który z nikim się nie komunikuje. On z reguły komunikuje się z dużą ilością systemów. My to widzimy jako integracje, ale też te elementy integracji można przenieść właśnie do Service Mesh'a.

[00:14:47.060] **Łukasz Kałużny:** Dobra, to jeszcze teraz mówimy o funkcjonalnościach, które wchodzą. To może zagłębmy się już w konkretne rzeczy, które taki mesh nam może przynieść.

[00:14:56.300] **Szymon Warda:** Pierwszy, najważniejszy, developerzy nie martwią się ustawieniami circuit breakerów, timeoutów i tak dalej i tak dalej, rzeczy, o których i tak z reguły nie mają większego pojęcia. Co więcej, którymi się z reguły nie interesują tak naprawdę. Jak przeniesiemy te rzeczy, gdzie się nie martwią, to nagle te rzeczy lądują, ponieważ lądują w osobach, które faktycznie się tym interesują i mają o tym pojęcia, czyli OPS-ach. To OPS-i mają, powinni mieć dashboardy z monitorowaniem, znać timeouty, statystyki i tak dalej operacji.

[00:15:25.760] **Łukasz Kałużny:** Przypomniała mi się jedna anegdota, to ją wtrącę. Kiedyś mieliśmy requesty, żeby przestawiać timeouty na 60 minut czy 120 minut na firewallach.

[00:15:37.090] **Szymon Warda:** Długo.

[00:15:37.750] **Łukasz Kałużny:** Na połączenie, tak, długo.

[00:15:40.120] **Szymon Warda:** No ale właśnie, czy jak taki timeout będzie zakodowany w aplikacji, to teraz co?  Redeploy aplikacji? Nie, to powinno być na poziomie tej galaretki, która obsługuje te systemy. Kolejna opcja to jest to, co daje chmura, to jest monitoring, tracing, observability z pudełka. To po prostu jest. Z reguły albo developerzy nad palą bardzo dużo czasu, albo robią to za późno, albo tego w ogóle nie robią, albo robią to źle, bo to są kosztowne elementy infrastruktury. A na przykład posiadanie trzech systemów do tracingu albo na przykład różnych systemów do zbierania logów też nie ma większego sensu. To powinno być scentralizowane i już.

[00:16:17.500] **Łukasz Kałużny:** Czyli tak naprawdę poprzez monitoring komunikacji...

[00:16:21.640] **Szymon Warda:** Tak.

[00:16:22.360] **Łukasz Kałużny:** Dostajemy metryki całościowe z platformy, gdzie można zobaczyć całą tą sieć powiązań.

[00:16:28.570] **Szymon Warda:** Tak. Praktycznie to samo co daje na przykład Application Insights albo każdy dobry system do monitorowania. Nie musimy tego wpinać w każdy system, wystarczy, że to jest w miarę wspierane i przekazujemy nagłówki tylko HTTP, co jest proste do implementacji.

[00:16:40.300] **Łukasz Kałużny:** Jeżeli popatrzymy nad zaletami, to jeszcze z mojej perspektywy będą wsparcie aplikacji, jeżeli chodzi o security, tak jak dostępy, TLS czy AAA.

[00:16:52.750] **Szymon Warda:** Dobra, dobra, Ty się już rozpędzasz, bo mamy feedback od słuchaczy, że generalnie skrótów jest trochę za dużo. Rozwijasz.

[00:16:59.470] **Łukasz Kałużny:** Dobra, to chyba AAA trzeba rozwinąć. Authentication, authorization, accounting albo po polsku już nie tak ładnie: uwierzytelnianie, autoryzacja, rozliczalność. Czyli w tym wypadku zrzucenie na platformę odpowiedzialności za security pomiędzy serwisami, service to service. Czyli powiedzenie kto z kim może rozmawiać i czy ma prawo do danego serwisu. Bo zobaczmy, ostatnio coraz częściej do serwisu dajemy prawo tak naprawdę albo do wszystkiego, albo w ogóle w backendach.

[00:17:36.060] **Szymon Warda:** Tak, często, ja widziałem takie zastosowanie, pomysły, że na przykład jak ktoś, że sprawdzanie czy ktoś może wejść, request może wejść, jest tylko na API Gateway, a później to już generalnie wszystko śmiga bez żadnej weryfikacji. I tak nie powinno się robić, to serwisy też muszą uwierzytelniać. Tak że nie może być takiej sytuacji, że jak atakujący przejdzie przez API Gatewaya, to już ma dostęp do wszystkiego.

[00:17:57.420] **Łukasz Kałużny:** Tak, to jest jedno i tam są różne funkcjonalności też, żeby rozdzielić po pathach co do czego ma dostęp, bo tworzymy zwykle albo typu komandowe Remote Command API albo REST-owe API jakieś. To w zależności od implementacji. Tutaj jeszcze, tam w zależności od implementacji, to dochodzą, że te poziomy są razem. Wsparcie na przykład nie tylko dla HTTP, ale też dla warstwy wyżej, czyli na przykład gRPC czy innych już nakładek na HTTP i komunikację synchroniczną. Co za tym idzie? To jest też mikrosegmentacja sieci. Czyli rzecz, której developerzy nienawidzą, security i OPS-i bardzo wymagają, czyli przez konfigurację możemy sterować kto z kim, jak. Po drodze powiedziałem też o szyfrowaniu, czyli TLS-ie i to jest takie, akurat mam z tym dwojakie podejście, bo kiedyś wspominaliśmy o tym, że wdrożyliśmy konteneryzację Kubernetesa i Istio po to, żeby mieć mutal TLS-a. To jest dość słabe wymaganie, ale pozwala zarządzać właśnie tym szyfrowaniem, tym mTLS-em, tą autoryzacją, więc to jest taka rzecz. No i na koniec rzecz, która mi się podoba, to jest fault injection. Czyli że razem z pewnymi komponentami meshe mogą nam wstrzykiwać, zrobić swoją chaos monkey i wstrzykiwać nam błędne rzeczy do platformy.

[00:19:23.800] **Szymon Warda:** A przy pewnej skali to jest konieczne.

[00:19:26.310] **Łukasz Kałużny:** Tak, jest to konieczne, ponieważ cały czas jest w ruchu testowanie, nawet na produkcji naszej aplikacji.

[00:19:31.770] **Szymon Warda:** Tak, jeszcze tylko wrócę do tego, co powiedziałeś właśnie o certyfikatach i tak dalej. Umiejętność obsługi certyfikatów, żeby one nie wyciekły i żeby to było robione z głową, nie jest prosta, to jest kawałek security. Developerzy z reguły mają o tym pojęcie, nie aż tak dobre i nie będą mieli, bo nie możemy być ekspertami we wszystkim. Tak że to jest duża wartość.

[00:19:51.750] **Łukasz Kałużny:** Tak, całe zarządzanie certyfikatami jest, potrafi być problematyczne.

[00:19:57.120] **Szymon Warda:** Tak. Ale w tym momencie wracamy, tak trochę kręcimy się wokół tego tematu, że Service Mesh jest bardzo bliski serverlessowi. To jak się ma jedno do drugiego i trzeba by jakieś porównanie zrobić.

[00:20:09.300] **Łukasz Kałużny:** Wiesz co, jeżeli bym na to popatrzył tak z mojej perspektywy, to mesh chyba jest drogą do tego prawdziwego serverlessa. Bo teraz mamy ten czas, kiedy jesteśmy napaleni na kontenery. Dosłownie powiem, że...

[00:20:23.260] **Szymon Warda:** Tak.

[00:20:23.500] **Łukasz Kałużny:** Jest, zaczynamy zachłystywać się kolejny raz platformowością w innym wydaniu i tym i podejściem do tego całego systemu wokół. I ten mesh to jest taka kolejna droga bycia platformowości i obietnica tego. Dla mnie to jest którejś, nie wiem, druga, trzecia generacja serverlessu, że to jest droga.

[00:20:47.740] **Szymon Warda:** Tak, zgodziłbym się z taką opcją, że serverless najczęściej wymaga takiej opcji, żeby pisać aplikacje w serverlessie, a część Service Meshy daje aplikacje, daje możliwość wrzucenia istniejącej aplikacji, przy implementacjach to zobaczymy jak to właśnie działa, że to niekoniecznie nawet musi być kontener. Może to być stara aplikacja, która po prostu jest i ją obudować, trochę unowocześnić nie ruszając jej kodu.

[00:21:13.720] **Łukasz Kałużny:** Jeszcze popatrząc się, to jest trochę, sumując to, co powiedzieliśmy o tych wcześniejszych, czyli technikaliach, podejściu do CTO, ale też patrząc na serverlessa, oba robią to samo. Oba te podejścia, czyli serverless i mesh robią to samo, przenoszą odpowiedzialność na platformę...

[00:21:31.260] **Szymon Warda:** Tak, jak najbardziej.

[00:21:32.700] **Łukasz Kałużny:** Za różne funkcjonalności.

[00:21:34.290] **Szymon Warda:** Przy czym Service Mesh często nie powoduje, że musisz wejść w vendor lock-in, takie.

[00:21:41.190] **Łukasz Kałużny:** Przy meshu, tak, to jest teoria.

[00:21:44.580] **Szymon Warda:** Praktyka bywa różna.

[00:21:45.690] **Łukasz Kałużny:** Tak, praktyka bywa różna, ale tak, masz rację, teoria jest taka, że mesh nie powinien wprowadzać aż takiego vendor lock-ingu, co w przeciwieństwie do serverlessa, już teraz widzimy, że ten kod ma być łatwy do przepisania.

[00:21:57.720] **Szymon Warda:** Tak, zgadza się jak najbardziej. Dobrze, zaczęliśmy coraz więcej mówić o rodzajach meshy i różnych implementacjach, bo ten rynek zaczyna być coraz gorętszy. Powoli wyłaniają się prowadzące technologie. Ale przejdźmy jak to w ogóle wygląda?

[00:22:13.320] **Łukasz Kałużny:** To chyba Ty zacznij pierwszy od Istio, którego jesteś fanem.

[00:22:16.470] **Szymon Warda:** Tak, z pewnymi ale, ale tak, faktycznie, Istio jest chyba liderem obecnie na rynku, od tego zacznijmy. Zaczęło się m.in. od IBM-a. Obecnie jest promowane przez Google'a. I to jest bardzo duża siła. Nie oszukujmy się, jak Google coś wypuści, to prawie każdy to sprawdzi, dotknie, więc to trybi. Ta magia, którą Google roztacza, działa. W Google istnieje to generalnie jako serwis. Jest to bardziej w formie bety, ale faktycznie istnieje, można używać.

[00:22:50.820] **Łukasz Kałużny:** Raczej jako serwis, to może tak, jako usługa. To razem z GKE to jest produkcyjne, ale jeżeli popatrzymy na detale, jak jest bardzo z tyłu, to można uznać, że jest to beta na produkcji.

[00:23:08.280] **Szymon Warda:** Jak z wieloma usługami. Tak, podstawa, działa na Kubernetisie. I jak działa? To jest dość ważne. Działa przez to, że wykorzystuje coś, co było swego czasu antypatternem w (...), czyli mianowicie wrzucenie dwóch kontenerów w jednego POD-a.

[00:23:26.850] **Łukasz Kałużny:** Raczej nie do końca...

[00:23:28.230] **Szymon Warda:** Nie było zalecane.

[00:23:29.010] **Łukasz Kałużny:** Raczej czy nie jest zalecane? Tak i nie, bo to jest ten wzorzec sidecaru. W zależności jak popatrzymy, niektórzy mówią, że dodaje to dużo złożoności, niektórzy mówią, że to ułatwia.

[00:23:41.610] **Szymon Warda:** Tak. Cały myk polega na tym, że jest to niezalecane, żeby samodzielnie to robić, bo w tym momencie w Kubernetesie może siedzieć tylko ten jeden image dockerowy. Tu jest, mamy taki myk, mamy aplikację, definiujemy ją, dodatkowo wrzucamy bardzo małe proxy, które jest zarządzane przez całe Istio. Przez to proxy, jest ważne, idzie cała komunikacja wchodząca i wychodząca, dzięki czemu możemy sterować co z kim rozmawia i tak dalej i dzięki temu działa. Jest to trochę nahakowane i to czuć w całym Istio. I Istio potrafi być też zasobożerne.

[00:24:16.380] **Łukasz Kałużny:** Tak, to jest chyba gdzieś tam największa rzecz, że jest zasobożerne, mimo że korzysta właśnie z tego super lekkiego reverse proxy, jakim jest Envoy.

[00:24:24.840] **Szymon Warda:** Tak, ale jak widzimy, to tak mniej więcej konfiguracja Istio, żeby to wszystko trybiło, to jest z reguły kilka tysięcy linii Yamla, jak tego nie rozbijemy. Jest to trochę nahakowany, trochę się czuję, ale jest liderem na chwilę obecną.

[00:24:39.690] **Łukasz Kałużny:** Częściowym. To zaraz do tego może przejdę. I wezmę teraz, nazwijmy to oficjalny mesh, śmiejąc się z tego, LinkerD. Czyli projekt od Cloud Native Foundation, Computing Foundation. Jest to właśnie, tak jak powiedziałem, jest to oficjalny projekt i on ma, jest już druga generacja jego. Czyli został już raz przepisany, co jest to zaletą i teraz się rozwija, dodaje dużo nowych funkcjonalności do środka i ma odmienny sposób działania od Istio. Czyli w przeciwieństwie do Istio mamy tylko jedną instancję per węzeł. Oczywiście węzeł Kubernetesa, bo jest tak samo, tak samo można powiedzieć, że wintegrowany w Kubernetesa i z nim się działa na jego bazie. I to jest jego, i dla mnie jego największą zaletą, chwalą się, że są mniej zasobożerni, szybsi od Istio. To jest pierwsza zaleta.

[00:25:40.590] **Szymon Warda:** I łatwiejsze w konfiguracji, po prostu działa.

[00:25:43.560] **Łukasz Kałużny:** Tak, jest łatwiejszy w konfiguracji. I to, co na początku powiedziałem przy Istio i zarządzającym komitecie, tutaj jest w Cloud Native Foundation, więc jest troszkę bezpieczniejszy z punktu widzenia rozwoju tego projektu i utrzymania.

[00:25:59.940] **Szymon Warda:** Dobra, teraz przejdźmy do zupełnie innego podejścia, od Hashicorpa, Consul Connect.

[00:26:06.060] **Łukasz Kałużny:** Tak, to Consul Connect to jest jedyny produkcyjny mesh w tej chwili, tak patrząc się na cały rynek, który jest w ogóle używalny bez jakiegokolwiek Kubernetesa, ale z nim się integruje. Czyli Consul Connect wykorzystuje, jest zbudowany, jest to rozszerzenie samego Consula. I do agenta, którego mamy w Consulu do health checków całej komunikacji, całego service discovery zostało dodane reverse proxy, którą konfigurujemy po prostu przez cały service discovery i reguły. Więc pozwala nam to włączyć się do istniejących już systemów. To jest jego duża zaleta. A dużo firm wykorzystuje Consula do service discovery.

[00:26:45.570] **Szymon Warda:** Tak i z rzeczy fajnych, to jest to, że umożliwia właśnie, nie wymaga kontenerów.

[00:26:50.340] **Łukasz Kałużny:** Tak, zupełnie nie wymaga konteneryzacji i można go wrzucić w istniejącą infrastrukturę. Czyli można mieć system, który będzie komunikował się na zewnątrz tak jak zawsze się komunikował, ale wpiąć go do mesha, żeby nowe integracje szły przez takiego mesha do niego. Więc to jest duża zaleta. I druga, bardzo ważna, jest wersja z supportem. Można kupić do tego support producenta.

[00:27:15.730] **Szymon Warda:** Podkreślmy, producenta, bo do Kubernetesa i Linkerd też można kupić nie będzie oficjalny często.

[00:27:22.180] **Łukasz Kałużny:** Tak, można dokupić tak naprawdę, bierzemy go albo w wersji cloudowej, albo w wersji jakiegoś, w Istio powoli się przechodzi na strzechy, bo mamy jeszcze OpenShifta, gdzie zaczyna być jego komponentem. Ale to jest już cała kobyła, którą musimy, platforma, którą musimy wdrożyć.

[00:27:38.470] **Szymon Warda:** Dodajmy też, że Consul Connect jest bardzo lekki jako cały service mesh. Te binarki są bardzo małe.

[00:27:44.800] **Łukasz Kałużny:** Tak, idea jest tego, przychodzi wszystko w jednej binarce, którą instalujemy jako serwis, wrzucamy konfigurację, reszta leci w locie. To co Szymonie, może teraz o zupełnie innej koncepcji, która gdzieś się po drodze tworzy i jest niszowa.

[00:27:58.510] **Szymon Warda:** Jest niszowa. Więc mały mały rys historyczny. Service Fabric. Czemu rys historyczny? Ponieważ Service Fabric był w General Availability w 2016 roku, czyli availability, dla klientów, tak to powiedzmy.

[00:28:13.860] **Łukasz Kałużny:** Tak. A sam Fabric produkcyjnie to w zależności jak na to popatrzeć. Jest na Azure, Fabric jest produkcyjny od 2010 roku razem, bo jest to corowa część do pewnych usług, takich jak SQL-e. Chodzą na Service Fabricu, SQL Database i inne chodzą na Fabricu i nawet wcześniej. Sam projekt Fabrica wywodzi się z projektu iHome i w 2001 roku Microsoft budował rozwiązanie backendowe dla Smart City, które będzie rozproszone. Wyobraźcie sobie, kiedy Google miało serwery w kanciapie na miotły, oni projektowali rozproszoną platformę pod Smart City. Więc te koncepty są bardzo stare i w kilku projektach Microsoftu onpremowych Fabric też siedzi, ale siedzi bardzo schowany i administratorzy tego nie widzą nawet.

[00:29:06.600] **Szymon Warda:** Tak, to jest kolejna technologia, którą Microsoft wyprzedził swój czas i trochę się nie udało ją wdrożyć. Rynek nie załapał tego. Ale teraz czemu o niej mówimy mimo, że tak nie za bardzo to się udało? Dlatego, że tam była chyba najfajniejsza abstrakcja nad komunikację synchroniczną jaką ja widziałem, w tym momencie dodawanie do kolejki. Aplikacje w Service Fabricu oryginalnie to były aplikacje w Service Fabricu, czyli w odpowiednich klasach dziedziczyły, miały odpowiednie interfejsy, implementowały. I teraz co się działo? Jeżeli na przykład w jednej aplikacji dodawaliśmy do kolejki, to ten obiekt, informacja pojawiała się automagicznie w innych instancjach tego serwisu, w tych konkretnych kolejkach. I to jest ta warstwa abstrakcji, którą bym chciał zobaczyć. Bardzo swoją drogą blisko do tego, jak jest realizowane Azure Functions, bo tam też dodajemy, mamy ICollectory, gdzie dodajemy elementy do kolejki i się automatycznie pojawiają. Tylko tam jest trochę bardziej leaky, tu, w Service Fabricu, trochę to lepiej działało.

[00:30:01.540] **Łukasz Kałużny:** Tak, całe to podejście. No i ważne powiedzieć, że Fabric też pozwala na hostowanie rzeczy, które nie są z nim zintegrowane.

[00:30:09.030] **Szymon Warda:** Tak, to jest w wersji mesha.

[00:30:11.520] **Łukasz Kałużny:** I jeszcze w zwykłym. W zwykłym też można hostować execi. No i właśnie wspomniałeś o meshu. Czyli to jest rzecz, która też może nie wyprzedziła, ale trochę w Microsofcie nie wiadomo publicznie, co się z tym dzieje, czyli...

[00:30:26.400] **Szymon Warda:** podajmy może pełną nazwę, bo to jest Service Fabric Mesh.

[00:30:28.620] **Łukasz Kałużny:** Tak, Service Fabric Mesh, czyli w założeniu Service Fabric Mesh miał być warstwą abstrakcji pracującą na bazie konteneryzacji, która wstrzykuje te wszystkie elementy na poziomie właśnie, wszystkie elementy całe na zewnątrz i wystawia tylko API do komunikacji, do tych poszczególnych elementów. I od strony cloudu, od strony Azure'a, miało to działać w ten sposób, że my tego Fabrica w ogóle nie widzimy, tylko wstrzykujemy opisy konfiguracji. Czyli nie mamy orkiestratora, którego nie chcemy, orkiestratora, którego nie chcemy posiadać.

[00:31:02.760] **Szymon Warda:** I utrzymywać.

[00:31:03.600] **Łukasz Kałużny:** Tak. A w przypadku przejścia do onprema to te same elementy, te same opisy konfiguracyjne, Yamle, JSON-y, paczki aplikacyjne dokładnie takie same możemy zdeployować w onpremie na samym właśnie Service Fabricu. I implementacja gdzieś z założenia miała być też otwarta, czyli tak naprawdę sam sposób wrzucania innych rzeczy to miała być otwarta specyfikacja, którą można potem wziąć i zaimplementować gdziekolwiek. Wiem, że Microsoft gdzieś tą wizję u siebie na razie, co można zobaczyć na prezentacjach architektonicznych na przykład od Marka Russinovicha, jak jest zbudowany Azure, to pod spodem jest ten serwis Fabric Mesh, to co, ten koncept już jest wykorzystywany. Przez to mamy kontenery serverlessowe, AC i linuksowe właśnie chodzi na meshu, teraz nazywa się to Atlas. I Azure Functions, te linuksowe, gdzie płacimy za wywołania, jest hostowane w kontenerach właśnie na Atlasie. Jest to serverless kontenerowy hostowany na Atlasie z wywoływaniem requestami i płaceniem za requesty. Więc jest to ciekawe. Idąc dalej trochę do projektów microsoftowych, ale tutaj open sourceowych, to Microsoft zainicjował inicjatywę SMI, Service Mesh Interface. Czyli wspólny język dla konfiguracji meshy, który właśnie pozwoli nam uspójnić i żeby te meshe stały się agnostyczne. Co z tego wyjdzie? Zobaczymy. Wygląda na to, że te, które omówiliśmy, projekty takie właśnie jak Istio czy Linkerd zaczynają implementować SMI i współpracować z tym, więc jest to ciekawa rzecz. Jak sobie popatrzymy, to oczywiście jest tego znacznie więcej. No i praktycznie wszystkie nowe projekty dotyczą Kubernetesa, a my wymieniliśmy chyba te główne + te ciekawe koncepcje, które gdzieś tworzyły się obok.

[00:33:02.770] **Szymon Warda:** Dobra, ale żeby nie być posądzonym o to, że jedziemy dość mocno na hype trainie, to spójrzmy czemu nie. Bo są też powody, czemu nie warto wchodzić w Service Mesha i się nie powinno wchodzić w Service Meshe.

[00:33:13.270] **Łukasz Kałużny:** Ja pierw zacznę od przesady i hype trainu. Jeżeli zbyt dużo zdelegujemy i zaczniemy robić fancy konfiguracje, to wyjdzie nam SOA 2004.

[00:33:23.740] **Szymon Warda:** Tak, nie oszukujmy się, cały IT kręci się w kółko i popełniamy czasem te same błędy co ileś tam lat.

[00:33:29.560] **Łukasz Kałużny:** Tak, bo mikrousługi to jest po prostu jeden ze sposobów implementacji SOA.

[00:33:34.210] **Szymon Warda:** Usługi.

[00:33:34.870] **Łukasz Kałużny:** Tak, ja wiem, że się tak, usługi, ja też nie lubię, ale mikroserwisy bardziej przemawiają do ludzi aktualnie. I Service Mesh będzie takim ESB Cloud Native, czyli stanie się takią ciężką zależnością. Być może bez tylu zespołów, które były za ESB i ich zależnościami, ale stanie się taką ciężką zależnością, którą potem ludzie zaczęli pomijać i stąd mamy te mikroserwisy.

[00:33:58.310] **Szymon Warda:** Tak, jest to ryzyko, jeżeli zrobi się to źle, albo się nie będzie pilnowało, bo każdą technologię umiemy coś nadużyć. Dobra. Dla mnie, co dla mnie jest takim problemem, jest to, że nie mamy standardu i nie ma jeszcze wyłonionego takiego jasnego lidera, że wszyscy za tym pójdą. I może okazać się to samo, co było z orkiestratorami, że na przykład wybierzemy coś, co będzie odpowiednikiem takiego Docker Swarma albo Mesosa i potem utrzymywanie technologii, z której już nikt nie korzysta i nikt nie chce korzystać jest kosztowne i potem usunięcie nie jest takie wcale proste. Istio pewnie będzie, ale może wyłoni się SMI właśnie jako ten standard. Zobaczymy. Kolejny dla mnie element to jest to, co już mówiliśmy wcześniej, ale podkreślmy, nie ma sensu robienie Service Mesha dla jednej małej aplikacji.

[00:34:50.450] **Łukasz Kałużny:** Tak, to jest, jeżeli w szczególności to jest, chcemy sami wszystko zbudować from scratch, od zera zbudować, nie ma sensu, bo to jest budowa platformy. No i ja się spotykam tak już życiowo często z pytaniem o meshe, właśnie z powodu tego, że potrzebuję testy AB, trochę bardziej zaawansowany routing aplikacyjny czy mikrosegmentację w Kubernetesie, gdzie zwykle jest to dla jednej, dwóch usług. I jest to robione, bo przeczytaliśmy, zobaczyliśmy na prezentacjach, jest fajne, a da się to zrobić w zupełnie inny sposób, prostszy.

[00:35:25.680] **Szymon Warda:** Tak, ale na przykład ja to samo widuję jak na przyklad rozmawiam z zespołami, że chcą mieć Kubernetesa dlatego, żeby mieć autoscaling. A potem pokazujemy na przykład App Services, gdzie jest autoscaling out of the box i działa nieźle.

[00:35:36.960] **Łukasz Kałużny:** Czyli jeżeli ktoś potrzebuje większej kontroli immutable IaaS, który tak samo działa.

[00:35:40.500] **Szymon Warda:** Tak, dokładnie. No i na końcu chyba co się zgadzamy chyba we dwóch, kompetencje zespołu. To jest kolejny duży klocek infrastrukturalny i zespół musi umieć go obsługiwać.

[00:35:50.040] **Łukasz Kałużny:** Tak, kompetencje są tutaj kluczowe i czy ktoś będzie chciał się, nazwijmy to, zpivotować albo rozszerzyć na to.

[00:35:57.200] **Szymon Warda:** Dobra, wrapujemy ten odcinek?

[00:35:58.910] **Łukasz Kałużny:** Tak.

[00:36:01.250] **Szymon Warda:** Coś teraz mówiliśmy o Kubernetesie. Dla mnie, coraz mocniej widzę, że Kubernetes jest krokiem pośrednim i że na chwilę obecną gdybym miał rozważać, czy Kubernetes czy Service Mesh, mimo wszystko zacząłbym badać Service Mesha, większa wartość.

[00:36:17.510] **Łukasz Kałużny:** Tak. Dla mnie również Mesh jest właśnie tym krokiem pośrednim do prawdziwego serverlessa. Zastanawiając się, Mesh tak, ale wtedy, kiedy przestaniemy myśleć z nim tak, jak o Kubernetesie i OPS heavy. Jeżeli nie chcemy wykorzystać w jakimś skończonym czasie tych funkcjonalności, których daje, to lepiej skorzystać z czystego Kubernetesa.

[00:36:43.580] **Szymon Warda:** Do rozwagi, tak.

[00:36:44.720] **Łukasz Kałużny:** Rozwagi, wymaga mniejszego narzucenia kompetencji.

[00:36:47.750] **Szymon Warda:** Zdecydowanie tak. Dobra, kończymy. Dzięki. Na razie.

[00:36:52.820] **Łukasz Kałużny:** Na razie.

