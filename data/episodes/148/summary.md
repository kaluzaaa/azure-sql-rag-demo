## 1. Wstęp i szkolenia
Summary: Prowadzący rozpoczynają odcinek Patoarchitektów i zachęcają słuchaczy do zapoznania się z ich szkoleniami, które cieszą się bardzo dobrymi opiniami.

Speaker summaries:
- Szymon Warda: Rozpoczyna odcinek nietypowym powitaniem i zachęca słuchaczy do zapoznania się z ofertą szkoleń.
- Łukasz Kałużny: Potwierdza wysoką jakość szkoleń i wskazuje, że są one dostępne na różne tematy.

Most interesting quotes:
1. Szymon Warda: "Cześć, czołem, kluski z rosołem! Słuchacie Patoarchitektów."
2. Łukasz Kałużny: "Nasze szkolenia otwarte, które mają pozytywne opinie, są dostępne na różnorodne tematy."
3. Szymon Warda: "Łukasz, mają bardzo dobre opinie."

## 2. Kubescape - narzędzie do zabezpieczania Kubernetesa
Summary: Prowadzący omawiają Kubescape, narzędzie do zabezpieczania i monitorowania Kubernetesa, które wychodzi z Sandboxa i wchodzi w Incubation w CNCF. Narzędzie wspiera różne frameworki bezpieczeństwa, wykorzystuje eBPF do monitorowania aktywności i zdobywa coraz większą popularność.

Speaker summaries:
- Szymon Warda: Przedstawia Kubescape jako dojrzałe narzędzie wspierające różne frameworki bezpieczeństwa, które wykorzystuje eBPF do monitorowania aktywności w klastrze.
- Łukasz Kałużny: Zauważa, że Kubescape może być dobrą alternatywą dla droższych rozwiązań komercyjnych, choć kluczowym wyzwaniem pozostaje to, czy ktoś będzie faktycznie analizował dane z narzędzia.

Most interesting quotes:
1. Szymon Warda: "Wspiera NSA-CISA, Kubernetes Hardening Guidance, MITRE ATT&CK, Soca2, CIS benchmarks właśnie w kontekście odpowiedniego funkcjonowania."
2. Łukasz Kałużny: "Patrząc na Kubescape'a, jego funkcjonalności i dojrzałość, o której wspominasz, mogę powoli stwierdzić, że jeśli nie chcesz kupować dużego pakietu od Palo Alto czy Aqua Security, warto włączyć Kubescape'a."
3. Łukasz Kałużny: "Nieważne ile zapłacisz za narzędzie, problemem jest to, czy ktokolwiek będzie na nie reagował."

## 3. Co się stanie, gdy region cloudowy zostanie zniszczony?
Summary: Prowadzący omawiają artykuł Aidana Finna dotyczący przygotowania na sytuację, w której region chmurowy zostałby zniszczony. Podkreślają, że dostawcy chmury nie zapewniają automatycznego disaster recovery i konieczne jest własne przygotowanie strategii.

Speaker summaries:
- Łukasz Kałużny: Przedstawia artykuł Aidana Finna, który analizuje, co się stanie, jeśli region chmurowy zostanie zniszczony i jak się do tego przygotować.
- Szymon Warda: Zwraca uwagę na problem rozjazdu czasów synchronizacji danych między regionami i wynikające z tego konsekwencje dla automatycznego przełączania.

Most interesting quotes:
1. Łukasz Kałużny: "Microsoft, w tym wypadku Azure'a, nie zrobi za Ciebie Disaster Recovery domyślnie."
2. Szymon Warda: "Jeśli masz region z replikacją asynchroniczną, to nie ma automatycznego przełączania. Masz 15 minut opóźnienia, więc nie możesz tego zrobić, utracisz dane."
3. Łukasz Kałużny: "Gdzie tylko to możliwe, compute powinien być bezstanowy i łatwy do odbudowania w domyśle, IaC."

## 4. OpenSearch kontra Elastic w wyszukiwaniu wektorowym
Summary: Prowadzący dyskutują o raporcie pokazującym, że OpenSearch wyprzedza Elastica w wyszukiwaniu wektorowym. Mimo że wyniki testów mogą być zmanipulowane, cieszy ich fakt, że OpenSearch staje się realną alternatywą dla Elastica.

Speaker summaries:
- Szymon Warda: Cieszy się, że OpenSearch staje się realną alternatywą dla Elastica, choć zaznacza, że wyniki testów mogą być zmanipulowane.
- Łukasz Kałużny: Analizuje metodologię testów i zauważa, że różnice w algorytmach mogły wpłynąć na wyniki.

Most interesting quotes:
1. Szymon Warda: "Znalazłem raport o tym, jak OpenSearch przewyższa Elastica w kontekście wyszukiwania wektorowego."
2. Szymon Warda: "Ustalmy, każdy test można tak skonstruować, aby uzyskać pożądany wynik. Nie skupiajmy się więc na tym, kto jest szybszy."
3. Szymon Warda: "Dobrze, że OpenSearch wychodzi z cienia i tam, gdzie potrzebujemy wyszukiwania pełnotekstowego, możemy rozważyć alternatywę dla Elastica."

## 5. OpenAI i propozycja planu działania dla USA
Summary: Prowadzący omawiają propozycję OpenAI dla USA dotyczącą regulacji sztucznej inteligencji, która sugeruje ograniczenie praw autorskich i swobodny dostęp do danych. Komentują, że propozycja służy interesom amerykańskich firm technologicznych.

Speaker summaries:
- Łukasz Kałużny: Krytycznie odnosi się do propozycji OpenAI, cytując fragment, który mówi o "wolności inteligencji".
- Szymon Warda: Przytacza przykład historii praw autorskich Myszki Miki, wskazując na podwójne standardy w amerykańskiej polityce handlowej.

Most interesting quotes:
1. Łukasz Kałużny: "Streszczając ten dokument, niektórzy pięknie to ujęli: odwalcie się od danych, które zgromadziliśmy i skończmy z prawami autorskimi."
2. Łukasz Kałużny: "Jest imponujący fragment: 'but we must ensure that people have freedom of intelligence, by which we mean the freedom to access and benefit from AI.'"
3. Szymon Warda: "Dokładnie była chroniona 50 lat i to było wymuszane przez umowy handlowe, że skoro handlujecie z nami, to respektujecie, żeby Myszka Miki była chroniona u was przez 50 lat."

## 6. Grafana Loki 3.4 i koniec Promtaila
Summary: Prowadzący informują o wydaniu Grafana Loki 3.4, która wprowadza wsparcie dla Thanos Object Storage. Ważną informacją jest planowane wygaszenie Promtaila, który zostanie zastąpiony przez Grafana Alloy.

Speaker summaries:
- Szymon Warda: Informuje o nowej wersji Grafana Loki i planach wygaszenia Promtaila, sugerując użytkownikom przygotowanie planu migracyjnego.
- Łukasz Kałużny: Zwraca uwagę na nowy przewodnik dotyczący wymiarowania (Sizing Guide), który pokazuje skalę obsługiwanych danych.

Most interesting quotes:
1. Szymon Warda: "Promtail wchodzi do Grafany Alloy i ma już określony czas wygaszenia do 13 lutego 2025, czyli będzie objęty długoterminowym wsparciem. Ale od 2 marca 2026 nie będzie już dalszego wsparcia."
2. Łukasz Kałużny: "Do trzech terabajtów logów dziennie, to jest bardzo istotna informacja."
3. Łukasz Kałużny: "Na 10 terabajtów RAM-u potrzebujesz 38 rdzeni, 71 GB RAM-u na 100 terabajtów logów miesięcznie."

## 7. Stan Infrastructure-as-Code w 2024 roku
Summary: Prowadzący omawiają raport o stanie Infrastructure-as-Code (IaC) w 2024 roku. Zwracają uwagę, że mimo popularności IaC, wiele organizacji nadal ręcznie konfiguruje infrastrukturę, a wyzwaniem pozostaje bezpieczeństwo i zarządzanie zmianami.

Speaker summaries:
- Łukasz Kałużny: Analizuje raport o stanie IaC, zwracając uwagę na to, że mimo popularności, wiele organizacji nadal ręcznie konfiguruje infrastrukturę.
- Szymon Warda: Podkreśla, że developerzy często nie myślą o sieciówce i bezpieczeństwie, co stanowi wyzwanie dla wdrażania IaC.

Most interesting quotes:
1. Łukasz Kałużny: "72% ankietowanych organizacji używa IaC-a, czyli 3/4. I to jest realne, gdy spojrzysz na rynek. Ale tylko 1/3 jest na tyle pewna, że posiada 3/4 obciążeń zautomatyzowanych."
2. Szymon Warda: "Developerzy nie myślą o sieciówce, o bezpieczeństwie, o bardzo wielu innych rzeczach. I to nie jest zarzut, po prostu to jest sposób myślenia."
3. Łukasz Kałużny: "Pipeline'y stają się normą, ale około 30% nadal ręcznie uruchamia Terraforma."

## 8. Krytyka .NET Aspire
Summary: Prowadzący krytykują podejście Davida Fowlera, jednego z architektów .NET, do tworzenia .NET Aspire. Zwracają uwagę na nierealistyczne założenia dotyczące uprawnień aplikacji w chmurze.

Speaker summaries:
- Łukasz Kałużny: Krytykuje założenia .NET Aspire, szczególnie pomysł, że aplikacja będzie miała uprawnienia do nadawania sobie uprawnień w chmurze.
- Szymon Warda: Zgadza się z krytyką, zauważając, że takie podejście jest nierealistyczne i rzadko potrzebne.

Most interesting quotes:
1. Łukasz Kałużny: "Aspire ma z założenia też zrobić autoprovisioning aplikacji. I tu jest np. wyobrażenie właśnie developera, że aplikacja będzie miała uprawnienia do nadawania uprawnień."
2. Szymon Warda: "Załóżmy, że aplikacja musi rzeczywiście stworzyć jakieś zasoby magazynowe, to może się zdarzyć. Ale to są promile przypadków użycia ogólnie rzecz biorąc, to nie powinno mieć miejsca."
3. Łukasz Kałużny: "Nie potrzebujesz... Inaczej, masz od tego SDK i jeżeli już dotarłeś do tego etapu, poradzisz sobie."

## 9. Przedwczesna optymalizacja - pułapki i podejście
Summary: Prowadzący omawiają artykuł o przedwczesnej optymalizacji, który porządkuje podejście do tego tematu poprzez 3T: things (rzeczy), time (czas) i trade-offs (kompromisy). Podkreślają, że często optymalizujemy niewłaściwe rzeczy lub nie uwzględniamy wszystkich kosztów optymalizacji.

Speaker summaries:
- Szymon Warda: Dzieli się doświadczeniami z walki o powstrzymanie nieuzasadnionych optymalizacji i omawia podejście 3T z artykułu.
- Łukasz Kałużny: Nawiązuje do problemu optymalizacji w kontekście AI, gdzie czasem poświęcamy więcej czasu na automatyzację niż wynosi oszczędność.

Most interesting quotes:
1. Szymon Warda: "Ilość przypadków, kiedy walczyłem w organizacjach o to, żeby czegoś nie optymalizować, jest fascynująca. Często wygląda to tak, jakby ktoś wskazywał mokrym palcem kierunek: w lewo idziemy, albo to trzeba zoptymalizować."
2. Szymon Warda: "To jest ten słynny tekst Donalda Knutha: 'Premature optimization is the root of all evil.'"
3. Szymon Warda: "Zysk z optymalizacji względem ilości czasu, jaki w to zainwestujemy. Fajnie, że będzie szybciej, pewnie będzie szybciej, tylko kiedy nam się to zwróci."

## 10. Wzorce anty-managerskie
Summary: Prowadzący omawiają artykuł o wzorcach anty-managerskich, który opisuje różne typy problematycznych managerów oraz sposoby radzenia sobie z nimi. Artykuł zawiera również wskazówki, co robić, gdy pracuje się dla takiego managera, gdy taki manager raportuje do nas lub gdy sami jesteśmy takim managerem.

Speaker summaries:
- Łukasz Kałużny: Prezentuje artykuł o różnych typach problematycznych managerów, zwracając uwagę na tech lead managera.
- Szymon Warda: Zauważa, że każdy manager prawdopodobnie ma cechy któregoś z opisanych typów, i docenia wartość artykułu jako narzędzia do rozwoju umiejętności miękkich.

Most interesting quotes:
1. Łukasz Kałużny: "Najważniejszy jest chyba w IT ten ostatni - tech lead manager."
2. Szymon Warda: "To jest ważne, najlepszy developer, żeby był managerem. Czyli osoba, która najlepiej koduje, niech teraz zarządza ludźmi."
3. Łukasz Kałużny: "Są trzy scenariusze, czyli jak naprawić sytuację, kiedy pracujesz dla takiego managera, gdy taki manager raportuje do Ciebie albo gdy odkryjesz, że sam jesteś tym typem menadżera."

## 11. Bezpieczeństwo aplikacji - test OWASP Top Ten
Summary: Prowadzący omawiają raport, według którego 52% aplikacji przechodzi pomyślnie test OWASP Top Ten, co stanowi wzrost z wcześniejszych 32%. Przypominają o znaczeniu podstawowego bezpieczeństwa aplikacji mimo nowych trendów technologicznych.

Speaker summaries:
- Szymon Warda: Przedstawia raport o wzroście liczby aplikacji przechodzących test OWASP Top Ten i przypomina o znaczeniu podstawowego bezpieczeństwa aplikacji.
- Łukasz Kałużny: Nie komentuje bezpośrednio tematu, ale zgadza się z jego ważnością.

Most interesting quotes:
1. Szymon Warda: "Mamy wielki postęp, bo już teraz całe 52% aplikacji przechodzi pomyślnie test OWASP Top Ten."
2. Szymon Warda: "Mimo całego szumu wokół AI, Kubernetes i innych nowinek technologicznych, bezpieczeństwo aplikacji jest nadal kluczowe."
3. Szymon Warda: "Zerknijcie na OWASP Top Ten i sprawdźcie, w których procentach się mieścicie."

## 12. Multi-node cluster w Docker Desktop
Summary: Prowadzący omawiają funkcję Docker Desktop, która pozwala na lokalne uruchomienie wielowęzłowego klastra Kubernetes. Ta funkcja, bazująca na narzędziu Kind, umożliwia symulowanie działania klastra na jednej maszynie.

Speaker summaries:
- Łukasz Kałużny: Prezentuje funkcję Docker Desktop umożliwiającą uruchomienie wielowęzłowego klastra Kubernetes lokalnie i wyjaśnia, że bazuje ona na narzędziu Kind.
- Szymon Warda: Zauważa, że funkcja pozwala na utworzenie do 10 węzłów na jednej maszynie, bez potrzeby angażowania innych komputerów.

Most interesting quotes:
1. Łukasz Kałużny: "Można lokalnie uruchomić klaster wielowęzłowy. Twój Docker po wykonaniu polecenia kubectl get nodes nie pokaże już jednego węzła, ale określoną liczbę węzłów, którą skonfigurujesz."
2. Szymon Warda: "To jest ważne, to działa na jednej maszynie. Nie musimy włączać do tego komputera kolegi."
3. Łukasz Kałużny: "Jest narzędzie w ramach Kubernetesa, które nazywa się Kind. Pozwala ono postawić węzły i klaster kubernetesowy w kontenerach."
