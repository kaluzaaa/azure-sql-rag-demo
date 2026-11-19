## 1. Wprowadzenie do observability i open telemetry
Summary: Dyskusja rozpoczyna się od wyjaśnienia podstawowych pojęć observability oraz open telemetry. Observability to ewolucja od tradycyjnego monitoringu, pozwalająca zrozumieć, co dzieje się wewnątrz aplikacji, podczas gdy open telemetry to dojrzały standard do raportowania danych z serwisów.
Speaker summaries:
- Szymon Warda: Wyjaśnia różnicę między monitoringiem a observability, podkreślając że observability pozwala zobaczyć co się dzieje wewnątrz aplikacji.
- Łukasz Kałużny: Pyta o podstawowe pojęcia i prowadzi rozmowę w kierunku zrozumienia fundamentów observability.
Most interesting quotes:
1. Szymon Warda: "Observability to dążenie do zrozumienia, dlaczego coś nie działa."
2. Szymon Warda: "Open telemetry to już dojrzały standard - wersja 1.0 została wydana."
3. Szymon Warda: "Jeśli wczoraj działało, a dzisiaj nie działa, to coś się musiało zmienić."

## 2. Trzy filary observability
Summary: Omówienie trzech głównych składników observability: logów, metryk i trace'ów. Logi to tekst często w formie strukturalnej, metryki to wartości liczbowe opisujące zachowanie systemu, a trace'y pozwalają śledzić przepływ między serwisami.
Speaker summaries:
- Szymon Warda: Szczegółowo opisuje każdy z trzech filarów, koncentrując się na ich praktycznym zastosowaniu i wartości biznesowej.
- Łukasz Kałużny: Dopytuje o szczegóły i wprowadza kolejne tematy związane z architekturą open telemetry.
Most interesting quotes:
1. Szymon Warda: "Logów się nie pozbędziemy - nie oszukujmy się."
2. Szymon Warda: "Trace'y to sposób śledzenia przepływu między serwisami, co jest krytyczne i fenomenalne."

## 3. Architektura open telemetry
Summary: Przedstawienie architektury open telemetry składającej się z aplikacji, SDK, kolektora i eksporterów. Kolektor pełni kluczową rolę w buforowaniu, wzbogacaniu i przekierowywaniu danych do różnych konsumentów.
Speaker summaries:
- Szymon Warda: Tłumaczy jak działa architektura open telemetry, podkreślając rolę kolektora w średnich i większych systemach.
- Łukasz Kałużny: Upraszcza architekturę do kluczowych elementów: aplikacja, SDK, kolektor, eksporter.
Most interesting quotes:
1. Szymon Warda: "W każdym średnim i większym systemie wdrażamy kolektora."
2. Szymon Warda: "Możemy wstawić nowy kolektor open telemetry, a przez pewien czas raportować dane do starego systemu."

## 4. Zalety open telemetry w porównaniu do komercyjnych APM
Summary: Dyskusja o korzyściach płynących z adopcji open telemetry w porównaniu do komercyjnych rozwiązań APM. Główne zalety to przenośność, kontrola kosztów, standardowość i lepsze zarządzanie danymi.
Speaker summaries:
- Szymon Warda: Argumentuje za open telemetry, wskazując na korzyści finansowe i techniczne oraz przyszłościowość rozwiązania.
- Łukasz Kałużny: Kwestionuje sens przesiadania się z działających rozwiązań APM na open telemetry.
Most interesting quotes:
1. Szymon Warda: "To jest przyszłość bez dwóch zdań - cały rynek idzie w tym kierunku."
2. Szymon Warda: "Cenniki dużych APM-ów to niemałe koszty."
3. Szymon Warda: "To są standardy rynkowe - dostawcy chmurowi przechodzą na przykład na Prometheus."

## 5. Dojrzałość implementacji w różnych językach programowania
Summary: Przegląd dojrzałości implementacji open telemetry w różnych językach programowania. Java i .NET prowadzą pod względem stabilności, Node.js i Python mają solidne wsparcie, podczas gdy Go i Rust pozostają w tyle.
Speaker summaries:
- Szymon Warda: Szczegółowo omawia stan implementacji w różnych językach, wskazując na mocne i słabe strony każdego z nich.
- Łukasz Kałużny: Komentuje stan implementacji w Go, wyrażając zdziwienie słabym wsparciem.
Most interesting quotes:
1. Szymon Warda: "Java ma chyba najlepszą dojrzałość, choć nie w każdym obszarze."
2. Łukasz Kałużny: "Go wydawało się, że powinno być rock solid."

## 6. Wsparcie dla aplikacji frontendowych
Summary: Omówienie możliwości śledzenia aplikacji frontendowych przez open telemetry, w tym możliwość raportowania danych pod własną domeną, co zmniejsza ryzyko blokowania przez adblockers.
Speaker summaries:
- Szymon Warda: Wyjaśnia jak działa śledzenie po stronie przeglądarki i jakie daje to korzyści w porównaniu do tradycyjnych APM.
- Łukasz Kałużny: Potwierdza wartość śledzenia transakcji od frontendu do backendu.
Most interesting quotes:
1. Szymon Warda: "Możemy raportować dane telemetryczne do naszego endpointu pod własną domeną, zmniejszając ryzyko blokowania przez adblockers."

## 7. Stos technologiczny open source dla observability
Summary: Przedstawienie kompletnego stosu open source składającego się z Grafany jako frontendu, Prometeusza dla metryk, Loki dla logów i Tempo dla trace'ów. Omówienie zalet i ograniczeń każdego komponentu.
Speaker summaries:
- Szymon Warda: Szczegółowo opisuje każdy element stosu, wskazując na ich mocne strony i ograniczenia, szczególnie Tempo.
- Łukasz Kałużny: Dopytuje o szczegóły techniczne i porównuje możliwości z komercyjnymi rozwiązaniami.
Most interesting quotes:
1. Szymon Warda: "Składnia Elasticsearch do wyszukiwania jest prosta - można postawić tam juniora i będzie z tego dobrze korzystać."
2. Szymon Warda: "Loki nie działa zbyt dobrze - trochę działają, ale kulawą."
3. Szymon Warda: "Tempo obsługuje tylko trasy - nie ma raportowania ani agregacji."

## 8. Przechowywanie i zarządzanie danymi
Summary: Dyskusja o przechowywaniu danych w systemach open source, wykorzystaniu blob storage i korzyściach płynących z takiego podejścia, szczególnie w środowiskach chmurowych.
Speaker summaries:
- Szymon Warda: Tłumaczy jak działa przechowywanie danych w blob storage i jakie daje to korzyści kosztowe.
- Łukasz Kałużny: Dodaje praktyczne uwagi o wykorzystaniu istniejących licencji storage'u z API S3.
Most interesting quotes:
1. Szymon Warda: "Dane są dzielone, archiwizowane i przechowywane głównie w blob storage."
2. Łukasz Kałużny: "Klienci często mają już licencje do storage'u z API S3."

## 9. Proces adopcji open telemetry
Summary: Szczegółowy opis procesu wdrażania open telemetry w organizacji, od wyboru środowiska począwszy, przez konfigurację, aż po szkolenia zespołów. Proces jest stopniowy i nie wymaga wielkiej rewolucji.
Speaker summaries:
- Szymon Warda: Opisuje praktyczny proces wdrażania, podkreślając znaczenie Kubernetes i stopniowego podejścia do migracji.
- Łukasz Kałużny: Dopytuje o czas trwania procesu i praktyczne aspekty wdrożenia.
Most interesting quotes:
1. Szymon Warda: "Nie robimy rewolucyjnego przejścia na nowy system."
2. Szymon Warda: "Mówimy o godzinach na system - po pierwszym wdrożeniu tworzymy prostą wewnętrzną bibliotekę."
3. Szymon Warda: "Całe rozwiązanie wdrażamy w maksymalnie 3 miesiące."

## 10. Docelowi odbiorcy open telemetry
Summary: Określenie grup organizacji, które najwięcej zyskują na wdrożeniu open telemetry - duże organizacje z aktywnymi zespołami deweloperskimi, systemy w aktywnym rozwoju oraz firmy chcące ujednolicić swój stos technologiczny.
Speaker summaries:
- Szymon Warda: Identyfikuje duże organizacje jako głównych beneficjentów, przestrzegając przed wdrożeniem w małych firmach lub przy starych systemach.
- Łukasz Kałużny: Podsumowuje kluczowe kryteria decyzyjne, szczególnie aktywny development jako wyznacznik.
Most interesting quotes:
1. Szymon Warda: "Największą wartość mają duże organizacje, które mogą narzucić standard wszystkim dostawcom swojego oprogramowania."
2. Łukasz Kałużny: "Aktywny development to główny wyznacznik zainteresowania open telemetry."
3. Szymon Warda: "To zabezpieczenie aplikacji na najbliższe 2-5 lat."
