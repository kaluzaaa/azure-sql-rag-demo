# 173.mp3

[00:00:00.050] **Łukasz Kałużny:** Dawanie tego ludziom to jak dawanie dziecku brzytwy, żeby pobiegało sobie po placu zabaw.

[00:00:05.480] **Szymon Warda:** Tylko to jest takie podejście na zasadzie, że jak damy, to ktoś popsuje. Oczywiście, że popsuje. Widzieliśmy przykład Customize'a, z którym ja walczyłem i zgodzisz się, że tam też było nadziergane jak tylko można było.

[00:00:17.600] **Łukasz Kałużny:** Jeszcze dodam jedną straszną rzecz, którą kurde ileś razy widziałem i zawsze widzę ją z problemami, to jeżeli ktoś próbuje zrobić Master Helma, który zainstaluje całe środowisko z logiką warunkową.

[00:00:28.790] **Szymon Warda:** I potem prowadzi do tego, że całą logikę jakby na serwis mamy gdzie? Mamy tam nadpisywaną, a potem w sumie nikomu nie zależy na tym, żeby to przemigrować do głównego, bo rozwali wszystkim innym. Cześć. Słuchacie, o dziwo, Patoarchitektów. Prowadzą Szymon Warda...

[00:00:55.520] **Łukasz Kałużny:** I Łukasz Kałużny. Wszystkie linki do tego odcinka na Patoarchitekci.io albo tutaj na dole. Nie po boku, nie po prawo, góra, tylko na dole.

[00:01:04.590] **Szymon Warda:** Dobrze Łukaszu, to co tam dzisiaj?

[00:01:07.770] **Łukasz Kałużny:** Przypomnijmy szkolenia, bo znalazły się już na stronie, bo dużo z Was płakało, marudziło albo było niezadowolonych z tym, że proces wydawania budżetów szkoleniowych w firmie jest długi, więc wrzuciliśmy już terminy szkoleń na początek przyszłego roku, różnych. Z moich jest jedno nowe, to taki sneak peak, Agentic AI the Hard Way, czyli napisz agenta od zera, bez żadnego frameworku, bez żadnego Lang Chaina. A na 16 grudnia zostały też miejsca na Kubernetes The Hard Way. Szczegóły możecie znaleźć sobie na stronie. Dobra, a jak jesteśmy przy hard wayu, to dzisiaj rzecz, po której ja się z Tobą totalnie nie zgadzam, bo dawanie tego ludziom to jak dawanie dziecku brzytwy, żeby pobiegało sobie po placu zabaw, czyli Helm versus Customize. Czyli odwieczny problem czego powinniśmy użyć do templatingu, przygotowywania deploymentów na Kubernetesa, bo tak to można określić.

[00:02:10.210] **Szymon Warda:** Dobrze, to może małe wprowadzenie co jest czym. Customize umożliwia nam zmiany yamla mówiąc bardzo prosto i modyfikację przez tam wiele poziomów. Mamy bazowy obraz i go tam modyfikujemy różnymi overlay'ami.

[00:02:23.050] **Łukasz Kałużny:** Raczej trzeba powiedzieć po prostu robimy... Inaczej, robimy patche, można tak to określać, patchujemy, robimy nakładkę, nakładki na czyste yamle, czyli nazywamy to overlay'em. Czyli to są nakładki, czyli bierzemy i robimy nakładki.

[00:02:40.420] **Szymon Warda:** Czyli modyfikujemy to, mówiąc bardzo prosto.

[00:02:40.870] **Łukasz Kałużny:** Tak, w prosty sposób.

[00:02:43.210] **Szymon Warda:** Z tym prostym... Modyfikujemy go, z tym się możemy zgodzić. Dobrze, teraz Helm. Helm natomiast jest takim enginem template'owym do Yamla. Czyli generalnie mamy Yamla, a tam elementami mamy jakieś while, ify i tak dalej. I na koniec tego Yamla wygenerujemy i całość przedstawiamy jako paczkę i masz, instaluj sobie i jasno określamy, które wartości można rozszerzać.

[00:03:04.930] **Łukasz Kałużny:** Dobra i teraz jak sobie popatrzymy, najważniejsza dla mnie różnica jest taka i to co powiem to jest w kontekście tego, co oglądam na rynku. Bo ja Helmem nie gardzę, gardzę sposobem użycia i to jest bardzo istotna różnica.

[00:03:20.830] **Szymon Warda:** Już się nie broń.

[00:03:21.370] **Łukasz Kałużny:** Poczekaj, zaraz do tego przejdziemy. Dobra i Helm pierwotnie, to też jest bardzo ważne, jest package managerem. I tego jego pierwsze takie przeznaczenie, takie bardzo szerokie, to jest Packet Manager i mamy coś, co nazywamy Artifact Hub, na którym znajdziemy różne rzeczy do instalacji jako paczki na Kubernetes. Weźmy owianego sławą Prometheusza jakieś operatory. Third party softy teraz przychodzą enterpriseowe w postaci helma, więc jest tego, jest to sposób dystrybucji manifestu do Kubernetesa, żeby zrobić produkt do instalacji.

[00:03:57.150] **Szymon Warda:** Tu się zgodzimy, Helm jest świetny do dystrybucji produktów.

[00:04:01.140] **Łukasz Kałużny:** Tak, i to jest jedna rzecz. A Customize powstał po to, żeby bez narzędzi, bo jest wbudowany w kubectl'a, już w tym momencie w pełnej kompatybilnej wersji. Więc Szymon musisz odświeżyć wiedzę o ostatnich update'ach, jak to wygląda od jakiegoś czasu.

[00:04:15.450] **Szymon Warda:** Ale ja tutaj nie twierdziłem nic innego.

[00:04:19.320] **Łukasz Kałużny:** To pozwala Wam w prosty sposób po prostu zmienić manifest w jakiś sposób, albo dodać do niego elementy, podmienić po prostu pisząc kawałek Yamla, bądź wpisując komendę JSON patcha, którego Szymon nienawidzi. Dobra, i to są takie elementy, które posiadamy. Jak popatrzymy ze strony wsparcia narzędziowego, czy od strony tego, jak to robimy z pipeline'ów, czy jak to robimy z GitOpsa typu Argo, oba są pierwszymi obywatelami, zachowują się dokładnie tak samo.

[00:04:50.100] **Szymon Warda:** Tak, i tu dam małą gwiazdkę, że mówimy oczywiście o Helm w wersji 3 i wyżej, pomijamy wersję 2, żeby uprościć, żeby nie było wytykania.

[00:05:01.580] **Łukasz Kałużny:** Tego już nie powinno być. Dobra. I teraz słuchajcie, jakie są problemy z Helmem takie moje? Pierwsze, to jest ludzie robią tam nadmierną logikę. Czyli ja bym powiedział, że próbują dopieprzyć tam całą logikę biznesową, albo co jeszcze gorsza, zaczynają budować instrukcje warunkowe, drzewa warunkowe, czyli rzeczy, które powinny być konwencjami, zaczynają tam robić taką ifologię stosowaną. I to jest jeszcze pół biedy, bo nagle się okazuje, że przez to, że tam są GO template'y, które pozwalają na bardzo sporo logiki, zaczynają pisać własne funkcje. Czyli tam jest, zaczynają tworzyć własne reużywalne funkcje i inne rzeczy, wyrzucać je, współdzielić i zaczyna tworzyć się małe piekło, które nie wiemy dlaczego tak się dzieje.

[00:05:49.790] **Szymon Warda:** Dobrze.

[00:05:50.480] **Łukasz Kałużny:** I Szymon, pewnie spotkałeś się z tym, że developer zaczyna wymyślać jak się pokaleczyć, bo na tym środowisku powinna być jakaś specyficzna rzecz, która nie jest jawnie deklarowana.

[00:06:01.840] **Szymon Warda:** Łukasz, zgodzę się, tylko to jest takie podejście na zasadzie, że a jak damy, to ktoś popsuje. Oczywiście, że popsuje. Widzieliśmy przykład Customiza, z którym ja walczyłem i zgodzisz się, że tam też było nadziergane jak tylko można było. Ale odpowiadając, czy ifologia ta może być? Tak, ifologia może być. Drugim podejściem, które jest dużo lepsze w tej sytuacji, to jest po prostu jawne dawanie obszarów, które można rozszerzać przez extended załóżmy labele, i tak dalej, całą tą opcję, żeby jednak mimo wszystko ten Helm był rozszerzalny. Zgodzę się, że ifologia jest zła. Można to zrobić inaczej tak naprawdę, jawnie przekazywać pewne parametry i zrobić bez ifów. Można to uporządkować.

[00:06:49.300] **Łukasz Kałużny:** Dobra i teraz jeżeli popatrzymy o pisaniu dobrego Helma, jak mówimy. Bo zobacz, że sytuacja, kiedy dostarczamy coś już w ten sposób, jeżeli będziemy używać właśnie patrząc na te problemy, to pod tym względem Helm, tak jak powiedziałeś, one powinny być jawnie deklarowane. To jest rzecz, którą ludzie nie lubią bardzo często, że nie powinniśmy stosować tak naprawdę, w mojej ocenie, te wszystkie elementy, ten cały lukier składniowy, który tam leci, do wewnętrznych rzeczy nie powinien być w ogóle stosowany, tylko powinny być albo konwencje, czyli coś, co jest przewidywalne, albo jawnie zadeklarowane w valuesach jako parametry.

[00:07:31.070] **Szymon Warda:** Bym się z tym zgodził. Dla mnie kolejna siła... Znaczy, ja może dam mój główny argument, czemu ja jestem zwolennikiem Helma. Customize powoduje to, że jak mamy, bo to jest taki koronny argument, tak, mamy mikroserwisy to używajmy Customize'a. Ja powiem właśnie: nie, bo w tym momencie mówimy, że każdy mikroserwis jest do siebie w miarę podobny i tylko będziemy to modyfikować. A przy Helmie mówimy inną opcję: drogi zespole, twoją odpowiedzialnością jest dostarczenie pakietu, dostarczenie sposobu instalacji i mnie w sumie nie interesuje. Jak chce inny zespół użyć, to też po prostu dostaje plik values i ma go użyć. Więc to jest jawne budowanie pewnego zbioru abstrakcji. Tu się zgodzisz, że Helm fajnie buduje abstrakcję. Buduje proste wersjonowanie i mówi: to jest Twoja bajka, masz się tym zająć i to ma działać dobrze.

[00:08:19.240] **Łukasz Kałużny:** To dobra. I teraz taka rzecz, tak jak powiedziałeś, powiedziałeś wersjonowanie, płachta na byka. Mało kto poprawnie używa wersjonowania w Helmie.

[00:08:27.700] **Szymon Warda:** Łukasz, zgodzę się, ale...

[00:08:29.740] **Łukasz Kałużny:** I teraz...

[00:08:31.510] **Szymon Warda:** Jest łatwiejsze do zrobienia. I jak się ustali co i jak, a nie jest trudne ustalenie co i jak, to jest łatwiejsze niż z Customize.

[00:08:39.400] **Łukasz Kałużny:** Pod tym względem ok, tutaj wiesz... Inaczej, mówię, bo mamy, do czego piję, żebyście też wiedzieli, mamy chart version, czyli to jest manifest i app version, czyli wersja aplikacji. I powinniśmy, jeżeli podbijamy app version, czyli tylko aplikację, to będzie image tak naprawdę naszego release'u, to powinniśmy podbijać tylko app version. Jeżeli zmieniamy coś w Helmie, powinniśmy podbijać chart version. I to jest taka rzecz, której ludzie nie do końca akceptują.

[00:09:12.980] **Szymon Warda:** Znaczy, ja powiem tak, przeglądając coraz więcej rep odnośnie właśnie instalacji Helma, to już stało się standardem, że naprawdę... Inaczej, dobre praktyki w Helmie weszły i już zagościły i są.

[00:09:25.970] **Łukasz Kałużny:** Ale tylko patrzysz to z produktów. Teraz bardzo ważne. Patrzysz to z dużych produktów open source'owych.

[00:09:32.150] **Szymon Warda:** Łukasz, tak, ale kiedyś produkty open source'owe miały pierdolnik i ludzie się nauczyli z tego pierdolnika. A obecnie już się rynek uporządkował, więc to też spływa na dół i jednak te zasady są już, jak robić to dobrze, zostały ustalone.

[00:09:47.500] **Łukasz Kałużny:** Tak, ale są nieużywane dalej, bo lecimy z brzytwą. To tak z mojej perspektywy. Czy będziemy używać Helma z Kubernetesem? Zawsze. Ale to będą dla mnie, pierwszą rzeczą, to są pakiety ze świata zewnętrznego, zero customize'ów i innych rzeczy. Uważam, że to co przychodzi z open source'u, weźmy to Argo, Prometheusza, jakieś Ingresy i inne rzeczy, to wszystko powinno być instalowane Helmem. I tutaj w ogóle nie ma...

[00:10:14.770] **Szymon Warda:** Nie mamy dyskusji, oczywiście, że tak.

[00:10:15.700] **Łukasz Kałużny:** Tak. Jeżeli dostarczasz swój software jako produkt i ktoś będzie go instalował na klastrze i to jest zupełnie poza Tobą, tutaj również jest to Helm w 100%.

[00:10:26.170] **Szymon Warda:** Dobrze. Teraz wchodzimy w to ważne, jaka jest definicja produktu? Czy zespół dostarcza swój system pod system, zbiór serwisów, mikroserwisów?

[00:10:36.010] **Łukasz Kałużny:** Nie, ja patrzę jako produkt poza firmę zupełnie.

[00:10:39.250] **Szymon Warda:** Ok.

[00:10:40.120] **Łukasz Kałużny:** Czyli że nie masz w ogóle kontroli nad infrą i innymi rzeczami, zupełnie wypychasz to od siebie.

[00:10:44.650] **Szymon Warda:** Ogólnie rzecz biorąc, jeżeli coś pakujesz i ktoś ma faktycznie jak produktowo na to patrzeć, to się zgadzamy, Helm jest jak najbardziej świetny.

[00:10:50.220] **Łukasz Kałużny:** Tak i teraz wlatujemy w rzecz, w której ja preferuję, czyli nasze wewnętrzne aplikacje, które zespół own'uje jakoś, dostarcza, w zależności jak patrzymy, wewnątrz firmy, czyli gdzieś, gdzie mamy na to w teorii wpływ. Słowo "w teorii" jest tutaj kluczowe. Dlaczego preferuję tutaj, w tym miejscu? Dlaczego w tym miejscu preferuję...

[00:11:13.380] **Szymon Warda:** Customize.

[00:11:15.030] **Łukasz Kałużny:** Customize? Ponieważ w większości przypadków tam samo to, w jaki sposób aktualnie działa Customize... Co tutaj mam na myśli? To w jaki sposób podchodzi do wrzucania i robienia sobie nakładek na przykład per środowisko definiowania tego. Dla mnie Szymon na przykład bardzo ważną zaletą Customize'a są dwie pierdoły, które działają bardzo dobrze w postaci generatorów. Mamy Configmap Generator i Secret Map Generator, które w locie generują Ci, czy z SOPS-ów i innych rzeczy generują Ci Configmapy i Secrety. I teraz ważna funkcjonalność, która się w środku znajduje, to dla Was, jeżeli to będziecie robić, to Secret Map Generator i Configmap Generator potrafi wziąć te pliki .envy i inne takie, czy JSON, whatever, w czym trzymacie te configi. Wylicza sobie z zawartości hasha i generuje z tego, teraz to jest istotne, wylicza sobie hash i dokleja go do nazwy obiektu. Jeżeli w deployu na przykład odwołujecie się do Configmapy, weźmy tam config mojej aplikacji, to on w deployu podmieni nazwę tej Configmapy, czyli to będzie config mojej aplikacji i numerki i hash i tak samo będzie się nazywała Configmapa i przykładowo zrobi pierdołę, z którą jest, jak wiesz, zawsze problem. Czyli jeżeli nie zmieniamy deploymentu, to Helm go nie będzie w żaden sposób redeploy'ował w tym wypadku, jeżeli zmienisz samą Configmapę. A tutaj fajnie zrobi, wywoła cały rolling update i inne takie elementy i też widzimy co się zmienia, jak wygląda. To jest jedna z takich pierdół, które bardzo dobrze działają.

[00:13:02.000] **Szymon Warda:** Generatory są fajne, tutaj nie ma większej dyskusji. Chociaż w kontekście jak mówisz jeszcze generatory odnośnie Secretów, to Łukasz nie trzymasz swoich secretów w Key Vault? Tak jak Ty żartuję, to jest żart, spokojnie.

[00:13:13.550] **Łukasz Kałużny:** Tak, wiesz, wróćmy Szymon kto tu jest fanem SOPS-a od dawien dawna?

[00:13:21.050] **Szymon Warda:** Nie. Znaczy Mozillowe naprawdę są spoko secrety.

[00:13:25.490] **Łukasz Kałużny:** Nie, dlatego wiesz, mówię tak, że w tym, dlatego też jest plugin po prostu. Tak na przykład jak mamy SOPS-y, to SOPS-y bez problemu spina się z tym, sopsy można bez problemów... W scenariuszach GitOpsowych nawet pluginu nie potrzeba, żeby to wszystko spiąć ze sobą.

[00:13:41.480] **Szymon Warda:** Słuchaj, na zawsze, to mieliśmy swego czasu odcinek właśnie o tym, jak ja bardzo nienawidzę Secretów. Tak.

[00:13:48.380] **Łukasz Kałużny:** I tak, i ja też nienawidzę, więc tu akurat jesteśmy zgodni z tym, SOPS-y na szczęście przejęły.

[00:13:54.950] **Szymon Warda:** SOPS-y przejęły i przejęły bardzo dobrze. Wiesz co, dla mnie ok, zgodzę się, generatory są super fajne. Problem jaki ja mam z Customizem największy to jest fakt, że niestety to prowadzi do over architektury na poziomie overlay. Mamy overlay, który jest overlay'em, który ma overlay i overlay.

[00:14:10.886] **Łukasz Kałużny:** Inaczej...

[00:14:11.210] **Szymon Warda:** Czekaj i potem prowadzi do tego, że całą logikę jakby na serwis mamy gdzie? Mamy tam nadpisywaną i potem w sumie nikomu nie zależy na tym, żeby to przemigrować do głównego, bo rozwali wszystkim innym.

[00:14:23.990] **Łukasz Kałużny:** Znaczy wiesz co, dlatego ja podchodzę, że jeżeli chodzi o nakładki, może być tylko base, który zawiera w całą rzecz podstawową, tylko base i jedna nakładka per środowisko. I to będzie... Inaczej, czy można w Customizie się skrzywdzić? O Boże, jak... Inaczej, jak zaczynamy hackowanie, jak zaczynamy hackowanie...

[00:14:47.700] **Szymon Warda:** Nie hackowanie, to jest po prostu nadużywanie overlay'i, które jest bardzo łatwe do zrobienia.

[00:14:51.690] **Łukasz Kałużny:** Tak, dlatego ja podchodzę Szymon bardzo prosto. Deployujemy tylko jeden overlay nad środowisko i koniec, nie ma więcej. Bo jeżeli zacznie powstawać overlay do overlaya, to się... Inaczej, dobra, nazwijmy to wprost, już mamy tyle czasu, przepraszamy przedszkolaki, zajebiemy się, tak samo jak z Helmem.

[00:15:12.990] **Szymon Warda:** I wracamy do naszego głównego tematu, czyli w każdym z tych narzędzi możesz się pociąć. Ja bym tak, żeby to nie było na zasadzie, że zostaniemy przy swoich zdaniach i ja bym to zrobił w ten sposób, jeżeli podchodzimy do tego, że te nasze mikroserwisy, bo o tym głównie mówimy, są takie same i my kontrolujemy... Bo siła Customiza, łatwo jest zrobić konwencję w base'owym mamy i potem tylko overlay jest na kolejne serwisy, zapisuje sobie tylko image swój, jakieś swoje secrety i tak dalej. W tym jest świetny.

[00:15:44.320] **Łukasz Kałużny:** Przykładowo albo w ogóle, albo trzymamy w ogóle manifest per serwis i tyle. I oddzielnie każdy i wersjonujemy je.

[00:15:53.170] **Szymon Warda:** To samo można by było zrobić też w Helmie, że po prostu podmieniamy tylko image. To samo można by było zrobić, ale ok, zgodzę się, jak najbardziej. Natomiast jeżeli podchodzimy, że zespoły są niezależne i nie wnikam jak to wygląda i od siebie mogą się różnić i to mniej lub bardziej znacząco, to dla mnie wybór jest prosty - Helm. Bo w tym momencie wchodzimy, ma działać, koniec kropka, ogarnijcie się. Nie popsują sobie nawzajem.

[00:16:15.640] **Łukasz Kałużny:** Ja jeszcze dodam jedną straszną rzecz, którą kurde ileś razy widziałem i zawsze widzę ją z problemami, to jeżeli ktoś próbuje zrobić Master Helma, który zainstaluje całe środowisko z logiką warunkową.

[00:16:27.730] **Szymon Warda:** To jest kuszące.

[00:16:28.990] **Łukasz Kałużny:** Wiesz o czym... I wiesz jak się potem kończy w większości przypadków jak osoba, która to stworzyła odchodzi albo przechodzi do innego projektu, to jest płacz.

[00:16:39.010] **Szymon Warda:** Wiesz co, nie, to można zrobić poprzez użycie prostych dependencies, że masz dependencies i tyle. Nie robisz nic więcej, a potem tylko przekazujesz te fragmenty do valuesów dalszych. Więc to można. Ja podważałbym sensowność tego w większości przypadków. Większość organizacji tego nie potrzebuje, tam logika powinna być CI/CD. Chyba, że znowu wypychamy całość do jakiegoś klienta.

[00:17:00.970] **Łukasz Kałużny:** Produkt, robisz produkt, tam niestety będzie logika warunkowa. Weźmy na przykład: czy zainstalować Redisa, czy użyjesz zewnętrznego i podasz connection stringa? Czy zainstalować na przykład Postgressa z operatorem? To co mamy u jednego klienta w pewnym produkcie, który przychodzi z rynku. To tam na przykład to jest software, którego używają setki klientów, więc on musi mieć ifa: zainstaluj mi Postgressa, podaj connection string do Postgressa na przykład, czy secret, w którym będzie connection string. Więc to są, w tym, ta ifologia się znajdzie przy produkcie. Tylko tam ona jest potrzebna, ta cała zabawa z logiką będzie potrzebna, tylko...

[00:17:41.780] **Szymon Warda:** Tej ifologii tam nie ma dużo, bo to jest albo mam dependency podany, albo mam connection stringa po prostu, albo instaluję sam, albo śmiga.

[00:17:48.500] **Łukasz Kałużny:** Tak, tylko że to jest, tylko zobacz, to jest właśnie prosta ifa. A widzieliśmy jak ludzie próbują zbawić problemy, których nie będzie.

[00:17:55.370] **Szymon Warda:** Zgodzimy się z tym, jeżeli nagle widzimy, że ktoś ma cały zbiór funkcji w GO, które generują różne rzeczy, to zgodzimy się, że to już jest złe.

[00:18:06.830] **Łukasz Kałużny:** To tak, bardziej niż, zaczyna się robić wesoło.

[00:18:10.310] **Szymon Warda:** I zgodzimy się z tym, że trzymanie jednego i drugiego systemu jest dobre, póki jest proste. Teraz zostaje pytanie trzecie tak naprawdę, bo to nie jest czy Helm, Customize, tylko to jest takie połączenie jednego i drugiego. Czyli standardowa opcja, że mamy Helma, który nam wszystko generuje, a potem jeszcze Customizem zmieniamy pewne fragmenty.

[00:18:29.330] **Łukasz Kałużny:** Nie, ja... Naprawdę, to jest... Widziałem jedną tylko polecajkę na takie coś... Inaczej, spotkałem się tylko raz z takim jawnym wskazaniem tego. I to było w tym, ponieważ Helm kiedyś do Consula był bardzo mocno ograniczony od Hashicorp i rekomendowali, że jak chcesz sobie pozmieniać to zrób builda i przeleć go dopiero Customizem. I wiesz co? Ja Ci powiem tak, dla mnie to jest już piekło, zaczyna robić, piecze.

[00:18:57.460] **Szymon Warda:** Dla mnie to jest tak samo jak dostawanie się do prywatnych funkcji w kodzie przez refleksje i inne rzeczy, że polegamy na tym, że ten kawalek będzie wyglądał i prosimy się o to, żeby to się za chwilę rozwaliło. To tak, dla wewnętrznego użycia absolutnie nigdy nie, bo to jest absolutna rzeźnia. Dla zewnętrznego? Zgodzę się z tym, kiedyś te Helmy były ograniczone, teraz mamy te wszystkie możliwości rozszerzenia i labeli, i obrazów, podmiany, zmiany i tak dalej, to już prawie nie jest potrzebne. A jeżeli nagle ktoś czuje potrzebę, to ja bym zobaczył, czy na pewno nie można tego zmodyfikować i czy na pewno nie robimy czegoś totalnie pod prąd. Bo to śmierdzi czymś takim, że ja wiem lepiej niż ludzie, którzy na przykład wydają tego Prometheusza. Więc tak, dla mnie to jest takie bardzo poważne, powiedziałbym, że pomarańczowe, wpadające w czerwone nawet światełko.

[00:19:50.670] **Łukasz Kałużny:** Dobra, jest jedna rzecz, która w Helmie potrafi być bardzo dobra i bardzo zła.

[00:19:55.380] **Szymon Warda:** To dajesz.

[00:19:57.930] **Łukasz Kałużny:** Przy produkcie jest bardzo dobra, przy naszym wewnętrznym potrafi znowu skrzywdzić. Nie mamy tego zupełnie w Customizie. A Szymon odnoszę się do hooków i testów. I żeby teraz tylko wprowadzić o co chodzi, Helm ma 1, 2, 3, 4, 5, 6, 7, 8, 9 hooków. Mamy akcję pre post instal, pre post delete, pre post upgrade i pre rollback, post rollback oraz taki ostatni, który też jest pod komendą helm test, czyli zrobienie testu. I chodzi o to, że na naszym klastrze w tym momencie mamy możliwość wrzucenia specjalnych hooków, podpięcia się pod wywołania w tych momentach eventy i coś może zostać na Kubernetesie. Przykładowo tutaj w tym miejscu to jest odpalanie joba Kubernetesowego po prostu, który nam coś sprawdzi, przetestuje, zobaczy jak to wygląda. Na przykład Szymon Twoje ulubione pre instal, pre upgrade. Jeżeli mamy connection string do bazy danych, to zrób upgrade migracji schematu albo seedowanie bazy.

[00:21:08.180] **Szymon Warda:** Tu się łączy moja niechęć też do Fluxa w pewnych, dla instalacji aplikacyjnych nadmienię, aplikacyjnych, nie infrastrukturalnych. Sorry, taka logika dla mnie jednak mimo wszystko powinna być w CI/CD, odnośnie instalacji, weryfikacji i tak dalej.

[00:21:23.240] **Łukasz Kałużny:** Tak, jak nie robisz produktu, znowu, jak nie robisz produktu, nad którym nie będziesz miał kontroli, to będziesz zmuszony, to jest jedyna opcja, żeby to poprawnie zrobić...

[00:21:33.080] **Szymon Warda:** Nie kupuję tego.

[00:21:33.770] **Łukasz Kałużny:** Wiesz jak jest z puszczaniem, wiesz jak jest z puszczaniem skryptów przez adminów: o, nie puściłem.

[00:21:38.870] **Szymon Warda:** Ale w tym momencie jeżeli jakiś produkt będzie odpalał jakieś joby, które mają jakieś założenia, które mają jakieś migracje, z całym szacunkiem, nie. Kontrolę nad tym co się dzieje na moim klastrze produkcyjnym mam ja. Ten Helm powinien mi tylko zainstalować soft i odczepić się ode mnie. Nie, naprawdę, hooki, ewentualnie do weryfikacji czy coś się łączy i tak dalej, bardzo proste.

[00:22:00.320] **Łukasz Kałużny:** Tak, testowe tak. Ale wiesz, na przykład softy wykorzystują, wiesz o tym, że wykorzystują to w trakcie upgrade'u, żeby zrobić na przykład, podbić schemat danych, puścić skrypty migracyjne.

[00:22:09.680] **Szymon Warda:** Super, to jest, ładnie wygląda na prezentacji znowu, jak masz bazę 2 gigabajtów. Bardzo źle wygląda, jak masz bazę 300 gigabajtów albo i większą. Więc z całym szacunkiem, nie, nie, nie nie. To jest feature, który bardzo ładnie wygląda na prezentacji, nie sprawdza się w realnym życiu. Zbyt duże ryzyko i tak trochę wciskanie jest: ja wiem lepiej do organizacji, które instalują. Nie. Checki, czy jest połączenie, tego typu rzeczy - tak, nic więcej.

[00:22:39.080] **Łukasz Kałużny:** A potem apka zupgradeowana, a schemat nie podniesiony.

[00:22:43.670] **Szymon Warda:** Tak, migracja schematu to jest odpowiedzialność osoby, która robi wdrożenie. I doskonale wiesz, że tworzenie czegokolwiek większego to nie jest na zasadzie, że puszczam sobie skrypcik i idę do domu.

[00:22:54.260] **Łukasz Kałużny:** Ale wiesz, że ludzie by tak chcieli.

[00:22:56.180] **Szymon Warda:** Łukasz, zdaję sobie sprawę, że by chcieli. Ci, którzy tak zrobili i się wywalili na twarz, już tak nie chcą.

[00:23:05.630] **Łukasz Kałużny:** Dobra, czyli tak, to będą moje preferencje. Tak jak powiedziałem, rzeczy, które instalujemy z zewnątrz, z open source'u produkty, Helm jest super i tu nie kombinujcie, o tak. Ja wewnętrzne rzeczy jednak zrobię na Customizie, o tak. Chyba, że zespół nie będzie latał z brzytwą, to i prosty Helm też jest spoko w tym miejscu. Jestem antyfanem przekombinowania po prostu.

[00:23:34.020] **Szymon Warda:** Dobrze, to ja odnośnie Helma powiem tak, jakie jest (...) odpowiedzialności, a ja jestem zdania, że teamy są od siebie niezależne i jednak mówię ogarnijcie się. To jednak jest Helm, prosty, bardzo prosty. Możliwe, że jakieś powiedzmy funkcje wspierane z poziomu platformy jak najbardziej, ale to tak zobaczymy. Niezależność bym czy Customize i ja jednak mimo wszystko nie, zbyt się sparzyłem na Customizie, tak że nie. Tyle. Faktycznie z tą uwagą, żeby pilnowanie, żeby jasne ustalenie kiedy jest wersja i jak to wygląda, kiedy wersjonujemy, żeby to było znajome wszystkim i wszędzie zawsze, to jest ważna uwaga. I zwracanie też uwagi na to, co można rozszerzać i żeby te rozszerzenia były.

[00:24:26.230] **Łukasz Kałużny:** Szymon, zażartuję, żeby nie wyglądało to jak Pulumi, żeby ten Helm nie był ten, nie był pisany Solidem jak w C Sharpie.

[00:24:37.780] **Szymon Warda:** Tak, dokładnie tak, żeby nie było nawet potrzeby myślenia o Solidzie i Dry i tak dalej. To nie ten poziom.

[00:24:45.610] **Łukasz Kałużny:** Jedną rzecz w ogóle przegapiliśmy słuchajcie. Uwaga Szymon, bo ja w ogóle jedną rzecz przegapiłem zupełnie. Wyszedł Helm 4.0 tak w ogóle, tak by the way, by the way na koniec. Trzy dni temu, tak jak nagrywamy, wyszedł, przepraszam, dwa tygodnie temu, jak nagrywamy, czyli w połowie ten, w połowie. Zupełnie to przegapiłem. I uwaga Szymon, słuchajcie, trzymaj się, bo spadniesz tutaj mi. Stoisz, więc nie spadniesz, ale trzymaj się. Redesign plugin system that support WebAssembly based plugins.

[00:25:25.000] **Szymon Warda:** Jezus, Maria, to będzie może jeszcze lepsze funkcje pisać. Nie jest dobry rozwój.

[00:25:30.790] **Łukasz Kałużny:** Stary, Postgressa odpalisz z WebAssembly w ramach Helma.

[00:25:36.970] **Szymon Warda:** Ja się boję tych prezentacji, przysięgam.

[00:25:40.450] **Łukasz Kałużny:** Teraz widzicie minę Szymona, już wiesz dlaczego. I jeszcze za rok się przeprosisz z Customizem jak ktoś cię skrzywdzi.

[00:25:52.060] **Szymon Warda:** Customize z overlayem, może, ale dalej pisanie tych pathów nie.

[00:26:00.220] **Łukasz Kałużny:** Okej. Raczej tam pathów. Mówisz Sonetowi, że ma Ci dopisać w Copilocie i jest dobrze. Dobra.

[00:26:09.760] **Szymon Warda:** Kończymy.

[00:26:09.910] **Łukasz Kałużny:** To co, kończymy?

[00:26:11.110] **Szymon Warda:** Trzymajcie się, heja.

[00:26:11.560] **Łukasz Kałużny:** Trzymajcie się na razie.

