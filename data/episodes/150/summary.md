## 1. Wprowadzenie i ogłoszenia
Summary: Prowadzący rozpoczynają odcinek standardowym powitaniem i przedstawiają nadchodzące szkolenia. Łukasz wspomina o szkoleniu "Architektura 101", a Szymon o szkoleniu z observability z wykorzystaniem open source.

Speaker summaries:
- Szymon Warda: Wita słuchaczy i informuje o swoim szkoleniu dotyczącym observability z wykorzystaniem narzędzi open source.
- Łukasz Kałużny: Przedstawia swoje szkolenie "Architektura 101", które uczy myślenia jak architekt i projektowania systemów.

Most interesting quotes:
1. Łukasz Kałużny: "Patoarchitekci.io/szkolenia. Jeżeli słuchacie tego w kwietniu 2025, to słuchajcie najbliższe nadchodzące to Architektura 101, w której pokazuję jak myśleć jak architekt, jak projektować systemy, o czym pamiętać, co jest nieoczywiste."

## 2. Motywacje do budowania własnego PAS na onpremie
Summary: Prowadzący omawiają główne motywacje stojące za decyzją o budowie własnej platformy PAS (Platform as a Service) na infrastrukturze onpremise. Wskazują na kwestie regulacyjne, geopolityczne, finansowe oraz potrzebę niezależności od dostawców chmurowych.

Speaker summaries:
- Łukasz Kałużny: Wskazuje trzy główne motywatory: regulacje i kwestie geopolityczne, koszty oraz chęć uzyskania lewaru negocjacyjnego i niezależności od jednego dostawcy.
- Szymon Warda: Zauważa trend wynoszenia prostych usług (np. compute) z chmury na infrastrukturę własną, podczas gdy bardziej złożone usługi pozostają w chmurze.

Most interesting quotes:
1. Łukasz Kałużny: "Pierwsze, to są kwestie regulacyjne, które obecnie mają mniejsze znaczenie, ale nadal są istotne. Szczególnie widać to przy trendach związanych z AI i innych technologiach, gdzie preferujemy posiadanie wszystkich zasobów w Europie."
2. Łukasz Kałużny: "Kolejną rzeczą, która za tym idzie, są finanse. Tutaj wszystko zależy od organizacji firmy i sposobu liczenia kosztów, ponieważ chmura może być zarówno droższa jak i tańsza, w zależności od okoliczności."
3. Łukasz Kałużny: "Ostatnim istotnym punktem, który często obserwujemy, jest potrzeba uzyskania lewaru negocjacyjnego. Wynikać to może z sytuacji, gdy firma wyrasta z przekonania, że chmura zapewnia szybki dostęp do wielu funkcji, a gotowe API zaczynają być postrzegane jako zbyt mocne uzależnienie od jednego dostawcy."

## 3. Komponenty platformy PAS
Summary: Prowadzący wymieniają kluczowe komponenty platformy PAS, które są niezbędne dla aplikacji. Omawiają potrzeby aplikacji w zakresie compute, usług wspomagających oraz narzędzi zarządzających.

Speaker summaries:
- Łukasz Kałużny: Wymienia najważniejsze elementy platformy: compute, bazy danych, cache, storage, kolejki, repozytoria, CI/CD, logi, monitoring, observability oraz portal dostępowy.
- Szymon Warda: Potwierdza, że Kubernetes jest obecnie najbardziej sensownym wyborem jako fundament platformy PAS ze względu na jego ekosystem i możliwości orkiestracji.

Most interesting quotes:
1. Łukasz Kałużny: "Potrzebujesz dla aplikacji compute'a, co jest absolutnym minimum - miejsce, gdzie chcesz hostować swoje aplikacje. Z drugiej strony potrzebujesz wszystkich usług wspomagających, takich jak bazy danych, cache, storage, kolejki oraz inne ogólne komponenty."
2. Szymon Warda: "Kubernetes jest najlepszym wyborem z prostego powodu - posiada rozbudowany ekosystem i jest zarządzany za pomocą relatywnie czytelnego kodu w formacie YAML."
3. Łukasz Kałużny: "Mówiąc o Kubernetesie, nie bierzemy całego diagramu CNCF i nie implementujemy wszystkiego. To jest naprawdę staranne wybieranie poszczególnych komponentów."

## 4. Zarządzanie tożsamością
Summary: Prowadzący omawiają kwestię zarządzania tożsamością w platformie PAS. Podkreślają konieczność posiadania identity providera wspierającego OIDC oraz możliwe rozwiązania w tym zakresie.

Speaker summaries:
- Łukasz Kałużny: Podkreśla konieczność posiadania identity providera z obsługą OIDC, wymienia rozwiązania jak Keycloak czy DEX, które mogą się zintegrować z LDAP i wystawić go jako OIDC.
- Szymon Warda: Zastanawia się nad sensem utrzymywania wszystkich elementów platformy lokalnie, sugerując możliwość korzystania z rozwiązań hybrydowych.

Most interesting quotes:
1. Łukasz Kałużny: "Twój identity provider musi dostarczać OIDC, ponieważ wszystkie usługi, takie jak Kubernetes czy inne komponenty, o których wspominamy, potrafią integrować się poprzez OIDC w celu zrealizowania federacji tożsamości."
2. Łukasz Kałużny: "Jeżeli posiadasz Active Directory z ADFS, możesz wykorzystać narzędzia takie jak Keycloak czy DEX. Są to rozwiązania, które umożliwiają podłączenie się do LDAP i wystawienie go jako OIDC."

## 5. Repozytorium kodu i CI/CD
Summary: Dyskusja na temat wyboru repozytorium kodu oraz systemów CI/CD dla platformy PAS. Prowadzący rozważają korzyści i wady utrzymywania własnych rozwiązań versus korzystanie z usług zewnętrznych.

Speaker summaries:
- Łukasz Kałużny: Wskazuje, że repozytorium kodu jest warstwą dostępu i zarządzania platformą, a wybór między rozwiązaniem lokalnym a hostowanym zależy od motywacji stojących za budową platformy.
- Szymon Warda: Preferuje korzystanie z zewnętrznych usług CI/CD ze względu na trudności w utrzymaniu własnych rozwiązań, szczególnie w kontekście backupów i bezpieczeństwa danych.

Most interesting quotes:
1. Łukasz Kałużny: "Repozytorium kodu jest niezbędne, ponieważ stanowi ono warstwę dostępu i zarządzania całą platformą."
2. Szymon Warda: "Będę raczej wybierał zewnętrzne rozwiązania, ponieważ utrzymanie własnego CI/CD, szczególnie biorąc pod uwagę backupy danych i związane z tym kwestie, jest bardzo ryzykownym przedsięwzięciem."
3. Łukasz Kałużny: "Jeżeli motywacją nie są kwestie geopolityczne, regulacyjne czy uniezależnienie się, to zdecydowanie można wybrać wersję hostowaną takiego rozwiązania."

## 6. Kubernetes jako fundament platformy
Summary: Prowadzący szczegółowo omawiają wybór Ranchera jako rozwiązania do zarządzania Kubernetesem w kontekście budowy platformy PAS. Wyjaśniają zalety tego rozwiązania i jego funkcjonalności.

Speaker summaries:
- Łukasz Kałużny: Rekomenduje Ranchera jako rozwiązanie do zarządzania Kubernetesem, wymieniając jego zalety: łatwość wdrożenia, gotowe konfiguracje, możliwość przeprowadzania upgrade'ów in-place oraz zintegrowany portal dostępowy.
- Szymon Warda: Zwraca uwagę na aspekt cenowy Ranchera, który jest często liczony od klastra, co może być korzystne finansowo.

Most interesting quotes:
1. Łukasz Kałużny: "Z naszego doświadczenia obecnie najlepszym rozwiązaniem jest Rancher, jeśli chodzi o zarządzanie Kubernetesem."
2. Łukasz Kałużny: "Rancher rozwiązuje problem wdrożenia klastra. Dodatkowo, oferuje gotową, sprawdzoną konfigurację, zawierającą zestaw kompatybilnych driverów Ingressa."
3. Łukasz Kałużny: "Najważniejszą zaletą jest dla mnie kompletny, gotowy do użycia zestaw zawierający portal dostępowy oraz mechanizmy zarządzania uprawnieniami."

## 7. Infrastruktura bare metal i wirtualizacja
Summary: Dyskusja na temat warstwy infrastruktury bare metal i wirtualizacji dla platformy PAS. Prowadzący omawiają zmiany na rynku spowodowane przejęciem VMware przez Broadcom oraz alternatywne rozwiązania.

Speaker summaries:
- Łukasz Kałużny: Omawia zmiany na rynku po przejęciu VMware przez Broadcom i wskazuje alternatywy jak Harvester, OpenShift Virtualization czy Proxmox.
- Szymon Warda: Zauważa, że wybór rozwiązania do wirtualizacji zależy od skali projektu i specyfiki środowiska.

Most interesting quotes:
1. Łukasz Kałużny: "Jeszcze dwa lata temu bez wahania rekomendowałbym VMware, który był relatywnie tani w implementacji, sprawdzony i nie wymagał dodatkowych analiz."
2. Łukasz Kałużny: "VMware został przejęty przez Broadcoma, który obecnie maksymalizuje zyski z tej inwestycji. Ostatnio tempo zmian nieco zwolniło, ale proces optymalizacji przychodów nadal trwa."
3. Łukasz Kałużny: "Zaczynają pojawiać się rozwiązania wirtualizacyjne bazujące na Kubernetesie, choć można również rozważyć bardziej klasyczne podejście z wykorzystaniem Proxmoxa."

## 8. Wysoka dostępność w platformie PAS
Summary: Prowadzący dyskutują o możliwościach zapewnienia wysokiej dostępności w platformie PAS budowanej na onpremie w porównaniu do rozwiązań chmurowych.

Speaker summaries:
- Łukasz Kałużny: Zauważa, że większość firm nie wykorzystuje prawidłowo stref dostępności w chmurze, a w przypadku onpremise można osiągnąć podobne SLA jak w pojedynczej strefie chmurowej.
- Szymon Warda: Podkreśla, że zbudowanie wysokiej dostępności na onpremie jest realne, ale kosztowne czasowo i finansowo, a odtworzenie infrastruktury po awarii jest trudniejsze niż w chmurze.

Most interesting quotes:
1. Łukasz Kałużny: "Jeśli chodzi o wysoką dostępność, większość organizacji nie wykorzystuje prawidłowo stref dostępności w swoich systemach chmurowych, a co dopiero mówić o innych rozwiązaniach."
2. Łukasz Kałużny: "Gdy przedstawiasz koszty i architekturę rozwiązania active-passive w chmurze, często kończy się na konfiguracji active z backupem danych do drugiego regionu."
3. Szymon Warda: "W przypadku awarii całego centrum danych, pojawia się pytanie, czy w ogóle będziesz miał możliwość fizycznego dostępu do infrastruktury lub jakikolwiek inny sposób komunikacji."

## 9. Rozwiązania hybrydowe
Summary: Prowadzący omawiają możliwości wykorzystania rozwiązań hybrydowych, łączących infrastrukturę onpremise z usługami chmurowymi, jako element strategii budowy platformy PAS.

Speaker summaries:
- Łukasz Kałużny: Wskazuje, że Rancher pozwala na podpięcie zarządzanych Kubernetesów z chmury, co umożliwia hybrydowe podejście do infrastruktury.
- Szymon Warda: Rekomenduje podejście hybrydowe, gdzie stałe obciążenia utrzymywane są onpremise, a zmienne lub developerskie w chmurze.

Most interesting quotes:
1. Łukasz Kałużny: "Wykorzystując rozwiązanie takie jak Rancher, możesz zintegrować zarządzane klastry Kubernetes z chmury, co daje możliwość połączenia różnych środowisk."
2. Szymon Warda: "Systemy o przewidywalnym obciążeniu warto utrzymywać na infrastrukturze on-premise, choćby ze względów finansowych. Natomiast systemy o zmiennym obciążeniu lub środowiska deweloperskie i testowe doskonale nadają się do modelu hybrydowego."
3. Łukasz Kałużny: "Istniał mit, że chmura jest ekonomicznym rozwiązaniem dla środowisk deweloperskich, ale jest to prawdą jedynie w przypadku małych projektów, które wymagają szybkiego wdrożenia."

## 10. Rejestry kontenerów i pakietów
Summary: Dyskusja na temat rejestrów kontenerów i pakietów jako elementów platformy PAS. Prowadzący omawiają dostępne rozwiązania komercyjne i open source.

Speaker summaries:
- Łukasz Kałużny: Wymienia JFrog Artifactory jako kompleksowe rozwiązanie komercyjne oraz Harbor jako rekomendowane rozwiązanie open source dla repozytorium kontenerów.
- Szymon Warda: Potwierdza, że Artifactory jest powszechnie stosowanym rozwiązaniem w organizacjach.

Most interesting quotes:
1. Łukasz Kałużny: "Jeśli chcesz zintegrować wszystkie repozytoria w jednym miejscu z centralnym zarządzaniem, możesz rozważyć JFrog Artifactory, który oferuje kompleksowe rozwiązanie."
2. Łukasz Kałużny: "Repozytorium powinno być zlokalizowane blisko klastrów Kubernetes. To jest element, którego nie da się pominąć."
3. Łukasz Kałużny: "Jeśli chodzi o rozwiązania open source, Harbor z projektu CNCF jest rekomendowanym repozytorium i nie ma potrzeby szukać alternatyw w tym zakresie."

## 11. Bazy danych w platformie PAS
Summary: Prowadzący omawiają podejście do baz danych w platformie PAS, koncentrując się na wykorzystaniu operatorów Kubernetesowych dla różnych typów baz danych.

Speaker summaries:
- Łukasz Kałużny: Rekomenduje wykorzystanie operatorów Kubernetesowych dla baz danych open source, takich jak MongoDB, PostgreSQL czy Cassandra, oraz tradycyjne podejście dla SQL Server i Oracle.
- Szymon Warda: Zgadza się z podejściem do baz korporacyjnych jak SQL Server, sugerując automatyzację poprzez pipeline CI/CD.

Most interesting quotes:
1. Łukasz Kałużny: "Jeśli chodzi o bazy danych, operatory Kubernetes są rekomendowanym rozwiązaniem."
2. Łukasz Kałużny: "Operator umożliwia deklaratywne zarządzanie bazą danych poprzez prosty plik YAML, w którym określasz parametry takie jak rozmiar przestrzeni dyskowej czy liczba węzłów."
3. Łukasz Kałużny: "Mamy klienta, który świadczy usługi bazodanowe w środowisku on-premise. Wspominaliśmy niedawno o operatorze PostgreSQL - Cloud Native PG, który został włączony do projektu CNCF."

## 12. Storage w platformie PAS
Summary: Prowadzący omawiają rozwiązania storage'owe dla platformy PAS, podkreślając różne podejścia do persistent volumes w Kubernetes oraz storage obiektowego.

Speaker summaries:
- Łukasz Kałużny: Omawia rozwiązania dla persistent volumes, takie jak Longhorn czy Portworx, oraz rekomenduje Minio jako sprawdzone rozwiązanie dla storage obiektowego z API S3.
- Szymon Warda: Zgadza się z rekomendacją Minio, przypominając, że polecali to rozwiązanie już wcześniej.

Most interesting quotes:
1. Łukasz Kałużny: "Przede wszystkim, nie udostępniamy persistent volumes bezpośrednio aplikacjom. To fundamentalna zasada - aplikacja nie powinna mieć bezpośredniego dostępu do wolumenów trwałych."
2. Łukasz Kałużny: "Można zaimplementować rozwiązania hiperkonwergentne, które wykorzystują lokalną przestrzeń dyskową serwerów i zapewniają jej replikację."
3. Łukasz Kałużny: "Dla aplikacji rekomendujemy storage obiektowy. W tym kontekście najlepszym wyborem będzie rozwiązanie udostępniające API kompatybilne z S3, a sprawdzonym w praktyce produktem jest Minio."

## 13. Backupy w platformie PAS
Summary: Dyskusja o strategiach backupu dla platformy PAS, podkreślająca konieczność wypychania danych poza infrastrukturę onpremise.

Speaker summaries:
- Łukasz Kałużny: Podkreśla konieczność backupowania konfiguracji, storage'u S3 oraz baz danych, najlepiej poza główną infrastrukturę.
- Szymon Warda: Zgadza się z podejściem hybrydowym do backupów, gdzie dane są przechowywane w lokalizacji oddalonej od głównej infrastruktury.

Most interesting quotes:
1. Łukasz Kałużny: "Znaczna część konfiguracji powinna być przechowywana w repozytorium, dotyczy to szczególnie plików konfiguracyjnych używanych przy edycji aplikacji."
2. Łukasz Kałużny: "Należy przesyłać kopie zapasowe poza główną infrastrukturę i centrum danych. Priorytetem są backupy konfiguracji, które umożliwią szybkie odtworzenie systemu."
3. Łukasz Kałużny: "Niektóre rozwiązania umożliwiają automatyczne tworzenie kopii zapasowych na zewnętrznych systemach zgodnych z API S3. Alternatywnie, należy rozważyć sposób wykonywania snapshotów i przesyłania ich poza infrastrukturę."

## 14. Cache w platformie PAS
Summary: Prowadzący omawiają rozwiązania cache'owe dla platformy PAS, koncentrując się na Redis i podkreślając konieczność prawidłowej konfiguracji bez persystencji.

Speaker summaries:
- Łukasz Kałużny: Podkreśla, że Redis nie powinien mieć persystencji i powinien być sklastrowany, wymienia dostępne operatory open source dla Redisa.
- Szymon Warda: Zauważa, że Redis jest dobrym rozwiązaniem, ponieważ działa jako self-healing cluster, który potrafi się sam naprawić i rozrzucić dane.

Most interesting quotes:
1. Łukasz Kałużny: "Redis nie powinien posiadać mechanizmów persystencji danych. Musimy wreszcie odejść od praktyki wykorzystywania go jako bazy danych lub projektowania aplikacji, które nie potrafią funkcjonować bez cache'a, a jedynie zwalniają w przypadku jego awarii."
2. Łukasz Kałużny: "Należy pamiętać o konieczności sklastrowania Redisa. Jeśli planujemy udostępniać go jako usługę, powinien być wdrożony jako dedykowany, niewielki klaster."

## 15. Logi i monitoring w platformie PAS
Summary: Prowadzący omawiają podejście do logów i monitoringu w platformie PAS, koncentrując się na stosie Grafana i Open Telemetry jako standardach.

Speaker summaries:
- Szymon Warda: Preferuje stos Grafana (Loki) zamiast Elastica ze względu na koszty i wydajność, podkreśla znaczenie standaryzacji i strukturyzacji logów oraz zaleca wykorzystanie Open Telemetry.
- Łukasz Kałużny: Zgadza się, że stos Grafana jest dobrym wyborem, ponieważ można go zbudować "z jednej paczki" i oferuje podstawowe funkcje wykrywania anomalii.

Most interesting quotes:
1. Szymon Warda: "Budując profesjonalną platformę, należy wymagać od deweloperów odpowiedniego podejścia do logowania. Mówię to jako osoba wywodząca się ze środowiska deweloperskiego - pełnotekstowe wyszukiwanie w celu znalezienia kontekstu błędu zazwyczaj nie jest niezbędne."
2. Łukasz Kałużny: "Wracamy do tematu, o którym często wspominamy - standaryzacji. W tym przypadku chodzi o standaryzację i strukturyzację logów, aby można je było odpowiednio kategoryzować i oznaczać."
3. Szymon Warda: "Nie zbudujemy efektywnej platformy bez wprowadzenia standardów. Wykorzystanie Open Telemetry umożliwia implementację wielu użytecznych funkcjonalności, co staje się obecnie niemal wymogiem."

## 16. Kolejki w platformie PAS
Summary: Dyskusja o rozwiązaniach kolejkowych dla platformy PAS, z rekomendacjami dla RabbitMQ i Kafki, wraz z ich operatorami Kubernetesowymi.

Speaker summaries:
- Łukasz Kałużny: Rekomenduje dwa typy produktów: RabbitMQ z operatorem dla smart brokerów oraz Kafkę z operatorem, mimo że technicznie nie jest ona kolejką.
- Szymon Warda: Potwierdza, że operator Kafki działa dobrze w praktyce.

Most interesting quotes:
1. Łukasz Kałużny: "W kategorii inteligentnych brokerów wiadomości, RabbitMQ oferuje własny operator klastra, który jest dostępny jako gotowe rozwiązanie i jest regularnie utrzymywany."
2. Łukasz Kałużny: "Kafka technicznie nie jest przeznaczona do pełnienia funkcji kolejki, jednak wiemy, że jest powszechnie wykorzystywana w tym celu. Dla Kafki również dostępny jest dedykowany operator."
3. Szymon Warda: "Operator Kafki jest dostępny i mogę potwierdzić z własnego doświadczenia, że działa niezawodnie - warto z niego korzystać."

## 17. Portal dostępowy i Backstage
Summary: Prowadzący omawiają podejście do portalu dostępowego dla platformy PAS, w tym wykorzystanie istniejących UI i ewentualne wdrożenie Backstage na późniejszym etapie.

Speaker summaries:
- Łukasz Kałużny: Rekomenduje wykorzystanie istniejących UI (Grafana, repo/CI/CD, Argo, Rancher) jako pierwszej warstwy dostępowej, a Backstage dopiero na samym końcu procesu budowy platformy.
- Szymon Warda: Podkreśla, że Backstage jest dobrym narzędziem do inwentaryzacji i zwiększenia używalności aplikacji, ale nie powinien być wdrażany na początku.

Most interesting quotes:
1. Łukasz Kałużny: "Na początkowym etapie Grafana, repozytorium kodu z CI/CD, Argo oraz portal Ranchera powinny stanowić podstawowe elementy dostępowe. Należy jasno określić, gdzie użytkownicy mogą przeglądać swoje klastry Kubernetes i aplikacje, gdzie znajdą logi i metryki w Grafanie, oraz gdzie mogą zarządzać konfiguracją i wdrożeniami usług PAS."
2. Łukasz Kałużny: "Samodzielne budowanie rozwiązania typu Backstage prawdopodobnie nie jest opłacalne, ponieważ może przekształcić się w niekończący się projekt zamiast w funkcjonalne narzędzie, lub będzie źródłem ciągłych problemów."
3. Szymon Warda: "Backstage jest wartościowym narzędziem służącym do inwentaryzacji zasobów, szczególnie gdy ilość komponentów zaczyna być trudna do zarządzania. Poprawia użyteczność aplikacji, umożliwiając zespołom identyfikację istniejących rozwiązań, które można wykorzystać, oraz obowiązujących standardów."

## 18. Podsumowanie i wnioski
Summary: Prowadzący podsumowują dyskusję o budowie platformy PAS na onpremie, omawiając kiedy warto to robić, ile czasu zajmuje budowa i jak wygląda przyszłość takich rozwiązań.

Speaker summaries:
- Łukasz Kałużny: Podkreśla, że budowa własnego PAS-a ma sens przy chęci odcięcia się od chmury, a MVP może być gotowe w 3-4 miesiące przy odpowiedniej wiedzy, ale wymaga ciągłego utrzymania i rozwoju.
- Szymon Warda: Zwraca uwagę na konieczność posiadania odpowiedniej skali (50+ workerów) i zespołów do utrzymania platformy, aby inwestycja się zwróciła.

Most interesting quotes:
1. Łukasz Kałużny: "Jeżeli posiadasz konkretne powody, takie jak chęć uniezależnienia się od chmury, konieczność opuszczenia jej lub potrzeba niezależności, to jest właściwy moment na budowę własnej platformy. Nie jest to decyzja motywowana względami technologicznymi."
2. Łukasz Kałużny: "Przy odpowiednich zasobach, możliwe jest stworzenie działającego MVP zawierającego wszystkie niezbędne elementy w ciągu 3-4 miesięcy. Bez odpowiednich zasobów, proces ten może trwać nieokreślenie długo."
3. Łukasz Kałużny: "Najczęściej popełnianym błędem jest próba jednoczesnej implementacji zbyt wielu komponentów. Patrząc na diagram CNCF, istnieje pokusa wdrożenia wszystkich dostępnych narzędzi na platformie. Dlatego ważne jest przestrzeganie zasady minimalizmu w podejściu do budowy platformy."
