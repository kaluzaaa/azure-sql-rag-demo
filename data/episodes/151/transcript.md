# 151.mp3

[00:00:11.180] **Łukasz Kałużny:** Cześć, słuchacie Patoarchitektów. Prowadzą Łukasz Kałużny...

[00:00:14.510] **Szymon Warda:** I Szymon Warda. Linki do odcinka - Patoarchitekci.io, gdzieś na dole, w opisie, wygooglacie, chaty, Claude i inne rzeczy, dacie radę, wierzymy w Was.

[00:00:24.320] **Łukasz Kałużny:** Tak, dobra, niedługo nadchodzą dwa szkolenia. Ja będę prowadził Architekturę 101, a Szymon Observability na open source.

[00:00:35.420] **Szymon Warda:** Tak, który się bardzo ładnie łączy z tym, co będziemy dzisiaj omawiali.

[00:00:39.410] **Łukasz Kałużny:** Tak? Nie dotykałem, nie widziałem. Dobra, słuchajcie, przyszło się pastwienie, a może i nie, zobaczę... Raczej inaczej, będzie pastwienie, o tak, jest parę punktów, gdzie będziemy się pastwić i to już widziałem.

[00:00:53.030] **Szymon Warda:** I zobaczymy, nie jest tak źle, ja uważam mimo wszystko.

[00:00:55.550] **Łukasz Kałużny:** Nie jest źle, jest w tym... A słuchajcie, omawiamy Technology Radar Volume 32 od firmy Thoughtworks, bo wyszedł, więc tutaj zgodnie z naszą kronikarską powinnością, to rzecz, nad którą regularnie się znęcamy, tudzież wyciągamy dobre rzeczy.

[00:01:14.900] **Szymon Warda:** Tak, a czasami olewamy jak jest faktycznie nudno i nic się nie dzieje. Ale ostatnio się dzieje, więc jak najbardziej rzucimy okiem.

[00:01:20.060] **Łukasz Kałużny:** I teraz ważne, Thoughtworks to jest taka duża firma doradcza, raczej mała firma doradcza względem dużych doradczych, bo jest tam z pięć, sześć tysięcy konsultantów. I oni zwykle co parę miesięcy wydają taki Technology Radar, czyli technologie, które używają w projektach, weszły im, PoC'ują, czyli nowe rzeczy z ich perspektywy, które sprzedają.

[00:01:44.660] **Szymon Warda:** Twierdzą, że używają ich, mają jakąś opinię, bo to fajnie wyjdzie w tym Radarze.

[00:01:49.820] **Łukasz Kałużny:** Tak, dokładnie. Dlatego jest to bardzo opinionated z perspektywy jednej, bardzo konkretnej firmy, ale daje rzeczy, które można wyciągnąć i opinie, które są czasem przydatne, niektóre nie. I słuchajcie, i to jest podzielone na cztery takie obszary: techniki, czyli rzeczy, które mówimy, w jaki sposób podchodzimy do czegoś. Platformy, czyli takie większe zbiory narzędzi. Toole małe narzędzia. I języki i frameworki, co można nazwać bardziej biblioteki i frameworki. Plus też narzędzia, które nie pasowały za bardzo do tools, bo można się kłócić, że czasem powinny być w toolach albo platformach.

[00:02:30.000] **Szymon Warda:** Tak, Languages and Framework to jest taki trochę bałagan tam. Ale dobra, każdy z tych rzeczy podzielony jest na takie trzy kręgi. Idąc od...

[00:02:37.200] **Łukasz Kałużny:** Cztery.

[00:02:37.530] **Szymon Warda:** Cztery kręgi, masz rację, tak, cztery kręgi. Idąc od najbardziej wewnętrznego, czyli adopt. To jest, gdzie oni twierdzą praktycznie, że używajcie po prostu. Bez większego myślenia można wziąć i użyjmy. Trial, to jest zróbcie poka, mówiąc bardzo prosto. A sens taki jak będziecie te typy narzędzi rozważać, to przy assessie rozważcie na poziomie możliwości i kosztów, co on w ogóle umie zrobić. I najciekawsze czasami, to jest hold, czyli nie używajcie.

[00:03:06.830] **Łukasz Kałużny:** Tak i u mnie chyba się przejawia status hold albo new na Radarze najczęściej w moich rzeczach. I słuchajcie, ja bym dodał jeszcze do trial i assess, ja czasami używam innej rzeczy. Assess to jest czasami mały PoC i sprawdzenie technologii, a trial może być pierwszym pilotem w jakiejś małej rzeczy, ale w sensie nie więcej niż mały pilot. Teraz jak popatrzymy.

[00:03:31.460] **Szymon Warda:** Dokładnie tak. Dobra, to lecimy.

[00:03:34.040] **Łukasz Kałużny:** To zaczynaj Szymon, bo tu są dwie zabawne rzeczy, które już były w sumie w Radarze, ale przypominają o nich.

[00:03:40.910] **Szymon Warda:** Jest parę rzeczy. W kręgu najbliższym, czyli w adopt, mamy: pierwsza rzecz to jest fast testing. I co do tego... Fast testing jest, nie, fast testing jest pierwszy raz w Radarze.

[00:03:53.300] **Łukasz Kałużny:** Jest pierwszy raz, a może źle oznaczyliśmy.

[00:03:55.820] **Szymon Warda:** Dobra, ale zapytacie: o co w ogóle w tym chodzi? Skupia się na tym, że w ogóle jaki mamy problem? Taki, że wszystkie modele AI-owe, LLM-y, itd., pytają w różnej formie w różne API i tworzy się po prostu bałagan. Więc fast testing jest pomysłem, żebyśmy ponaparzali do tego API różnymi zapytaniami i zabezpieczyli, żeby to API zachowywało się w miarę normalnie i się nam nie wykrzaczało itd. Opinia moja jest taka, że trochę nie czuję tego do końca. Okej, ma to sens.

[00:04:26.530] **Łukasz Kałużny:** Słuchaj, wiesz co, ja Ci powiem tak, to jest pytanie, ja np. tego w ogóle nie tknąłem w części, bo kurde, oni teraz mówią o randomowym, bo fast testing bierze się z niskopoziomowych języków, kiedy mamy C, C++ i w...

[00:04:43.540] **Szymon Warda:** Kontekście pamięci, itd.

[00:04:45.040] **Łukasz Kałużny:** Tak, szukamy memory leak'ów i innych rzeczy, buffer overflow, które się pojawią, żeby znaleźć podatność, którą zaczniemy ręcznie exploitować. Czyli zaczynamy randomowo nawalać.

[00:04:56.980] **Szymon Warda:** Tak, to jest takie testowanie, jest elementem czego? Testowania bezpieczeństwa. Więc wydzielenie tego do osobnego... Znaczy inaczej, to, co mówiłeś, to się działo już wcześniej, były takie pomysły. [Niesłyszalne 00:05:14] średnia.

[00:05:15.310] **Łukasz Kałużny:** Szymon, odpowiem ci inaczej. Jeżeli nie masz schemy zrobionej z walidacją, np. ma jakimś API management, polecamy się w tym temacie i nie walidujesz tego i nie detonujesz tego kodu pierwszy raz na wejściu do infry, to ten fast testing może być ciekawą rzeczą. Ale jeżeli walidujesz schemy, robisz walidację przed Twoim, co jest ważne, istotne, schemę powinniście walidować zanim trafi bezpośrednio do przetwarzania na waszym serwerze aplikacyjnym. Tylko właśnie jakieś reverse proxy, API gateway, jak to sobie nazwiecie, powinno to wysadzić i sprawdzić.

[00:05:54.340] **Szymon Warda:** Łukasz, tak, ale to, co mówiłeś, ile obecnie API pisane jest i to API, nie aplikacji, API HTTP pisanych w językach niskopoziomowych, bo głównie od tego jest właśnie wyłapywanie schemów.

[00:06:05.080] **Łukasz Kałużny:** Wiesz co, ja rozumiem jaka idea za tym szła, ale tak, zgadzam się, że jest to... Lepiej to zabezpieczyć niż w ogóle takie coś uprawiać i taniej będzie zrobić schematy.

[00:06:16.750] **Szymon Warda:** W językach zarządzanych mała jest tego wartość po prostu, mało rzeczy wyłapiemy. Może ewentualnie lepsze komunikaty błędów i zdecydujemy co raportujemy jako błąd, a co raportujemy jako załóżmy brak dostępu. Te rzeczy. Dobra.

[00:06:28.000] **Łukasz Kałużny:** Dobra. Drugi punkt dawaj, który wykopałeś?

[00:06:31.510] **Szymon Warda:** Drugie to jest coś, co już od dawna o tym mówimy, Software Bill of Materials, czyli SBOM tak zwany. On był poprzednio w trial w 2022 i bardzo dobrze. Tam w ogóle listują parę narzędzi, które lubimy i nie lubimy: Syft, Trivi, Snyk właśnie.

[00:06:51.100] **Łukasz Kałużny:** O co chodziło ze Snykiem? Bo ja już nie pamiętam. Hejtowaliśmy go chyba za stabilność.

[00:06:55.600] **Szymon Warda:** Za stabilność hejtowaliśmy go, za to, że ma dużo feature'ów, które potem w sumie nie do końca działają i że cholernie wolno działa i jest bardzo drogi.

[00:07:05.200] **Łukasz Kałużny:** Trzeba było sprawdzić jak teraz, co wolno i nie działa. Wreszcie można byłoby sprawdzić.

[00:07:10.150] **Szymon Warda:** Z tego co mi wychodzi, bo już nie bawię się nim bezpośrednio, niewiele się zmieniło.

[00:07:14.380] **Łukasz Kałużny:** Okej.

[00:07:17.260] **Szymon Warda:** Okej. W ogóle skąd to się wzięło? Bo to jest bardzo ważne czemu taki SBOM tak wyleciał z triala poprzednio, a teraz nagle jest w adopcie? Prosta rzecz. Regulacje prawne. Rząd brytyjski wprowadził AI Cybersecurity Code of Practice i CISA: AI Cybersecurity Collaboration Playbook i one właśnie wymagają. Kolejna rzecz to jest to, że regulacje chyba sprzed dwóch lat amerykańskiego bezpieczeństwa też wymagają, co [niesłyszalne 00:07:45]. W kontekście obrony przed supply chainem też często właśnie SBOM jest wymagany. I jest coraz więcej narzędzi, które to wspierają. Tak że tu polecamy. Efektem ubocznym posiadania dobrego SBOM-a jest też zarządzanie licencjami.

[00:08:02.070] **Łukasz Kałużny:** Właśnie chciałem powiedzieć, że to jest w ogóle oprócz SCA Supply Chaina, to jest drugi duży benefit.

[00:08:09.030] **Szymon Warda:** Tak, polecamy, korzystajcie. Ewidentnie jest w tym wartość i trzeba to robić.

[00:08:14.820] **Łukasz Kałużny:** Dobra, jeżeli teraz lecimy. Rzecz, która jest ciekawa, bo znalazła się w trialu. Ty też to miałeś wybrane, to Architecture Advice Process. I kurde, inaczej, mam mieszane uczucia.

[00:08:31.470] **Szymon Warda:** Wpierw powiedz co to jest.

[00:08:32.430] **Łukasz Kałużny:** Czyli założenie, że każdy może podejmować decyzje architektoniczne, tylko powinien zasięgnąć porady mądrzejszych w postaci formalnego procesu. Tak to można byłoby skrócić.

[00:08:44.370] **Szymon Warda:** Nie Łukasz, ujęcie inne: decentralized approach where anyone can make architecture decision, to się zgadzamy, provided they seek advice from those affected and thoes with relevant expertise.

[00:08:54.960] **Łukasz Kałużny:** Tak, tak jak mówię, że architektura jest kolektywna. To tutaj jest... Uważam, że taka osoba może zrobić ADR-a i powinien on przejść review i akceptację. Czyli sama idea, że każdy powinien kontrybuować do architektury jest super i zgadzam się, ale z tym, że to jest taka decentralizacja i takie relevant experience, bo z perspektywy juniora mid już będzie relevant.

[00:09:25.830] **Szymon Warda:** Znaczy to prowadzi do chaosu... Bo tam jest ważne zdanie, że oni stwierdzają, że właśnie Gildie Architektoniczne nie działają, że już to w ogóle spowalnia, itd. Częściowo się z tym zgodzę. Tylko jak mamy dużą organizację, to pewien poziom zwinności prowadzi w dłuższej perspektywie do bałaganu, bardzo proste. Inna bajka, że szukanie, żeby ktoś wiedział kto ma odpowiednie doświadczenie prowadzi do tego, że pytamy się najbliższych, to o czym powiedziałeś, zapyta swojego seniora albo Team Leada. No sorry, wylądujemy za 2 lata z całą kakofonią systemów różnych, które będą strasznie drogie w utrzymaniu.

[00:10:03.580] **Łukasz Kałużny:** I teraz mówienie, że gildie nie działają. Ja uważam, że ktoś...

[00:10:07.870] **Szymon Warda:** Ktoś coś źle zrobił.

[00:10:09.520] **Łukasz Kałużny:** Gildia jest miejscem wymiany wiedzy i dyskusje na temat standardów, a nie podejmowania decyzji w kontekście kawałka systemu. To jest taka rzecz, która ciągle chyba kuleje w świadomości, że takie... Myli komitety, architektury i takie ciała mocno standaryzacyjne z miejscem wymiany wiedzy.

[00:10:28.750] **Szymon Warda:** Dla mnie też bardziej problem jest tutaj, jak szybko one reagują i procesy wokół tego, żeby ci ludzie mieli na to czas, niż fakt, że wyrzucamy i wylewamy dziecko z kąpielą. Nie, to nie to.

[00:10:41.350] **Łukasz Kałużny:** Pomysł dobry, zwinniej akceptujmy ADR-y.

[00:10:46.210] **Szymon Warda:** Tak, tu się zgadzamy, jak najbardziej.

[00:10:47.800] **Łukasz Kałużny:** Dobra, następna rzecz, która mnie... Przepraszam.

[00:10:51.790] **Szymon Warda:** O, to jest ciekawe. Tak.

[00:10:53.260] **Łukasz Kałużny:** Słuchajcie, to jest rzecz, która powiedziałem, że ci ludzie, tak jak David Fowler powinien od Aspire kiedyś zdeployować aplikację na produkcję.

[00:11:01.270] **Szymon Warda:** Wstrzymaj się z tym, a to będzie...

[00:11:02.620] **Łukasz Kałużny:** Wiem, będziemy jeszcze hejtować Aspire nie jeden raz tutaj i inne wymysły Microsoftu, ale chyba robili wreszcie jakiś projekt na produkcji w branży regulowanej. To jest takie wrażenie.

[00:11:16.090] **Szymon Warda:** O czym mówimy?

[00:11:17.020] **Łukasz Kałużny:** Just in time privileged access management, czyli to, że w jakiejś chmurze czy narzędziu klikacie, że dostajecie, np. podbijacie sobie uprawnienia i klikacie MFA. Czy jeżeli są większe uprawnienia, to kolega z zespołu, właściciel systemu Wam akceptuje uprawnienia. I to pojawiło się jako trial.

[00:11:35.590] **Szymon Warda:** I co ważne to się odkłada w audycie i musisz powiedzieć czemu to masz i to jest na określony czas i jest jawnie ograniczony, że pewnych rzeczy nawet admin nie może robić z pudełka, tylko musi poprosić.

[00:11:45.550] **Łukasz Kałużny:** Tak i tutaj list privileges pojawia się w 2025 roku jako trial i new.

[00:11:54.540] **Szymon Warda:** Nie ogarniam, co się w ogóle wydarzyło. Tak. Jest to ciekawe.

[00:11:58.560] **Łukasz Kałużny:** Nowa CTO jest w raporcie też bym zauważył. Jest zmiana, już jest nowa CTO w raporcie.

[00:12:04.140] **Szymon Warda:** A to może być.

[00:12:05.520] **Łukasz Kałużny:** Taka ustąpiła już.

[00:12:07.740] **Szymon Warda:** Okej.

[00:12:08.850] **Łukasz Kałużny:** Dobra, idziemy dalej.

[00:12:09.480] **Szymon Warda:** Kolejna rzecz, która mnie zdziwiła właściwie, bo o tym było głośno i uważam, że to jest akurat bardzo dobry ruch - using GenAI to understand legacy codebased, czyli używanie modeli wszystkich AI-owych do rozumienia starych baz kodu. To jest trial. Było to w ogóle w assess od stycznia 2024.

[00:12:33.150] **Łukasz Kałużny:** Nie, jest w trialu, było już w tym, więc... Dobra, nie patrząc się było, to nie jest nowa rzecz w ogóle w raporcie.

[00:12:41.760] **Szymon Warda:** Tak, ale to jest coś, co już się dzieje. Akurat jeżeli chodzi o tego typu zachowania, to widzimy bardzo dużą wartość w tym. I sorry, tu czekamy tylko na narzędzia, żeby się trochę polepszyły, ale one też już się pojawiają, więc dziwi mnie, że to jest tak nisko.

[00:12:56.420] **Łukasz Kałużny:** Dobra. Czy wiesz, z drugiej strony trzeba... Okej, dobra. Jeszcze co masz w assessie, bo ty wybrałeś coś z assessu.

[00:13:03.470] **Szymon Warda:** Już Ci mówię o assessie - AI-powered UI Testing. Coś, o czym mówiłem rok temu, jak się pojawiał ten cały ruch, czyli mianowicie podejście, że okej, testowanie UI jest niewyobrażalnie kosztowne, zmienia się, jest bardzo niestabilne, no i jest to droga przez mękę, każdy, kto o tym mówił. I nie mówię o testowaniu HTTP, tylko mówię o testowaniu, weryfikacji UI. I teraz tu się pojawiły dwa fajne podejścia. Po pierwsze, jest pierwszy raz w assessie, to jest bardzo ważne, a narzędzia się podzieliły na dwie kategorie: modele modularne, takie sfine-tune'owane na procesowanie zdjęć UI-owych, no nie. Czyli patrzymy na czystą grafikę, czystego PNG, BMP, itd. Drugie podejście, to jest połączenie właśnie modelów multimodalnych z playwait. I on daje informacji odnośnie o strukturze HTML-a. I to jest też dość ciekawe podejście, fajnie to będzie wyglądało. Ja będę bardzo mocno obserwował rozwój tego rynku, bo tu się będą działy naprawdę, naprawdę ciekawe rzeczy. Super, że to się pojawia. Wydaje mi się, że z całego testowania, całych rzeczy UI-owych, to to może być naprawdę małą rewolucją, jeżeli wypali w formie dobrych narzędzi, a ma szansę.

[00:14:19.130] **Łukasz Kałużny:** Dobra, to idziemy słuchajcie do mojego ukochanego holda. Dobra i pierwsza rzecz, która się tutaj pojawia, cieszy mnie, że to od razu się pojawiło. Z tym się zgadzam: AI accelerated shadow IT.

[00:14:34.190] **Szymon Warda:** Tak, jest w holdzie.

[00:14:34.880] **Łukasz Kałużny:** Czyli powiedzmy sobie wprost, dla osób nietechnologicznych, nie dla psa kiełbasa, jak z low-codem, no-codem. Sorry, rozwiązania AI, jeżeli chodzi o technologię, generowanie i inne rzeczy, powinny zostać w IT. I osoby, które są power userami z biznesu tak zwanego, które nie są z IT, sorry, nie mają pojęcia co robią. I to jest podkreślone w tym, że trzeba to, tak jak było z chmurą, należy to ubijać.

[00:15:10.640] **Szymon Warda:** To jest nie do utrzymania na dłuższą metę, bym tak powiedział. Tak.

[00:15:14.240] **Łukasz Kałużny:** To jest piękne. Następna rzecz, która się pojawiła, co mnie cieszy, to local coding assistant, czyli te narzędzia, o których jeszcze dzisiaj będziemy zaraz wspominać, do kodowania ze wsparciem AI, tak jak Cursor, VS Code, że odpalamy sobie lokalnie model na swojej stacji i żeby nie wysyłać tego do serwera, mieć to wszystko u siebie. Jest słusznie na hold, ponieważ przepalasz na to pieniądze i czas, a nie ma z tego żadnej wartości, bo jakość jest tego wbrew pozorom mniejsza.

[00:15:50.580] **Szymon Warda:** Doprecyzujmy jakość. Te modele po prostu są zbyt wolne, żeby działając na lokalnej maszynie, albo są zbyt okrojone i działają szybko. Nie mamy tyle kasy i tyle hardware, żeby władować, żeby komputer każdego developera w odpowiednie karty wyposażyć.

[00:16:06.600] **Łukasz Kałużny:** Zobaczymy jak postawię sobie na biurku 2 DGT-sy, jeżeli uda mi się kupić, wypowiem się na ten temat za parę miesięcy. Więc zobaczymy co to będzie.

[00:16:16.980] **Szymon Warda:** Łukasz, ale mamy teraz jeszcze jedną wspólną rzecz na holdzie.

[00:16:20.040] **Łukasz Kałużny:** Tak, jest cudowna.

[00:16:21.450] **Szymon Warda:** Przygotowujemy to osobno. Widzimy to w momencie jak się łączy ten doc, co tam...

[00:16:25.740] **Łukasz Kałużny:** Tak.

[00:16:26.790] **Szymon Warda:** SAFe jest na holdzie, czyli Scaled Agile Framework. Jest na holdzie, pokazują, że to w ogóle nie działa. Znaczy ładnie ujmują to, że to nie działa, to, że zwalnia, że robi się z tego po prostu powoli waterfall i to w ogóle nie gra.

[00:16:44.010] **Łukasz Kałużny:** Inaczej, to jest: zróbmy Agile, ale miejmy waterfall i miejmy dupokrytki na wszystko, ale jesteśmy zwinni.

[00:16:52.280] **Szymon Warda:** Tak, SAFe, kto ma doświadczenie, ten doskonale wie. Nie znam osoby, która by z tego była zadowolona.

[00:16:58.160] **Łukasz Kałużny:** Słuchaj, przepraszam, mamy wspólnego kolegę, który jest architektem, ma papier architekta i cieszy się, bo jak jest większość spotkań, to może przechodzić kolejne, grać na Xboxie w trakcie spotkań, bo i tak się nic nie wydarzy.

[00:17:11.900] **Szymon Warda:** Tam się nic nie dzieje, dokładnie. Dobra, kolejny obszar, tools, czyli narzędzia.

[00:17:17.630] **Łukasz Kałużny:** No to co? Bo Ty masz najwięcej tutaj. Więc zacznijmy od triala.

[00:17:22.580] **Szymon Warda:** Kilka rzeczy, bo to się ze sobą łączy. Claude Sonnet. Pierwszy raz. Jest. No to korzystamy obydwaj, wyniki bardzo fajne.

[00:17:32.990] **Łukasz Kałużny:** Tak. Szymon się przekonał.

[00:17:35.690] **Szymon Warda:** Tak, zdecydowanie tak. Dobra, idziemy dalej. Klein, tak się chyba to czyta.

[00:17:42.350] **Łukasz Kałużny:** No.

[00:17:44.720] **Szymon Warda:** CLI and Editor. Pierwszy raz trial, nie ma co się dziwić. To jest wtyczka do Visual Studio Code. Trochę taka alternatywa do Cursora. Co tam możesz zrobić? Możesz mieć plain text and act mode, wykorzystywanie MCP, o którym Ty powiesz za jakiś czas, czym jest MCP. Dobrze współpracuje z Claude, wsparcie dla dużych baz kodu, jakkolwiek to nazwiemy, codebases po angielsku, ładnie. Wsparcie dla Headless Browser Testing, to też jest przydatne i przechowuje dane lokalnie, ale dane, nie model jako taki.

[00:18:17.650] **Łukasz Kałużny:** No i wiesz tylko, że musisz podać klucz API do modelu. I teraz zaczynamy się bawić, czy przypadkiem VS Code, bo tryb agentowy, jak teraz to już nagrywamy, to jest już w GA tryb agentowy do Visual Studio Code, więc patrząc na cenę, że będziesz korzystał z jakiegoś tam modelu, czy na Cursora, którego zaraz będziesz miał... I wiesz co ja na to? Rozważałem to, czy nie wrzucić tego w API i sobie darowałem. Jedyna z takich rzeczy zewnętrznych, która mnie zainteresowała i nie ma, ją też gdzieś tam na boku testuję sobie, to jest konsolowy agent w postaci plode code, czyli jest tam taki agent command line'owy zupełnie, który Ci pracuje na codebase. I tutaj to jest, np. tak jak ja na to popatrzyłem, to jeszcze trzy tygodnie temu, czyli gdzieś tam pod koniec marca, ten Klein był bardzo ciekawą rzeczą, którą nawet sobie na nią popatrzyłem i w ogóle okej. Jedyna rzecz, która jest z niego wartościowa, jak wyciągamy, to jest ten Headless Browser Support.

[00:19:25.390] **Szymon Warda:** Tak, to robi różnicę.

[00:19:26.050] **Łukasz Kałużny:** Wbudowany.

[00:19:26.680] **Szymon Warda:** To jest fajne.

[00:19:28.150] **Łukasz Kałużny:** Ale reszta...

[00:19:29.740] **Szymon Warda:** Reszta, Cursor jest lepszy finalnie.

[00:19:32.920] **Łukasz Kałużny:** No i właśnie Szymon, Cursor. To jest... Szymon był jak z mema przy tej pozycji.

[00:19:39.460] **Szymon Warda:** To lecimy w takim razie rzeczy formalnych. Był w assess w październiku 2024, żeby było, wsparcie dla MCP, odnoszenie się do [niesłyszalne 00:19:50], to jest bardzo fajne, do poprzednich rozmów, przeszukiwanie sieci, do dokumentacji bibliotek też się umie odnosić. Więc sporo fajnych rzeczy umie zrobić. Jest liderem na rynku. No nie oszukujmy się, oni tutaj wymiatają po prostu i działa fajnie, mogę powiedzieć też tyle. Robi to robotę.

[00:20:07.270] **Łukasz Kałużny:** Przepraszam, jeszcze dorzucę. Szymon od razu przy tym wziął i poleciał jak z mema, bożesz, ten z pieniędzmi, to jest kultowy serial animowany i zapomniałem nazwę.

[00:20:20.590] **Szymon Warda:** Futurama oczywiście.

[00:20:21.490] **Łukasz Kałużny:** Z Futuram, tak, Szymon był jak z Futuramy: bierzcie moją kartę, bierzcie moje pieniądze, jak zobaczył po ostatnich release'ach jak to działa.

[00:20:28.990] **Szymon Warda:** Tak, robi wrażenie, naprawdę robi. Mi się przypominają czasy kodowania, kiedy odpalasz prostą komendę i mówisz idę coś zrobić, bo właśnie się build'uje, a ona po prostu przelicza rzeczy.

[00:20:42.070] **Łukasz Kałużny:** Tak, za dwa trzy odcinki podyskutujemy o tym jeszcze, więc damy Wam nasze wrażenia i spostrzeżenia na ten temat.

[00:20:48.430] **Szymon Warda:** A teraz mam jeszcze jedną rzecz, parę rzeczy mam, ale generalnie jedna rzecz, która faktycznie zrobiła na mnie wrażenie - D2.

[00:20:55.750] **Łukasz Kałużny:** No właśnie, kurde, ja to wyrzuciłem, bo w ogóle czemu.

[00:20:59.980] **Szymon Warda:** Nie mylić z D3. Bo jest biblioteka D3.js, która rysuje, robi wizualizację. D2 jest czymś zupełnie innym. To jest taki Mermaid, czyli język do rysowania diagramów. I to jest w ogóle pierwszy raz trial. Mnie to zaciekawiło bardzo mocno, bo to wygląda fajnie. Tak, składnia nie jest w Yamlu, co jest ogromnym plusem, jest taka bardziej mermaidowa z powiedzmy...

[00:21:25.300] **Łukasz Kałużny:** Ale właśnie Szymon, co jest plusem realnie? Co jest realnie plusem, bo ja nie widzę wartości, tak jak sobie na to popatrzę.

[00:21:31.570] **Szymon Warda:** Właśnie przejdziemy do tego, bo mnie to zaciekawiło. Tak, to ma dwie opcje jak można tego używać. Jest taki playground, który po prostu, jak Mermaid tak naprawdę, tam niewiele się dzieje. Druga opcja to jest to, że ma swoje studio. I studio jest ciekawe, bo studio umożliwia przejścia między poziomami diagramów, to samo co się dzieje w C4. Klikasz i sobie wchodzisz głębiej, głębiej, wyżej, itd.

[00:21:55.090] **Łukasz Kałużny:** Dobra, czyli trochę struktura jest.

[00:21:55.960] **Szymon Warda:** To robi wrażenie. Ale teraz uważaj, czemu ja uważam, że to nie ma większego sensu? Bo ta cała mapa, która jest, którą się poruszasz w górę, w dół jest w jednym pliku. I nawet na ich przykładach bardzo prostej architektury azure'owej, itd., ten plik zaczyna być duży i tak nieczytelny.

[00:22:16.870] **Łukasz Kałużny:** Czyli jednak kit.

[00:22:19.690] **Łukasz Kałużny:** Czekaj, jeszcze jedna rzecz. Wiesz ile kosztuje studio ich?

[00:22:22.360] **Łukasz Kałużny:** Ile?

[00:22:23.020] **Szymon Warda:** 25 dolarów za użytkownika miesięcznie.

[00:22:26.470] **Łukasz Kałużny:** Dobra, pomińmy to, przejdźmy dalej. To jest rzecz, którą wydłubałeś, na którą nie popatrzyłem ze względu na nazwę, a jest super.

[00:22:34.840] **Szymon Warda:** Tak, znaczy jedna rzecz, moja rekomendacja, studio - fajne, ale chyba to jeszcze nie teraz. Playground od diagramów naprawdę jest fajny. To robi robotę, ma pełne wsparcie dla języka, itd. Zobaczcie w kontekście np. alternatywy do Mermaid, chociaż może Mermaid być ciekawszy. Mermaid trochę słabo wygląda wizualnie, to wygląda dużo ładniej, dużo bardziej profesjonalne.

[00:22:54.580] **Łukasz Kałużny:** Ale tylko tyle.

[00:22:55.600] **Szymon Warda:** Tak, dokładnie. Dobra, bo się rozgadałem. Teraz Ty lecisz.

[00:22:59.380] **Łukasz Kałużny:** Wiesz co, ale to Twój jest jeszcze JSON Crack, gdzie cena jest uczciwa Szymon, bo za darmo, jak w Kapitanie Bombie. Nie. Tak, w Kapitanie Bombie bodajże.

[00:23:08.800] **Szymon Warda:** Co to jest? Bo to jest pierwszy raz trial, to jest narzędzie, które wizualizuje strukturę JSON i Yamla. Czyli widzicie takie ładne przejścia, że tu mamy taki duży plik i on ma takie podsekcje, on się dzieli na podsekcje, itd. Ja do końca nie rozumiem sensowności tego narzędzia.

[00:23:25.540] **Łukasz Kałużny:** Czy wiesz co, ale ja czasami jak mam z jakiegoś API, rozpoznaję sobie odpowiedzi i inne rzeczy, struktury, do których nie ma schematów lub muszę przejrzeć jakieś tam dziwolągi czy Yamle, to może być ciekawe Szymon pod tym względem.

[00:23:39.070] **Szymon Warda:** Ja mam do tego zastosowanie takie, że jak załóżmy widzę jakiegoś Yamla kubernetesowego, gdzie on po prostu, gdzie w jednym pliku mamy wszystko, wtedy okej, to może mieć sens. Ale to i tak się zamieni szybko w potwora. W sensie dla mnie fajne, ale np. zwijanie w kodzie gdzie może zwijać sekcje, szybsze w użyciu wydaje mi się mimo wszystko...

[00:23:58.440] **Łukasz Kałużny:** Wiesz co, zobaczę. Inaczej, doinstalowałem sobie to, bo otwieram i zobaczę sobie jak to będzie wyglądało przy takich typowych wiesz innych elementach, których się używa. Bo jestem ciekaw. Wiesz, nie mówię nie, to bardziej taki jako dodatkowy. To nie, że to jest tam wow super, tylko taki nice to have, które za tą uczciwą cenę dorzucę.

[00:24:21.660] **Szymon Warda:** Jestem ciekaw jak będziesz z tego często korzystał, bo to fajnie wygląda, ale zobaczymy.

[00:24:26.730] **Łukasz Kałużny:** Ja dlatego mówię doinstalowałem. Dobra, pierwsza rzecz, która mnie w tym rozwaliła.

[00:24:36.450] **Szymon Warda:** Assess, zakładam mówisz.

[00:24:39.360] **Łukasz Kałużny:** Tak, już w assessie, Jujutsu, nawet ciężko to wygooglać jak sobie wrzucicie. Ktoś wymyślił nowy VCS, czyli alternatywę dla Gita. Alternatywę dla Gita, nowy dystrybuowany Version Control, który jest kompatybilny z Gitem. I kurde zastanawiam się... Dużo... Inaczej, słyszałem opinie, że Git to zło, że ma ciężki poziom wejścia i w ogóle. I tak się zastanawiam, o co w ogóle chodzi?

[00:25:27.870] **Szymon Warda:** Oni sprzedają się tym, że są both simple and powerful. Naprawdę, jeżeli nie wchodzi się w zaawansowane komendy gitowe, to to są rzeczy, które można spokojnie i UI-em ogarnąć. Tam mówimy o sześciu komendach, około, nie liczyłem dokładnie na paluszkach, ale wydaje mi się, że coś koło tego. Tak że też, nie rozumiem jaki problem rozwiązujemy na chwilę obecną. Może Git jest trudny dla osób, które wchodzą, które są spoza kodowania i właśnie power userów, w tym kontekście się zgodzę.

[00:25:58.500] **Łukasz Kałużny:** Tak, ale dla nich, jak powiedzieliśmy, no sorry.

[00:26:03.270] **Szymon Warda:** Ale oni będą mieli: git add., git commit i git push.

[00:26:07.230] **Łukasz Kałużny:** Raczej tak, raczej robione z GUI-a. No i tylko... Inaczej, najtrudniejszą rzeczą, którą żadne narzędzie nie rozwiąże, to będą i tak merge.

[00:26:15.480] **Szymon Warda:** Tak.

[00:26:16.710] **Łukasz Kałużny:** Więc tego nie rozwiąże. Więc to w ramach ciekawostki, bo... Inaczej, są inne systemy, które gdzieś tam są. Jest ten, nie pamiętam jak się nazywa, googlowski, jest też w gamingu, jest też wykorzystywane inne repa, ale to ze względu na assety i inne takie rzeczy, które też się tam walają.

[00:26:33.870] **Szymon Warda:** Binarki po prostu różne.

[00:26:35.100] **Łukasz Kałużny:** Tak, więc to jest zupełnie inne. Więc tak, w większości przypadków, sorry, trochę nie rozumiem.

[00:26:44.480] **Szymon Warda:** Dobra, to lecimy do kolejnego.

[00:26:46.730] **Łukasz Kałużny:** Dobra i kolejne co mnie zainteresowało do sprawdzenia, bo nie sprawdziłem jeszcze tego, od ClickHouse'a Kubenetmon do monitoringu sieci. Który pozwala monitorować przepływ, ten, pozwala w ClickHousie... Właśnie, w ClickHousie i to jest problem, ale pozwala trzymać logi komunikacyjne.

[00:27:10.820] **Szymon Warda:** Dla trzech providerów AWS, GCP i Azure.

[00:27:13.760] **Łukasz Kałużny:** Tak.

[00:27:14.930] **Szymon Warda:** Czyli monitorujemy ile tam danych wchodzi i wychodzi, żebyśmy też wiedzieli ile zapłacimy i co się tam właściwie dzieje.

[00:27:20.690] **Łukasz Kałużny:** Dokładnie, żeby zrobić też rozliczalność. I to jest w ogóle ciekawa... Inaczej, sama koncepcja wygląda ciekawie z perspektywy, słuchajcie, do zrobienia sobie chargebacków bardziej dokładnych w niektórych miejscach albo zobaczenia co się dzieje, jak wygląda ruch sieciowy. Dlatego mówię ciekawe do sprawdzenia. I ten assess świetnie tu pasuje.

[00:27:45.020] **Szymon Warda:** Ja bym się z tym zgodził. Tym bardziej jak mówimy, mieliśmy trochę klastrów rozpiętych pomiędzy chmurami a onpremem, a chmurami i chmurami, tak że w tym kontekście...

[00:27:52.430] **Łukasz Kałużny:** Aplikacji, tak, żeby sobie poszukać co z czym gada.

[00:27:55.430] **Szymon Warda:** Dokładnie. Dobra, to teraz dwie rzeczy. Jedna taka na zasadzie, że może - AnythingLLM. Pierwsze, jest w assess, aplikacja desktopowa, która łączy modele komercyjne z lokalnymi dokumentami. I to jest fajne. Oczywiście wiadomo, że wspiera, pełna kompatybilność z MCP, kreator agentów AI bez kodowania i tego typu rzeczy, obsługa wielu dokumentów. No ogólnie rzecz biorąc umie zaciągać to co mamy lokalnie i ładnie się odpytywać naszego ukochanego AI co tam się znajdzie. Zobaczmy, pobawcie się. Tyle.

[00:28:29.750] **Łukasz Kałużny:** Ja raczej nie widzę w tym sensie, tak osobiście no nie mam akurat ten...

[00:28:35.090] **Szymon Warda:** Assess jest idealnym miejscem na to, ustalmy, do zobaczenia. Ale druga rzecz jest fajniejsza, chociaż mogłaby być jeszcze fajniejsza - Hurl. Czym jest Hurl? Pierwsze, jest w assess. Nie wiem czy pamiętacie, wielokrotnie chwaliliśmy takie narzędzie jak z VS Code'a - HTTP Client czy tam HTTP Rest Client, jakoś tak się nazywa. Taki, że mamy sobie tekst i piszemy tam powiedzmy get jakiś tam URL, możemy dać zawartość, możemy dać headery, tego typu rzeczy, klikamy, ona wysyła nam ładnie requesty. Super to działa. Dobra, problem jest taki, że nie umie parsować odpowiedzi, nie umie paru rzeczy zrobić i działa w Code'dzie. A Hurl to właśnie jest krok dalej, czyli umie parsować odpowiedzi, umie [niesłyszalne 00:29:17] rzeczy do zmiennych, umie robić weryfikację i ma narzędzie CLI, żeby to wpiąć w CI/CD jako testy. I teraz czemu twierdzę, że paru rzeczy brakuje? Nie ma operacji warunkowych, czyli nie mamy IF-ów, nie mamy switchy, nie mamy nic z tych rzeczy. Czyli możemy rzeczy przekazywać, ale nie możemy podejmować warunkowych operacji i warunkowych akcji w wyniku tego, co się wydarzyło w requeście. Tak że fajnie wygląda, będę obserwował czy to się może dalej rozwinie, bo IF-y by się przydały. No jak ktoś ma jakoś dużo Postmana, to np. to może być fajną alternatywą, bo ten kod naprawdę fajnie wygląda i jest czytelny.

[00:29:56.840] **Łukasz Kałużny:** Czekaj, aż muszę coś sprawdzić.

[00:29:59.390] **Szymon Warda:** No dajesz.

[00:30:01.670] **Łukasz Kałużny:** Jedną rzecz pozwól. Zaraz Wam powiem czego, bo mi się wydawało, że część rzeczy dało się w tym, że REST Client, chyba dało się coś z bodziaka wyjąć, wiesz, z response'a.

[00:30:16.520] **Szymon Warda:** Ale przekazanie do zmiennych, tego już nie mogłeś zrobić. Może coś pozmieniali ostatnio, ale to dalej...

[00:30:21.770] **Łukasz Kałużny:** Nie dam sobie ręki uciąć. Więc wiesz, to jest tak idąc... Dobra, jesteśmy, dobra, to co platformy Szymon? I co pierwsze?

[00:30:29.750] **Szymon Warda:** Jeszcze ważna rzecz, nie ma nic on holda w toolach.

[00:30:33.020] **Łukasz Kałużny:** A tak, faktycznie.

[00:30:35.840] **Szymon Warda:** Platformy.

[00:30:37.250] **Łukasz Kałużny:** Platformy, to w sumie Ty jesteś platformy, ja tylko będę szydził po drodze. Zacznij od adopta.

[00:30:44.120] **Szymon Warda:** No właśnie. A w adopcie jest GitLab CI/CD, co mnie zdziwiło w ogóle, bo to jest bardzo mocna rekomendacja. I teraz takich trochę kronikarskich rzeczy. On był w trialu ostatnio w 2022, czyli trzy lata temu był w trialu i nagle wyskoczył i pojawił się. Tam go chwalą przez rzeczy odnośnie skanowania kodu, itd. Ale nie ogarniam czemu nagle wyskoczyli z adoptem w tym momencie. Możliwe do tego, co Ty mówisz, że nagle jakiś duży klient, który ma regulacje i musi mieć na onpremie, bo faktycznie GitLab CI/CD fajnie się spisuje na onpremie i...

[00:31:24.920] **Łukasz Kałużny:** Cloudowy jest, cloudowy też jest spoko. Inaczej, czy GitLab czy GitHub - preferencje. Ma parę fajnych... GitLab, ten SAS-owy, też ma parę fajnych rzeczy, w szczególności w CI/CD ma trochę sporo ciekawych tych elementów.

[00:31:39.850] **Szymon Warda:** Dobre narzędzia ogólnie rzecz biorąc, bez dwóch zdań. Dziwiło mnie, że nagle to wyskoczyło aż tak wysoko. No i teraz Łukasz kolejny w trialu jest Dapr.

[00:31:47.080] **Łukasz Kałużny:** Co on tam robi? Dla zrozumienia, Microsoft próbował zrobić agnostyczną nakładkę aplikacyjną service mesha na poziomie aplikacyjnym, bo tak to trzeba nazwać.

[00:31:59.530] **Szymon Warda:** Żeby było jasne, to ideowo to jest świetny pomysł.

[00:32:02.470] **Łukasz Kałużny:** Tak, na papierze, Dapr - Distributed Application Runtime, czyli to był service... To miał być service mesh, który rozumie komunikację synchroniczną i asynchroniczną, uwierzytelnianie i łatwo się wpina w to swoje aplikacje. Na papierze przez długi czas w to wierzyliśmy.

[00:32:24.490] **Szymon Warda:** Ale nie przyjęło się na rynku.

[00:32:27.070] **Łukasz Kałużny:** Tylko oddane do CNCF-u, gdzieś tam sobie żyje w swojej niszy. Jakość taka sobie. Microsoft w ogóle, to taka ciekawostka, wycofał wszystkich ludzi od Dapra, z tego open sourceowego projektu, wszystkich inżynierów zabrał, więc projekt sobie żyje swoim życiem w tym. I słuchajcie, ja nie wiem co to robi w ogóle w trialu.

[00:32:48.100] **Szymon Warda:** Ja też nie.

[00:32:48.250] **Łukasz Kałużny:** To powinno być double hold.

[00:32:53.170] **Szymon Warda:** Mówiliśmy, ostatni raz było w assessie w 2023, więc tak, no tak, czemu to wypaliło? Ale teraz idziemy do rzeczy, które mają sens.

[00:33:01.900] **Łukasz Kałużny:** No właśnie, dajesz.

[00:33:02.860] **Szymon Warda:** Grafana gwiazdka, bo jest tak - Grafana Alloy, Grafana Loki i Grafana Tempo. Wszystko co się liczy od Grafany. No i zakładam, że Grafna też jako taka jest w assessie i chwalą to bardzo, bardzo mocno. Ja się pod tym zgodzę, bo o tym też jest mocno bardzo szkolenie z Observability, bo to są bardzo fajne narzędzia, które wymagają conieco tego, żeby trochę przeorać mózgi developerów i jeszcze OPS-ów, żeby nie mieli Full Text Search'a.

[00:33:31.540] **Łukasz Kałużny:** Wiesz co, ja bym powiedział, że trzeba tylko oduczyć się Full Text Search'a.

[00:33:38.860] **Szymon Warda:** Tak, ale to są super narzędzia. Jeszcze jak mówimy o całym systemie do integracji, itd., jak aktualnie ze sobą gra, rewelka. Na tym buduje się świetne platformy do monitorowania. Dla skali, to są narzędzia, które wymagają lepszego skalowania, jak mówimy ile terabajtów danych przyjmiemy miesięcznie tak naprawdę. Więc bardzo fajnie, cieszy mnie, że to zostało zauważone.

[00:34:02.530] **Łukasz Kałużny:** W szczególności scaling był piękny na tym, jak pokazane, jak mało potrzeba.

[00:34:07.660] **Szymon Warda:** Tak.

[00:34:08.590] **Łukasz Kałużny:** Dobra, słuchaj, coś mnie zaciekawiło. Pierwsza rzecz...

[00:34:13.630] **Szymon Warda:** Mnie też.

[00:34:14.110] **Łukasz Kałużny:** Ciebie też, że nie wiem czemu jest to w platformach w ogóle, a mówię o DeepSeeku.

[00:34:20.260] **Szymon Warda:** Tak.

[00:34:20.770] **Łukasz Kałużny:** DeepSeeku R1, czyli tym pierwszym otwartym reasoningowym. Dobra...

[00:34:26.440] **Szymon Warda:** Chińskim modelu.

[00:34:27.730] **Łukasz Kałużny:** Chińskim, tak. Inaczej, czy całość, że znalazł się tutaj, nie dziwi mnie, bo DeepSeek miał bardzo ważne dwa elementy, które zrobił. Zrobił korektę na giełdzie oczekiwań. I pokazał, że da się zrobić to taniej.

[00:34:47.060] **Szymon Warda:** Tak.

[00:34:47.750] **Łukasz Kałużny:** A trzecia, dał dużo open source, że ludzie zaczęli eksperymentować z destylacją modeli i uczeniem reasoningu mniejszych modeli.

[00:34:55.670] **Szymon Warda:** To teraz co jest tu ważne? To jest po pierwsze, w DeepSeeku, przeczytałem dokładnie notatkę, nie ma żadnych informacji o ich doświadczeniach. Oni piszą ogólnie, piszą bardzo, bardzo ogólnie o DeepSeeku. Jest to oparte na własnym... Z reguły to PR mówi, że na własnych, nasi inżynierowie, itd. Tu nie ma takich zdań. To jest bardzo ważne. Moja teoria czemu się to pojawiło? To pojawiło się dlatego, że ktoś robi ukłon w kierunku pewnego rynku obstawiam i to musiało się pojawić jako to, że nie są tylko nastawieni na modele europejsko-amerykańskie powiedzmy sobie tak i też pewnie rozszerzenie wpływów. Więc pojawienie się tego i komentarze jakie są, według mnie mimo wszystko chyba sprzedażowy trochę element, pochwalenie się co i jak.

[00:35:41.360] **Łukasz Kałużny:** Dokładnie i tyle. I słuchajcie, jak pójdziemy, co my tam dalej mamy? A właśnie Deno, który wybrałeś.

[00:35:49.370] **Szymon Warda:** Deno, który wybraliśmy, bo mówiliśmy o nim w poprzednim odcinku.

[00:35:52.250] **Łukasz Kałużny:** Akurat ty je sam wybrałeś, ja go nie wybrałem.

[00:35:54.260] **Szymon Warda:** O co chodzi? Mówiliśmy w poprzednim odcinku odnośnie tego, co się dzieje w okolicy TypeScript, jak się zachowuje. Deno, który pierwszy raz było w assess w 2019 roku. Runtime dla JavaScriptu, ale głównie tak naprawdę dla TypeScriptu, alternatywa dla Node'a. Parę rzeczy, ma lepszy sandboxing, lepszą dependency management i natywne wsparcie właśnie dla TypeScripta. Jestem ciekaw jak to się rozwinie, bo zaczyna ewidentnie nabierać trochę wiatru w żagle. Cały ten ekosystem wokół JavaScript, Node, NodeJS, itd., jest ciekawy też z racji na to, co będziemy mieli w dalszych jeszcze on holdach, że tak powiem. Już trochę zdradzę tajemnicę co się tam wydarzyło. Dla mnie ciekawe do rozważenia, że tak powiem. Tyle.

[00:36:43.750] **Łukasz Kałużny:** Dobra. Dobra, jeżeli słuchajcie popatrzymy sobie dalej, to w assesie nowy, co już wspominaliśmy, od Anthropica specyfikacja - Model Context Protocol, czyli w jaki sposób wystawiać świat zewnętrzny w postaci API integracji do modeli. Czyli jak zrobić to, żeby model lepiej umiał wołać zewnętrzne narzędzia.

[00:37:09.580] **Szymon Warda:** Czy to powinno być w assessie? Czy to nie jest trochę za nisko, że tak powiem?

[00:37:13.030] **Łukasz Kałużny:** Czy wiesz co, inaczej, teraz jest problem, to też będziemy niedługo o tym dyskutować oddzielnie. Słuchaj, Szymon, właśnie i to jest z jednej strony tak, ja patrzę teraz po pierwszej rozmowie, którą gdzieś tam mam np. z klientem na temat pewnej standaryzacji, no, to jest jedyna rzecz, którą możesz powiedzieć, że jest to jedyna specyfikacja i patrząc się na rynek wiodąca.

[00:37:33.370] **Szymon Warda:** Absolutnie tak. Dokładnie.

[00:37:35.170] **Łukasz Kałużny:** Tak. Jest teraz boom, hype, przehajpowane jest to za bardzo, nie wiadomo dlaczego. Olejmy sposób. Sama logika, że ta specyfikacja to jest coś, co świetnie, że powstało. No i jak rozmawiamy to też wyszedł na rynek wczoraj, w momencie nagrywania, agent-to-agent, którego tutaj nie zaznacie. Czyli mamy dwie specyfikacje, które zamykają nam wszystkie potrzeby standaryzacji komunikacji z LLM-ami.

[00:38:00.880] **Szymon Warda:** Znaczy może uprośćmy tak. Czy jest sens pisania MCP teraz po prostu, żeby było? Nie, nie ma. Ale jeżeli piszemy cokolwiek, żeby się komunikować z agentami, no to mamy jeden wybór - MCP tak naprawdę.

[00:38:14.440] **Łukasz Kałużny:** Tak, koniec.

[00:38:15.250] **Szymon Warda:** Tak. Dobra, to teraz, bo jest jeszcze on hold ciekawy - Tyk Hybrid API Management.

[00:38:24.040] **Łukasz Kałużny:** What the fuck w ogóle?

[00:38:25.180] **Szymon Warda:** Ile tam się żali wylało. Ewidentnie mieli jakieś problemy, bo rzadko widzimy... To jest pierwszy raz na holdzie, zjechali ich okrutnie. To oni służą jako platforma do właśnie zarządzania wieloma chmurami. Zjechali ich od ticketów, stabilności, dokumentacji, wszystko.

[00:38:48.700] **Łukasz Kałużny:** Aż dziwne.

[00:38:49.810] **Szymon Warda:** Musieli coś położyć albo coś się tam musiało zadziać na poziomie firma-firma, bo takich żali to jeszcze nie widzieliśmy w tym raporcie, ewidentnie. Tak że no ktoś zadarł za bardzo chyba z ThoughtWorksem.

[00:39:02.650] **Łukasz Kałużny:** Tak. Dobra, no i przechodzimy prawie do końca, czyli języki i frameworki. To lecisz pierwsze.

[00:39:11.770] **Szymon Warda:** Co jest najważniejsze? No i super, że jest Open Telemetry w adopcie. No to tak, no co tu dużo mówić, tak, korzystajcie, przyjmuje się bardzo ładnie na rynku. Jeżeli chodzi o rozwój w aplikacjach, to nie ma innego wyjścia. To jest coś, co daje kilka, dodanie kilku bibliotek do projektu i nagle to zaczyna śmigać, mamy duże możliwości i możemy też masę kasy oszczędzić. Tak że w ogóle super. Tyle, nie ma co komentować.

[00:39:41.890] **Łukasz Kałużny:** No dobra, idziemy sobie dalej. Biblioteka, o której wspominaliśmy do Pythona od Microsoftu jako trial.

[00:39:50.740] **Szymon Warda:** Markdown, który Ty wspominałeś swoją drogą, pamiętam.

[00:39:53.710] **Łukasz Kałużny:** Tak, dokładnie. Czyli biblioteka pythonowa, która wam z wielu formatów, w tym Microsoftu, robi konwersję do Markdown, czyli scyzoryk pod LLM-y i pipeline do ładowania danych.

[00:40:06.730] **Szymon Warda:** Ja to w ogóle dodałem dlatego, że powoli będziemy się chyba bawili w thoughtworksowe i patoarchitektowe bingo tak naprawdę, gdzie się pokrywamy albo co jest...

[00:40:17.590] **Łukasz Kałużny:** To jest straszne.

[00:40:18.970] **Szymon Warda:** [Niesłyszalne 00:40:19], powiem Ci tak. Jedna ważna rzecz, to jest od Microsoftu. Więc to, że parsuje Wordy...

[00:40:25.180] **Łukasz Kałużny:** Nic dziwnego.

[00:40:28.640] **Szymon Warda:** Nic dziwnego, ale też chodzi o to, że będzie działało dobrze i będzie parsowało się fajnie. Bo jedna myśl, to jak fenomenalnie Markdown wpasował się w rozwój wszystkich LLM-ów. No nie, jest tak idealnie dopasowane. A teraz Łukasz najważniejsze, bo jest .Net Aspire. Łukasz, powiedz czym jest .Net Aspire?

[00:40:46.460] **Łukasz Kałużny:** .Net Aspire jest projektem ego osoby, która robiła w Microsofcie fajne rzeczy i nigdy nie zrobiła żadnej aplikacji na produkcji, nie wdrożyła jej. To jest bardzo istotny element tego, bo zawsze siedziała przy tej stronie frameworkowej, więc ma to wady i zalety siedzenia w złotej wieży z kości słoniowej. I .Net Aspire to jest takie założenie, że zrobimy sobie takiego, developer będzie mógł w kodzie napisać jak microservice ma sam siebie zdeployować. I szydziliśmy z tego jakieś trzy odcinki temu nawet.

[00:41:23.360] **Szymon Warda:** Łukasz, przypomnę Ci, że chciałeś z tego szydzić jeszcze wczoraj tak naprawdę.

[00:41:26.570] **Łukasz Kałużny:** Tak, tylko nie mam jeszcze... Tak, więc słuchajcie, pomysł jest z d\*\*\*, przepraszam Was przedszkolaki, z pupy w tym miejscu. Ale słuchajcie i tutaj jest tak, założenie, koncept gdzieś na papierze może był spoko, ale rzeczywistość jest zupełnie inna.

[00:41:48.110] **Szymon Warda:** Znaczy doprecyzuję, to jest opcja, że w kodzie .Netowym, C Sharpowym czy tam F Sharpowym, piszemy sobie co nasza aplikacja potrzebuje, tworzymy storage accounty, tworzymy wszystkie usługi. I czemu twierdzimy, że to jest taki pomysł dziwny? No bo kto da aplikacji kontrybutora na jakiejś resource grupie.

[00:42:06.230] **Łukasz Kałużny:** Albo subskrypcji, żeby sam był też... Koncept jest niedogrzany w... Inaczej, poza lokalnym developmentem, gdzie może ma jakąś wartość.

[00:42:17.060] **Szymon Warda:** Ale no właśnie, chciałem tu zaznaczyć, bo tam jest w tekście, uzasadniają to, że jest: design to simplify the orchestration of distributed applications on developers local machine.

[00:42:32.370] **Łukasz Kałużny:** Tak, ale to jak jest sprzedawane przez Microsoft to tak kurde nie jest.

[00:42:37.020] **Szymon Warda:** Właśnie, więc jak? I też z całym szacunkiem, o takie czy jest Docker Compose?

[00:42:43.920] **Łukasz Kałużny:** Czy wiesz co są w Aspire, bo zawsze, powiedzmy też o zaletach, są dwie zalety.

[00:42:48.540] **Szymon Warda:** No.

[00:42:49.770] **Łukasz Kałużny:** Ma wbudowany lock collector open telemetry...

[00:42:53.490] **Szymon Warda:** No ok.

[00:42:54.660] **Łukasz Kałużny:** Lokalny, jak developujesz lokalnie i ma dashboard lokalny. Więc z założenia jak developer ma kawałek swojej subskrypcji, to taki development aplikacji chmurowych w oparciu o Azure upraszcza, o tak. I to jest jedyna zaleta Szymon.

[00:43:10.080] **Szymon Warda:** Tak, copy paste kilku POD-ów, przepraszam, kilku kontenerów, image'y grafanowych i też Ci śmiga, powiedzmy szczerze.

[00:43:18.750] **Łukasz Kałużny:** Tak, ale okej, to wiesz, to trochę ja patrzę, że to jest trochę jakieś uproszczenie, ale no [niesłyszalne 00:43:24] powinno być na double holdzie, tak jak wcześniej Dapr.

[00:43:28.400] **Szymon Warda:** No i co, teraz mamy, jak już mówisz o holdzie... Nie, Ty masz jeszcze jedno w assessie.

[00:43:35.060] **Łukasz Kałużny:** Tak. I to jest akurat spoko, browser use, czyli wystaw sobie w wersji open source, jest też wersja tam płatna, ale interesuje nas open source, bo uczciwa cena, jak to z Walaszka tutaj szydzimy. Wczoraj oglądałem film o jego twórczości. Słuchaj, ktoś zrobił godzinny dokument o Walaszku i jego twórczości.

[00:43:56.600] **Szymon Warda:** Wiem, o którym mówisz.

[00:43:57.410] **Łukasz Kałużny:** Obejrzyj, obejrzyjcie, podlinkujemy. Ale z tym, browser use to jest pythonowa biblioteka, która waszemu LLM-owi agentowi może dać po prostu dostęp do przeglądarki jako Vision i HTML Extraction.

[00:44:17.450] **Szymon Warda:** Dobra, to teraz hold, bo jest ciekawy hold bardzo, o którym też mówiliśmy, kolejne bingo - node overload, czyli za dużo node'a. I tam jest taki fajny tekst o tym, że może powinniśmy wrócić do poliglot programming, czyli właśnie do tego, żeby developer znał wiele języków. Ogólnie mówią to, że node wkradł się do wielu miejsc, gdzie się nie powinien wkradać. No serio?

[00:44:39.780] **Łukasz Kałużny:** Ale on tam był. On tam, to też nie jest nowa pozycja, bo ona tam już była, na holdzie.

[00:44:46.050] **Szymon Warda:** Tak, ale teraz jest bardzo mocno zaznaczone, bym powiedział. I faktycznie to też chyba pokazuje, że Node już powoli schodzi z tego piedestału najbardziej nahype'owanego języka i powoli co innego. Node już staje się legacy powoli.

[00:45:01.590] **Łukasz Kałużny:** Legacy. Ale czy wiesz co ja Ci powiem? Tak znowu jeżeli mówimy o aplikacji biznesowej, w aplikacji biznesowej, teraz weźmy tak, zróbmy taki boksik, to z perspektywy kosztowej developmentu, full stacka i innych takich rzeczy, to nie jest najgłupsze rozwiązanie, Node plus frontend. Z takiej perspektywy, kiedy klepiemy apki biznesowe, start up, whatever.

[00:45:27.740] **Szymon Warda:** Ja bym powiedział, że w zależności od skali. Pisanie dużego ERP-a dużych systemów w Node, sorry, nie widzę tego.

[00:45:33.410] **Łukasz Kałużny:** No dobrze, to wiesz, to jest też już z drugiej strony. Tak, tutaj przyznam Ci rację, że... Ale wiesz, tak jak zawsze się śmieję, te wszystkie śmieciosystemy, które są, to nie jest to najgorsze, bez urazy.

[00:45:48.590] **Szymon Warda:** To jest fajny język do wprowadzania, fajny język do nauki, fajny jest do małych systemów i do generowania jakiegoś kodu, żeby to po prostu gdzieś stało. Fenomenalne. Do całego serverlessa idealnie się nadaje, do wszystkich node'ów, workerów cloudfrontowych, itd., świetnie. Ten język ma bardzo, bardzo dużo plusów, ale wpychanie go np. jako zastępstwo do SQL czy do tworzenia np. infrastruktury czy innych, no niekoniecznie.

[00:46:12.920] **Łukasz Kałużny:** Dlatego wyrzućmy to na mikroserwisy biznesowe.

[00:46:16.160] **Szymon Warda:** Tak. Dobra, to co właściwie, jakie wrażenia z tego?

[00:46:19.990] **Łukasz Kałużny:** Czy wiesz co, stabilny Thoughtworks.

[00:46:23.920] **Szymon Warda:** Może stabilny, dużo AI-a, ale w takiej wersji ucywilizowanej, bym powiedział.

[00:46:28.180] **Łukasz Kałużny:** Raczej tak. Wytknięcie Shadow IT jest piękne. To jest takie, wiesz, tak. Ale znowu jak zawsze nie zawodzi pod względem komediowym, tak jak Just in Time Privilege, Dapry, Aspire nie zawodzą pod tym względem.

[00:46:44.350] **Szymon Warda:** Nie. Tak, faktycznie są takie elementy, które jak zwykle są - czemu to w ogóle jest w tym raporcie? No ale bywa.

[00:46:50.710] **Łukasz Kałużny:** Tak. I zobacz nie trzymaliśmy się, że po 3, w niektórych miejscach mieliśmy więcej.

[00:46:55.960] **Szymon Warda:** Tak, tak, tak, mogliśmy sobie...

[00:46:57.310] **Łukasz Kałużny:** Ale było warto.

[00:46:58.870] **Szymon Warda:** No dobra, napiszcie co tam Wy może znaleźliście, z czym się nie zgadzacie, co powinno być wyżej, niżej i tyle chyba. No to co? Na razie.

[00:47:07.990] **Łukasz Kałużny:** Na razie. Trzymajcie się. Hej!

[00:47:09.430] **Szymon Warda:** Hej!

