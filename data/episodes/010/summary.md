## 1. Wstęp i przedstawienie odcinka
Summary: Prowadzący witają słuchaczy i zapowiadają temat odcinka — Service Mesh z perspektywy CTO i architektów. Podają też adres z linkami do materiałów omawianych w audycji.
Speaker summaries:
- Szymon Warda: Otwiera odcinek i zapowiada główny temat oraz sekcję linków.
- Łukasz Kałużny: Przedstawia się i podaje adres strony z linkami do odcinka.
Most interesting quotes:
1. Łukasz Kałużny: "Wszystkie linki do tego odcinka znajdziecie na Patoarchitekci.io/10."
2. Szymon Warda: "Temat na dziś to Service Mesh, ale z punktu widzenia CTO i architektów."

## 2. Knative, Google i polityka projektów open source
Summary: Google odmówił przekazania projektu Knative do Cloud Native Computing Foundation, co nikogo nie dziwi — cztery z siedmiu osób w komitecie sterującym to pracownicy Google'a. Spotkania komitetu odbywają się za zamkniętymi drzwiami, publikowane są tylko decyzje. Prowadzi to do refleksji, że otwartość kodu nie oznacza otwartego wpływu na rozwój projektu.
Speaker summaries:
- Łukasz Kałużny: Referuje decyzję Google'a i strukturę zarządzania Knative, wskazując na brak transparentności prac komitetu.
- Szymon Warda: Przypomina, że ten kto finansuje open source, ma wobec niego oczekiwania i trzeba być tego świadomym.
Most interesting quotes:
1. Łukasz Kałużny: "Dobrze, że źródła są dostępne, ale wpływ na rozwój projektu jest często bardzo mocno podyktowany warunkami sponsorów."
2. Szymon Warda: "Nie oszukujmy się — ktoś za ten open source, za czas tych ludzi płaci. A tam, gdzie są pieniądze, są też oczekiwania."
3. Łukasz Kałużny: "Komitet sterujący Knative składa się z siedmiu osób, z czego cztery to pracownicy Google'a."

## 3. Nieudana migracja w brytyjskim banku — anatomia death marchu
Summary: Szymon poleca link opisujący nieudaną fuzję i migrację systemów dwóch banków w Wielkiej Brytanii, która skończyła się interwencją nadzoru finansowego i stratami rzędu ponad 100 mln przy 200 mln przychodu. Rozmówcy zwracają uwagę, że takie projekty często widać z góry jako death march, a klasycznym błędem jest ustalanie terminu migracji z góry i oczekiwanie, że technicy się wyrobią.
Speaker summaries:
- Szymon Warda: Przedstawia case study spektakularnej porażki migracyjnej i punktuje błąd narzucania terminów upfront.
- Łukasz Kałużny: Dzieli się obserwacjami z rynku konsultacyjnego o tym, jak przebiegają i jak są widoczne migracje w bankach.
Most interesting quotes:
1. Szymon Warda: "Czasami widzimy, że projekt idzie źle, a mimo to wmawiamy sobie, że i tak się uda, że będzie sukces. Nie zawsze. Czasami przychodzi spektakularna porażka."
2. Szymon Warda: "Czas migracji ustalono z góry, a potem ludzie techniczni mieli się do tego wyrobić. To tak nie działa."
3. Łukasz Kałużny: "Komunikaty o braku płatności czy brak możliwości zapłaty kartą — to jest dla osób nietechnicznych najbardziej widoczne."

## 4. Czym jest Service Mesh — definicja i relacja z Kubernetesem
Summary: Service Mesh definiowany jest jako nowa platforma dla serwisów, która przenosi circuit breakery, retry, timeouty i fallbacki z kodu aplikacji do warstwy infrastruktury. Ponieważ mesh musi na czymś działać i korzystać ze skalowania, większość implementacji opiera się na Kubernetesie. Szymon opisuje mesh metaforą galaretki, w którą wrzucamy serwisy i która zapewnia im wszystko, czego potrzebują do życia.
Speaker summaries:
- Szymon Warda: Tłumaczy istotę Service Mesha jako platformy przenoszącej problemy komunikacji synchronicznej do infrastruktury.
- Łukasz Kałużny: Dopytuje o precyzyjną definicję i zwraca uwagę, że każde wyszukanie Service Mesha prowadzi do Kubernetesa.
Most interesting quotes:
1. Szymon Warda: "To wyniesienie wszystkich circuit breakerów, retry, timeoutów czy fallbacków do poziomu infrastruktury, czyli wyrzucenie ich z kodu aplikacyjnego."
2. Szymon Warda: "Zawsze widzę to jako galaretkę, w którą wrzucamy nasze serwisy."
3. Łukasz Kałużny: "Gdy wpiszę w Google czy w Bingu Service Mesh, od razu pojawia się Kubernetes."

## 5. Mesh od Microsoftu — koncept wyprzedzający swój czas
Summary: Krótka wzmianka o podejściu Microsoftu, który realizował ideę mesha o poziom abstrakcji wyżej, bezpośrednio na chmurze. Prowadzący zapowiadają, że szczegóły omówią przy okazji Service Fabrica.
Speaker summaries:
- Łukasz Kałużny: Przypomina o koncepcji Microsoftu działającej na czystym cloudzie, ponad poziomem kontenerów.
- Szymon Warda: Ocenia, że Microsoft jak zwykle miał świetny pomysł, tylko zbyt wcześnie.
Most interesting quotes:
1. Szymon Warda: "Microsoft, jak to zwykle z nim bywa, miał świetny pomysł, tylko zbyt wcześnie i o poziom abstrakcji wyżej."

## 6. Jak architekt ma sprzedać Service Mesh CTO — problemy i cele
Summary: Rozmowa o dwóch sposobach argumentacji wobec C-levelu: przez problem (upraszczanie integracji synchronicznych, oswajanie starych systemów, których nikt nie chce dotykać) i przez cel (obniżenie kosztów implementacji nowych systemów przez wyeliminowanie kodu infrastrukturalnego). Podkreślono, że mesh dotyczy dziś komunikacji synchronicznej i usług backendowych, a mesh dla kolejek to wciąż pieśń przyszłości.
Speaker summaries:
- Szymon Warda: Rozkłada narrację dla CTO na dwie ścieżki — rozwiązywanie problemów i realizację celów kosztowych.
- Łukasz Kałużny: Doprecyzowuje zakres (komunikacja synchroniczna, backend) i pilnuje poprawnej terminologii, np. uwierzytelniania.
Most interesting quotes:
1. Szymon Warda: "Wrzucamy serwisy w galaretkę, która ogarnia kilka rzeczy, i dzięki temu system działa lepiej. Nie rozwiązuje wszystkich problemów, ale zmniejsza ich liczbę."
2. Szymon Warda: "Gdy zbierzemy wyceny systemów, okazuje się, że kod infrastrukturalny to znaczący koszt niemal każdego systemu, który nie zawsze się zwraca."
3. Łukasz Kałużny: "Przepraszam — uwierzytelnianie."

## 7. Koszt kompetencji zespołu OPS i usługi zarządzane
Summary: Łukasz podnosi ryzyko: platformę trzeba utrzymywać, a to wymaga spivotowania zespołu operations na zupełnie nowe kompetencje. Szymon przyznaje, że skillset do nabycia jest bardzo duży, ale wskazuje, że w chmurach mesh bywa usługą zarządzaną, a ten sam kod można uruchomić on-premise — analogicznie do managed Kubernetesa.
Speaker summaries:
- Łukasz Kałużny: Wskazuje kompetencje zespołu OPS jako główny koszt i ryzyko wdrożenia platformy poza modelem managed.
- Szymon Warda: Potwierdza skalę wymaganych umiejętności i porównuje sytuację do wyboru między managed a self-hosted Kubernetesem.
Most interesting quotes:
1. Łukasz Kałużny: "Zwykle gdy mówimy o platformie, zespół operations trzeba spivotować na nowe kompetencje."
2. Szymon Warda: "Umiejętności, które nagle musi nabyć zespół OPS, są bardzo rozległe."

## 8. Cloud-like features on-premise bez vendor lockingu
Summary: Mesh daje w środowisku on-premise funkcjonalności znane z chmury: deployment zastępujący tysiące linii PowerShella, tracing i monitoring out of the box oraz skalowanie. Powyżej Kubernetesa dochodzą zaawansowane strategie wdrożeń — canary, testy A/B, blue-green — a także automatyzacja dostępu, routingu i budowa application map.
Speaker summaries:
- Szymon Warda: Wylicza gotowe funkcje platformy, porównując doświadczenie do serverlessu, gdzie „po prostu działa".
- Łukasz Kałużny: Uzupełnia listę o zaawansowane metody deploymentu oraz warstwę security i routingu aplikacyjnego.
Most interesting quotes:
1. Szymon Warda: "Deployment, czyli coś, co bywa dziesiątkami, a czasem tysiącami linii kodu w PowerShellu, dostajemy out of the box."
2. Łukasz Kałużny: "Przy deploymencie powyżej Kubernetesa dostajemy z pudełka zaawansowane metody: canary, testy A/B, blue-green deployment."

## 9. Perspektywa architekta — boilerplate, przeniesienie odpowiedzialności i skala platformy
Summary: Dla architekta kluczową korzyścią jest zniknięcie boilerplate'u: uwierzytelniania, logowania, metryk implementowanych od nowa w każdym języku i platformie. Prowadzący podkreślają, że złożoności nie da się usunąć, tylko przenieść — z kodu do konfiguracji i infrastruktury — a to opłaca się tylko przy skali platformy, nie dla jednego systemiku. Dla mniejszych przypadków rekomendują usługę zarządzaną zamiast wdrożenia on-premise.
Speaker summaries:
- Szymon Warda: Argumentuje z pozycji wyceniającego system architekta i przypomina, że mesh to inwestycja platformowa robiona raz dla wielu systemów.
- Łukasz Kałużny: Precyzuje, że przenosimy zależności do konfiguracji, a wyłączony kod należy usuwać, oraz radzi model managed dla mniejszych wdrożeń.
Most interesting quotes:
1. Szymon Warda: "Wiemy, że w żadnym systemie IT nie da się usunąć złożoności — można ją tylko przenieść w inne miejsce."
2. Szymon Warda: "Nie ma sensu robić tego dla jednego systemiku, chyba że jako proof of concept. Docelowo to jest platforma."
3. Łukasz Kałużny: "Wyłączony kod powinien zostać usunięty — to również jest założenie."

## 10. Wielojęzyczność — utopia mikroserwisów czy realna korzyść?
Summary: Service Mesh ma umożliwiać sensowne kosztowo utrzymywanie systemów w wielu technologiach, ale Łukasz przypomina, że taka obietnica padła już przy mikroserwisach i się nie sprawdziła. Szymon precyzuje, że nie chodzi o jeden system w wielu językach, lecz o krajobraz systemów w firmie — księgowość, HR, raportowanie — które i tak są w różnych technologiach i z których można wyciągnąć wspólne elementy integracyjne.
Speaker summaries:
- Szymon Warda: Broni polyglot persistence na poziomie całej organizacji, a nie pojedynczego systemu, wskazując na integracje między systemami.
- Łukasz Kałużny: Sceptycznie konfrontuje obietnicę wielojęzyczności z nieudanym doświadczeniem ery mikroserwisów.
Most interesting quotes:
1. Łukasz Kałużny: "Mówimy o kolejnej pięknej, utopijnej wizji, która pojawiła się już przy mikroserwisach — bez żadnych Kubernetesów i bez żadnych meshy."
2. Szymon Warda: "Nawet Google ma określony zbiór języków."
3. Szymon Warda: "Widzimy to jako integracje, ale te elementy integracji można przenieść właśnie do Service Mesha."

## 11. Konkretne funkcjonalności: circuit breakery, timeouty i podział odpowiedzialności
Summary: Deweloperzy przestają zajmować się circuit breakerami i timeoutami, o których zwykle nie mają pojęcia ani ich to nie interesuje — odpowiedzialność trafia do OPS-ów z dashboardami i statystykami. Łukasz przywołuje anegdotę o żądaniach ustawiania timeoutów na 60–120 minut na firewallach, a Szymon punktuje absurd redeployu aplikacji tylko po to, by zmienić zakodowany timeout.
Speaker summaries:
- Szymon Warda: Argumentuje, że parametry odporności powinny być w warstwie platformy, bo tam siedzą kompetencje i narzędzia OPS-ów.
- Łukasz Kałużny: Wtrąca anegdotę o absurdalnych żądaniach wydłużania timeoutów na firewallach.
Most interesting quotes:
1. Szymon Warda: "Deweloperzy nie martwią się ustawieniami circuit breakerów czy timeoutów — rzeczy, o których z reguły i tak nie mają większego pojęcia."
2. Szymon Warda: "A jeśli taki timeout jest zakodowany w aplikacji, to co wtedy? Redeploy aplikacji?"
3. Łukasz Kałużny: "Kiedyś dostawaliśmy prośby, żeby przestawiać timeouty na firewallach na 60 albo 120 minut."

## 12. Monitoring, tracing i observability z pudełka
Summary: Mesh dostarcza monitoring, tracing i observability out of the box, podczas gdy zespoły zwykle robią to za późno, źle albo wcale, bo to kosztowne elementy infrastruktury. Prowadzący podkreślają wartość centralizacji — posiadanie trzech systemów tracingu czy wielu systemów logów nie ma sensu — a integracja sprowadza się do przekazywania nagłówków HTTP.
Speaker summaries:
- Szymon Warda: Wskazuje, że scentralizowana obserwowalność z platformy zastępuje kosztowne i zaniedbywane implementacje w aplikacjach.
- Łukasz Kałużny: Podsumowuje, że dzięki monitoringowi komunikacji dostajemy całościowy obraz sieci powiązań między usługami.
Most interesting quotes:
1. Szymon Warda: "Z reguły deweloperzy albo spalają na tym bardzo dużo czasu, albo robią to za późno, albo źle, albo w ogóle."
2. Szymon Warda: "Nie musimy wpinać tego w każdy system — wystarczy, że jest to w miarę wspierane i że przekazujemy nagłówki HTTP."

## 13. Security: AAA, mTLS, mikrosegmentacja i fault injection
Summary: Mesh przejmuje odpowiedzialność za uwierzytelnianie, autoryzację i rozliczalność w komunikacji service-to-service, co eliminuje antywzorzec sprawdzania uprawnień wyłącznie na API Gateway. Dochodzi do tego mikrosegmentacja sieci przez konfigurację, wsparcie dla gRPC, zarządzanie certyfikatami i mTLS oraz fault injection pozwalający na własną chaos monkey. Prowadzący zaznaczają, że wdrażanie całego Kubernetesa i Istio tylko dla mutual TLS to słabe uzasadnienie.
Speaker summaries:
- Łukasz Kałużny: Rozwija skrót AAA i szczegółowo omawia warstwę bezpieczeństwa mesha, w tym mikrosegmentację i fault injection.
- Szymon Warda: Krytykuje poleganie wyłącznie na API Gateway i podkreśla, że poprawna obsługa certyfikatów przerasta kompetencje deweloperów.
Most interesting quotes:
1. Szymon Warda: "Nie może być tak, że gdy atakujący przejdzie przez API Gateway, ma już dostęp do wszystkiego."
2. Łukasz Kałużny: "Mikrosegmentacja sieci, czyli rzecz, której deweloperzy nienawidzą, a security i OPS-i bardzo jej wymagają."
3. Szymon Warda: "Umiejętność obsługi certyfikatów tak, żeby nie wyciekły i żeby było to zrobione z głową, nie jest prosta."

## 14. Service Mesh a serverless — droga do prawdziwego serverlessu
Summary: Obaj prowadzący zgadzają się, że mesh i serverless robią to samo — przenoszą odpowiedzialność na platformę — tylko za inne funkcjonalności. Łukasz widzi mesh jako drugą lub trzecią generację serverlessu, przewagą mesha jest możliwość wrzucenia istniejącej, nawet niekonteneryzowanej aplikacji bez zmiany jej kodu. Teoretycznie mesh nie wprowadza vendor lock-inu w takim stopniu jak serverless, choć praktyka bywa różna.
Speaker summaries:
- Łukasz Kałużny: Twierdzi, że mesh to kolejna generacja serverlessu i krok pośredni na drodze do niego, choć zastrzega, że brak lock-inu to teoria.
- Szymon Warda: Podkreśla, że serverless wymaga pisania aplikacji pod siebie, a mesh potrafi obudować i unowocześnić stary system bez ruszania kodu.
Most interesting quotes:
1. Łukasz Kałużny: "Dla mnie to druga albo trzecia generacja serverlessu — to jest droga w tym kierunku."
2. Szymon Warda: "Może to być stara aplikacja, która po prostu istnieje, a którą można obudować i trochę unowocześnić, nie ruszając jej kodu."
3. Łukasz Kałużny: "Teoria jest taka, że mesh nie powinien wprowadzać aż takiego vendor lock-inu."

## 15. Istio — lider rynku, sidecar i zasobożerność
Summary: Istio, zapoczątkowane przez IBM i promowane przez Google'a, jest obecnie liderem rynku i dostępne jako usługa przy GKE, choć w praktyce w stanie zbliżonym do bety. Działa przez wzorzec sidecar — wstrzyknięcie drugiego kontenera (proxy Envoy) do poda, przez który przechodzi cały ruch wchodzący i wychodzący. Wadą jest zasobożerność i konfiguracja liczona w tysiącach linii YAML-a, przez co całość sprawia wrażenie „nahakowanej".
Speaker summaries:
- Szymon Warda: Przedstawia Istio jako lidera, ale otwarcie krytykuje jego zasobożerność i nahakowany charakter konfiguracji.
- Łukasz Kałużny: Doprecyzowuje status usługi w GKE i zwraca uwagę na paradoks zasobożerności mimo lekkiego proxy Envoy.
Most interesting quotes:
1. Szymon Warda: "Nie oszukujmy się — gdy Google coś wypuści, prawie każdy to sprawdzi i tego dotknie. Ta magia, którą Google roztacza, działa."
2. Szymon Warda: "Konfiguracja Istio, żeby wszystko działało, to z reguły kilka tysięcy linii YAML-a."
3. Łukasz Kałużny: "Jeżeli spojrzymy na detale i na to, jak bardzo jest z tyłu, można uznać, że to beta na produkcji."

## 16. Linkerd — oficjalny mesh CNCF
Summary: Linkerd to projekt Cloud Native Computing Foundation, będący już w drugiej, przepisanej generacji. W przeciwieństwie do Istio używa jednej instancji na węzeł Kubernetesa, dzięki czemu chwali się mniejszą zasobożernością i większą szybkością. Dodatkowym atutem jest łatwiejsza konfiguracja oraz bezpieczniejsze z punktu widzenia rozwoju umocowanie w fundacji.
Speaker summaries:
- Łukasz Kałużny: Prezentuje Linkerd jako lżejszą, wydajniejszą i bezpieczniej zarządzaną alternatywę wobec Istio.
- Szymon Warda: Dorzuca, że Linkerd jest po prostu łatwiejszy w konfiguracji i działa bez zbędnych ceregieli.
Most interesting quotes:
1. Łukasz Kałużny: "W przeciwieństwie do Istio mamy tylko jedną instancję na węzeł."
2. Szymon Warda: "Jest też łatwiejszy w konfiguracji — po prostu działa."
3. Łukasz Kałużny: "Znajduje się w Cloud Native Computing Foundation, więc z punktu widzenia rozwoju projektu jest nieco bezpieczniejszy."

## 17. Consul Connect od HashiCorp — mesh bez Kubernetesa
Summary: Consul Connect to jedyny produkcyjny mesh używalny całkowicie bez Kubernetesa, będący rozszerzeniem Consula o reverse proxy przy agencie odpowiedzialnym za health checki i service discovery. Pozwala wpiąć istniejące, niekonteneryzowane systemy do mesha, tak by nowe integracje szły przez niego. Dodatkowe atuty to bardzo lekkie binarki oraz dostępność komercyjnego wsparcia producenta.
Speaker summaries:
- Łukasz Kałużny: Szczegółowo opisuje architekturę Consul Connect i podkreśla brak wymogu konteneryzacji oraz dostępność supportu producenta.
- Szymon Warda: Akcentuje lekkość rozwiązania i to, że nie wymaga kontenerów, oraz dopytuje o kwestię oficjalnego wsparcia.
Most interesting quotes:
1. Łukasz Kałużny: "Consul Connect to obecnie jedyny produkcyjny mesh, który jest w ogóle używalny bez jakiegokolwiek Kubernetesa."
2. Łukasz Kałużny: "Można mieć system, który komunikuje się na zewnątrz tak jak dotychczas, ale wpiąć go do mesha, żeby nowe integracje szły właśnie przez niego."
3. Szymon Warda: "Consul Connect jest bardzo lekki jak na cały service mesh. Te binarki są bardzo małe."

## 18. Service Fabric — historia, korzenie i abstrakcja nad komunikacją
Summary: Service Fabric trafił do GA w 2016 roku, ale produkcyjnie w Azure działa od około 2010 jako fundament usług takich jak SQL Database, a jego korzenie sięgają projektu iHome z 2001 roku, gdy Microsoft budował rozproszony backend dla Smart City. Rynek nie załapał technologii, ale Szymon uważa, że zawierała najlepszą abstrakcję nad komunikacją, jaką widział — dodanie obiektu do kolejki automagicznie replikowało go do innych instancji serwisu, podobnie jak ICollector w Azure Functions, tylko mniej leaky.
Speaker summaries:
- Łukasz Kałużny: Przedstawia genezę i historię Service Fabrica, od projektu Smart City z 2001 roku po ukryty fundament usług Azure.
- Szymon Warda: Ocenia Service Fabric jako technologię wyprzedzającą swój czas z najlepszą abstrakcją nad komunikacją, jaką widział.
Most interesting quotes:
1. Łukasz Kałużny: "Wyobraźcie sobie: kiedy Google miał serwery w kanciapie na miotły, oni projektowali rozproszoną platformę pod Smart City."
2. Szymon Warda: "Jeżeli w jednej aplikacji dodawaliśmy obiekt do kolejki, ta informacja pojawiała się automagicznie w innych instancjach tego serwisu."
3. Szymon Warda: "To kolejna technologia, którą Microsoft wyprzedził swój czas i której nie udało się wdrożyć."

## 19. Service Fabric Mesh i Atlas — serverless kontenerowy w Azure
Summary: Service Fabric Mesh miał być warstwą abstrakcji nad konteneryzacją, w której użytkownik nie widzi orkiestratora, tylko wstrzykuje opisy konfiguracji, a te same paczki i YAML-e można zdeployować on-premise. Choć publicznie los projektu jest niejasny, koncept żyje w Azure pod nazwą Atlas — na nim działają kontenery serverless (ACI) oraz linuksowe Azure Functions rozliczane per wywołanie.
Speaker summaries:
- Łukasz Kałużny: Wyjaśnia założenia Service Fabric Mesh oraz wskazuje, gdzie ten koncept realnie żyje dziś w Azure jako Atlas.
- Szymon Warda: Doprecyzowuje pełną nazwę produktu i dopowiada, że chodzi o unikanie utrzymywania orkiestratora.
Most interesting quotes:
1. Łukasz Kałużny: "Nie mamy orkiestratora, którego nie chcemy posiadać."
2. Łukasz Kałużny: "To serverless kontenerowy hostowany na Atlasie, wywoływany requestami i rozliczany za requesty."

## 20. SMI — Service Mesh Interface jako próba standaryzacji
Summary: Microsoft zainicjował SMI, czyli wspólny język konfiguracji meshy, mający uczynić je agnostycznymi. Istio i Linkerd zaczynają implementować ten standard, co czyni inicjatywę obiecującą, choć jej losy pozostają otwarte. Prowadzący zauważają, że praktycznie wszystkie nowe projekty w tej przestrzeni dotyczą Kubernetesa.
Speaker summaries:
- Łukasz Kałużny: Przedstawia SMI jako próbę uspójnienia konfiguracji meshy i odnotowuje pierwsze adopcje przez Istio i Linkerd.
Most interesting quotes:
1. Łukasz Kałużny: "To wspólny język konfiguracji meshy, który pozwoli je uspójnić i sprawić, że staną się agnostyczne."
2. Łukasz Kałużny: "Praktycznie wszystkie nowe projekty dotyczą Kubernetesa."

## 21. Czemu NIE wchodzić w Service Mesh — ESB Cloud Native i brak standardu
Summary: Nadmierne delegowanie i fancy konfiguracje mogą doprowadzić do odtworzenia SOA z 2004 roku, a mesh może stać się ESB Cloud Native — ciężką zależnością, którą ludzie znów zaczną omijać. Szymon dodaje ryzyko braku standardu i wyłonionego lidera: można wybrać odpowiednik Docker Swarma czy Mesosa, a utrzymanie i usunięcie martwej technologii jest kosztowne.
Speaker summaries:
- Łukasz Kałużny: Ostrzega przed powtórzeniem historii ESB i SOA, przypominając że mikroserwisy to tylko jeden ze sposobów implementacji SOA.
- Szymon Warda: Wskazuje brak standardu i niepewność co do zwycięskiej technologii jako główne ryzyko inwestycyjne.
Most interesting quotes:
1. Łukasz Kałużny: "Jeżeli zbyt dużo zdelegujemy i zaczniemy tworzyć fancy konfiguracje, wyjdzie nam SOA z 2004 roku."
2. Łukasz Kałużny: "Service Mesh stanie się takim ESB Cloud Native, czyli ciężką zależnością."
3. Szymon Warda: "Może się okazać to samo, co z orkiestratorami — że wybierzemy coś, co będzie odpowiednikiem Docker Swarma albo Mesosa."

## 22. Mesh dla jednej aplikacji i pułapka cargo cultu
Summary: Nie ma sensu budować mesha from scratch dla jednej małej aplikacji, bo to inwestycja w platformę. Łukasz często spotyka pytania o mesh motywowane potrzebą testów A/B, zaawansowanego routingu czy mikrosegmentacji dla jednej lub dwóch usług — a te cele da się osiągnąć prościej. Szymon dodaje analogiczny przykład zespołów chcących Kubernetesa wyłącznie dla autoscalingu, który daje np. App Services out of the box.
Speaker summaries:
- Łukasz Kałużny: Opisuje typowe realne motywacje zapytań o mesh i podkreśla, że zwykle istnieje prostsza droga do celu.
- Szymon Warda: Ilustruje ten sam antywzorzec przykładem Kubernetesa wybieranego tylko dla autoscalingu.
Most interesting quotes:
1. Łukasz Kałużny: "Robimy to, bo o tym przeczytaliśmy i zobaczyliśmy na prezentacjach, że jest fajne — a da się to zrobić w zupełnie inny, prostszy sposób."
2. Szymon Warda: "Rozmawiam z zespołami, które chcą mieć Kubernetesa po to, żeby mieć autoscaling. A potem pokazujemy App Services, gdzie autoscaling jest out of the box."

## 23. Podsumowanie — Kubernetes jako krok pośredni i rekomendacje końcowe
Summary: Szymon uważa, że Kubernetes jest krokiem pośrednim i że dziś w wyborze między Kubernetesem a Service Meshem badałby raczej mesh, bo daje większą wartość. Łukasz zgadza się, ale zastrzega, że mesh ma sens tylko wtedy, gdy przestaniemy myśleć o nim jak o Kubernetesie i podejściu OPS heavy — jeśli nie wykorzystamy jego funkcjonalności w skończonym czasie, lepiej zostać przy czystym Kubernetesie, który wymaga mniejszych kompetencji.
Speaker summaries:
- Szymon Warda: Rekomenduje badanie Service Mesha zamiast samego Kubernetesa, widząc w tym drugim jedynie etap przejściowy.
- Łukasz Kałużny: Warunkuje sens mesha zmianą sposobu myślenia i realnym wykorzystaniem jego funkcji, inaczej doradza czysty Kubernetes.
Most interesting quotes:
1. Szymon Warda: "Kubernetes jest krokiem pośrednim i gdybym miał rozważać, czy Kubernetes, czy Service Mesh, mimo wszystko zacząłbym badać Service Mesha — daje większą wartość."
2. Łukasz Kałużny: "Mesh tak, ale wtedy, gdy przestaniemy myśleć o nim jak o Kubernetesie i podejściu OPS heavy."
