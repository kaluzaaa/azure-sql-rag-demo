## 1. Wprowadzenie do odcinka i informacje o szkoleniach
Summary: Prowadzący przedstawiają się i omawiają nadchodzące szkolenia - GitHub Actions przez Szymona oraz Model Context Protocol Masterclass przez Łukasza. Szkolenia są ostatnimi w tym półroczu i dotyczą zaawansowanych technologii.
Speaker summaries:
- Łukasz Kałużny: Prowadzi szkolenie MCP Masterclass, wyjaśnia poziom wejścia i wymagania techniczne dla uczestników.
- Szymon Warda: Prowadzi intensywne dwudniowe szkolenie GitHub Actions, podkreśla rozwój tej technologii od początków.
Most interesting quotes:
1. Szymon Warda: "GitHub Actions znacznie się rozbudowały od czasu, gdy po raz pierwszy z nimi pracowaliśmy, i obecnie można za ich pomocą zrealizować wiele różnorodnych zadań."
2. Łukasz Kałużny: "24 czerwca odbędzie się Model Context Protocol Masterclass - jednodniowe szkolenie, po którym będziecie całkowicie wyczerpani."

## 2. Wprowadzenie do tematu biedahostingu
Summary: Prowadzący przedstawiają główny temat odcinka - biedahosting jako miejsce na side projecty i MVP. Inspiracją był wpis Oskara Dudycza o Continuous Deployment z Docker Compose i GitHub Actions.
Speaker summaries:
- Łukasz Kałużny: Definiuje biedahosting jako rozwiązanie dla projektów, gdzie nie chce się płacić pełnej opłaty za chmurę.
- Szymon Warda: Wspomina czasy studenckie, gdy takie rozwiązania były popularne i zastanawia się nad obecną popularnością.
Most interesting quotes:
1. Łukasz Kałużny: "Biedahosting to miejsce przeznaczone na nasze projekty poboczne, MVP i inne eksperymenty."
2. Szymon Warda: "Zastanawiam się, jak popularne są obecnie takie rozwiązania? Czy ludzie rzeczywiście tworzą tego typu hosting dla swoich projektów pobocznych?"

## 3. Historia homelabów prowadzących
Summary: Łukasz i Szymon dzielą się swoimi doświadczeniami z homelabami - od klastrów Hyper-V na laptopach po serwery z dużą ilością RAM-u. Omawiają ewolucję swoich setupów domowych.
Speaker summaries:
- Łukasz Kałużny: Opisuje swój historyczny homelab z 2013 roku z 32 GB RAM-u, Xeonem i klastrami wirtualizacyjnymi.
- Szymon Warda: Wspomina swoje doświadczenia z hostowaniem stron, repozytoriów SVN i narzędzi do skanowania kodu.
Most interesting quotes:
1. Łukasz Kałużny: "W 2013 roku mój serwer domowy miał 32 GB pamięci RAM oraz dyski SAS."
2. Szymon Warda: "Posiadałem serwer ISA, na którym hostowałem strony internetowe i repozytorium kodu - wówczas był to jeszcze SVN."

## 4. Rachunki za prąd jako argument przeciwko homelabom
Summary: Szymon przedstawia kalkulacje kosztów energii dla urządzeń działających 24/7. Okazuje się, że urządzenie o mocy 60W kosztuje rocznie około 250-300 zł w rachunkach za prąd.
Speaker summaries:
- Szymon Warda: Przeprowadza szczegółowe kalkulacje kosztów energii i argumentuje przeciwko homelabom ze względów ekonomicznych.
- Łukasz Kałużny: Przyznaje, że wcześniej ceny prądu były pomijalne w porównaniu do obecnych.
Most interesting quotes:
1. Szymon Warda: "Czy wiesz, ile kosztuje utrzymanie urządzenia o mocy 60 watów działającego całodobowo przez rok? Około 250-300 złotych."
2. Łukasz Kałużny: "To było tyle lat temu, że koszt energii elektrycznej był wówczas pomijalnymi w porównaniu do obecnych cen."

## 5. Obecny stan homelabów prowadzących
Summary: Prowadzący omawiają swoje obecne setupy domowe, które ograniczają się głównie do routerów, NAS-ów i Raspberry Pi. Dyskutują o różnicy między homelabem a home automation.
Speaker summaries:
- Łukasz Kałużny: Ma minimalistyczny setup z routerem, NAS-em i okazjonalnie Raspberry Pi.
- Szymon Warda: Podobnie ograniczył swój setup, zachowując tylko niezbędne elementy w szafie rack.
Most interesting quotes:
1. Łukasz Kałużny: "Poza eksperymentami z Raspberry Pi w kontekście wysokiej dostępności, mój setup składa się jedynie z routera i serwera NAS."
2. Szymon Warda: "Automatyzacja domowa to nieco inny cel niż homelab."

## 6. Opcje tanich VPS-ów
Summary: Łukasz przedstawia swoje ulubione rozwiązania tanich VPS-ów, szczególnie Mikrus od Unknowa, który oferuje 4 GB RAM i 40 GB dysku za 197 zł rocznie. Omawia też inne opcje jak NETCAP i Contabo.
Speaker summaries:
- Łukasz Kałużny: Poleca konkretne usługi VPS-ów, szczególnie Mikrus, i porównuje ceny z europejskimi odpowiednikami.
- Szymon Warda: Wyraża obawy dotyczące stabilności tanich dostawców i możliwości nagłego zakończenia usług.
Most interesting quotes:
1. Łukasz Kałużny: "Mikrus od Unknowa to interesująca platforma. Autor stworzył również ciekawy materiał wideo wyjaśniający, jak to działa od strony technicznej i jaki jest model biznesowy."
2. Szymon Warda: "Dla projektów pobocznych kluczowe jest to, aby nie marnować na nie zbyt dużo czasu."

## 7. VPS-y klasy "bieda-plus"
Summary: Dyskusja o droższych, ale bardziej stabilnych opcjach VPS-ów jak DigitalOcean i AWS Lightsail. Te rozwiązania kosztują 2-3 razy więcej, ale oferują lepszą stabilność i wsparcie.
Speaker summaries:
- Łukasz Kałużny: Przedstawia opcje "bieda-plus" jako kompromis między ceną a stabilnością dla projektów MVP.
- Szymon Warda: Potwierdza wartość płacenia więcej za spokój duszy i stabilność usługi.
Most interesting quotes:
1. Łukasz Kałużny: "DigitalOcean to prawdopodobnie drugi co do popularności dostawca w środowisku startupowym w Stanach Zjednoczonych."
2. Szymon Warda: "Takie rozwiązania są warte dodatkowych kosztów ze względu na spokój ducha."

## 8. Free tiery od hyperscalerów
Summary: Omówienie darmowych poziomów usług od głównych dostawców chmurowych. Prowadzący wyjaśniają różnice między vendor-specific technologiami a uniwersalnymi rozwiązaniami.
Speaker summaries:
- Łukasz Kałużny: Tłumaczy strukturę free tierów, w tym różnice między zawsze darmowymi a darmowymi przez 12 miesięcy.
- Szymon Warda: Doprecyzowuje, że dotyczy to zarówno usług compute'owych jak i bazodanowych.
Most interesting quotes:
1. Łukasz Kałużny: "Mowa o darmowych poziomach usług oferowanych przez głównych dostawców chmurowych."
2. Szymon Warda: "Dotyczą one zarówno usług obliczeniowych, jak i bazodanowych."

## 9. Hosting statycznych stron
Summary: Szczegółowe omówienie opcji hostingu statycznych stron, w tym GitHub Pages, Cloudflare Pages i rozwiązania z object storage. Prowadzący podkreślają to jako najlepszą opcję dla wielu projektów.
Speaker summaries:
- Łukasz Kałużny: Opisuje różne opcje hostingu statycznego, szczególnie doceniając preview funkcjonalność Cloudflare Pages.
- Szymon Warda: Określa hosting statyczny jako "najlepszą opcję" i poleca Cloudflare jako must-have.
Most interesting quotes:
1. Szymon Warda: "To najlepsza dostępna opcja."
2. Łukasz Kałużny: "Jeżeli tworzysz pull requesty, system automatycznie wystawia strony podglądu pod dedykowaną domeną preview."

## 10. Podejście do budowania i deploymentu
Summary: Łukasz przedstawia swoje podejście do CI/CD bez Kubernetesa, wykorzystując GitHub Actions do budowania obrazów Docker i przechowywania ich w GitHub Container Registry.
Speaker summaries:
- Łukasz Kałużny: Opisuje swój workflow z GitHub Actions, Docker i repozytorium obrazów GitHub.
- Szymon Warda: Ostrzega przed stawianiem Jenkinsa na słabych VPS-ach i budowaniem kodu lokalnie.
Most interesting quotes:
1. Łukasz Kałużny: "Pierwszym elementem mojego podejścia do budowania i wdrażania jest rezygnacja z Kubernetesa."
2. Szymon Warda: "Budowanie kodu na słabym VPS-ie z ograniczonymi zasobami może całkowicie zakłócić działanie strony."

## 11. Spór o Docker Compose vs natywne instalacje
Summary: Prowadzący prezentują różne podejścia do deploymentu - Łukasz preferuje Docker Compose z monorepo, Szymon opowiada się za natywnymi instalacjami usług dla lepszego monitoringu.
Speaker summaries:
- Łukasz Kałużny: Argumentuje za Docker Compose z powodu prostoty i przenośności rozwiązania.
- Szymon Warda: Preferuje natywne instalacje dla lepszego monitoringu i mniejszej liczby ruchomych elementów.
Most interesting quotes:
1. Łukasz Kałużny: "Wszystkie aplikacje wdrażane na jednym VPS-ie przechowuję w monorepozytorium i wszystkie usługi są zdefiniowane w Docker Compose."
2. Szymon Warda: "Zdecydowanie polecam uruchamianie, tam gdzie to możliwe, usług zainstalowanych natywnie w systemie."

## 12. Reverse proxy i Cloudflare
Summary: Dyskusja o wykorzystaniu Caddy'ego i Traffica jako reverse proxy oraz obowiązkowym użyciu Cloudflare'a dla publicznych aplikacji. Omówienie tuneli Cloudflare vs tradycyjnego proxy.
Speaker summaries:
- Łukasz Kałużny: Opisuje swoje doświadczenia z Caddy (wbudowany Let's Encrypt) i Traefik (dynamiczna konfiguracja).
- Szymon Warda: Potwierdza konieczność używania Cloudflare'a jako must-have dla publicznych aplikacji.
Most interesting quotes:
1. Łukasz Kałużny: "Jedną z kluczowych funkcji Caddy jest wbudowana obsługa Let's Encrypt."
2. Szymon Warda: "Konfiguracja Cloudflare z przechowywaniem DNS-u i wykorzystaniem cachowania oraz dystrybucji to niezbędny element dla tego typu projektów."

## 13. Strategia backupów
Summary: Łukasz przedstawia swoje podejście do backupów wykorzystując GitHub Actions do monitoringu, S3 do przechowywania i Rclone do synchronizacji z różnymi dostawcami storage.
Speaker summaries:
- Łukasz Kałużny: Opisuje system backupów z wykorzystaniem GitHub Actions, S3 i narzędzi jak Rclone.
- Szymon Warda: Dzieli się negatywnymi doświadczeniami z Backblaze, szczególnie z ich oprogramowaniem do odzyskiwania danych.
Most interesting quotes:
1. Łukasz Kałużny: "Osoby zadowolone z życia nie tworzą kopii zapasowych."
2. Szymon Warda: "Miałem doświadczenie z odzyskiwaniem danych z Backblaze. Problem nie leży w szybkości, ale w jakości ich oprogramowania do pobierania danych, które jest wyjątkowo niedopracowane."

## 14. Zarządzanie secretami
Summary: Omówienie różnych podejść do zarządzania secretami - od commitowania w repo przez GitHub Secrets po wykorzystanie 1Password CLI i natywnych rozwiązań providerów.
Speaker summaries:
- Łukasz Kałużny: Przedstawia ewolucję od commitowania secretów przez GitHub Secrets do 1Password CLI.
- Szymon Warda: Opowiada się za minimalizowaniem liczby providerów i używaniem natywnych rozwiązań.
Most interesting quotes:
1. Łukasz Kałużny: "Powiedz mi, jak często z lenistwa commitowałeś sekrety bezpośrednio do repozytorium?"
2. Szymon Warda: "Nadal preferuję posiadanie jak najmniejszej liczby dostawców, aby później nie mieć dodatkowych komplikacji."

## 15. Free tiery maszyn wirtualnych
Summary: Szczegółowe omówienie darmowych tierów dla maszyn wirtualnych w Azure, Oracle i Google Cloud, wraz z ich ograniczeniami i ukrytymi kosztami.
Speaker summaries:
- Łukasz Kałużny: Prezentuje specyfikacje free tierów, szczególnie Oracle z 1/8 OCPU i 1GB RAM.
- Szymon Warda: Komentuje ograniczenia i problemy z dostępnością zasobów u darmowych providerów.
Most interesting quotes:
1. Łukasz Kałużny: "Rzeczywisty poziom 'always free' u Oracle to 1/8 OCPU oraz 1GB pamięci RAM."
2. Szymon Warda: "Należy się liczyć z tym, że czasami nie można uruchomić maszyny wirtualnej z powodu wyczerpania dostępnych zasobów."

## 16. Serverless i budżetowanie
Summary: Dyskusja o wykorzystaniu rozwiązań serverless w ramach free tierów oraz konieczności ustawiania budżetów i monitorowania kosztów, by uniknąć nieprzyjemnych rachunków.
Speaker summaries:
- Łukasz Kałużny: Opisuje bogaty offering serverless w free tierach - miliony wywołań, kolejki, bazy NoSQL.
- Szymon Warda: Ostrzega przed niemonitorowanymi kosztami i poleca karty prepaidowe lub budżety.
Most interesting quotes:
1. Łukasz Kałużny: "W ramach poziomów 'always free' dostępne są miliony wywołań funkcji lambda oraz miliony komunikatów w kolejkach."
2. Szymon Warda: "Warto skonfigurować kartę przedpłaconą lub ustawić budżety, aby kontrolować koszty."

## 17. Azure Storage jako niedoceniana usługa
Summary: Szczegółowe omówienie możliwości Azure Storage, w tym wbudowanego PUB/SUB, NoSQL tables i kolejek jako kompletnego rozwiązania dla aplikacji serverless.
Speaker summaries:
- Łukasz Kałużny: Przedstawia Azure Storage jako niedocenianą usługę z bogatymi możliwościami.
- Szymon Warda: Potwierdza wartość Azure Storage, szczególnie jego tanich kolejek i tables.
Most interesting quotes:
1. Łukasz Kałużny: "Azure Storage jest prawdopodobnie najbardziej niedocenianą usługą, ponieważ oferuje elegancki, prosty mechanizm PUB/SUB oraz tabele NoSQL typu column-wide."
2. Szymon Warda: "Te rozwiązania są bardzo ekonomiczne nawet przy dużych wolumenach danych, a dodatkowo oferują funkcjonalność kolejek."

## 18. Monitoring w modelu free tier
Summary: Omówienie dostępnych rozwiązań monitoringu w ramach darmowych tierów, w tym Grafana Cloud i ograniczeń związanych z czasem przechowywania metryk.
Speaker summaries:
- Szymon Warda: Opisuje możliwości free tierów dla monitoringu, szczególnie Grafana Cloud.
- Łukasz Kałużny: Potwierdza dostępność różnych usług monitoringu w ramach darmowych planów.
Most interesting quotes:
1. Szymon Warda: "Należy pamiętać, że na przykład Grafana również oferuje darmowy poziom usług."
2. Szymon Warda: "Większość dostawców oferuje darmowe poziomy dla swoich specjalistycznych usług."

## 19. Dla kogo jest biedahosting
Summary: Prowadzący definiują grupę docelową dla rozwiązań biedahostingu - osoby wystawiające projekty publicznie lub uczące się administracji i DevOps.
Speaker summaries:
- Łukasz Kałużny: Wyklucha programistów eksperymentujących lokalnie, skupia się na projektach publicznych i nauce administracji.
- Szymon Warda: Rozszerza o aspekt edukacyjny - konieczność zrozumienia całego procesu przez praktyczne doświadczenie.
Most interesting quotes:
1. Łukasz Kałużny: "Jeżeli zajmujesz się programowaniem i nie planujesz wystawiać aplikacji publicznie, tylko eksperymentujesz lokalnie, nie ma sensu zajmować się tym zagadnieniem."
2. Szymon Warda: "Nic nie nauczy człowieka funkcjonowania internetu tak skutecznie, jak wystawienie czegoś publicznie."

## 20. Wartość edukacyjna publicznego hostingu
Summary: Szymon argumentuje, że wystawienie czegoś publicznie jest kluczowe dla zrozumienia całego stosu technologicznego - od administracji przez aplikacje po bazy danych.
Speaker summaries:
- Szymon Warda: Podkreśla edukacyjną wartość publicznego hostingu jako "must have" dla rozwoju.
- Łukasz Kałużny: Wspomina o trendzie self-hostingu dla prywatności, ale wyraża sceptycyzm co do jego praktyczności.
Most interesting quotes:
1. Szymon Warda: "To prawdziwa kopalnia wiedzy. Bez praktycznego doświadczenia z publicznym hostingiem nie zrozumiesz i nie opanujesz tych zagadnień."
2. Szymon Warda: "To niezbędny element dla osób, które rzeczywiście chcą się rozwijać."

## 21. Self-hosting i jego problemy
Summary: Krytyczna dyskusja o trendzie self-hostingu wszystkich aplikacji dla prywatności. Prowadzący wyrażają sceptycyzm wobec złożoności i problemów z utrzymaniem takich rozwiązań.
Speaker summaries:
- Łukasz Kałużny: Szanuje ideę prywatności, ale uważa self-hosting za stratę czasu.
- Szymon Warda: Ostrzega przed złożonością i częstymi awariami w rozwiązaniach self-hosted.
Most interesting quotes:
1. Łukasz Kałużny: "Szanuję ich stanowisko, ale uważam, że to strata czasu."
2. Szymon Warda: "Liczba problemów wynikających z konieczności integracji wielu komponentów do prawidłowego funkcjonowania takiego systemu jest naprawdę znacząca."

## 22. Filozoficzne podsumowanie - warto vs opłaca się
Summary: Łukasz kończy cytatem Bartoszewskiego o różnicy między tym co warto a tym co się opłaca, jako filozoficzne podsumowanie dylematu biedahostingu.
Speaker summaries:
- Łukasz Kałużny: Przywołuje filozoficzną refleksję o różnicy między wartością a opłacalnością.
- Szymon Warda: Dodaje praktyczną uwagę o przejściu na lepsze rozwiązania gdy projekt się rozwinie.
Most interesting quotes:
1. Łukasz Kałużny: "W życiu istnieją rzeczy, które warto robić, i takie, które się opłacają. Nie zawsze to, co warto, jest opłacalne, i nie zawsze to, co się opłaca, warto robić."
2. Szymon Warda: "Gdy projekt odniesie sukces, w pewnym momencie warto przejść na bardziej profesjonalne rozwiązanie i zapłacić więcej."

## 23. Finalne rekomendacje
Summary: Końcowe podsumowanie z konkretnymi rekomendacjami - thrashowy VPS z minimalistycznym setupem i CI/CD lub free tier cloudowy, w zależności od potrzeb projektu.
Speaker summaries:
- Łukasz Kałużny: Podsumowuje dwie główne ścieżki: tani VPS z automatyzacją lub free tier cloudowy.
- Szymon Warda: Potwierdza sensowność obu podejść w zależności od celów projektu.
Most interesting quotes:
1. Łukasz Kałużny: "Podstawowy VPS z minimalistyczną konfiguracją, gdzie wszystko wdraża się automatycznie przez CI/CD z GitHub, GitLab lub podobnych platform."
2. Łukasz Kałużny: "Alternatywnie można wykorzystać darmowy poziom usług od dostawcy chmurowego, mając świadomość prawidłowego funkcjonowania takiego rozwiązania."
