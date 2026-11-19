## 1. Wprowadzenie do odcinka i ogłoszenia o szkoleniach

Podsumowanie: Prowadzący omawiają nadchodzące szkolenia dostępne na stronie Patoarchitekci.io, w tym nowe szkolenie "Agentic AI the Hard Way" oraz "Kubernetes The Hard Way". Szkolenia zostały wcześniej opublikowane w odpowiedzi na długie procesy budżetowe w firmach uczestników.

Podsumowania prowadzących:
- Łukasz Kałużny: Informuje o nowym szkoleniu dotyczącym tworzenia agentów AI od podstaw bez frameworków oraz o dostępnych miejscach na szkolenie Kubernetes.
- Szymon Warda: Potwierdza informacje i prowadzi dalszą część wprowadzenia do głównego tematu odcinka.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Agentic AI the Hard Way - napisanie agenta od zera, bez żadnego frameworka, bez LangChaina."
2. Łukasz Kałużny: "Wielu z Was narzekało na długie procesy budżetowe w firmach, dlatego wcześniej publikujemy terminy szkoleń."

## 2. Wprowadzenie do tematu Helm vs Customize

Podsumowanie: Łukasz wprowadza główny temat odcinka, porównując Helm i Customize jako narzędzia do zarządzania deploymentami na Kubernetes. Przedstawia swoją kontrowersyjną opinię, że dawanie niektórych narzędzi deweloperom jest jak dawanie dziecku brzytwy.

Podsumowania prowadzących:
- Łukasz Kałużny: Wyraża silne zastrzeżenia wobec nieodpowiedniego używania niektórych narzędzi, porównując to do niebezpiecznej sytuacji.
- Szymon Warda: Argumentuje, że zawsze ktoś może coś zepsuć, niezależnie od narzędzia, przywołując przykład Customize.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Dawanie tego ludziom to jak dawanie dziecku brzytwy na plac zabaw."
2. Szymon Warda: "To podejście zakłada, że jak damy narzędzie, to ktoś je zepsuje. Oczywiście, że zepsuje."

## 3. Podstawowe definicje Helm i Customize

Podsumowanie: Prowadzący wyjaśniają podstawowe różnice między Helm a Customize. Helm jest przedstawiony jako engine templateowy z logiką warunkową, podczas gdy Customize działa jako system nakładek (overlay) na czyste pliki YAML.

Podsumowania prowadzących:
- Szymon Warda: Definiuje Customize jako narzędzie do modyfikacji YAML przez wiele poziomów nakładek, a Helm jako engine templateowy z logiką warunkową.
- Łukasz Kałużny: Precyzuje, że Customize to system patchowania i nakładek na czyste YAML-e, podczas gdy Helm jest przede wszystkim package managerem.

Najciekawsze cytaty:
1. Szymon Warda: "Helm to engine templateowy do YAML-a z elementami logiki - pętlami, warunkami i podobnymi konstrukcjami."
2. Łukasz Kałużny: "Customize działa na zasadzie nakładek - overlay'ów. Bierzemy bazowy YAML i nakładamy na niego kolejne warstwy zmian."

## 4. Helm jako package manager i sposób dystrybucji

Podsumowanie: Łukasz podkreśla pierwotne przeznaczenie Helma jako package managera do dystrybucji produktów przez Artifact Hub. Obaj prowadzący zgadzają się, że Helm jest doskonały do dystrybucji produktów zewnętrznych i oprogramowania enterprise.

Podsumowania prowadzących:
- Łukasz Kałużny: Podkreśla, że pierwotnym i najważniejszym zastosowaniem Helma jest bycie package managerem do dystrybucji manifestów jako produktów.
- Szymon Warda: Zgadza się bez zastrzeżeń, że Helm jest świetny do dystrybucji produktów.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Helm jest przede wszystkim package managerem - to jego pierwotne i najważniejsze zastosowanie do dystrybucji manifestów jako produktów."
2. Szymon Warda: "Zgadzamy się bez dyskusji - Helm jest świetny do dystrybucji produktów."

## 5. Customize jako narzędzie wbudowane w kubectl

Podsumowanie: Łukasz wyjaśnia, że Customize powstał jako narzędzie wbudowane w kubectl, które pozwala na proste modyfikowanie manifestów bez dodatkowych narzędzi. Oba rozwiązania są równoprawnie wspierane w pipeline'ach CI/CD i narzędziach GitOps.

Podsumowania prowadzących:
- Łukasz Kałużny: Argumentuje, że Customize jest wbudowany w kubectl i pozwala na proste zmiany manifestów bez zewnętrznych zależności.
- Szymon Warda: Nie kwestionuje tego faktu i zgadza się z opisem funkcjonalności.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Customize powstał jako narzędzie wbudowane w kubectl, działające bez dodatkowych zależności."
2. Łukasz Kałużny: "Z perspektywy wsparcia w pipeline'ach CI/CD i narzędziach GitOps jak Argo, oba rozwiązania są traktowane równorzędnie."

## 6. Problem nadmiernej logiki w Helmie

Podsumowanie: Łukasz przedstawia główne problemy z używaniem Helma, szczególnie nadmierną logikę biznesową, skomplikowane instrukcje warunkowe i pisanie własnych funkcji w GO templates. Ostrzega przed tworzeniem złożonych drzew warunkowych i własnych reużywalnych funkcji.

Podsumowania prowadzących:
- Łukasz Kałużny: Krytykuje tendencję do umieszczania zbyt dużej ilości logiki biznesowej i warunkowej w Helmie, co prowadzi do trudnego w utrzymaniu kodu.
- Szymon Warda: Zgadza się, że ifologia jest zła, ale sugeruje alternatywne podejście przez jawne deklarowanie parametrów.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Ludzie umieszczają w Helmie nadmierną ilość logiki, próbując wpakować tam całą logikę biznesową aplikacji."
2. Łukasz Kałużny: "Programiści zaczynają tworzyć własne reużywalne funkcje, współdzielić je między chartami - i wtedy zaczyna się prawdziwe piekło."

## 7. Dobre praktyki w pisaniu Helma

Podsumowanie: Prowadzący dyskutują o właściwym podejściu do pisania chartów Helm. Zgadzają się, że parametry powinny być jawnie deklarowane, a logika powinna być ograniczona do minimum. Zamiast skomplikowanych ifów, należy stosować konwencje lub jawne parametry w values.

Podsumowania prowadzących:
- Łukasz Kałużny: Postuluje, że lukier składniowy nie powinien być stosowany do wewnętrznych rzeczy, a zamiast tego należy używać konwencji lub jawnych deklaracji.
- Szymon Warda: Zgadza się i dodaje, że można unikać ifologii przez jawne przekazywanie parametrów.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Parametry powinny być jawnie deklarowane - to podstawowa zasada, której ludzie często nie przestrzegają."
2. Szymon Warda: "Ifologia może występować, ale lepszym podejściem jest jawne definiowanie obszarów, które można rozszerzać."

## 8. Argument Szymona za Helmem - budowanie abstrakcji

Podsumowanie: Szymon przedstawia swój główny argument za Helmem, mówiąc że pozwala on zespołom na niezależne dostarczanie pakietów z własnymi abstrakcjami. Każdy zespół jest odpowiedzialny za dostarczenie działającego sposobu instalacji bez ingerencji w inne zespoły.

Podsumowania prowadzących:
- Szymon Warda: Argumentuje, że Helm pozwala na budowanie abstrakcji i jasne określenie odpowiedzialności zespołów za dostarczanie pakietów.
- Łukasz Kałużny: Kwestionuje ten argument, wskazując na problem z wersjonowaniem w Helmie.

Najciekawsze cytaty:
1. Szymon Warda: "Zespół ma jasną odpowiedzialność: dostarczyć pakiet i sposób instalacji. Nie interesuje mnie, jak to zrobicie - po prostu ma działać."
2. Szymon Warda: "Helm pozwala na jawne budowanie abstrakcji - zgodzisz się, że w tym jest naprawdę dobry."

## 9. Problem z wersjonowaniem w Helmie

Podsumowanie: Łukasz podnosi kwestię niewłaściwego używania wersjonowania w Helmie. Wyjaśnia różnicę między chart version (wersja manifestu) a app version (wersja aplikacji) i jak powinny być właściwie zarządzane.

Podsumowania prowadzących:
- Łukasz Kałużny: Wskazuje, że większość ludzi nie rozumie i nie stosuje poprawnie dwóch typów wersji w Helmie.
- Szymon Warda: Twierdzi, że w dużych projektach open source dobre praktyki już się przyjęły i są standardem.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Niewielu poprawnie stosuje wersjonowanie w Helmie, rozróżniając chart version i app version."
2. Szymon Warda: "Przeglądając repozytoria dużych projektów, widzę że dobre praktyki w Helmie już się przyjęły i stały się standardem."

## 10. Różnica perspektyw - produkty open source vs rzeczywistość

Podsumowanie: Łukasz wskazuje na różnicę między dużymi projektami open source, które Szymon obserwuje, a rzeczywistością w typowych firmach. Argumentuje, że dobre praktyki z wielkich projektów nie zawsze spływają do mniejszych organizacji.

Podsumowania prowadzących:
- Łukasz Kałużny: Podkreśla, że Szymon patrzy głównie na duże projekty open source, podczas gdy w typowych firmach praktyki są gorsze.
- Szymon Warda: Twierdzi, że dobre praktyki z projektów open source już spływają na rynek i są przyjmowane.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Patrzysz przede wszystkim na duże projekty open source - to ważne zastrzeżenie. Rzeczywistość w typowych firmach wygląda inaczej."
2. Szymon Warda: "Dawniej projekty open source miały chaos, z którego ludzie się uczyli. Teraz rynek się uporządkował i dobre praktyki są standardem."

## 11. Zastosowanie Helma dla produktów zewnętrznych

Podsumowanie: Prowadzący osiągają konsensus, że Helm jest idealny dla pakietów zewnętrznych, oprogramowania open source i produktów dystrybuowanych poza firmą. Zgadzają się, że narzędzia takie jak Prometheus, Argo czy Ingress powinny być instalowane przez Helm.

Podsumowania prowadzących:
- Łukasz Kałużny: Jednoznacznie stwierdza, że wszystkie pakiety zewnętrzne i produkty powinny używać Helma bez wyjątków.
- Szymon Warda: W pełni zgadza się z tym podejściem bez żadnych zastrzeżeń.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Wszystkie pakiety open source - Argo, Prometheus, Ingress - powinny być instalowane wyłącznie przez Helm. Tu nie ma dyskusji."
2. Szymon Warda: "Zgadzamy się w stu procentach - oczywiście, że tak."

## 12. Definicja produktu i kontrola nad infrastrukturą

Podsumowanie: Łukasz precyzuje swoją definicję produktu jako czegoś dystrybuowanego całkowicie poza firmą, gdzie nie ma kontroli nad infrastrukturą. To rozróżnienie jest kluczowe dla wyboru między Helmem a Customize dla aplikacji wewnętrznych.

Podsumowania prowadzących:
- Łukasz Kałużny: Definiuje produkt jako coś dystrybuowanego poza firmę bez żadnej kontroli nad infrastrukturą klienta.
- Szymon Warda: Kwestionuje tę definicję, pytając o wewnętrzne produkty zespołów.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Produkt to coś dystrybuowanego całkowicie poza firmę - bez jakiejkolwiek kontroli nad infrastrukturą i środowiskiem klienta."
2. Szymon Warda: "Jak definiujesz produkt? Czy zespół dostarczający swój system, zbiór mikroserwisów, też tworzy produkt?"

## 13. Zalety Customize - generatory ConfigMap i Secret

Podsumowanie: Łukasz przedstawia kluczowe zalety Customize, szczególnie generatory ConfigMap i Secret, które automatycznie generują hashe z zawartości i aktualizują referencje w deploymentach. To rozwiązuje problem z brakiem automatycznego redeploymentu przy zmianie tylko konfiguracji.

Podsumowania prowadzących:
- Łukasz Kałużny: Entuzjastycznie opisuje funkcjonalność generatorów, która automatycznie wyzwala rolling update przy zmianie konfiguracji.
- Szymon Warda: Zgadza się, że generatory są fajne, ale żartobliwie pyta o używanie Key Vault do secretów.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Generator wylicza hash z zawartości i dodaje go do nazwy obiektu. Jeśli w deployment odwołujesz się do ConfigMap, automatycznie podmieni nazwę z nowym hashem."
2. Łukasz Kałużny: "Zmiana samej ConfigMap automatycznie wywołuje rolling update - to eleganckie rozwiązanie problemu, który w czystym Kubernetes wymaga ręcznej interwencji."

## 14. Integracja SOPS z Customize

Podsumowanie: Prowadzący dyskutują o integracjі SOPS (Secrets OPerationS) z Customize jako sposobu zarządzania secretami. Obaj wyrażają niechęć do przechowywania secretów bezpośrednio w repozytoriach, ale doceniają rozwiązanie SOPS.

Podsumowania prowadzących:
- Łukasz Kałużny: Jest długoletnim fanem SOPS i podkreśla łatwość integracji z Customize, szczególnie w scenariuszach GitOps.
- Szymon Warda: Przyznaje, że SOPS jest dobrym rozwiązaniem, choć wcześniej nagrali odcinek o jego niechęci do secretów w ogóle.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Przypomnę, kto jest wieloletnim fanem SOPS? Integracja z Customize jest niezwykle prosta, szczególnie w kontekście GitOps."
2. Szymon Warda: "SOPS przejął rynek i sprawdził się bardzo dobrze w praktyce."

## 15. Problem z nadużywaniem overlay'ów w Customize

Podsumowanie: Szymon przedstawia swój główny zarzut wobec Customize - tendencję do tworzenia wielu poziomów overlay'ów (overlay na overlay na overlay), co prowadzi do nadmiernej architektury i trudności w utrzymaniu. Logika rozpraszana jest po różnych warstwach overlay'ów.

Podsumowania prowadzących:
- Szymon Warda: Krytykuje łatwość tworzenia zbyt wielu warstw overlay'ów, co prowadzi do chaosu i braku chęci do refaktoryzacji.
- Łukasz Kałużny: Zgadza się z problemem, ale proponuje restrykcyjne podejście - tylko base i jeden overlay per środowisko.

Najciekawsze cytaty:
1. Szymon Warda: "Największy problem z Customize to tendencja do nadmiernej architektury na poziomie overlay'ów - overlay na overlay na overlay, tworząc nieskończone warstwy abstrakcji."
2. Szymon Warda: "Logika serwisu jest rozproszona po różnych overlay'ach i nikt nie ma motywacji do migracji do głównego brancha, bo to rozwali konfiguracje wszystkim innym."

## 16. Zasada ograniczania overlay'ów w Customize

Podsumowanie: Łukasz proponuje surową zasadę dla Customize - tylko base i jeden overlay per środowisko, bez zagnieżdżania. Obaj prowadzący zgadzają się, że w każdym narzędziu można się "pociąć" przy niewłaściwym użyciu.

Podsumowania prowadzących:
- Łukasz Kałużny: Proponuje restrykcyjne podejście z maksymalnie jednym overlayem per środowisko, aby uniknąć chaosu.
- Szymon Warda: Zgadza się, że nadużywanie overlay'ów jest łatwe i prowadzi do problemów.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Moje podejście jest proste: deployujemy tylko jeden overlay na środowisko. Koniec, bez wyjątków."
2. Łukasz Kałużny: "Przy niewłaściwym użyciu każdego narzędzia można się poważnie skrzywdzić - tak samo z Helmem, jak i z Customize."

## 17. Kiedy używać Customize - konwencje i podobne serwisy

Podsumowanie: Szymon przedstawia scenariusz, w którym Customize sprawdza się dobrze - gdy mikroserwisy są podobne i stosują konwencje. W base można umieścić wspólny manifest, a overlay tylko podmienia image i secrety dla każdego serwisu.

Podsumowania prowadzących:
- Szymon Warda: Opisuje idealny przypadek użycia Customize dla podobnych mikroserwisów z konwencjami.
- Łukasz Kałużny: Sugeruje alternatywę - osobny manifest per serwis z wersjonowaniem.

Najciekawsze cytaty:
1. Szymon Warda: "Customize świetnie sprawdza się gdy mikroserwisy są podobne i stosujemy konwencje. W base definiujemy wspólny szablon, a overlay dla każdego serwisu tylko podmienia image i secrety."
2. Szymon Warda: "Siła Customize polega na łatwości tworzenia konwencji w base - potem overlay jest minimalny, tylko specyficzne dla serwisu wartości."

## 18. Kiedy używać Helma - niezależne zespoły

Podsumowanie: Szymon argumentuje, że gdy zespoły są niezależne i mogą się znacząco różnić w swoich potrzebach, Helm jest lepszym wyborem. Pozwala to na izolację odpowiedzialności i uniknięcie wzajemnego wpływu zespołów na siebie.

Podsumowania prowadzących:
- Szymon Warda: Silnie opowiada się za Helmem dla niezależnych zespołów, gdzie każdy musi sam ogarnąć swoją instalację.
- Łukasz Kałużny: Nie kwestionuje tego argumentu bezpośrednio, ale przechodzi do kolejnego problemu.

Najciekawsze cytaty:
1. Szymon Warda: "Gdy zespoły są niezależne i mogą się znacząco różnić w swoich potrzebach, wybór jest prosty - Helm."
2. Szymon Warda: "Jasne wymaganie: ma działać, kropka. Zespoły muszą się ogarnąć same, a przy tym nie mogą sobie nawzajem niczego zepsuć."

## 19. Antywzorzec - Master Helm dla całego środowiska

Podsumowanie: Łukasz ostrzega przed próbami tworzenia jednego "master" Helma z logiką warunkową, który instaluje całe środowisko. Taki chart staje się niemożliwy do utrzymania, szczególnie gdy twórca opuszcza projekt.

Podsumowania prowadzących:
- Łukasz Kałużny: Ostrzega przed tym antywzorcem, który widział wielokrotnie i zawsze kończy się problemami.
- Szymon Warda: Zgadza się, że można to zrobić przez dependencies, ale kwestionuje sensowność tego podejścia.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Próby tworzenia master charta Helm z logiką warunkową, który instaluje całe środowisko, zawsze kończą się katastrofą."
2. Łukasz Kałużny: "Gdy osoba, która stworzyła taki master chart, odchodzi z projektu, pozostali mogą tylko płakać nad niemożliwym do utrzymania kodem."

## 20. Logika warunkowa w produktach komercyjnych

Podsumowanie: Prowadzący zgadzają się, że w produktach komercyjnych dystrybuowanych do klientów logika warunkowa w Helmie jest niezbędna i uzasadniona. Przykłady to wybór między instalacją własnej bazy danych a używaniem zewnętrznej.

Podsumowania prowadzących:
- Łukasz Kałużny: Przedstawia realne przypadki użycia logiki warunkowej w produktach dla setek klientów.
- Szymon Warda: Zgadza się, ale podkreśla, że taka logika powinna być prosta i ograniczona.

Najciekawsze cytaty:
1. Łukasz Kałużny: "W produkcie komercyjnym logika warunkowa jest niezbędna - na przykład wybór między instalacją własnego Redisa a użyciem zewnętrznego z connection stringiem."
2. Szymon Warda: "Logiki warunkowej w takich przypadkach nie ma dużo - albo podajesz dependency, albo connection string. Albo instalujesz sam, albo używasz zewnętrznego."

## 21. Antywzorzec - pisanie funkcji w GO templates

Podsumowanie: Prowadzący zgadzają się, że pisanie własnych funkcji w GO templates w Helmie jest zdecydowanie złą praktyką. To znak, że coś poszło bardzo nie tak z architekturą rozwiązania.

Podsumowania prowadzących:
- Łukasz Kałużny: Ostrzega przed próbami "zbawienia problemów, których nie będzie" przez skomplikowane funkcje.
- Szymon Warda: Zgadza się, że obecność wielu funkcji GO w chartach jest czerwoną flagą.

Najciekawsze cytaty:
1. Szymon Warda: "Gdy widzimy chart z całym zbiorem funkcji GO generujących różne elementy, zgadzamy się - to już jest definitywnie złe rozwiązanie."
2. Łukasz Kałużny: "Widzieliśmy próby rozwiązywania przez skomplikowane funkcje problemów, które w rzeczywistości nigdy nie wystąpią."

## 22. Antywzorzec - Helm + Customize razem

Podsumowanie: Prowadzący dyskutują o praktykowaniu łączenia Helma z Customize - najpierw generowanie manifestów Helmem, a potem modyfikowanie ich Customizem. Obaj zgadzają się, że to jest bardzo zły pomysł, porównywalny do używania refleksji dla dostępu do prywatnych metod.

Podsumowania prowadzących:
- Łukasz Kałużny: Wspomina jedyny przypadek, gdy widział rekomendację takiego podejścia (Consul od Hashicorp) i uważa to za piekło.
- Szymon Warda: Kategorycznie odrzuca to podejście, porównując do anti-patternów w kodzie.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Widziałem tylko jedną rekomendację takiego podejścia - dla Consula od Hashicorp. To już jest absolutne piekło."
2. Szymon Warda: "To jak używanie refleksji do dostępu do prywatnych metod w kodzie - prosimy się o katastrofę, gdy coś się zmieni w wewnętrznej implementacji."

## 23. Hooki i testy w Helmie

Podsumowanie: Łukasz przedstawia system hooków w Helmie (9 różnych typów) i testów, które pozwalają na wykonywanie akcji w określonych momentach cyklu życia instalacji. Funkcjonalność ta jest dobra dla produktów, ale może być problematyczna dla aplikacji wewnętrznych.

Podsumowania prowadzących:
- Łukasz Kałużny: Opisuje różne typy hooków (pre/post install, upgrade, delete, rollback) i możliwość uruchamiania jobów Kubernetes.
- Szymon Warda: Wyraża niechęć do tej funkcjonalności, szczególnie w kontekście aplikacji, preferując logikę w CI/CD.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Helm oferuje dziewięć typów hooków: pre-install, post-install, pre-delete, post-delete, pre-upgrade, post-upgrade, pre-rollback, post-rollback i test."
2. Szymon Warda: "Mam niechęć do tej funkcjonalności, szczególnie dla aplikacji - nie infrastruktury. Taka logika powinna być w CI/CD, nie w narzędziu deploymentowym."

## 24. Kontrowersja - migracje bazy danych w hookach

Podsumowanie: Prowadzący ostro się nie zgadzają co do używania hooków do migracji schematów bazy danych. Łukasz widzi to jako konieczność w produktach, Szymon kategorycznie odrzuca to jako zbyt ryzykowne dla dużych baz danych produkcyjnych.

Podsumowania prowadzących:
- Łukasz Kałużny: Argumentuje, że w produktach to jedyna opcja, aby poprawnie zarządzać migracjami schematu.
- Szymon Warda: Stanowczo sprzeciwia się, twierdząc że kontrola nad bazą produkcyjną musi należeć do administratora, nie do Helma.

Najciekawsze cytaty:
1. Szymon Warda: "To wygląda fatalnie przy bazie 300 GB lub większej. Z całym szacunkiem - absolutnie nie. To funkcjonalność, która pięknie wygląda na prezentacji, ale nie sprawdza się w rzeczywistości."
2. Łukasz Kałużny: "Produkty komercyjne wykorzystują hooki do aktualizacji schematu podczas upgrade'u - uruchamiają skrypty migracyjne automatycznie."

## 25. Odpowiedzialność za migracje bazy danych

Podsumowanie: Szymon podkreśla, że migracja schematu bazy danych to odpowiedzialność osoby robiącej wdrożenie, nie automatycznego procesu. Łukasz ripostuje, że ludzie chcieliby to zautomatyzować, ale Szymon twierdzi, że ci którzy się wywalili już tak nie myślą.

Podsumowania prowadzących:
- Szymon Warda: Stanowczo stoi na stanowisku, że migracje to odpowiedzialność człowieka, nie automatu.
- Łukasz Kałużny: Wskazuje na ryzyko, że aplikacja zostanie zaktualizowana bez aktualizacji schematu.

Najciekawsze cytaty:
1. Szymon Warda: "Migracja schematu to odpowiedzialność osoby wykonującej wdrożenie. Doskonale wiesz, że przy większych zmianach nie można po prostu uruchomić skryptu i iść do domu."
2. Łukasz Kałużny: "Problem pojawia się, gdy aplikacja jest zaktualizowana, a schemat bazy pozostaje w starej wersji."

## 26. Podsumowanie preferencji Łukasza

Podsumowanie: Łukasz podsumowuje swoje preferencje - Helm dla zewnętrznych pakietów i produktów, Customize dla aplikacji wewnętrznych, z zastrzeżeniem że prosty Helm też jest akceptowalny jeśli zespół nie będzie się krzywdzić nadmiernym komplikowaniem.

Podsumowania prowadzących:
- Łukasz Kałużny: Jasno określa swoje preferencje z naciskiem na unikanie przekombinowania.
- Szymon Warda: Słucha podsumowania przed przedstawieniem swojego stanowiska.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Pakiety zewnętrzne i open source - Helm bez dyskusji. Dla aplikacji wewnętrznych preferuję Customize."
2. Łukasz Kałużny: "jestem przeciwnikiem nadmiernego komplikowania rozwiązań - to moja główna zasada."

## 27. Podsumowanie preferencji Szymona

Podsumowanie: Szymon podsumowuje swoje stanowisko za Helmem, podkreślając znaczenie niezależności zespołów i jasnego podziału odpowiedzialności. Zgadza się z Łukaszem co do niebezpieczeństwa nadmiernego komplikowania i potrzeby jasnych zasad wersjonowania.

Podsumowania prowadzących:
- Szymon Warda: Opowiada się za Helmem dla niezależnych zespołów, z prostymi zasadami i jasnymi obszarami rozszerzalności.
- Łukasz Kałużny: Słucha i przygotowuje się do żartu o Pulumi.

Najciekawsze cytaty:
1. Szymon Warda: "Gdy zespoły są niezależne, wybór jest oczywisty - Helm, prosty i przejrzysty."
2. Szymon Warda: "Kluczowe jest jasne ustalenie zasad wersjonowania - kiedy i jak wersjonujemy, aby było to zrozumiałe dla wszystkich i stosowane konsekwentnie."

## 28. Żart o Solid i Pulumi

Podsumowanie: Łukasz żartobliwie porównuje nadmiernie skomplikowany Helm do pisania kodu według zasad SOLID w C#, nawiązując do wcześniejszych kontrowersji wokół Pulumi. Szymon zgadza się, że to nie jest odpowiedni poziom abstrakcji.

Podsumowania prowadzących:
- Łukasz Kałużny: Żartuje, że Helm nie powinien być pisany jak kod aplikacyjny z zasadami SOLID.
- Szymon Warda: Zgadza się, że zasady jak SOLID i DRY nie są odpowiednie na tym poziomie.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Helm nie powinien wyglądać jak Pulumi - nie piszemy go według zasad SOLID jak w C#."
2. Szymon Warda: "Na tym poziomie nie powinno być nawet potrzeby myślenia o SOLID czy DRY - to nie ten poziom abstrakcji."

## 29. Helm 4.0 i wsparcie dla WebAssembly

Podsumowanie: Łukasz informuje o wydaniu Helma 4.0 z przeprojektowanym systemem pluginów wspierającym WebAssembly. Szymon reaguje z przerażeniem, obawiając się że to umożliwi jeszcze bardziej skomplikowane rozwiązania i gorsze prezentacje.

Podsumowania prowadzących:
- Łukasz Kałużny: Z rozbawieniem informuje o nowej funkcjonalności WebAssembly w Helmie 4.0.
- Szymon Warda: Wyraża obawy, że to doprowadzi do jeszcze gorszych praktyk i nadmiernie skomplikowanych rozwiązań.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Helm 4.0 wprowadza przeprojektowany system pluginów z wsparciem dla WebAssembly."
2. Szymon Warda: "O Boże, teraz będzie można pisać jeszcze bardziej skomplikowane funkcje. To nie jest dobry kierunek rozwoju."

## 30. Zakończenie i żartobliwa wymiana

Podsumowanie: Na zakończenie prowadzący żartują, że z WebAssembly można by uruchomić Postgresa w ramach Helma. Łukasz sugeruje, że Szymon może się jeszcze przeprosić z Customizem, gdy ktoś go skrzywdzi Helmem. Odcinek kończy się wesołą nutą.

Podsumowania prowadzących:
- Łukasz Kałużny: Żartuje o możliwości uruchomienia Postgresa przez WebAssembly i przewiduje, że Szymon zmieni zdanie.
- Szymon Warda: Upiera się przy swoim zdaniu, odrzucając JSON patche w Customize, ale dopuszcza możliwość overlay'ów.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Z WebAssembly będzie można uruchomić Postgresa bezpośrednio w Helmie."
2. Szymon Warda: "Boję się tych nadchodzących prezentacji, szczerze mówiąc."
