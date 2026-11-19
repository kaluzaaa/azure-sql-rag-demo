## 1. Zapowiedź jesiennych szkoleń - Architektura 101

**Podsumowanie:** Łukasz zapowiada szkolenie "Architektura 101" (25-26 listopada, 2-3 grudnia), które ma na celu uporządkowanie i ustrukturyzowanie wiedzy o architekturze dla osób aspirujących do roli architekta. Szkolenie obejmuje fundamenty architektury, wzorce projektowe, charakterystyki architektury, bezpieczeństwo, podstawy sieci, build vs buy oraz wybór stosu technologicznego z licznymi ćwiczeniami grupowymi.

**Podsumowania wypowiedzi:**
- Łukasz Kałużny: Prowadzi szkolenie porządkujące wiedzę architektoniczną z naciskiem na praktyczne ćwiczenia grupowe i Architectural Kata.
- Szymon Warda: Podkreśla, że szkolenie pomaga uporządkować rolę architekta w organizacji i zdefiniować cele oraz narzędzia pracy.

**Najciekawsze cytaty:**
1. Łukasz Kałużny: "Wiele osób ma styczność z architekturą, jej projektowaniem lub aspiruje do roli architekta. Szkolenie pokazuje, w jaki sposób ustrukturyzować tę wiedzę."
2. Szymon Warda: "To szkolenie porządkuje temat, który często widzę w rozmowach z ludźmi awansowanymi do roli architekta, mianowicie uporządkowanie tego, co właściwie powinienem robić w organizacji."

## 2. Szkolenie z Observability ze stosem Grafana

**Podsumowanie:** Szymon prezentuje jednodniowe szkolenie techniczne o Observability skupiające się na stosie Grafana i Prometheus. Szkolenie obejmuje architekturę systemu, Loki do agregacji logów, Prometheus do metryk z naciskiem na kardynalność i labelowanie, oraz Tempo do zbierania trace'ów, z praktycznymi warsztatami i składnią zapytań.

**Podsumowania wypowiedzi:**
- Szymon Warda: Prowadzi praktyczne szkolenie z narzędzi Grafana z dużym naciskiem na składnię, wydajność i zrozumienie architektury systemów monitorowania.

**Najciekawsze cytaty:**
1. Szymon Warda: "To nie są narzędzia typu Elastic, gdzie wpisujemy 'error' i działa. Działa, póki działa."
2. Szymon Warda: "Tempo to system, który bardzo fajnie działa. Jest z reguły zbudowany dla developerów w obecnej wersji, a całą agregację musimy sobie z reguły napisać na boku."

## 3. Szkolenie Kubernetes The Hard Way

**Podsumowanie:** Łukasz przedstawia całodniowe szkolenie praktyczne, podczas którego uczestnicy budują klaster Kubernetes od podstaw z binarek na gołych wirtualkach. Obejmuje to przygotowanie certyfikatów, CA, szyfrowanie etcd, stawianie control plane'ów, konfigurację sieci CNI, DNS, testy wysokiej dostępności i troubleshooting.

**Podsumowania wypowiedzi:**
- Łukasz Kałużny: Prowadzi zaawansowane szkolenie pokazujące wewnętrzną architekturę Kubernetes poprzez praktyczne budowanie klastra od zera.

**Najciekawsze cytaty:**
1. Łukasz Kałużny: "Po całym dniu wiecie, gdzie te elementy w Kubernetesie są i co za co odpowiada. W większości przypadków doceniacie już Azure AKS, że nie musicie się z tym męczyć i tego utrzymywać."
2. Łukasz Kałużny: "Trzeba patrzeć na Kubernetesa jak na cepa i wtedy od razu wiemy, dlaczego coś nielogicznego jest bardzo logiczne."

## 4. Główne problemy z logami w organizacjach

**Podsumowanie:** Szymon identyfikuje dwa kluczowe problemy z logami: nadmierna ilość prowadząca do wysokich kosztów utrzymania (szczególnie w Elasticu) oraz niezdolność do efektywnego korzystania z zebranych logów. Organizacje często tonią w ilości logów bez możliwości szybkiego zrozumienia, co się wydarzyło i dlaczego.

**Podsumowania wypowiedzi:**
- Szymon Warda: Wskazuje na problem nadmiernej ilości logów i trudności w ich wykorzystaniu do debugowania bez pomocy developerów.
- Łukasz Kałużny: Dodaje obserwację o przerażającej sytuacji, gdy zespoły muszą szukać logów w czterech różnych miejscach.

**Najciekawsze cytaty:**
1. Szymon Warda: "Główne problemy z logami są właściwie dwa. Pierwszy to nadmierna ilość - organizacja zaczyna tonąć w kosztach ich utrzymania."
2. Łukasz Kałużny: "Ogarnęło mnie przerażenie podczas prac serwisowych przy większej zmianie w infrastrukturze, gdy ludzie z zespołów aplikacyjnych szukali logów w czterech różnych miejscach."

## 5. Rodzaje logów w systemach

**Podsumowanie:** Dyskusja o klasyfikacji logów obejmuje logi aplikacyjne, systemowe (infrastrukturalne), dostępowe (access control), bezpieczeństwa (audytowe), oraz kontrowersyjne kategorie jak logi biznesowe i diagnostyczne. Panelowie debatują, czy niektóre rodzaje logów nie powinny być zastąpione metrykami lub trace'ami.

**Podsumowania wypowiedzi:**
- Szymon Warda: Proponuje zastąpienie logów biznesowych metrykami, a diagnostycznych trace'ami, podkreślając że niektóre kategorie logów są przestarzałe.
- Łukasz Kałużny: Wskazuje na problem mieszania logów technicznych z biznesowymi i konieczność ich rozdzielenia.

**Najciekawsze cytaty:**
1. Szymon Warda: "Tak zwane logi biznesowe nie mają obecnie zastosowania w systemach. Powinny być zastąpione metrykami."
2. Łukasz Kałużny: "Logi techniczne są wymieszane z logami biznesowymi i to jest jeden wielki bałagan."

## 6. Sampling versus retencja - podejście do zarządzania logami

**Podsumowanie:** Szymon stanowczo odradza stosowanie samplingu logów, argumentując że zawsze odsampluje to, czego akurat potrzebujemy i jest praktycznie niemożliwy do poprawnego wykonania. Zaleca zamiast tego logowanie wszystkiego z bardzo krótką retencją oraz wykorzystanie Open Telemetry Collector do dynamicznej zmiany konfiguracji bez restartu aplikacji.

**Podsumowania wypowiedzi:**
- Szymon Warda: Kategorycznie odrzuca sampling jako rozwiązanie, promując krótką retencję i dynamiczną konfigurację collectorów.

**Najciekawsze cytaty:**
1. Szymon Warda: "Sampling zawsze będzie złem, bo odsampluje to, czego właśnie potrzebujecie. Sampling jest trudny i praktycznie niemożliwy do wykonania tak, żeby miał ręce i nogi."
2. Szymon Warda: "Nie stosujcie samplingu, logujcie wszystko, tylko z krótszą retencją."

## 7. Format i struktura logów - podstawowe zasady

**Podsumowanie:** Panelowie omawiają fundamentalne decyzje dotyczące formatowania logów: wybór JSON jako standardu, UTF jako kodowania, zapisywanie w jednej linii oraz konsekwentne używanie UTC dla znaczników czasu. Podkreślają znaczenie ustrukturyzowanych logów dla efektywnego przetwarzania i analizy.

**Podsumowania wypowiedzi:**
- Szymon Warda: Stanowczo promuje JSON w jednej linii jako standard formatowania, podkreślając problemy z parsowaniem multiline.
- Łukasz Kałużny: Zwraca uwagę na problemy z niespójnością formatów dat i stref czasowych między systemami.

**Najciekawsze cytaty:**
1. Szymon Warda: "Jeżeli to możliwe, zamieniamy znaki nowej linii, aby logi były w jednej linii."
2. Szymon Warda: "Ile razy zdarza się sytuacja, gdy odpytujesz o logi i pada pytanie: logujemy w UTC czy w czasie lokalnym?"

## 8. Obowiązkowe pola w logach

**Podsumowanie:** Szczegółowe omówienie wymaganych pól w logach strukturyzowanych: data (w UTC), poziom logowania (ze standardem z Open Telemetry), typ logu, opcjonalnie środowisko, service name, trace ID, span ID, opcjonalnie parent trace ID, wiadomość oraz error ze stackiem. Podkreślono znaczenie dokumentacji tych pól w repozytorium.

**Podsumowania wypowiedzi:**
- Szymon Warda: Szczegółowo definiuje wymagane pola logów i ich znaczenie dla efektywnego debugowania.
- Łukasz Kałużny: Proponuje rozwiązanie konfliktów nazewniczych przez przyjęcie standardu Open Telemetry zamiast wewnętrznych dyskusji.

**Najciekawsze cytaty:**
1. Łukasz Kałużny: "Jeżeli macie dyskusję w firmie, jak coś nazwać, oznacza to, że bałagan będzie kontynuowany. Przyjmijmy standard z Open Telemetry."
2. Szymon Warda: "Zakładamy repozytorium, gdzie wpisujemy, które pole co znaczy, żeby nie było ustalane doraźnie."

## 9. Problemy z nazwami poziomów logowania

**Podsumowanie:** Dyskusja o chaosie związanym z różnymi konwencjami nazewniczymi poziomów logowania (fatal vs critical) i niebezpieczeństwem niespójności między zespołami. Rozwiązaniem jest przyjęcie zewnętrznego standardu jak Open Telemetry, co eliminuje wewnętrzne konflikty i dyskusje o "lepszym" podejściu.

**Podsumowania wypowiedzi:**
- Szymon Warda: Opisuje problemy z wyszukiwaniem logów gdy zespoły używają różnych nazw poziomów logowania.
- Łukasz Kałużny: Podkreśla absurdalność sytuacji z 15 poziomami logowania i custom poziomami jako "płatkami śniegu".

**Najciekawsze cytaty:**
1. Szymon Warda: "Ile razy widziałeś sytuację, gdy ktoś szukał 'fatal' albo 'critical'?"
2. Szymon Warda: "Moim faworytem była firma z 15 poziomami logów. Piętnaście."

## 10. Architektura wysyłania logów - bezpośrednio vs przez collector

**Podsumowanie:** Omówienie różnych architektur wysyłania logów w zależności od wolumenu: małe systemy mogą wysyłać bezpośrednio do systemu docelowego, średnie i duże wymagają warstwy pośredniej (Open Telemetry Collector, Grafana Alloy) dla buforowania, batchowania, wzbogacania i filtrowania logów. Kafka jest możliwa, ale często niepotrzebna.

**Podsumowania wypowiedzi:**
- Szymon Warda: Szczegółowo opisuje korzyści z używania collectorów jako warstwy pośredniej dla wzbogacania i filtrowania logów.
- Łukasz Kałużny: Zgadza się z podejściem wielowarstwowym dla różnych skal systemów.

**Najciekawsze cytaty:**
1. Szymon Warda: "Mamy Open Telemetry Collector i Grafanę Alloy, które umieją buforować i spełniać tę rolę. Mogą też batchować."
2. Szymon Warda: "Możemy w tym momencie wzbogacać logi, dodawać labele i pola, które nas interesują, o których często nawet aplikacja może nie wiedzieć."

## 11. Stdout jako ostateczność, nie standard

**Podsumowanie:** Panelowie argumentują, że stdout powinien być używany tylko jako ostateczność w sytuacjach krytycznych, gdy aplikacja nie może połączyć się z systemem centralnym. Stdout jest miejscem na logi systemowe do szybkiego sprawdzenia stanu, ale nie na regularną agregację logów aplikacyjnych, które powinny być wysyłane bezpośrednio.

**Podsumowania wypowiedzi:**
- Szymon Warda: Traktuje stdout jako sygnał problemów, nie jako standardowe miejsce logowania aplikacji.
- Łukasz Kałużny: Widzi stdout jako narzędzie OPS-owe do szybkiego sprawdzenia stanu instancji.

**Najciekawsze cytaty:**
1. Szymon Warda: "To ostateczność - jeżeli coś pojawiło się na stdout, oznacza to, że mamy już problem."
2. Szymon Warda: "Stdout jest absolutnym złem i ostatecznością."

## 12. Określenie źródeł logów - co zbierać

**Podsumowanie:** Kluczowa dyskusja o świadomym wyborze źródeł logów zamiast zbierania "wszystkiego". Obowiązkowe są logi z aplikacji i kluczowej infrastruktury aplikacyjnej (Ingress, bazy danych dla błędów krytycznych), ale należy unikać zbierania wszystkich logów systemowych. Decyzje muszą być kompromisem między kosztami a potrzebami.

**Podsumowania wypowiedzi:**
- Łukasz Kałużny: Używa metafory managera mówiącego "give me everyone" jako anty-wzorca podejścia do logów.
- Szymon Warda: Podkreśla konieczność świadomego wyboru źródeł i ostrzega przed zbieraniem absolutnie wszystkiego.

**Najciekawsze cytaty:**
1. Łukasz Kałużny: "Po pierwszej awarii manager wygląda jak w słynnej scenie z Hollywood - 'give me everyone' - po kresce w łazience. Tak wygląda manager, który chce mieć wszystkie logi."
2. Szymon Warda: "Logi wszystkiego to naprawdę bardzo dużo logów, do których z reguły nie mamy żadnej potrzeby."

## 13. Tenanty i podział logów według struktury organizacji

**Podsumowanie:** Omówienie znaczenia używania tenantów w systemach logowania dla rozdzielenia logów różnych systemów i zespołów. Unikanie jednego tenanta dla całej organizacji, podział per system (nie serwis), pozwalający na różne pola i konteksty. Struktura tenantów odzwierciedla prawo Conwaya i strukturę komunikacyjną firmy.

**Podsumowania wypowiedzi:**
- Szymon Warda: Argumentuje za podziałem per system z uwzględnieniem struktury organizacyjnej i politycznej firmy.
- Łukasz Kałużny: Przywołuje prawo Conwaya jako wyjaśnienie struktury tenantów i namespace'ów.

**Najciekawsze cytaty:**
1. Szymon Warda: "Nie powinniśmy mieć jednego systemu z jednym tenantem dla całej organizacji. To prowadzi do sytuacji, gdy każdy widzi wszystko i mamy totalny bałagan."
2. Łukasz Kałużny: "Struktura namespace'ów i klastrów w Kubernetesie odzwierciedla strukturę komunikacyjną w firmie. Struktura tenantów będzie to również odzwierciedlać."

## 14. Retencja i budżety logowania

**Podsumowanie:** Omówienie strategii retencji logów - lepiej zbierać więcej z krótszą retencją niż długo trzymać wszystko. Unikanie archive'ów dla logów info z uwagi na koszty odzyskiwania. Wprowadzenie budżetów logowania dla zespołów na środowiskach dev/test jako mechanizmu kontroli jakości i ilości, bez stosowania na produkcji.

**Podsumowania wypowiedzi:**
- Szymon Warda: Proponuje budżety jako "bicz" na nadgorliwe zespoły logujące wszystko na poziomie info.
- Łukasz Kałużny: Podkreśla znaczenie doprecyzowania, na których środowiskach stosować limity.

**Najciekawsze cytaty:**
1. Szymon Warda: "Lepiej jest zbierać więcej logów, a krócej je trzymać."
2. Szymon Warda: "Ilość nie idzie w parze z jakością. Potrzebujemy logów dobrej jakości, a nie wszystkiego, co komukolwiek przyszło do głowy wysłać."

## 15. Problem ciągłego dodawania logów bez usuwania

**Podsumowanie:** Szymon identyfikuje wredną tendencję, że logi są tylko dodawane, nigdy nie usuwane, co prowadzi do nieustannego wzrostu bez względu na użyteczność. Bez budżetów i kontroli jakości, systemy logowania zapełniają się bezużytecznymi logami dodanymi kiedyś przez kogoś, co zwiększa koszty i zmniejsza przydatność.

**Podsumowania wypowiedzi:**
- Szymon Warda: Ostrzega przed naturalną tendencją do akumulacji bezużytecznych logów bez mechanizmów kontrolnych.
- Łukasz Kałużny: Porównuje chaotyczne logowanie do "troubleshootingu dupą".

**Najciekawsze cytaty:**
1. Szymon Warda: "Logi mają wredną tendencję - tylko je dodajemy, nigdy nie usuwamy."
2. Łukasz Kałużny: "Czasem mam wrażenie, że logi przypominają troubleshooting na czuja."

## 16. Quality of life improvements - usprawnienia praktyczne

**Podsumowanie:** Omówienie drobnych, ale istotnych usprawnień: standardy labelowania w Kubernetes, linkowanie trace'ów z logami dla łatwiejszego debugowania, pozwolenie developerom na pisanie do stdout lokalnie (z innym formatem) przy zachowaniu strukturyzowanych logów na produkcji. Konfigurowalne środowiska logowania.

**Podsumowania wypowiedzi:**
- Szymon Warda: Proponuje pragmatyczne podejście z różnymi konfiguracjami dla środowisk lokalnych i produkcyjnych.
- Łukasz Kałużny: Podkreśla znaczenie wsparcia różnych configów w bibliotekach do logowania.

**Najciekawsze cytaty:**
1. Szymon Warda: "Pozwólmy developerom pisać lokalnie do stdout, tylko na produkcji niech używają odpowiedniego formatu."
2. Szymon Warda: "Lokalnie logi są często nieustrukturyzowane. Nie ma co się porywać na wypisywanie JSON w jednej linii - to nie zadziała."

## 17. Problem multiline i parsowania logów

**Podsumowanie:** Szczegółowe omówienie problemu parsowania logów wieloliniowych, szczególnie stack trace'ów. Szymon stanowczo zaleca konwersję wszystkich logów do jednej linii (poprzez replace new line'ów), argumentując że pisanie regexów do parsowania multiline to dziesiątki osobogodzin pracy, która nigdy nie będzie działać generycznie.

**Podsumowania wypowiedzi:**
- Szymon Warda: Kategorycznie odrzuca próby parsowania multiline jako niemożliwe do generycznego rozwiązania.
- Łukasz Kałużny: Zgadza się, że nie osiągniemy tego generycznie, mimo że ludzie będą się kłócić w komentarzach.

**Najciekawsze cytaty:**
1. Szymon Warda: "Jeżeli to możliwe, zamieniamy znaki nowej linii, aby logi były w jednej linii. Ktoś pomyśli: ale jak to czytać? Tak, będziemy czytać. Ale w sytuacji, gdy nie uda się coś zrobić i będziemy musieli wypisać błąd na stdout, logi się nie rozjadą."
2. Szymon Warda: "Spędziłem dużo czasu na pisaniu regexów do wyłapywania multiline'ów i nie zamierzam tego robić więcej."

## 18. Obowiązki aplikacji przy wysyłaniu logów

**Podsumowanie:** Gdy aplikacja wysyła logi bezpośrednio lub przez collector, musi implementować retry, buforowanie i raportowanie problemów z komunikacją. W przypadku niemożności połączenia z systemem logowania, aplikacja powinna fallbackować na stdout jako ostateczność, jednocześnie logując sam fakt problemów z połączeniem.

**Podsumowania wypowiedzi:**
- Szymon Warda: Definiuje wymagania dla aplikacji odpowiedzialnych za wysyłanie logów, podkreślając konieczność mechanizmów awaryjnych.

**Najciekawsze cytaty:**
1. Szymon Warda: "Jeżeli aplikacja wysyła logi, ma pewne obowiązki. Musi implementować retry, powtarzanie, buforowanie oraz raportowanie, że nie mogła się skomunikować."
2. Szymon Warda: "Przydałoby się wiedzieć, co się właściwie dzieje. Ponownie, stdout jest absolutnym złem i ostatecznością."

## 19. Asynchroniczny zapis logów

**Podsumowanie:** Krótkie, ale istotne omówienie konieczności asynchronicznego zapisywania logów. Developerzy nie powinni implementować synchronicznego wysyłania logów z oczekiwaniem na potwierdzenie, ponieważ terminal i inne mechanizmy zapisu są wolne i mogą znacząco spowolnić aplikację.

**Podsumowania wypowiedzi:**
- Szymon Warda: Podkreśla znaczenie asynchroniczności w zapisie logów dla wydajności aplikacji.

**Najciekawsze cytaty:**
1. Szymon Warda: "Zapis powinien być asynchroniczny. Dlatego między innymi nie piszemy na terminal - terminal jest wolny i może znacząco spowolnić aplikację. Developerzy nie powinni implementować synchronicznego zapisu."

## 20. Podsumowanie - trzy kluczowe rzeczy do zapamiętania

**Podsumowanie:** Na zakończenie Szymon destyluje całą dyskusję do trzech kluczowych działań: stworzenie dokumentu definiującego pola logów i ich znaczenie, ustalenie architektury wysyłania logów (preferowane przez collector), oraz formatowanie wszystkiego w jednej linii. Te trzy elementy stanowią fundament uporządkowanego systemu logowania.

**Podsumowania wypowiedzi:**
- Szymon Warda: Podsumowuje najważniejsze wnioski z całej dyskusji w formie trzech konkretnych działań.
- Łukasz Kałużny: Dopytuje o konkretne punkty do zapamiętania dla słuchaczy.

**Najciekawsze cytaty:**
1. Szymon Warda: "Spisać dokument - pierwsza rzecz. Pola z nazwami i opisem, do czego służą. Druga rzecz - ustalić, gdzie te logi są wysyłane."
2. Szymon Warda: "Wszystko w jednej linii. Spędziłem dużo czasu na pisaniu regexów do wyłapywania multiline'ów i nie zamierzam tego robić więcej."
