## 1. Historia konteneryzacji - początki
Summary: Omówienie początków konteneryzacji, od wprowadzenia chroota w Unixie w 1979 roku, przez FreeBSD Jail w 2000 roku, aż po namespace'y w kernelu Linuxa i Solaris Container Zones.

Speaker summaries:
- Łukasz Kałużny: Przedstawia chronologiczny rozwój technologii konteneryzacji, podkreślając znaczenie chroota jako pierwszego narzędzia do izolacji.
- Szymon Warda: Koncentruje się na rozwoju technologii izolacji w kontekście hostingu i potrzeb ekonomicznych.

Most interesting quotes:
1. Łukasz Kałużny: "Cała branża IT opiera się na wieloletnich koncepcjach, które są jedynie odświeżane i wykorzystywane do budowania nowych rozwiązań."
2. Szymon Warda: "FreeBSD Jail rozszerza funkcjonalność, dodając nie tylko izolację systemu plików, ale także izolację procesów, sieci i użytkowników."

## 2. Rozwój technologii kontenerowej i powstanie Dockera
Summary: Omówienie przełomowego momentu w historii konteneryzacji - powstania Dockera w 2013 roku oraz późniejszej standaryzacji technologii kontenerowej poprzez CNCF i OCI.

Speaker summaries:
- Łukasz Kałużny: Wyjaśnia, jak Docker uprościł zarządzanie kontenerami poprzez przyjazne API i narzędzia CLI.
- Szymon Warda: Podkreśla znaczenie standaryzacji i uniezależnienia się od konkretnych implementacji.

Most interesting quotes:
1. Łukasz Kałużny: "Docker nie wprowadził nowych rozwiązań, ale zapewnił przyjazny interfejs wiersza poleceń i API, początkowo bazując na LXC."
2. Szymon Warda: "Funkcjonalność Dockera przewyższała wszystko, co powstało wcześniej, co przyczyniło się do jego niezwykłego sukcesu."

## 3. Architektura i działanie kontenerów
Summary: Szczegółowe wyjaśnienie procesu uruchamiania kontenera, od polecenia docker run, przez ContainerD, aż po runc i interakcje z kernelem.

Speaker summaries:
- Łukasz Kałużny: Opisuje techniczne aspekty działania ContainerD i proces przygotowania środowiska kontenera.
- Szymon Warda: Wyjaśnia rolę poszczególnych komponentów w procesie uruchamiania kontenera.

Most interesting quotes:
1. Szymon Warda: "Interfejs wiersza poleceń przekazuje polecenie do demona, który wykonuje całą pracę."
2. Łukasz Kałużny: "ContainerD shim pełni rolę interfejsu pośredniczącego między procesem kontenera a ContainerD."

## 4. Budowanie obrazów kontenerów
Summary: Wyjaśnienie procesu budowania obrazów kontenerów, ich warstwowej struktury oraz działania systemu repozytoriów.

Speaker summaries:
- Łukasz Kałużny: Tłumaczy techniczne aspekty budowania obrazów i działanie warstw.
- Szymon Warda: Koncentruje się na praktycznych aspektach budowania i optymalizacji obrazów.

Most interesting quotes:
1. Łukasz Kałużny: "Każde polecenie jest wykonywane w osobnym, tymczasowym kontenerze."
2. Szymon Warda: "Przechowywanie wersji z narzędziami do debugowania w obrazach produkcyjnych nie jest zalecane."
