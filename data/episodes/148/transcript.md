# 148.mp4

[00:00:11.00] **Szymon Warda:** Cześć, czołem, kluski z rosołem! Słuchacie Patoarchitektów. Prowadzą Szymon Warda...

[00:00:15.19] **Łukasz Kałużny:** I Łukasz Kałużny. Wszystkie linki do tego odcinka znajdziecie na Patoarchitekci.io lub gdzieś na dole. Oj, nietypowo walnąłeś początek.

[00:00:27.00] **Szymon Warda:** A co? Dobrze. Zerknijcie przy okazji na szkolenia, bo jest tam lista. Jakby czegoś brakowało - napiszcie. No ogarniacie ogólnie rzecz biorąc.

[00:00:38.02] **Łukasz Kałużny:** Nasze szkolenia otwarte, które mają fajne opinie, na różne tematy.

[00:00:45.03] **Szymon Warda:** Łukasz, mają bardzo dobre opinie.

[00:00:45.22] **Łukasz Kałużny:** Tak, mają bardzo dobre. Dobra, to zaczynaj od siebie. Znowu bank rozbity tematami, więc zaczynamy od Kubernetesa Szymonie i okolic.

[00:00:54.09] **Szymon Warda:** Tak, od Kubernetesa. Ale zacząłem od Kubernetesa, ale bardziej z Twoich tematów. Kubescape wychodzi z Sandboxa i wchodzi w Incubation w CNCF-ie. Czym to w ogóle jest? Zaczęło się w 2021 roku. To jest narzędzie do zabezpieczania, monitorowania Kubernetesa i jest o tyle fajne, że wspiera dość sporo frameworków, jeżeli chodzi o właśnie, czy benchmarków, różnie można by to nazwać, bo wspiera NSA-CISA, Kubernetes Hardening Guidance, MITRE ATT&CK, Soca2, CIS benchmarks właśnie w kontekście jak to tam powinno się dziać. Jeżeli chodzi, czym oni się chwalą tak naprawdę, bo tego trochę jest, to nabrało trochę dość mocno wiatru w żagle.

[00:01:38.19] **Łukasz Kałużny:** Tak.

[00:01:39.11] **Szymon Warda:** Oczywiście, że skanuje, integruje się w momencie IDE, w całym ruchu shift left, czyli jak najwcześniej mamy mieć informację, co jest bardzo dobre, że możemy na IDE w momencie VIDE, czyli u developera skanować te obrazy, wiedzieć co się dzieje, w CI/CD możemy to zrobić, to jest taki trochę standard. Ale co oczywiście robi? O dziwo wykorzystuje eBPF i skanuje. To, o czym mówiliśmy w poprzednim odcinku, więc mamy płynne przejście. Ciekawe czemu? Aktywność na plikach. To jest fajne. Aktywność procesów, operacje sieciowe i wywołania systemowe. Czyli faktycznie ma całkiem niezłe monitorowanie tego, co się obecnie dzieje w klastrze i może wyłapać nieco więcej. Rozwiązanie jest naprawdę niezłe. Co tam jeszcze mają w ogóle w takim pakiecie, jak patrzę na to produktowo? Anomaly Detection, czyli dziwne zachowania w całym engine dockerowym i tak dalej. Behavior analysis engine, czyli sygnatury ataków, itd. Chociaż też mówiliśmy o tym, że to też może wyglądać różnie w kontekście właśnie sieciówki, bo mamy wszystko zaszyfrowane.

[00:02:40.03] **Łukasz Kałużny:** Tak, ale widać to w plikach w runtime.

[00:02:41.20] **Szymon Warda:** Ale na tych plikach [niesłyszalne 00:02:42] będzie wyglądało.

[00:02:43.06] **Łukasz Kałużny:** Ale w runtime za to i odpalanie procesów i innych rzeczy będzie już wyglądało.

[00:02:47.12] **Szymon Warda:** Będzie wyglądało bardzo dobrze, tak.

[00:02:49.08] **Łukasz Kałużny:** Tak. Zostawmy tą sieć, ale na poziomie samego będzie dobrze wyglądać na poziomie środka naszego.

[00:02:56.18] **Szymon Warda:** Tak. I na końcu mamy jeszcze malware analysis. Czemu mnie jeszcze w ogóle Kubescape całkiem ciekawi? Bo naprawdę nabrał dojrzałości i to sporawo. Do tego stopnia, że w ogóle AWS dodał ich do swoich materiałów szkoleniowych z bezpieczeństwa. Tak że do zerknięcia przez wszystkich, bo wydaje mi się, że to się powoli może stać takim elementem should have.

[00:03:18.22] **Łukasz Kałużny:** Czy wiesz, co ja się teraz tak zastanawiam. No bo ja inaczej będę drążył troszeczkę, którędy pójdzie względem, bo takie produkty nie powstają znikąd.

[00:03:31.19] **Szymon Warda:** Ależ oczywiście, że nie.

[00:03:33.08] **Łukasz Kałużny:** Ta znikąd, to jest firma Armo, która robi, że tak powiem, dalszą rzecz. Nawet mają, oczywiście mają w tym zestawie do tego linka - Armo versus Kubescape, ich platforma vs Kubescape i tutaj pokazują właśnie L7, runtime analysis, kreowanie polityk, profilingi, Network Anomaly Detection, API, customowe rule, response prevention i quarantane. Więc tam troszeczkę rzeczy jest. Ale jak popatrzymy na Kubescape'a, to on zaczyna być narzędziem, które można sobie powiedzieć, że ja trochę mówiłem tak o microsoftowym Defenderze, że jest beznadziejny, ale jak nic nie masz, to jest naprawdę dobry za swoją cenę. I tą rekomendację...

[00:04:34.04] **Szymon Warda:** I co więcej, łatwość użycia go, włączenia, to jest też ważne.

[00:04:36.22] **Łukasz Kałużny:** Tak i teraz, jeżeli popatrzymy na Kubescape'a i te feature'y i tą dojrzałość, o której mówisz, ja mogę trochę powoli powiedzieć, że po prostu nie chcesz kupić dużego pakietu od Palo Alto czy Aqua Security, włącz Kubescape'a.

[00:04:50.06] **Szymon Warda:** Tak i pewnie zrobisz to dość łatwo, szybko i wyjdzie to taniej.

[00:04:53.20] **Łukasz Kałużny:** Tak, ale i tak problemem będzie to, czy będziesz w ogóle analizował to, co wyrzuca. Bo nieważne ile zapłacisz za narzędzie, to problemem jest to, czy ktoś w ogóle będzie na nie reagował.

[00:05:06.15] **Szymon Warda:** Łukasz, nie, jak długo będziesz patrzył w te logi? Przez pierwszy miesiąc pewnie tak. Po pół roku? Pewnie nie.

[00:05:12.21] **Łukasz Kałużny:** Słuchaj, przypomina mi się pewna rozmowa ze szkolenia w tym roku, że podsumuję to tak klient ma narzędzie, ale boi się przesłać logi centralnie, bo jest tego. Czyli nawet nie... Żeby określić co jest istotne, co nie z alertów, itd. Czyli jak masz już ciutkę większą skalę, to nagle nawet ten pierwszy miesiąc nie istnieje.

[00:05:43.22] **Szymon Warda:** Łukasz, ale sukces był? Był. Narzędzie wdrożone? Wdrożone. Więc o co chodzi? Dobrze, wychodząc z tego korporacyjnego podejścia, co tam Ty znalazłeś?

[00:05:54.13] **Łukasz Kałużny:** Idziemy do następnego korporacyjnego. Dla większości z Was osoba, która napisała ten wpis na blogu, nie jest znana, jest Aidan Finn. Hejtuje o wiele bardziej niż ja Microsoft i nadal mu nie zabrali MVP, a mamy od podobnego czasu. No i od jakiegoś czasu zajmuje się Azurem w sposób wbijający szpilki też po stronie grup produktowych. I tutaj taki temat na czasie, że tak powiem, ze względu na sytuację geopolityczną, co będzie, jest takie pytanie, co się stanie, to warto sobie w ogóle zadać pytanie, co się stanie, jeżeli twój region cloudowy, tu jest akurat Azure, ale co będzie, jeżeli Twój region zostanie zniszczony? I to jest bardzo w tym. I leci tutaj taką serią właśnie pogromcy mitów. Jeżeli popatrzymy, pierwszym jest taki, który ludzie nie chcą zaakceptować od zawsze, że Microsoft, w tym wypadku Azure'a, nie zrobi za Ciebie Disaster Recovery domyślnie.

[00:07:05.17] **Szymon Warda:** Nie może, bo mamy rozjazd czasów synchronizacji danych tak naprawdę. Więc to jest... Tak, to wychodzi często jak ja robię szkolenia, że ludzie się dziwią: ale jak to? Jak mam region gdzie jest replikacja asynchroniczna, to nie ma automatycznego przełączania? Mówię, że no tak, ale masz 15 minut opóźnienia, więc no nie możesz zrobić, dane utracisz.

[00:07:23.06] **Łukasz Kałużny:** Inaczej nawet teraz jak chciałbyś zrobić failover samodzielnie, masz wielki pop up: czy jesteś tego świadomy, że nieznany jest stan kopii?

[00:07:33.09] **Szymon Warda:** Tak.

[00:07:34.03] **Łukasz Kałużny:** Że możesz mieć rozjazd.

[00:07:35.13] **Szymon Warda:** Czasu 15 minut. Nie wiemy gdzie.

[00:07:37.21] **Łukasz Kałużny:** Tak, więc i dobrą rzeczą, która jest, jeżeli popatrzymy technicznie, ona się odnosi do wszystkiego. I tutaj w tym jest taka właśnie the solution, jak to ostatni w tym, jest dobrze podsumowane i pierwsze: gdzie tylko to możliwe, compute powinien być bezstanowy i łatwy do odbudowania w domyśle, IaC. Następnie, Recovery Strategy dla Twojej części DevOpsowej. O tym też nie myślimy. Następnie, tam gdzie jest to możliwe, korzystaj z tierów, które dają natywną replikację do innego, niezależną też od regionów, że możesz domyślnie się do innego regionu zreplikować, innego niż domyślny w parze. Następny, który jest szpilką w Cloud: consider using IaC for compute. Przy czym nadal Kubernetes jest jako bardziej skomplikowany IaC.

[00:08:44.11] **Szymon Warda:** Bo to jest IaC, takie bardziej skomplikowane, zarządzany.

[00:08:46.22] **Łukasz Kałużny:** Tak, zarządzany nadal, ale chodzi tutaj w tym wypadku, Kubernetes akurat się pod to łapie. Użyj niezależnego backupu od Microsoftu.

[00:08:57.12] **Szymon Warda:** Tak. A czy w ogóle to jest fajne, bo w sumie jakby na to spojrzeć, jakby zaatakować to położenie data center właśnie dostawców chmurowych, no to jest spory cios dla całego kraju, bo tam stoi od groma usług i to z każdego praktycznie kraju. Więc tak. No miejmy nadzieję, że nie jest to realny scenariusz, ale mimo wszystko jest to coś, co pewnie jest do rozważenia.

[00:09:20.03] **Łukasz Kałużny:** Ciekawe właśnie co zrobisz, jak jesteś pass native u danego dostawcy? I to dotyczy każdego, każdej chmury.

[00:09:26.16] **Szymon Warda:** Tak. Dobra, to powiedziałeś coś negatywnego, to ja powiem coś pozytywnego. Wygrzebałem raport o tym jak OpenSearch pobija Elastica, jeżeli chodzi o wyszukiwanie wektorowe, itd.

[00:09:42.04] **Łukasz Kałużny:** What?

[00:09:42.12] **Szymon Warda:** Tak. Uwaga!

[00:09:43.01] **Łukasz Kałużny:** Co tam się wydarzyło?

[00:09:45.01] **Szymon Warda:** No Łukasz, ustalmy przede wszystkim, to jest w jakichś tam benchmarkach, w dwóch właśnie, Vectorsearch i BigFive. I ustalmy, każdy test można tak stworzyć, żeby otrzymać odpowiedni wynik. Więc nie mówmy o tym, kto jest szybszy. Ale co mnie cieszy? To jest to, że faktycznie OpenSearch utrzymywany przez AWS-a powstał jako fork, fork od Elastica, itd., staje się już realną alternatywą dla Elastica. Pamiętam jak z rok temu, w którymś short'cie właśnie mówiłeś o tym, jak oni zrobili fajne właśnie monitorowanie chyba podatności na OpenSearch'u. Więc fajnie, że, bo przez jakiś czas fajnie, mamy Solra, który jest taką trochę mało żywą alternatywą dla Elastica, mało kto z niego korzysta. Ale fajnie też OpenSearch wychodzi z tego cienia i że tam gdzie potrzebujemy full-text search'a, możemy popatrzeć na coś innego poza Elasticiem. Więc cieszy mnie to bardzo, super, fajnie. Taka trochę bardziej informacja parafialna, gdyby się komuś to miało przydać.

[00:10:52.22] **Łukasz Kałużny:** Raczej jestem ciekaw czemu w ogóle wiesz, jak został ten test zamodelowany i przy czym, bo to jest w tym. Ok, dobra, czyli dodali... No dobra, ale to też jest... Dobra, patrzę, masz 3 wersje różnych algorytmów na OpenSearch vs Lucynka na Elasticu. To musiało się tak skończyć.

[00:11:15.11] **Szymon Warda:** Tak, no ustalmy, jest to tam trochę podmanipulowane, no tak. Ale mimo wszystko świadczy o dojrzałości, bo to mnie tutaj dużo bardziej interesuje.

[00:11:25.21] **Łukasz Kałużny:** Dobra, nie mieliśmy jeszcze dzisiaj AI-a. AI-a nie mieliśmy.

[00:11:30.20] **Szymon Warda:** Słuchaj, ja już nie mam AI-a dzisiaj żadnego.

[00:11:34.08] **Łukasz Kałużny:** A ja mam, tak, mam tam jakiegoś i lećmy, bo to jest, dowcipnie pokazuje, jak wszyscy próbują wykorzystać sytuację w Stanach. Więc jak sobie popatrzymy, jest tam OpenAI proposal for the US AI action plan. Jak go streścimy to niektórzy go pięknie ten z całości streścili, że odwalcie się od danych, które nazbieraliśmy i skończmy z prawami autorskimi.

[00:12:08.04] **Szymon Warda:** No tak by to brzmiało. Ameryka chce wygrać, więc myślę...

[00:12:11.13] **Łukasz Kałużny:** Że to dla dobra... Problemem jest ten, jak sobie popatrzymy, jest zajebisty tekst: but we must ensure that people have freedom of intelligence, by which we mean the freedom to access and benefit from AI.

[00:12:33.22] **Szymon Warda:** Nie wiem czy sobie zdajesz sprawę, z takich ciekawostek ekonomicznych to jest to, że m.in. jak Ameryka podpisuje umowy gospodarcze z różnymi krajami, to tak się chwalą, że wszystko fajnie jest, ale w ramach tych umów Ameryka też wymaga często respektowania praw autorskich, łącznie z tymi przedłużonymi. Np. czemu Myszka Miki, nasza kochana Myszka Miki, tak długo była chroniona prawem autorskim? Z reguły prawo autorskie trwa do 20 lat. Myszka Miki ma ciutkę więcej niż 20 lat, ustalmy to. Dokładnie była chroniona 50 lat i to było wymuszane przez umowy handlowe, że skoro handlujecie z nami, to respektujecie, żeby Myszka Miki była chroniona u was przez 50 lat. Więc wydaje mi się, że gdyby sytuacja była odwrotna, to by trochę to inaczej wyglądało.

[00:13:19.09] **Łukasz Kałużny:** No ale tak to jest, wiesz, tak to wygląda, mogą sobie na to pozwolić. Dobra.

[00:13:26.00] **Szymon Warda:** Dobra.

[00:13:26.15] **Łukasz Kałużny:** U Ciebie teraz.

[00:13:27.20] **Szymon Warda:** Kolejny wpis, informacyjny bardziej, bo to przy okazji, właściwie co się stało? Grafana Loki ma wersję 3.4 i tam się parę rzeczy wydarzyło. Między innymi to, że wchodzi opcja użycia Thanos Object Storage, czyli ujednolicamy to z innymi, z Pyroscopem i z innymi produktami. Ale co jest ważne i wydaje mi się, że większość ludzi zainteresuje, to jest to, że Promtail wchodzi do Grafany Alloy i ma już czas wygaszenia do 2025 do 13 lutego, czyli będzie long term support. Ale 2026, 2 marca, jest: nie ma dalszego wsparcia. Więc dla wszystkich i Alloy staje się tym takim centralnym punktem zbierania metryk, logów, jeszcze trace'ów, uwspólniają to. Więc dla wszystkich, którzy mają Promtail, a wiem, że sporo z Was ma, to pora na plan migracyjny.

[00:14:30.04] **Łukasz Kałużny:** Okej, tak, to będzie w tym z Promtailem. Co mnie najbardziej cieszy z tego wszystkiego, to New Sizing Guide.

[00:14:39.19] **Szymon Warda:** Tak, wróciło, bo on był, zniknął i potem wrócił.

[00:14:43.04] **Łukasz Kałużny:** Zniknął i jest.

[00:14:45.06] **Szymon Warda:** Tak, Sizing Guide, mianowicie ile potrzebujemy maszyn, żeby to wszystko działało, żeby to ładnie działało [niesłyszalne 00:14:50].

[00:14:52.08] **Łukasz Kałużny:** Przepraszam, tylko jedna rzecz mnie rozwala.

[00:14:57.04] **Szymon Warda:** Rozmiar danych?

[00:14:58.13] **Łukasz Kałużny:** Skala. Tak, zaczynamy mówić o sizingu, bo to jest teraz ważne przy sizingu o czym mówimy, żebyście... Bo to jest tam pytanie zawsze, jak proponujemy Lokiego, to zawsze jest tam trochę: jak w ogóle i o co chodzi? Mamy sizing - 3 terabajty dzień. 3 terabajty, 30 terabajtów, powyżej 30 terabajtów na dzień. Więc jak sobie popatrzymy: do trzech terabajtów logów dziennie, to jest bardzo ważne do zauważenia. To jest ile tutaj? Czekaj, wezmę, aż to zsumujemy szybciutko. Wrzucę to do Excela, bo chce powiedzieć ile. Trzy terabajty logów to nie jest już mało.

[00:15:44.19] **Szymon Warda:** I to oni w tym wymagają około 10 CPU.

[00:15:49.05] **Łukasz Kałużny:** Inaczej, to już tak, na 10 terabajtów RAM-u potrzebujesz 38 core'ów, 71 RAM-u na 100 terabajtów logów miesięcznie.

[00:16:01.07] **Szymon Warda:** Tak, skala jest bardzo ładna, bym powiedział.

[00:16:04.02] **Łukasz Kałużny:** Tak, nie mówimy tutaj o storage'u, ponieważ to jest po prostu storage blokowy na cloud'zie i tyle. Bądź na czymś co jest zgodne z S3 API, jak jesteście w onpremie.

[00:16:13.12] **Szymon Warda:** Dokładnie, bo może być na onpremie, to wtedy jest trochę bardziej tricky. Ale nie będzie. Więc ogłoszenia parafialne głównie pamiętajcie Promtail może niekoniecznie już teraz. Grafana Alloy, lecimy.

[00:16:23.10] **Łukasz Kałużny:** Nowe instalki na Alloyu.

[00:16:25.22] **Szymon Warda:** Dokładnie tak. Co tam jeszcze masz Łukaszu?

[00:16:29.09] **Łukasz Kałużny:** Raport i podsumowanie. The State of Infrastructure-as-Code na bieżący rok. Jak teraz popatrzymy, są dobre wnioski, które mnie w ogóle nie zaskakują, jak sobie patrzymy. Jeżeli popatrzymy, to tak, to jedna, która jest tam wrzucana, to czego oboje trochę nienawidzimy i mamy syndromy sztokholmskie do różnych rozwiązań, ale jedno to jest wspominanie o tym podejściu Programming language basics IaC, tak jak Pulumi, których dlaczego nie lubimy? Chyba już wiele razy się wypowiadaliśmy na ten temat. Ale jeżeli pójdziemy do takich wniosków, to jedna rzecz, która tutaj leci, którą zobaczysz, że dużo, jak sobie popatrzymy, ja tam zerkałem na to, dużo nadal jest ręcznie klikane.

[00:17:41.16] **Szymon Warda:** Data.

[00:17:42.09] **Łukasz Kałużny:** Mnie to nie dziwi. Data, to też. Ale tak, czyli jedna trzecia, czyli zobacz jak jest procentowo, 72% ankietowanych organizacji używa IaC-a, czyli 3/4. I to jest realne, jak sobie popatrzysz. Ale tylko 1/3 jest na tyle pewna, że posiada 3/4 workload'ów zautomatyzowanych.

[00:18:17.09] **Szymon Warda:** Dla jednego systemu workloud'u, gdzie masz prawie wszystko w kodzie, ale musisz potem coś doklikać, bo to jest masakra.

[00:18:23.00] **Łukasz Kałużny:** To jest w ogóle, tak, ale to jest jedna. Raczej, i tutaj, co mnie dziwi, że ludzie uważają, że IaC jest ten, że wyzwaniem w IaC-u może być bezpieczeństwo i governance.

[00:18:42.08] **Szymon Warda:** I tak, słyszałem takie opowieści, słyszałem to, że właśnie, że IaC jest mało bezpieczny, ponieważ lepiej jak ktoś mimo wszystko na to zerknie okiem i potwierdzi czy aby na pewno tak jest.

[00:18:53.20] **Łukasz Kałużny:** Znaczy ja wiesz, ja teraz po oglądaniu wszystkich tam i tam też jest, że tam 32% też ma problemy z change managementem i w ogóle. I po tym wszystkim uważam, że jeżeli nie mamy zainwestowanego zespołu znowu tam, nazwijmy to sobie platformą Cloud Center of Excellence, zespół chmurowy, czy jak chcecie, jeżeli nie ma tam naprawdę dużej inwestycji w ludzi, którzy naklepią moduły centralne, to lepiej zainwestować czas w użycie jakiejś wersji polityk na swojej chmurze.

[00:19:35.15] **Szymon Warda:** Bo developerzy nie myślą o sieciówce, o bezpieczeństwie, o bardzo wielu innych rzeczach. I to nie jest zarzut, po prostu to jest sposób myślenia. Każdy, jak przypowieść o ślepcach, którzy oglądali słonia, każdy chwytając za jeden kawałek, będzie myślał o czymś innym, zupełnie będzie inaczej to widział i to jest naturalne. To nie jest [niesłyszalne 00:19:53].

[00:19:54.09] **Łukasz Kałużny:** Tak. I z takich moich wniosków np., na danej w chmurze i tak ją powinieneś zabezpieczyć jakąś formą polityk.

[00:20:02.13] **Szymon Warda:** Tak, bo ktoś będzie chciał wejść, wyklikać, itd.

[00:20:05.11] **Łukasz Kałużny:** Tak, więc i tak trzeba je zrobić. Więc te moduły, tak czy siak, pierwsze powinno się zrobić polityki i to zabezpieczyć. Jak masz polityki, to w sumie można dać wolność. Pytanie, tam wiadomo, jak wygląda ekosystem, zarządzalność, przejmowalność i inne takie rzeczy? Tak, jest to istotne, ale pierwsze i tak będzie zabezpieczenie. I w tym jedna rzecz, która jest w tym, że pipeline'y stają się normą, ale z 30% nadal ręcznie odpala Terraforma.

[00:20:38.23] **Szymon Warda:** To jest przerażające, szczególnie jak pomyślisz gdzie ten plik się znajduje.

[00:20:43.07] **Łukasz Kałużny:** Tak, no a propos Terraforma, że jest spadek zużycia na rzecz OpenTofu i Pulumi.

[00:20:52.14] **Szymon Warda:** Ja jestem ciekawy. Pamiętam, że chyba przewidywałeś, że OpenTofu umrze. Widziałem, że to się utrzymało dlatego, że Terraform czuł oddech na plecach, że tak powiem.

[00:21:03.11] **Łukasz Kałużny:** Tak, więc zobaczymy co teraz, więc zobaczymy co będzie. Jak jesteśmy przy dowcipach na temat programowania, to Ty Davida Fowlera kojarzysz. Dla ludzi, którzy nie wiedzą, to jest jedna z osób, która stoi teraz za nowym .Netem. Jest jednym z architektów języka. I koleś ma manię chcenia, szanuję go za to, co robi w języku, ale próbuje się wykazać również w innych miejscach, niekoniecznie dobrych. Jednym z jego dziecka, które kurde jakoś nie idzie, do porzucenia niestety, jest .Net Aspire. Czyli tam, żeby łatwo było nam lokalnie odpalać i potem wdrażać mikroserwisy w chmurze. Zobacz sobie słuchaj, teraz na tego twitta...,

[00:21:47.08] **Łukasz Kałużny:** Raz już mówiłeś, jak bardzo go nie lubisz, Aspire'a, już parę razy mówiłeś, jak bardzo go nie lubisz.

[00:21:52.01] **Łukasz Kałużny:** Davida szanuję, ale tu jest przykład, że on powinien pójść do jakiegoś może jednego z niektórych klientów, których mamy i spróbować zdeployować aplikację na produkcji, bo widać, że nigdy nie wdrażał systemu produkcyjnego. Zobacz Szymonie na screena, który wrzucił, na ostatnią część buildera. I ostatnia przed build run, która jest.

[00:22:18.11] **Szymon Warda:** O Jezu, ale poczekaj.

[00:22:21.09] **Łukasz Kałużny:** Dobrze, to teraz już powiem Wam co Szymon ogląda. Aspire ma z założenia też zrobić autoprovisioning aplikacji. I tu jest np. wyobrażenie właśnie developera, że aplikacja będzie miała uprawnienia do nadawania uprawnień. Czyli, że aplikacja sama sobie do storage'u, który powoła, nada sobie uprawnienia RBAC-owe w cloudzie.

[00:22:43.05] **Szymon Warda:** Potwierdzam, że to właśnie widzę i nie rozumiem.

[00:22:48.18] **Łukasz Kałużny:** Wiesz co, szukając, gdzieś była inna drama, ja to ten tego nie wklejałem. Była gdzieś bardziej zabawna drama z tym, zabawna, bo próbował się w podobny sposób brać za identity i był długo wyjaśniany w komentarzach. Więc skupiają się moim... Może by napisali jakiś działający driver do event sourcingu na .Necie, zrobili może Entity Framework, Event Sourcing Edition, albo coś takiego.

[00:23:21.06] **Szymon Warda:** Czyżby nie było. [Niesłyszalne 00:23:21]

[00:23:22.03] **Łukasz Kałużny:** Są bardziej przydatne.

[00:23:23.07] **Szymon Warda:** Kiedy załóżmy aplikacja musi realnie stworzyć storage jakiś tam i to może być. Ale to są jakieś tam promile użycia ogólnie rzecz biorąc, to się nie powinno dziać, nie za bardzo.

[00:23:32.11] **Łukasz Kałużny:** Nie potrzebujesz... Inaczej masz od tego SDK i jeżeli już dotarłeś do tego kroku, dasz sobie radę.

[00:23:38.15] **Szymon Warda:** Tak. Dobra, to ja teraz idę, znowu przechylam to wahadełko w kierunku drugim, czyli rozsądku. Bardzo fajny wpis premature optimization. Ilość razy kiedy walczyłem w organizacjach o to, żeby czegoś nie optymalizować jest fascynujący, bo to często wygląda na tej zasadzie, ktoś myśli sobie, jak bierze takiego palca i mokrego: tak, w tym kierunku, w lewo idziemy, albo to trzeba zoptymalizować. Brak, bez jakichkolwiek metryk, mierzenia i jaki to będzie miało wpływ na realną wydajność. To co w ogóle Google fajnie pokazuje, że właśnie wpływ na użytkownika, bo to nas w sumie interesuje tak naprawdę. Ja pamiętam, jak w jednym projekcie był pomysł, żeby przejść z REST-a, czy też HTTP, jakkolwiek to nazwiemy, na gRPC. Była zrobiona próba, okazało się, że jest dużo wydajniejszy. Tylko problem był taki, że serwisów było około 10, gRPC był szybszy o kilka milisekund narzutu per każdy request. Tylko problem był taki, że ten główny system, do którego wszystkie śmigały, miał czas odpowiedzi rzędu kilku, kilkudziesięciu sekund. No i naprawdę była długa wojna, żeby ubić ten cały pomysł, że te milisekundy to może nie jest dobrze zainwestowany czas. Ale artykuł jest bardzo fajny, bo on bardzo ładnie porządkuje i daje takie narzędzia, żeby takie głupie pomysły optymalizacyjne ubić. On się skupia za tym, że to jest optymalizacja przez 3T. Że optymalizujemy z things, time i trade offs. Czyli po pierwsze, możemy optymalizować złą rzecz. Np. optymalizujemy właśnie złą rzecz albo załóżmy zespół próbuje np. optymalizować, czyli ograć np. metryki Dora. Time, czyli zbyt wczesna optymalizacja. Czyli to jest ten słynny tekst Donalda Knutha czyli: Premature optimization is the root of all evil. Ale fajne też jest trade offs, to chyba jest najczęściej pomijane, że zysk z optymalizacji względem ilość czasu jaki w to zainwestujemy. Fajnie, że będzie szybciej, pewnie będzie szybciej, tylko kiedy nam się to spłaci. Jest taki świetny właśnie komiks XKCD odnośnie automatyzacji. Kiedy nam się dana automatyzacja spłaci? Bo często tak, że tak, zużyliśmy, powiedzmy zużywamy pół godziny tygodniowo czy pół godziny miesięcznie, a zajmie nam to prawie miesiąc w developowaniu automatyzacji wokoło tego, że no to się po prostu nie opłaca. Fajny trade offs...

[00:26:13.17] **Łukasz Kałużny:** Tak jak z agentami. Mamy AI Agenta, żeby poświęcić 5 minut czatowania na coś, co zajmowało mi minutę.

[00:26:22.02] **Szymon Warda:** Tak, Łukasz, miało być bez AI-a tym razem.

[00:26:24.15] **Łukasz Kałużny:** Nie uda się.

[00:26:26.13] **Szymon Warda:** Ale fajny trade off jest, jak się pomyśli i który też widywałem, np. przepisanie kodu z [niesłyszalne 00:26:34] na Rusta. Fajnie, udało się, jest szybciej. Tylko nagle musimy mieć wsparcie dla Rusta w organizacji, którego nie mieliśmy, musimy umieć to utrzymywać, itd. I miałem taką znowu opowiastkę z innego systemu, jak firma stwierdziła, że będzie wspierała Dockera. Super. Efektem było to, że musiała wspierać system chodzący na Linuksie i Windowsie jednocześnie, jedne w Dockerze i Kubernetesie, drugie jako VM-ki windowsowe. Świetnie. Był zysk, ale niekoniecznie w tym kierunku, który byśmy chcieli. Także fajny artykuł do zbudowania takiej struktury pytań, struktury wektorów albo właśnie takich kątów, jak patrzeć na wszystkie takie pomysły optymalizacyjne, bo tam będziemy mieli te minusy całego działania. Pytanie, czy jesteśmy z nimi ok i czy świadomie podejmiemy, że to nam się opłaca? Bo to się na tym głównie kończy. Czas możemy zawsze zainwestować gdzie indziej, może być bardziej opłacalne. Tyle.

[00:27:34.19] **Łukasz Kałużny:** Dobra, to ja lecę teraz z wpisem Manager Anti-Patterns. Jest to, słuchaj, jest to ciekawa rzecz, bo są to zebrane różne typy managerów. Najważniejszy jest chyba w IT ten ostatni - tech lead manager.

[00:28:02.13] **Szymon Warda:** To jest częste.

[00:28:03.03] **Łukasz Kałużny:** Czyli jak developer będzie jednocześnie managerem.

[00:28:08.04] **Szymon Warda:** To jest ważne, najlepszy developer, żeby był managerem. Czyli osoba, która najlepiej koduje, niech teraz zarządza ludźmi. Po prostu...

[00:28:15.17] **Łukasz Kałużny:** Są jeszcze Hammer Manager, czyli mam młotek, będę traktował wszystko młotkiem.

[00:28:22.18] **Szymon Warda:** Kubernetes.

[00:28:24.14] **Łukasz Kałużny:** Tak. Bezgłowy kurczak, The Headless Chicken Manager: oh my god, oh my god, oh my god, I don't know how to do it. Więc jest ileś przykładów managerów, z których można się tutaj ponabijać. Ale za każdym z nich idzie sobie takie większe rozpisanie razem z tak zwanymi mitygacjami tutaj. Czyli pod tytułem, są trzy scenariusze, czyli jak naprawić sytuację, kiedy pracujesz dla takiego managera, gdy taki manager raportuje do Ciebie albo gdy odkryjesz, że sam jesteś tym typem menadżera.

[00:29:14.12] **Szymon Warda:** Ale którymś typem pewnie będziesz, realnie na to patrząc. Może jakimś miksem, ale  zawszeb którymś będziesz.

[00:29:20.15] **Łukasz Kałużny:** Będziesz przeważał.

[00:29:23.19] **Szymon Warda:** Warte w kierunku namierzenia, jak test psychologiczny, którym managerem jestem? Można by to wrzucić. Faktycznie, mimo że Ty to sprzedajesz jako taki dość zabawny, ale to jest naprawdę wartościowy link.

[00:29:35.05] **Łukasz Kałużny:** Jest wartościowy. Ja się tutaj wiesz, bo te opisy są zabawne, musi się sprzedać, w szczególności jak popatrzymy na sample, żeby zobaczyć, to one podkreślają ten... A nie, to, które Ty nazwałeś, to nie jest Tech Lead, tylko Smart Test Engineer Manager.

[00:29:53.09] **Szymon Warda:** Tak.

[00:29:53.17] **Łukasz Kałużny:** Jest oddzielnie wydzielony tutaj, w tym, Let's Promote the Smart Test.

[00:30:00.01] **Szymon Warda:** Ale jeszscze mitygacje są bardzo dobre. Naprawdę to jest dobra seira artykułów właściwie do umiejętnych umiejętności miękkich. To naprawdę jest dobre. Ja to sobie dokładnie przejrzę. Taka mała uwaga, że ta lista nie jest pełna, bo tam na samym dole jeszcze jest: the full list is here.

[00:30:22.22] **Łukasz Kałużny:** Tak, jest sporo różnych podejść, zwrotów, więc warto sobie to przejrzeć. Można powiedzieć, że trochę instrukcja obsługi Twojego managera w niektórych przypadkach w IT.

[00:30:40.23] **Szymon Warda:** Jak najbardziej. Dobra, ja mam bardzo krótki artykuł. Mianowicie to znowu jakiś raport, ok, niech będzie, odnośnie tego, że mamy wielki postęp, bo już teraz całe 52% aplikacji przechodzi pomyślnie test OWASP Top Ten. Ten, kto nie wie, niech wygoogla, bo trochę głupio nie wiedzieć. Sorry, że tak brutalnie, ale taka prawda. Cały raport, jest wzrost, ponieważ wcześniej było to 32%, więc super. Ok, cały raport zrobiony jest przez firmę, która dostarcza produkty odnośnie security, itd., więc z wielkim przymrużeniem oka bym na niego patrzył. Ale takie bardziej przypomnienie, że OWASP Top Ten dalej istnieje, warto rzucić okiem. I mimo całego AI hype'u, Kubernetes hype'u, itd., całego zachłyśnięcia, no to bezpieczeństwo aplikacji jest dalej ważne i przydałoby się sprawdzić, czy przynajmniej mamy majtki założone na dobrą stronę i czy po prostu nasze systemy działają jak powinny działać, a nie na zasadzie, że pewnie jest ok, bo niestety pewnie nie będzie ok. Tak że zerknijcie, przypominajka, zerknijcie na OWASP Top Ten i zobaczcie w których procentach się mieścicie właściwie, o tak.

[00:31:58.12] **Łukasz Kałużny:** Dobra. Pierdoła, o której nie wiedziałem w Docker Desktopie.

[00:32:03.02] **Szymon Warda:** Świetna pierdoła.

[00:32:04.12] **Łukasz Kałużny:** Świetna pierdoła, można sobie włączyć lokalnie multi node cluster. Czyli już Twój Docker, jak zrobisz kubectl get nodes, już nie zobaczysz jednego węzła, tylko zobaczysz X węzłów, które sobie ustawisz. Czyli możesz sobie symulować działanie lokalnie klastra.

[00:32:26.11] **Szymon Warda:** Tak, to jest ważne, to jest na jednej maszynie. Nie nie musimy włączać do tego komputera kolegi.

[00:32:32.22] **Łukasz Kałużny:** Tak, ja pod spodem, technicznie z tego już od dawna korzystałem, ale dla ludzi było to niewygodne. Jest taki tool w ramach Kubernetesa, który się nazywa Kind. On pozwala wam postawić węzły, postawić klaster kubernetesowy w kontenerach. Czyli ładujemy tu incepcję, jest tam specjalny obraz kontenera przygotowany pod odpalanie węzła kubernetesowego. I z takich ciekawych rzeczy, to świetnie się nadaje do nauki czy testowania różnych rzeczy, bo można przykładowo zainstalować sobie tam dowolnego, jak używacie czystego Kinda, to można zainstalować sobie dowolnego CNI-a przykładowo i robić różne dziwne, ciekawe setupy. A w tym miejscu to jest bardziej do przetestowania jak zachowuje się nasza aplikacja, albo to co robimy na wielonodowym klastrze, czyli wystarczy w ustawieniach Kubernetesa na naszym Docker Desktopie kliknąć Kind i powiedzieć ile chcemy mieć węzłów. I na tym kończy się setup.

[00:33:30.22] **Szymon Warda:** A suwaczkiem mozna polecić dość daleko, bo aż do 10 node'ów, więc...

[00:33:35.01] **Łukasz Kałużny:** 3 wystarczą pewnie albo dwa do takich testów zwykłych. 3 powiedzmy, o tak, powiedzmy, że będzie 3. Dobra, to co, kończymy.

[00:33:43.07] **Szymon Warda:** Kończymy. Tyle.

[00:33:44.14] **Łukasz Kałużny:** Na razie.

[00:33:45.06] **Szymon Warda:** Hej.

