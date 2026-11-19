## 1. Wprowadzenie do odcinka i zapowiedź szkoleń

Summary: Prowadzący przedstawiają się i zapowiadają nadchodzące szkolenia techniczne. Łukasz Kałużny promuje szkolenie "Architektura 101" startujące 25 listopada, Szymon Warda zapowiada szkolenie o Observability z Grafaną 8 grudnia, a na 16 grudnia planowany jest powrót szkolenia "Kubernetes The Hard Way".

Speaker summaries:
- Szymon Warda: Zapowiada swoje szkolenie o Observability skupione na praktycznym wykorzystaniu narzędzi Grafana i Prometheus.
- Łukasz Kałużny: Promuje szkolenie o architekturze systemów, które ma pomóc uporządkować wiedzę na temat projektowania systemów z szerszej perspektywy niż tylko kod.

Most interesting quotes:
1. Łukasz Kałużny: "Na tym szkoleniu będziecie mogli uporządkować wiedzę na temat projektowania systemów i podejścia do architektury nie tylko z perspektywy kodu, ale także wszystkich innych aspektów, które sprawiają problemy w praktyce."
2. Łukasz Kałużny: "Uczymy się, jak działa Kubernetes, stawiając go od zera bez żadnej pomocy, zagłębiając się w konfiguracje i sprawdzając, gdzie faktycznie ukryta jest każda funkcjonalność."

## 2. Przedstawienie gościa i jego roli w Allegro

Summary: Bartosz Gałek przedstawia się jako Principal Engineer w obszarze Developer Experience w Allegro. Wyjaśnia, że jego praca polega na dbaniu o to, aby developerom dobrze, sprawnie i wydajnie się pracowało. Podkreśla, że w Allegro istnieje cały dział zajmujący się Developer Experience.

Speaker summaries:
- Bartosz Gałek: Przedstawia swoją rolę jako osoby odpowiedzialnej za developer experience w dużej organizacji technologicznej.
- Łukasz Kałużny: Zauważa nietypowość dedykowanych ról i działów zajmujących się developer experience w polskich firmach.

Most interesting quotes:
1. Bartosz Gałek: "Jestem Bartosz Gałek, pracuję w Allegro jako Principal Engineer w obszarze Developer Experience. Na co dzień dbam o to, aby developerom i developerkom dobrze, sprawnie i wydajnie się pracowało."
2. Łukasz Kałużny: "To nietypowe, że w polskich firmach pojawiają się już dedykowane role i osoby odpowiedzialne za developer experience."

## 3. Geneza powstania Allegro Tech Radar

Summary: Bartosz wyjaśnia, że pomysł Tech Radaru wynikał z potrzeby uporządkowania wiedzy technologicznej w dużej organizacji. W Allegro jest kilkaset zespołów i kilka tysięcy aplikacji, co utrudnia wiedzę o tym, kto czego używa. Dodatkowo chcieli wyciągać lekcje z decyzji technicznych, podobnie jak robią to z post mortemami po awariach.

Speaker summaries:
- Bartosz Gałek: Opisuje problemy skali w dużej organizacji technologicznej i potrzebę centralizacji wiedzy o używanych technologiach.
- Łukasz Kałużny: Dopytuje o źródła pomysłu i motywacje stojące za inicjatywą Tech Radar.

Most interesting quotes:
1. Bartosz Gałek: "Mamy kilkaset zespołów i kilka tysięcy aplikacji budujących Allegro. Trudno wiedzieć, kto, gdzie i jak używa poszczególnych technologii oraz jak można tę wiedzę propagować."
2. Bartosz Gałek: "Jeżeli coś się nie sprawdziło, warto zostawić po tym ślad i kontekst: dana technologia nie sprawdziła się w Allegro z konkretnych powodów."

## 4. Decyzja o upublicznieniu Tech Radaru

Summary: Bartosz wyjaśnia, że decyzja o upublicznieniu Tech Radaru wynikała częściowo z jego pasji do open source, ale głównie z chęci pokazania technologicznej strony Allegro. Firma chce być postrzegana jako technologiczna, a nie tylko jako marketplace. Upublicznienie ma pomóc kandydatom do pracy zrozumieć, z jakimi technologiami będą pracować.

Speaker summaries:
- Bartosz Gałek: Tłumaczy, że jako fan open source nalegał na publiczne udostępnienie projektu i widzi w tym wartość dla employer brandingu.
- Łukasz Kałużny: Pyta o motywację upublicznienia, porównując z podobną inicjatywą Zalando.

Most interesting quotes:
1. Bartosz Gałek: "Jestem absolutnym fanem open source i uznałem, że skoro już to robimy, powinniśmy to zrobić publicznie na GitHubie, zamiast chować wewnątrz firmy."
2. Bartosz Gałek: "Allegro to przede wszystkim firma technologiczna. Z zewnątrz może wyglądać jak marketplace i duży e-commerce, ale wkładamy ogromną energię, pracę i pasję w technologię."

## 5. Proces tworzenia Tech Radaru i inwentaryzacja technologii

Summary: Projekt Tech Radaru rozpoczął się około rok temu od inwentaryzacji używanych technologii. Zespół wykorzystał Software Bill of Materials do identyfikacji bibliotek i narzędzi. Musieli również wyciągnąć wiedzę od ludzi, przeanalizować historie z wewnętrznych forów i czasami podjąć trudne decyzje o ujednoliceniu technologii.

Speaker summaries:
- Bartosz Gałek: Opisuje czasochłonny proces inwentaryzacji i konieczność pełnienia roli arbitra w decyzjach technologicznych.
- Szymon Warda: Pyta o szczegóły procesu, zaangażowane osoby i poziomy decyzji.

Most interesting quotes:
1. Bartosz Gałek: "Pierwszą rzeczą była inwentaryzacja bibliotek i narzędzi, których używamy."
2. Bartosz Gałek: "Musieliśmy pełnić rolę arbitra i jako gremium Tech Radarowe zadecydować: nie może być trzech identycznych rozwiązań w firmie, trzeba wybrać jedno."

## 6. Radar v1 jako snapshot obecnego stanu

Summary: Pierwsza wersja Radaru jest zrzutem obecnego stanu technologicznego Allegro bez oceniania wszystkich decyzji. Przykładem jest Groovy używany do testów od 2013 roku - mimo że mogą istnieć lepsze alternatywy, nie można zmusić całej firmy do migracji testów. Radar obserwuje obecny stan i prowadzi rozmowy o przyszłości poszczególnych technologii.

Speaker summaries:
- Bartosz Gałek: Wyjaśnia pragmatyczne podejście do pierwszej wersji Radaru, które akceptuje historyczne decyzje i obecny stan rzeczy.
- Szymon Warda: Dopytuje o wpływ Radaru na faktyczne działania migracyjne i decyzje technologiczne.

Most interesting quotes:
1. Bartosz Gałek: "Radar v1 to zrzut obecnego stanu. Wszystko, co jest obecnie używane, prezentujemy as is, nie dyskutujemy z niektórymi decyzjami."
2. Bartosz Gałek: "Nie mogę zmigrować całej firmy tylko dlatego, że Groovy mi się nie podoba. To moja opinia, ale trzeba ważyć intencje i kontekst."

## 7. Wpływ Tech Radaru na decyzje technologiczne

Summary: Tech Radar wpływa na decyzje poprzez zachowanie autonomii zespołów przy jednoczesnym wymaganiu feedbacku. Zespoły mogą wybierać dowolne technologie, ale muszą podzielić się doświadczeniami. Inwentaryzacja pozwala unikać odkrywania koła na nowo i obserwować trendy w kodzie, co umożliwia reagowanie na wzrosty lub spadki popularności technologii.

Speaker summaries:
- Bartosz Gałek: Opisuje balans między autonomią zespołów a potrzebą standaryzacji i dzielenia się wiedzą.
- Szymon Warda: Pyta o konkretny wpływ Radaru na migracje i planowane akcje.

Most interesting quotes:
1. Bartosz Gałek: "Jeżeli zespół potrzebuje PostgreSQL z pgvector, niech to przetestuje i się nauczy. Tech Radar wprowadził tylko jeden wymóg: po przećwiczeniu musisz przekazać nam feedback."
2. Bartosz Gałek: "Obserwowanie na bieżąco zależności używanych w kodzie pozwala nam identyfikować nowe trendy w firmie."

## 8. Proces zbierania feedbacku i znajdowania właścicieli technologii

Summary: Zespół Tech Radaru podzielił się zadaniami i dla każdej technologii musiał znaleźć właściciela - osobę będącą twarzą danej technologii. Proces wymagał fizycznego chodzenia po ludziach i zbierania opisów, historii i kontekstu decyzji. Informacje były zapisywane w markdownach w wewnętrznym Radarze, który zawiera szczegóły niedostępne publicznie.

Speaker summaries:
- Bartosz Gałek: Opisuje pracochłonny proces identyfikacji właścicieli technologii i zbierania od nich wiedzy kontekstowej.
- Szymon Warda: Pyta o metody zbierania informacji i feedbacku od pracowników.

Most interesting quotes:
1. Bartosz Gałek: "Przeprowadziliśmy swoistą krucjatę. Czasami łatwo było znaleźć zespół odpowiedzialny za decyzje frontendowe, czasami było to trudne."
2. Bartosz Gałek: "Fizycznie chodziliśmy do ludzi, rozmawialiśmy z nimi i prosiliśmy o wyjaśnienie, kontekst i historię stojącą za decyzjami."

## 9. Proces decyzyjny dotyczący poziomów w Radarze

Summary: Decyzje o poziomach (trial, adopt, assess, hold) są podejmowane przez właścicieli technologii, a nie na poziomie organizacji. Właściciele technologii decydują o statusie na podstawie swoich planów i kontekstu użycia. Zespół Tech Radaru prowadzi z nimi rozmowy i pomaga określić odpowiedni poziom.

Speaker summaries:
- Szymon Warda: Dopytuje o proces decyzyjny dotyczący poziomów w Radarze.
- Bartosz Gałek: Wyjaśnia, że decyzje są zdecentralizowane i leżą po stronie właścicieli technologii.

Most interesting quotes:
1. Bartosz Gałek: "Właściciele części angularowej mówili: chcemy z tego zejść, ponieważ widzimy, że reszta firmy jest już gdzie indziej, a my pracujemy nad migracją i mamy na to plany."
2. Szymon Warda: "Poziomy w Radarze to decyzje nie na poziomie organizacji, tylko na poziomie zespołów utrzymujących dane technologie."

## 10. Największe wyzwania w tworzeniu Tech Radaru

Summary: Największym wyzwaniem był czas, ponieważ Tech Radar nie przynosił bezpośrednich korzyści biznesowych i był inicjatywą oddolną. Trudnością było zorganizowanie się i znalezienie ludzi gotowych poświęcić czas z pasji. Po rozpoczęciu projektu i komunikacji w firmie, proces stał się łatwiejszy, gdy ludzie zrozumieli cel inicjatywy.

Speaker summaries:
- Bartosz Gałek: Podkreśla, że najtrudniejsze było wystartowanie projektu niż jego późniejsza realizacja.
- Łukasz Kałużny: Pyta o największe trudności, wyzwania organizacyjne i kontrowersje.

Most interesting quotes:
1. Bartosz Gałek: "Tech Radar nie przyniesie milionów dolarów ani nie ma ogromnego uzasadnienia biznesowego, ale wynika z naszej wewnętrznej potrzeby."
2. Bartosz Gałek: "Najtrudniejsze było się zorganizować. Trzeba było ustalić, kto to będzie robił i kto może poświęcić na to więcej czasu."

## 11. Zaskoczenia podczas tworzenia Tech Radaru

Summary: Bartosz był zaskoczony mnogością używanych technologii - mimo 12 lat pracy w Allegro odkrył obszary z całkowicie nieznanymi mu stackami technologicznymi. Drugim szokiem było rozwarstwienie wersji - niektóre narzędzia były używane w 15 różnych wersjach, co powodowało problemy w integracjach.

Speaker summaries:
- Bartosz Gałek: Dzieli się osobistymi odkryciami dotyczącymi skali różnorodności technologicznej w organizacji.
- Łukasz Kałużny: Jest zaskoczony problemem wersjonowania, znając kulturę aktualizacji w Allegro.

Most interesting quotes:
1. Bartosz Gałek: "Zaskoczyła mnie mnogość technologii. Mimo 12 lat kariery w Allegro odkryłem obszary z całkowicie nieznanymi mi stackami technologicznymi."
2. Bartosz Gałek: "Okazało się, że niektóre narzędzia lub biblioteki używamy w firmie w piętnastu różnych wersjach."

## 12. Tech Radar jako narzędzie do standaryzacji

Summary: Tech Radar umożliwia identyfikację problemów jak rozwarstwienie wersji i pozwala na wypracowanie strategii standaryzacji. Może być zintegrowany z innymi inicjatywami jak health checki czy wymogi licencyjne. Dzięki wiedzy z Radaru można planować długoterminowe działania ujednolicające bez wymuszania natychmiastowych zmian.

Speaker summaries:
- Bartosz Gałek: Wyjaśnia, jak Tech Radar wspiera inne inicjatywy platformowe i umożliwia strategiczne planowanie.
- Łukasz Kałużny: Wyraża zaskoczenie problemem wersjonowania w kontekście znanej kultury aktualizacji w Allegro.

Most interesting quotes:
1. Bartosz Gałek: "Gdy mamy Tech Radar i widzę problem rozwarstwienia naszych wewnętrznych bibliotek, mogę skontaktować się z odpowiednim zespołem i wspólnie wypracować strategię."
2. Bartosz Gałek: "Nie mówię, że dzisiaj czy jutro, ale za pół roku lub rok chcę, aby tych wersji było maksymalnie dziesięć, a nie pięćdziesiąt trzy."

## 13. Poliglotyzm językowy w Allegro

Summary: Allegro wspiera wiele języków programowania, co czasem sprawia wyzwania, ale jest częścią filozofii autonomii zespołów. Platforma techniczna jest projektowana jako agnostyczna względem języka. Zamiast wymuszać jeden stack, Allegro wykorzystuje uniwersalne rozwiązania jak zmienne środowiskowe w Kubernetesie, które działają niezależnie od języka.

Speaker summaries:
- Bartosz Gałek: Broni poliglotyzmu jako elementu autonomii zespołów i wyjaśnia, jak platforma radzi sobie z różnorodnością.
- Łukasz Kałużny: Pyta o potencjalne problemy wynikające z używania wielu języków programowania.

Most interesting quotes:
1. Bartosz Gałek: "Jestem absolutnym fanem open source i wielość języków nie stanowi dla mnie ani mojego działu problemu. Można do tego podejść na dwa sposoby: narzekać na różnorodność lub ją wspierać."
2. Bartosz Gałek: "Allegro chce wspierać autonomię zespołów, a nasza platforma techniczna powinna być agnostyczna językowo. Nie ma znaczenia, w jakim języku uruchamiana jest aplikacja."

## 14. Decyzje dotyczące baz danych

Summary: Allegro ma długą historię z różnymi bazami danych. Cassandra jest na holdzie od kilku lat, Oracle jest niepotrzebny. Firma standaryzuje bazy relacyjne na Postgres, odchodząc od MySQL i innych. Decyzja wynika z potrzeby ujednolicenia i ułatwienia migracji do clouda. Postgres został wybrany ze względu na dynamikę rozwoju i wsparcie społeczności.

Speaker summaries:
- Szymon Warda: Pyta o decyzje dotyczące wielu baz danych i migrację do Postgresa.
- Bartosz Gałek: Wyjaśnia historyczne konteksty i strategię ujednolicenia na Postgres.

Most interesting quotes:
1. Bartosz Gałek: "Z Cassandrą byliśmy związani od 2016 lub 2017 roku i to się nie sprawdziło. Mam nadzieję, że kiedyś podzielimy się pełną historią tego doświadczenia."
2. Bartosz Gałek: "Chcielibyśmy, aby wszyscy w miarę możliwości przeszli na jedno rozwiązanie, co ułatwi nam później migrację części baz do clouda."

## 15. Migracja z własnego service mesha do Istio

Summary: Mimo że Allegro ma własny service mesh oparty na Envoy i Consulu, firma planuje migrację do Istio jako standardowego rozwiązania w Kubernetesie. Decyzja wynika z dojrzałości standardu, który dogonił customowe rozwiązania Allegro. Celem jest ujednolicenie i kompatybilność z rozwiązaniami cloudowymi jak GCP.

Speaker summaries:
- Łukasz Kałużny: Wyraża zaskoczenie obecnością Istio, znając historię własnego service mesha Allegro.
- Bartosz Gałek: Wyjaśnia, że standard dogonił ich customizacje i migracja ma sens mimo włożonej wcześniej pracy.

Most interesting quotes:
1. Łukasz Kałużny: "Co robi tam Istio? Mieliście przecież wiele prezentacji o tym, jak zbudowaliście własny service mesh na bazie Envoy."
2. Bartosz Gałek: "W dłuższej perspektywie chcielibyśmy ustandaryzować się na Istio, ponieważ jest to standardowy service mesh w Kubernetesie."

## 16. Stos monitoringu i observability

Summary: Allegro używa zarówno stosu ELK (Elasticsearch, Kibana) jak i Grafany z Prometheus i Victoria Metrics. Elasticsearch służy nie tylko do logów, ale również aplikacyjnie do wyszukiwania. Grafana Tempo przechowuje trace'y z OpenTelemetry. Prometheus scrape'uje metryki, a Victoria Metrics służy jako backend. Komponenty są traktowane jako wymienne klocki.

Speaker summaries:
- Szymon Warda: Pyta o pozornie rozdwojony stos monitoringu i decyzje dotyczące poszczególnych narzędzi.
- Bartosz Gałek: Wyjaśnia, że komponenty mają konkretne cele i są wybierane pragmatycznie, nie ideologicznie.

Most interesting quotes:
1. Bartosz Gałek: "Elasticsearch to odwrócony indeks, który pozwala nam efektywnie wyszukiwać. To, że przechowujemy tam logi dla Kibany, jest kwestią wtórną."
2. Bartosz Gałek: "To są dla mnie klocki, które mają konkretny cel, dlatego są osobne."

## 17. Migracja z push do pull w metrykach

Summary: Allegro przeszło długą drogę od wypychania metryk (Diamond, Graphite) do scrape'owania przez Prometheus. Migracja została zakończona około dwa lata temu. Ta historia pokazuje ewolucję podejścia do monitoringu w organizacji i jest przykładem kontekstu, którym Allegro chce się dzielić w przyszłych wersjach Radaru.

Speaker summaries:
- Szymon Warda: Jest zaskoczony kierunkiem migracji, który jest odwrotny do obecnych trendów.
- Bartosz Gałek: Potwierdza nietypową ścieżkę migracyjną i zapowiada podzielenie się pełną historią.

Most interesting quotes:
1. Bartosz Gałek: "Przez długi czas wypychaliśmy metryki, a następnie przeszliśmy na scraping. Migrację na Prometheus zakończyliśmy około dwa lata temu."
2. Szymon Warda: "To ciekawe, ponieważ obecne trendy wskazują raczej odwrotny kierunek."

## 18. Kontekst jako klucz do wartości Tech Radaru

Summary: Bartosz podkreśla, że prawdziwa wartość Tech Radaru leży w kontekście użycia, a nie tylko w liście używanych technologii. Allegro chce dzielić się historiami i doświadczeniami, wyjaśniać dlaczego coś działa lub nie działa w ich kontekście. Niektóre technologie mogą mieć różny status w różnych kontekstach użycia w organizacji.

Speaker summaries:
- Bartosz Gałek: Podkreśla znaczenie kontekstu i historii za decyzjami technologicznymi.
- Szymon Warda: Zwraca uwagę na ważność określenia kontekstu wykorzystania technologii.

Most interesting quotes:
1. Bartosz Gałek: "Każdy produkt SaaS ma listę klientów. Ale ja nie chcę być kolejnym logo mówiącym 'używamy tego'. Chcę powiedzieć: używamy tego, ponieważ..."
2. Bartosz Gałek: "Mamy punkty w Radarze, które są identyczne, ale w różnych kontekstach mają różny status."

## 19. Redis w trial i używanie Couchbase

Summary: Redis w Allegro jest w statusie trial, mimo że wielu mogłoby się spodziewać, że jest standardem. Firma używała i używa Couchbase jako cache i jest z niego zadowolona. Redis pojawiał się i znikał w historii firmy. Teraz wraca jako managed service, ale zespół zastanawia się nad najlepszym sposobem jego wdrożenia - czy w cloudzie, czy na własnej infrastrukturze.

Speaker summaries:
- Łukasz Kałużny: Jest zaskoczony, że Redis nie jest standardowym cachem w Allegro.
- Bartosz Gałek: Wyjaśnia historię z Redisem i obecne używanie Couchbase jako rozwiązania cache'ującego.

Most interesting quotes:
1. Bartosz Gałek: "Redis pojawiał się i znikał w naszej historii wielokrotnie. Dopiero teraz wracamy do tego, aby Redis stał się pełnoprawnym rozwiązaniem w wielu miejscach."
2. Bartosz Gałek: "Do cache'owania na co dzień używamy Couchbase i jesteśmy z niego zadowoleni."

## 20. Wybór Copilot zamiast Cursor

Summary: Allegro wybrało GitHub Copilot zamiast Cursor głównie ze względów korporacyjnych i integracyjnych. Firma opiera się na JetBrains i IntelliJ od 2013 roku, ma już kontrakty z Microsoftem przez GitHub, co ułatwiło negocjacje. Zmiana na Cursor wymagałaby zmian kulturowych i dodatkowych umów NDA. Bartosz uważa, że różnice między narzędziami się zacierają.

Speaker summaries:
- Szymon Warda: Pyta o przyczyny wyboru Copilot i odrzucenia Cursor.
- Bartosz Gałek: Wyjaśnia pragmatyczne powody korporacyjne i techniczne stojące za decyzją.

Most interesting quotes:
1. Bartosz Gałek: "Największym czynnikiem był poziom integracji z ekosystemem Allegro. Cursor to zewnętrzna firma, z którą musielibyśmy podpisać dodatkowe umowy NDA."
2. Bartosz Gałek: "Allegro działa na GitHubie, więc mamy już kontrakty z Microsoftem. Negocjowanie warunków dla Copilot było znacznie łatwiejsze."

## 21. Przyszłość Tech Radaru i plany rozwoju

Summary: Allegro planuje regularne spotkania otwarte dla wszystkich, gdzie można będzie aktualizować punkty w Radarze i proponować nowe. Przy okazji tych spotkań będą wydawane kolejne wersje publicznego Radaru. Celem jest, aby każda kropka na publicznym Radarze miała swoją historię - mini blog post wyjaśniający kontekst i doświadczenia Allegro z daną technologią.

Speaker summaries:
- Szymon Warda: Pyta o dalszy cykl życia Radaru i plany na przyszłość.
- Bartosz Gałek: Zapowiada ewolucję Radaru w kierunku platformy dzielenia się historiami i kontekstami decyzji.

Most interesting quotes:
1. Bartosz Gałek: "Chciałbym, aby za każdą kropką na publicznym Tech Radarze stała historia opublikowana przez Allegro - mini post opisujący kontekst tego punktu."
2. Bartosz Gałek: "U was może się sprawdzić świetnie, ale u nas nie zadziałało z konkretnych powodów."

## 22. Umowa na kolejny odcinek o kontekstach

Summary: Na zakończenie rozmowy Bartosz proponuje, a prowadzący przyjmują propozycję kolejnego odcinka, gdy ukaże się następna wersja Tech Radaru z kontekstami i historiami. Zapowiada możliwość szczegółowej rozmowy o pojedynczych historiach technologicznych, które mają ciekawe tło w Allegro.

Speaker summaries:
- Bartosz Gałek: Proponuje kolejne spotkanie po wydaniu wersji Radaru z kontekstami.
- Łukasz Kałużny: Wyraża zainteresowanie rozmową o kontekstach i trzyma kciuki za publikację.
- Szymon Warda: Potwierdza chęć rozmowy o realnym użyciu technologii na dużą skalę.

Most interesting quotes:
1. Bartosz Gałek: "Gdy ukaże się następna wersja i będziemy mogli porozmawiać o kontekstach, możemy poświęcić nawet pół godziny na omówienie jednej historii."
2. Łukasz Kałużny: "Nie mogę się doczekać. Być może zaprosimy was na review, gdy wydacie wersję z osadzeniem w kontekstach."
