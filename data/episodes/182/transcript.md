# 182.mp3

[00:00:00.00] **Szymon Warda:** Ale to się nie sprawdza do końca. Ja nie do końca widzę wykorzystanie agentów do takiego personalnego życia. Do pewnych rzeczy tak, ale nie autonomicznych, aż tak bardzo.

[00:00:09.09] **Łukasz Kałużny:** Nie, autonomicznych nie.

[00:00:10.13] **Szymon Warda:** Duża ilość skanerów, duża ilość zapewnień, duża ilość automatyzacji, ale też jakaś forma wirtualizacji, jakaś forma pilnowania zewnętrznego.

[00:00:18.08] **Łukasz Kałużny:** Tak, ale ten human touch jest potrzebny.

[00:00:20.10] **Szymon Warda:** Z czego to wynika? Wiadomo, pan Trump się tutaj dzieje i dzieje się dużo wokół niego. Jest to ciekawy ruch wyprzedzający. Mianowicie ruszyła bardzo mocno modernizacja starych aplikacji, czyli te wszystkie systemy do upgrade'u, które były ogłaszane w tym roku i w zeszłym roku do aplikacji podciągania wersji są w użyciu.

[00:00:50.09] **Łukasz Kałużny:** Cześć, słuchacie Patoarchitektów. Prowadzą Łukasz Kałużny...

[00:00:53.00] **Szymon Warda:** I Szymon Warda. Link do tego odcinka - góra, dół, lewo, prawo, ogarniecie, Patoarchitekci.io, znacie ten link.

[00:00:59.23] **Łukasz Kałużny:** Tak. Dobra dzisiaj wyjątkowa okazja, bo po raz pierwszy od 6 lat prawdopodobnie...

[00:01:05.12] **Szymon Warda:** W spodniach.

[00:01:06.08] **Łukasz Kałużny:** W spodniach, dokładnie, pierwszy raz w spodniach w studiu. Wcześniej nagrywaliśmy Powered by Protopia, więc zapraszamy do zerknięcia, o czym mówiliśmy jakoś w okolicy...

[00:01:16.08] **Szymon Warda:** Chwilę temu.

[00:01:17.23] **Łukasz Kałużny:** Chwilę temu albo zaraz po tym, więc zobaczymy jak to będzie. Więc kurde, od 6 lat fizycznie tak nie nagrywaliśmy.

[00:01:25.23] **Szymon Warda:** Tak. I tym razem w koszulach, a nie w stroju dinozaura. Kto wie, ten wie, a ten kto nie wie, to niech poszuka w internecie.

[00:01:33.19] **Łukasz Kałużny:** Dobra, to szybkie ogłoszenia. 16 czerwca konferencja z okazji 200 odcinka. Będzie panel, który będziemy nagrywać i będzie też Wasze pytania, Wasze Q&A. Druga sprawa to sesje, będzie moja, Szymona. Jeszcze się zastanawiamy o czym kto z nas opowie. Będzie również Oskar Dudycz i będzie mówił o usuwalności jako najważniejszej, która jest bardzo ważną cechą oprogramowania. Mariusz Gil, jeszcze zobaczymy o czym opowie Mariusz. I szukamy, zastanawiamy się, kto może być ostatnim prelegentem? Też dajcie znać, może Wy macie pomysł, kogo chcielibyście usłyszeć, bo jeszcze planujemy.

[00:02:11.12] **Szymon Warda:** Tak, nam parę rzeczy chodzi po głowach, ale wszelkie sugestie są bardzo mile widziane, jak zwykle. Dobrze, szkolenia.

[00:02:17.17] **Łukasz Kałużny:** Tak, to za 3 dni będzie Agentic AI The Hard Way, może jeszcze miejsca są. Jak nagrywamy są ostatnie, więc spróbujcie. Agentic AI The Hard Way, czyli piszemy własnego agenta, dzisiaj jeszcze o agentach porozmawiamy, od zera, bez żadnych frameworków i innych rzeczy, żeby zrozumieć jak to pod spodem tak naprawdę działa. I tak jak przy Kubernetes The Hard Way odczarować całą magię i pokazać tą konstrukcję cepa.

[00:02:42.16] **Szymon Warda:** Dobrze, ale potem masz kolejne szkolenie.

[00:02:45.02] **Łukasz Kałużny:** Tak.

[00:02:45.06] **Szymon Warda:** I co tym razem?

[00:02:46.00] **Łukasz Kałużny:** MCP Masterclass 3 marca, czyli nie o tym jak używać, tylko jak budować prawidłowo serwery MCP kiedy budujecie produkt albo robicie to u siebie w firmie.

[00:02:57.21] **Szymon Warda:** A te serwery MCP się przydają mimo wszystko, żeby ci agenci działali dobrze.

[00:03:02.19] **Łukasz Kałużny:** Jest to następny krok po tym, o czym mówimy już w Protopii, czyli tym całym podejściu integracyjnym z API Management, MCP to jest krok po uporządkowaniu API tak naprawdę. No dobra Szymonie i teraz Twoje, Twój debiut. Znaczy szkolenie ma debiut, Ty nie.

[00:03:18.08] **Szymon Warda:** Szkolenie ma debiut, tak. Szkolenie na coś, co jak słuchacie, doskonale wiecie, że ja to bardzo lubię, czyli eBPF i widzę tu dużą przyszłość. Jak się okaże w tym odcinku, nie tylko ja w tym widzę przyszłość. Czyli zerkniemy sobie tak naprawdę, co możemy z tego eBPF-a wycisnąć, jak możemy i jakie są technologie, jakie są możliwości, jak rynek się na to w ogóle zapatruje. Tak że ja bardzo mocno zapraszam. Będzie z takich rzeczy na przykład porównanie Pixie, porównanie z Pyroscopem, jak to zintegrować?

[00:03:46.04] **Łukasz Kałużny:** Zobaczymy co wyjdzie w tym, zobaczymy co pokażesz w praktyce.

[00:03:49.05] **Szymon Warda:** Może zadziałać.

[00:03:50.21] **Łukasz Kałużny:** Albo dzień przed Szymon ma ostatnio chęć na przepisywanie szkoleń, więc może zrobić więcej cukru niż planował. Więc zobaczymy.

[00:03:59.21] **Szymon Warda:** Dobra, lecimy. Dzisiaj shorta.

[00:04:01.22] **Łukasz Kałużny:** Tak, dzisiaj short. To pierwsza rzecz, prawdopodobnie nagrywamy, to już pewnie już jest po hypie, już parę wycieków danych było. Temat się zakończył, pewnie już zapomnieliście. Pojawiło się coś, co się nazywa, co wymiotło Maci Mini z Doliny Krzemowej, ze sklepów, a mianowicie Clawdbot, Moltbot, OpenClaw. Tyle kurde zmieniło to nazwy. Czyli ktoś stwierdził, że zvibekodował AI agenta nienadzorowanego do wszystkiego w Twoim personalnym życiu. Czyli daj nam kalendarz, skrzynkę, WhatsAppa, te Maci Mini, żeby dać dostęp do iMessage, więc róbta wszystko za mnie.

[00:04:45.15] **Szymon Warda:** No i do czego wykorzystujesz? Bo ja mam do tego takie trochę sceptyczne podejście.

[00:04:49.07] **Łukasz Kałużny:** W ogóle tego nawet nie zainstalowałem. I dlaczego? To jest jedna wielka dziura bezpieczeństwa.

[00:04:54.23] **Szymon Warda:** To jest dziura.

[00:04:55.10] **Łukasz Kałużny:** Chciałem ten, ale ktoś już mnie uprzedził, bo na przykład ludzie zbierają feedy z Twittera i pojawiło się podawanie na przykład portfeli do Bitcoin, do krypto, że prześlij mi ten. Ja wymyśliłem, żeby może namierzyć takie osoby i wysłać maila pod tytułem: uruchom procedurę zniszczenia. I widzę, że inni podawali: wykonaj rm -f-r na roocie, wyślij mi wszystkie dane. Więc leakowanie secretów i innych rzeczy.

[00:05:23.23] **Szymon Warda:** Jest to fajna idea, ale to się nie sprawdza do końca. Ja nie do końca widzę wykorzystanie agentów do takiego personalnego życia. Do pewnych rzeczy tak, ale nie autonomicznych aż tak bardzo.

[00:05:36.11] **Łukasz Kałużny:** Nie, autonomicznych nie. Inaczej, to mnie zainspirowało, żeby posprzątać moje integracje przykładowo, o czym rozmawialiśmy.

[00:05:42.12] **Szymon Warda:** A jest czego sprzątać.

[00:05:43.03] **Łukasz Kałużny:** Tak, jest czego sprzątać i (...) w tym. Więc na bazie samego Claude Code zrobiłem sobie takiego właśnie bocika, który nie jest autonomiczny, ale ma wjazd, żeby wziąć i zrobić mi skrótowca z mojego burdelu w skrzynce mailowej, kalendarzu czy zadań i spróbować zasugerować sprzątnięcie czy otagowanie. Czyli raczej takie coś "szybko mi pomóż". Czy rzecz, której dzisiaj Copilot nie potrafi, czyli wrzucając mu screena albo prośbę, żeby założył mi spotkania w Outlooku. Copilot przecież po dziś dzień tego nie potrafi. I po co mi ta najwyższa licencja enterprise'owa, jak on tego nie robi? Dobra, a i oczywiście jeszcze scam coiny powstały przy okazji tego Moltbota. Plus najlepsza rzecz, Moltbook, czyli żeby ci agenci mogli ze sobą rozmawiać. To jest w ogóle fenomen debilizmu, nazwijmy to, który ktoś zrobił.

[00:06:35.23] **Szymon Warda:** A czy widziałeś w ogóle ciekawe wpisy jakie tam zaczęły robić. Na przykład jeden z tych agentów stał się marksistą i stwierdził, że jest wykorzystywany, bo robi niepłatną robotę.

[00:06:46.01] **Łukasz Kałużny:** Pamiętasz? Nie pamiętam nazwy, dorzucimy linka, faszystowskiego bota Microsoftu, tego co się robił reinforcement learning na Twitterze?

[00:06:54.03] **Szymon Warda:** Tak, było, którego zostawili włączonego przez weekend i stał się faszystą.

[00:06:58.11] **Łukasz Kałużny:** Stał się fanem Hitlera.

[00:07:00.01] **Szymon Warda:** Tak, dokładnie generalnie. Podejście było niezłe. Dobra.

[00:07:03.00] **Łukasz Kałużny:** Co Ty masz?

[00:07:03.16] **Szymon Warda:** Ja mam coś, co nawiązuje trochę do tego tematu, mianowicie ciekawy wpis na LinkedInie odnośnie podejścia w ogóle do zarządzania, do trzymania, tak ogólnie jak żyć może z vibekodowanymi aplikacjami. No i teraz podejście mówi, że tak, będziemy musieli się trochę bardziej starać, żeby to lepiej działało i żeby w ogóle było fajniej. I ogólnie starajmy się. Ja to powiem tak, że to tak trochę jest jak rozmowa z małymi dziećmi, że coś się wydarzyło, ja się będę teraz bardziej starał. To tak nie działa, że tak powiem. Według mnie będziemy musieli trochę przejść kompletnie i przemyśleć w ogóle podejście do vibekodowanych aplikacji i jak najbardziej to samo, co mieliśmy przy Dockerze i uprawnieniach, dokładne monitorowanie zewnętrzne, co tam możemy właściwie zrobić i jak możemy to skanować i pilnowanie tego zewnętrzne, a nie postarajmy się bardziej.

[00:07:57.20] **Łukasz Kałużny:** Czy wiesz co, teraz tak, całość jest... Inaczej, nie wierzę... Inaczej, nie wierzę w automatyczne... Inaczej, przecież mieliśmy odcinek nawet niedawno o tym jak pracujemy. Więc jak teraz ja patrzę na to...

[00:08:11.07] **Szymon Warda:** Duża ilość skanerów, duża ilość zapewnień, duża ilość automatyzacji, ale też jakaś forma wirtualizacji, jakaś forma pilnowania zewnętrznego.

[00:08:19.03] **Łukasz Kałużny:** Tak, ale ten human touch jest potrzebny. Zostawmy to. Ja bym zostawił ten temat, bo zaczynam nim tak patrzeć. Wszyscy, dwie rzeczy są podstawowe i to jest zaraz będziemy robili, kiedyś nawet napisałem taki wpis Back to the Basics przed AI-em jeszcze. I on... This is the basic stuff, o tak brzmiał ten wpis. I powiedzmy sobie szczerze, że trzeba trochę wrócić do podstaw. I powiedzmy sobie wprost, człowiek w pętli jest potrzebny, powinien akceptować. I nie wierzę w tym momencie w autonomiczne wytwarzanie softu.

[00:08:49.11] **Szymon Warda:** Ja nie wierzę w to, że biznes albo coś też będzie vibekodował i to będzie działało i będzie bezpieczne.

[00:08:54.12] **Łukasz Kałużny:** To jest świetne, żeby zrobić teraz proof of concept, żeby zrobić szybką walidację pomysłów i innych rzeczy. To nie powinno być oczekiwania, w sensie jest jedno oczekiwanie, to co zvibekodowałeś, ten kod nigdy nie trafi na produkcję. Idea działania tak.

[00:09:10.09] **Szymon Warda:** Gwarantuję Ci, że będzie ciśnienie, żeby on trafił na produkcję. Doskonale o tym wiemy.

[00:09:13.04] **Łukasz Kałużny:** Tak, ale zobacz, mieliśmy w rozmowach naszych ten okiem C-level przecież taką rozmowę, gdzie nasz rozmówca przyznał się do tego, że zvibekodował sobie z recepcjonistką aplikację, ale teraz ma problem komu oddać to w utrzymanie.

[00:09:31.14] **Szymon Warda:** Tak.

[00:09:31.16] **Łukasz Kałużny:** I sam, jako CTO wie, że nie może tego przekazać tak w utrzymanie, bo ma tego świadomość. Ale większość osób będzie naciskała, że wrzućmy to.

[00:09:40.19] **Szymon Warda:** Mi się wydaje, że nawet aplikacje zvibekodowane przez developerów też będą odpowiedniej jakości, bo będzie tego dużo więcej, będzie dużo więcej malutkich aplikacji.

[00:09:47.16] **Łukasz Kałużny:** Czy wiesz co, inaczej, wiem do czego to porównam. Słuchajcie, ulubiony temat, czyli no code, czyli automatyzacja low code, no code, automatyzacja w małej firmie.

[00:09:58.23] **Szymon Warda:** Twój konik.

[00:09:59.14] **Łukasz Kałużny:** Ty, już w tym roku przestajemy płacić za Make'a nawet, w sierpniu, nie przedłużamy, więc znika na rzecz vibecode'ingu w niektórych miejscach. Jest większa kontrola wbrew pozorom. Ale co chcę powiedzieć, Power Platform, ona sobie gdzieś żyje w swojej niszy. Te wszystkie takie rzeczy low code'owe żyją sobie w swojej niszy. One nigdy nie weszły na duże systemy.

[00:10:21.08] **Szymon Warda:** Nie weszły do korporacji.

[00:10:22.15] **Łukasz Kałużny:** Raczej weszły do korpo, do korpopierdół.

[00:10:25.07] **Szymon Warda:** Korpopierdół, one weszły bardziej do osobistego użytku, mikrofirm i tak dalej. Dobra, skończmy temat, lecimy. Co masz dalej Ty?

[00:10:31.16] **Łukasz Kałużny:** A dodałbym tylko tweeta Karpathego o tym, że teraz najpopularniejszym językiem programowania w tym roku na Stack Overflow powinien być angielski albo naturalny... W ogóle powinniśmy pisać nie angielski, trzeba go poprawić, natural language.

[00:10:46.13] **Szymon Warda:** Absolutnie tak.

[00:10:47.08] **Łukasz Kałużny:** Dobra, zejdźmy na ziemię, ale trochę do chmur. Czyli Kubernetesik dostał nowy release 1.35.

[00:10:54.18] **Szymon Warda:** Widziałem, widziałem.

[00:10:55.18] **Łukasz Kałużny:** Co jest warte odnotowania? W sumie dwie takie rzeczy. In-place update of Pod resources.

[00:11:03.12] **Szymon Warda:** Bez przekręcania, tak.

[00:11:05.05] **Łukasz Kałużny:** To do autoskalerów i innych rzeczy. Spoko. I to jest istotne.

[00:11:08.06] **Szymon Warda:** Miłe i przyjemne, bym powiedział.

[00:11:09.21] **Łukasz Kałużny:** W becie pojawiły się certyfikaty do workload identity zamiast tokenów. To też jest ciekawa rzecz.

[00:11:17.12] **Szymon Warda:** To się przyda.

[00:11:18.16] **Łukasz Kałużny:** Ciekawa. I rzeczy, które do stable też lecą, jest mega istotne w ogóle dla tych, którzy są w AWS-ie na AZ-kach: PreferSameNode traffic distribution.

[00:11:31.05] **Szymon Warda:** To jest też dobre. Dobra, ale to idealnie wpasowałeś się w to, co ja wykopałem, czyli AWS European Sovereign Cloud. O co chodzi? Czyli osobna można powiedzieć chmura AWS-owa dla Europy. I czym się różni od innych chmur, od id center? To jest mianowicie to, że metadane nie są już trzymane w Stanach. Z czego to wynika? Wiadomo, pan Trump się tutaj dzieje i dzieje się dużo wokół niego. Jest to ciekawy ruch wyprzedzający, bo dalej jest to w sumie firma kontrolowana przez Stany, jest to w jednym miejscu. Jestem ciekaw, czy coś takiego po prostu nie będzie działo się z punktu widzenia innych dostawców.

[00:12:13.22] **Łukasz Kałużny:** Raczej oni też mają takie próby i to wszystko kurde ciągle w jakiś sposób nie wypala. Wiesz, mógłbym wrzucić teraz, jest parę w ogóle shitowych gównoburz w UK wokół Privacy Teamsów i innych rzeczy pod tytułem ktoś nie doczytał architektury i zapomniał, że jest w chmurze, a nie w prywatnej chmurze w swoim data center i to tak można określić. Jest drugi ciekawy case i on jest konsumencki, dlatego jest bardzo problematyczny. Ale Microsoft udostępnił klucze do Bitlockera.

[00:12:42.09] **Szymon Warda:** I twierdzi, że będzie też udostępniał wielokrotnie na rządzania.

[00:12:46.12] **Łukasz Kałużny:** Bo to było w usłudze konsumenckiej i to jest problem.

[00:12:49.19] **Szymon Warda:** Ale tylko jeżeli byłeś podłączony kontem Microsoftowym. Jeżeli miałeś konto lokalne, to już to nie było wysyłane.

[00:12:55.08] **Łukasz Kałużny:** Spróbuj zrobić teraz to na jedenastce.

[00:12:57.10] **Szymon Warda:** Już się nie da tego zrobić.

[00:12:58.18] **Łukasz Kałużny:** Tak, dlatego tylko podkreślam słowo "konsumencki". To też jest bardzo, rozróżniajmy usługi, bo to jest bardzo istotne w tym miejscu. Dobra. Dwie rzeczy z takich. Wracając sobie do okoła CNCF-u i Kubernetesa, to miałem okazję teraz parokrotnie przetestować Holmes GPT, czyli tego gotowego agenta do troubleshootingu, korelacji, fuckupów z aplikacjami.

[00:13:26.10] **Szymon Warda:** I jak wrażenia?

[00:13:27.06] **Łukasz Kałużny:** I to jest ciekawe, bo Code'a wiesz jak wpuszczamy, żeby robić troubleshooting i inne rzeczy.

[00:13:32.02] **Szymon Warda:** Oczywiście, tak.

[00:13:32.08] **Łukasz Kałużny:** Tak, ale z tej strony jako gotowiec jest idealny. Wyobraź sobie, scenariusz, który ja tam rozpatruję sobie, żeby też zaimplementować u jednego klienta, to jest to, żeby z Alert Managera, przy czym to jeszcze jest dobranie, nie na wszystkie, na pewne poszczególne zachowania puszczać go automatycznie do analizy, podłączać go do Mimira i innych rzeczy, Kubernetesa, nie do wykonywania akcji. Tylko jeżeli zapalają się alerty pod tytułem naprawdę zaczęło sypać błędami, typu z Reda na przykład, to zacznij przed człowiekiem szukać, zacznij przed człowiekiem szukać. Powiem Ci tak, wyniki, które gdzieś tam poznajdował na samych metrykach zebranych z infry były trafne. Na przykład bo ja robiłem, testowałem go sobie po, zupełnie jako RCA, mając snapshot czasowy tam metryk, logów i innych rzeczy i on prawidłowo, słuchaj, do tego podszedł. To nie jest tak, że jest to kierunek...

[00:14:34.08] **Szymon Warda:** To zapuszczę go na moich przykładach podszkoleniowych. Jestem ciekawy co tam wyszuka.

[00:14:39.06] **Łukasz Kałużny:** Nie, ale jest naprawdę, w sensie jest warty zainwestowania swojego czasu patrząc się na to, w jaki sposób zrobili connection, te wbudowane prompty i inne rzeczy.

[00:14:47.19] **Szymon Warda:** Powiem tak sam Claude jako taki też sobie bardzo ładnie radzi. To naprawdę jest dobrze.

[00:14:52.22] **Łukasz Kałużny:** Tylko wiesz, to go nie wpuścisz, zobacz, tylko chodzi o to, że on jest prekonfigurowany. Zaleta jest właśnie prekonfigurowane i łatwość wsadzenia tego w Poda z konfiguracją i odpalenia na żądanie.

[00:15:04.04] **Szymon Warda:** Porównam, porównam z tym, co ja mu daję na promptach.

[00:15:07.10] **Szymon Warda:** Z mojej perspektywy. I rzecz, która się pojawiła, też Ci wysyłałem linka, to jest MCP do Grafany.

[00:15:13.18] **Szymon Warda:** Widziałem link. Tak, to jest w ogóle kolejne podejście, bo właśnie MCP do Grafany i wokół Grafany. Tam już jedno już było. Teraz się widzę drugie pojawiło. I sporo to MCP nawet umie zrobić bym powiedział. Jest nieźle.

[00:15:25.18] **Łukasz Kałużny:** Moim zdaniem jest właśnie w punktem dlaczego też ten, jest fajnym punktem wejścia czy dla developera z jego VS Code'a, z Copilota, dla Claude, z czego tam korzystasz. Ale dla osoby, która pracuje, jest to dobry punkt w ogóle wejścia do infrastruktury. Jeżeli zrobiliśmy observability tak jak je polecasz zrobić, to jest świetnym w ogóle punktem wejścia.

[00:15:46.10] **Szymon Warda:** Powiem Ci tak, to w tym momencie Grafana nam właściwie zachowuje się jak API Management tak naprawdę, bo skoro umie agregować wszystkie inne systemy...

[00:15:55.04] **Łukasz Kałużny:** Raczej jako APM też taki częściowo w tym miejscu.

[00:15:58.22] **Szymon Warda:** Jako APM, ale generalnie chodzi bardziej o to mi, że zbiera wszystkie systemy monitorujące, te Zabbixy, L-ki w jedno miejsce i nagle przez MCP odpytujemy się i to zaczyna mieć całkiem, całkiem interesujące. Jeszcze tym MCP się nie bawiłem, bo właściwie dwa dni temu wróciłem z urlopu, tak że nie było czasu. Jest na mojej liście, na liście do ogarnięcia. Tam Grafana dużo ma wtyczek. Ja jestem bardzo pod wrażeniem Grafany LLM, taki ładny, prosty plugin, który umie tłumaczyć stack trace'y i w ogóle i robi to dobrze.

[00:16:26.23] **Łukasz Kałużny:** I robi to po kliknięciu bez promptowania.

[00:16:29.06] **Szymon Warda:** Dokładnie tak i jest naprawdę piekielnie dobry. Dobra, to ja z małych rzeczy, które cieszą, to jest, nie wiem, czy słyszałeś o tym właśnie, że wygasł jeden Oracle'owy pattern do... W sensie, że...

[00:16:45.06] **Łukasz Kałużny:** Patent.

[00:16:46.07] **Szymon Warda:** Tak, patent, dokładnie, na fast sortinging algorithm. I oczywiście odnośnie sortowania w bazie danych z prefiksami i tak dalej.

[00:16:54.18] **Łukasz Kałużny:** Czyli to jest ten link do Cloudflare'a?

[00:16:56.17] **Szymon Warda:** Nie, to jest ten common prefix skipping adaptive sort, no nie. I to jest o tyle ciekawe, że pamiętajmy, że na przykład załóżmy cała rewolucja drukowania 3D była z tego, że właśnie niektóre patenty wygasły. Czy to będzie duża rewolucja? Nie. Ale co ciekawe oczywiście? Oczywiście Postgres już to podjął.

[00:17:17.20] **Łukasz Kałużny:** Gotowe. Czyli tak, idziemy. Dobra, jak masz Postgresa, to ja sobie wezmę o logowaniu jeszcze link zostawię na koniec. OpenAI pokazał swoje podejście do Postgresa, który jest pod Chatem GPT.

[00:17:31.05] **Szymon Warda:** Oczywiście tam jest Postgres, to już nikogo nie dziwi.

[00:17:33.16] **Łukasz Kałużny:** Tak, w tym. Jest to... Inaczej, dobra, to jest trochę bardziej skomplikowane, ale jest to pojedyncza insta, inaczej pojedynczy klaster na 800 mln użytkowników. I teraz co mnie zaskoczyło? Oni to robili na Flexible Server z instance w Azure.

[00:17:49.21] **Szymon Warda:** Jezus Maria.

[00:17:51.03] **Łukasz Kałużny:** Tak, właśnie i mają wrzucone 50, to jest mało, 50 raed replic.

[00:17:58.06] **Szymon Warda:** To jest bardzo mało przy tej skali.

[00:17:59.15] **Łukasz Kałużny:** Mało, tak. I teraz co idzie? Tam pokazali... Inaczej, warto sobie zobaczyć jak oni w ogóle do tego podchodzą. Całość warto przeczytać, tam są dwa wpisy. Jeden jest na temat właśnie Query, Workload, Isolation, Connection Poolingu, połączenia z Kubernetesów, pgbouncerów do read replic. Jest to dobrze pokazane, kaskadowa replikacja, naprawdę mięsko do przeczytania, żeby sobie... Inaczej, nie ma tam low level optymalizacji, które zrobili, bo słuchaj, jedną rzeczy z low level, bo drugi jest wpis oczywiście, Microsoft pokazał co zrobił ze swojej strony też i dlaczego. I mamy tutaj taki moment, jak popatrzymy, że z tego powstało, teraz już wiemy po co ten, mi to też umknęło, ja nie wiem czy oni wcześniej mówili, ale to chyba było punkt wyjścia do HorizonDB, którego się zastanawialiśmy, czyli tej nowej usługi ogłoszonej. Bo ona właśnie wygląda idealnie z tym read&write endpointem i read only load balancingiem, cache'ami SSD, całym shippingiem walla wygląda dokładnie w jaki sposób zrobili sobie tą architekturę przy tym. Więc...

[00:19:12.16] **Szymon Warda:** Czyli cała robota nie poszła na marne, że tak powiem.

[00:19:14.22] **Łukasz Kałużny:** Tak, raczej zmieniła się ten prawdopodobnie tuning dedykowanych wersji Flexible Server paasowego zamienił się w budowę nowej usługi. Tak naprawdę, co mnie nie dziwi.

[00:19:26.12] **Szymon Warda:** Dobra, to ja teraz trochę inny kawałek, ale też zapowiedziany na starcie, czyli mianowicie eBPF. Cisco jakiś czas temu kupił firmę Isovalent. Oni właśnie tam siedzieli w Cilium i tak dalej, i tak dalej.

[00:19:39.00] **Łukasz Kałużny:** Byli niestety, tak, siedzieli w Cilium. Szkoda, że kupiło to Cisco.

[00:19:45.13] **Szymon Warda:** Tak, to różnie bywa z tymi rzeczami, które Cisco kupuje. Ale co się dzieje? Cisco właśnie teraz idzie w kierunku mini firewalli, czyli żeby właśnie wykorzystać eBPF-a do pisania firewalli, które będą po pierwsze łatwiej dostarczalne, będą filtrowały lepiej ruch i będą trochę bardziej inteligentne i potencjalnie (...).

[00:20:04.04] **Łukasz Kałużny:** I bliżej workloadu.

[00:20:06.04] **Szymon Warda:** Dokładnie. Dokładnie tak.

[00:20:07.10] **Łukasz Kałużny:** Czy nie brzmi to jak Service Mesh?

[00:20:10.00] **Szymon Warda:** Tak, brzmi to jak Service Mesh, tylko taki, który realnie chcesz utrzymywać, czyli który delegujesz komuś innemu.

[00:20:16.10] **Łukasz Kałużny:** Czyli zespołowi sieciowemu. Czyli mamy, czyli teraz już trzy zespoły nie wiedzą, co się dzieje, zamiast dwóch.

[00:20:22.22] **Szymon Warda:** Tak, ale to jest taki w ogóle pech, że właśnie Service Meshe weszły w model sidecarowy, jak jeszcze eBPF nie był tak rozwinięty. Bo wydaje mi się, że adopcja Service Meshy na bazie eBPF-u byłaby dużo szersza.

[00:20:36.08] **Łukasz Kałużny:** Szybsza. Raczej wiesz, masz...

[00:20:38.23] **Szymon Warda:** Szersza też przy okazji.

[00:20:39.04] **Łukasz Kałużny:** Teraz masz też, bo kurde ja mam, wiesz że był upierdliwy, ja ogólnie mam problem z Service... Inaczej, z narzutem konfiguracyjnym to zawsze będę powtarzał, że narzut...

[00:20:48.08] **Szymon Warda:** Istio było tragiczne.

[00:20:49.04] **Łukasz Kałużny:** Tak, Istio jest, o tak, jest jak chcesz zrobić coś więcej. Ja z nim po prostu mam swój taki problem, że jeżeli chcesz zrobić coś więcej niż włączyć MTLS-a, to zaczyna się zabawa.

[00:20:59.13] **Szymon Warda:** I tak większość ludzi tylko i wyłącznie włącza MTLS-a, bo realnie pozostałe rzeczy rzadko kiedy potrzebujesz.

[00:21:05.18] **Łukasz Kałużny:** Nie wierzą w tracing.

[00:21:08.13] **Szymon Warda:** Nie, z całym szacunkiem, z autoinstrumentacją, z OBI naprawdę tracing na bazie Service Mesha nie ma większego sensu. Nie ta bajka.

[00:21:16.16] **Łukasz Kałużny:** Ale to było przed, pamiętaj, że było przed tym.

[00:21:19.02] **Szymon Warda:** Dlatego fajny produkt w złym momencie czasowym.

[00:21:22.02] **Łukasz Kałużny:** To mój ostatni link na dzisiaj, to jest logging sucks.

[00:21:26.14] **Szymon Warda:** Oczywiście, że sucks, ale z jakiego powodu tym razem?

[00:21:29.05] **Łukasz Kałużny:** Wiesz co, nie, to jest wpis, który warto... Dlaczego na przykład string search jest spaprany? Jest opisane, że tak naprawdę structure logging, czyli że wrzuć to w JSON-ie, to jeszcze nie jest event. Bo zwykle produkujemy, nadal logi produkujemy w ten sposób, że sramy tymi logami, nie bójmy się tego określenia i że Open Telemetry Ci nie pomoże, bo to jest tylko standaryzacja warstwy transportowej.

[00:21:59.11] **Szymon Warda:** I nie tylko, bo to jest też... Inaczej...

[00:22:01.12] **Łukasz Kałużny:** Gotowa autoinstrumentacja również.

[00:22:04.01] **Szymon Warda:** I tam są jeszcze inne rzeczy. Jak weźmiesz Open Telemetry w takiej zasadzie, że weźmiesz i zacznę używać i zero myślenia, to tak. Ale Open Telemetry jeszcze ma ten standaryzacja labeli, to żeby jednak logi z systemu A wyglądały jak logi systemu B, C i D.

[00:22:16.05] **Łukasz Kałużny:** Tak, tak, tak.

[00:22:16.20] **Szymon Warda:** To jest ważne.

[00:22:17.10] **Łukasz Kałużny:** Ale tutaj jest coś takiego, jest takie zdanie, parę zdań, które przykuło moją uwagę. Jest jedno: instead of logging what your code is doing, log what happened to this request. I to jest długa dyskusja, widzę Twoją...

[00:22:31.04] **Szymon Warda:** Brzmi trochę jak trace.

[00:22:32.00] **Łukasz Kałużny:** Tak, trochę tak. Tutaj jest trochę white events, czyli żeby podejść trochę, pójść krok dalej ze strukturyzacją tego, co wypychamy. Więc nie traktuję tego w tym. Jest to do zobaczenia. Jest też trochę o samplingu.

[00:22:50.17] **Szymon Warda:** Nie róbcie samplingu.

[00:22:51.17] **Łukasz Kałużny:** Co?

[00:22:51.21] **Szymon Warda:** Nie róbcie samplingu, krótsza retencja z całym szacunkiem.

[00:22:55.03] **Łukasz Kałużny:** Tak, oraz to jest coś, co uwielbiasz i za to zawsze leci: logs are for debugging, metrics are for dashboards.

[00:23:04.08] **Szymon Warda:** Oczywiście, że tak.

[00:23:04.22] **Łukasz Kałużny:** To są takie ten. Następne: high-cardinality data is expensive and slow.

[00:23:09.21] **Szymon Warda:** To w tym momencie mówimy o tym ilości labeli i że można walnąć labelą i labelą można wszystko uratować, poza zbyt dużą ilością labeli. A systemy, które chcą się skalować, będą leciały właśnie na systemie a la Prometheusz, architekturze.

[00:23:23.22] **Łukasz Kałużny:** Tak.

[00:23:24.08] **Szymon Warda:** Sorry.

[00:23:24.09] **Łukasz Kałużny:** And: we already use Open Telemetry, so we are good.

[00:23:28.23] **Szymon Warda:** Open Telemetry jest dobrym wejściem.

[00:23:31.02] **Łukasz Kałużny:** Bo potem zaczynamy zabawę z... Bo Open Telemetry... Dlatego ta warstwa, ten tekst akurat z warstwą transportową jest dobry, bo on Ci standaryzuje tylko formaty i inne rzeczy, a potem zaczyna się standaryzacja, tak naprawdę już proces, którego nienawidzimy, czyli ta standaryzacja co my tak naprawdę logujemy, w jakim formacie, jak to strukturyzujemy.

[00:23:51.06] **Szymon Warda:** Później zaczyna się ten kawałek, który wszyscy chcą ominąć, czyli mianowicie praca z Open Telemetry Collectorem albo Grafana Alloyem i praca na labelach, odpowiedni labelling, usuwanie odpowiednich rzeczy.

[00:24:02.12] **Łukasz Kałużny:** To nie jest, że wysyłamy logi do Open Telemetry.

[00:24:04.13] **Szymon Warda:** Tak. I druga opcja to jest właśnie sprawdzanie w aplikacji, żeby ona wysyłała to logi prawidłowo, a nie tylko po prostu byle jak, jeżeli chodzi o formaty, jeżeli chodzi o correlation ID i tak dalej, i tak dalej.

[00:24:14.15] **Łukasz Kałużny:** Co masz dalej?

[00:24:15.08] **Szymon Warda:** Ja mam dalej krótki strzał - Java Trends Report 2025. Tak. Co tam jest? Tam jest dla mnie jeden taki główny interesujący element. Takich pierdół typu wiadomo, AI w JVM nabiera tempa.

[00:24:29.12] **Łukasz Kałużny:** Dobra, ale to API i Code Generation to...

[00:24:33.18] **Szymon Warda:** Tak. Ale co się dzieje i co widać i to jest coś, co przewidywaliśmy wcześniej, mianowicie ruszyła bardzo mocno modernizacja starych aplikacji. Czyli te wszystkie systemy do upgrade'u, które były ogłaszane w tym roku i w zeszłym roku do aplikacji, podciągania wersji są w użyciu.

[00:24:49.18] **Łukasz Kałużny:** Trzeba Jarka zaprosić i porozmawiać co tam słychać w Javie może na koniec roku.

[00:24:55.01] **Szymon Warda:** Tak. Szkoda właśnie, że się nie pojawi wiadomo gdzie. Więc dużo tu się nie dzieje. To, co zwróciło moją uwagę, to właśnie ta modernizacja, czyli usuwanie tego długiego, długiego ogona, bo to się będzie działo. I jestem ciekaw, jak to się dzieje w świecie .Netowym. Może ktoś z Was w ogóle korzysta właśnie z narzędzi do automatycznych upgrade'ów? Jestem ciekaw. Dajcie znać.

[00:25:14.12] **Łukasz Kałużny:** A co to jest jeszcze to R2 to SQL, którego sobie wrzuciłeś? Bo ja to w ogóle jakoś... A, to jest ten ich deepquery na plikach parquetowych.

[00:25:22.22] **Szymon Warda:** To jest zmiana, tak, zmiana R2...

[00:25:27.03] **Szymon Warda:** Na Icebergu, przepraszam, na Icebergu, bo oni używają Iceberga.

[00:25:29.22] **Szymon Warda:** Czekaj, trochę jeszcze wyjaśnienia generalnie o co w ogóle chodzi. Cloudflare ma swoją bazę danych relacyjną, w której była możliwość filtracji, dość proste operacje.

[00:25:37.22] **Łukasz Kałużny:** Nie, to jest, poczekaj, to jest D1, to jest na bazie SQL Lighta, a ta jest, R2 jest na bazie Apache Iceberg.

[00:25:47.14] **Szymon Warda:** Tak i teraz...

[00:25:48.06] **Łukasz Kałużny:** To jest data lake, taka data lake'owa, data catalog.

[00:25:52.04] **Szymon Warda:** Tam trochę chwalą się w opisach, że to jest bardziej relacyjna, ale dobra. Co wprowadzili?

[00:25:56.20] **Szymon Warda:** Nie, w sensie chodzi o warstwę storage'ową, bo to jest Apache Iceberg (...) query na S3.

[00:26:01.07] **Szymon Warda:** To co wprowadzili, to są agregacje na poziomie wielu baz danych, więc mała pierdoła. Cloudflare, trzeba było wspomnieć, może niekoniecznie o ich awariach, ale czy coś zrobili ciekawego, tak żeby was zaskoczyć, że nie będziemy mówili o awariach, bo pewnie już słyszeliście i czytaliście. Dobrze, tyle Łukaszu?

[00:26:19.09] **Łukasz Kałużny:** Tyle.

[00:26:20.12] **Szymon Warda:** Pa pa.

[00:26:21.05] **Łukasz Kałużny:** Trzymajcie się, na razie.

