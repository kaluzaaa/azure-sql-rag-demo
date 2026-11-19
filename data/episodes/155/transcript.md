# 155.mp3

[00:00:10.940] **Łukasz Kałużny:** Cześć, słuchacie Patoarchitektów. Prowadzą Łukasz Kałużny...

[00:00:13.700] **Szymon Warda:** I Szymon Warda. Wszystkie linki to tego odcinka - Patoarchitekci.io, gdzieś w opisie na dole, Bing, Chat, co tam wolicie, ogarniecie. Dobrze Łukaszu, co tam na wstępie?

[00:00:23.240] **Łukasz Kałużny:** Zaczynamy jak zwykle od szkoleń. Ostatnie dwa w tym półroczu, czyli Ty 16 i 17 - GitHub Actions.

[00:00:32.360] **Szymon Warda:** Actionsy, czyli tak wszystkim się wydaje, że tam Actionsy, a tam CI/CD, niewiele tam jest. Owszem, tam trochę, jak się tak poleci po powierzchni, to tego nie jest za dużo, ale akurat Actionsy się rozbudowały strasznie od czasu, kiedy ich pierwszy raz dotykaliśmy i tam można dużo rzeczy zrobić. Jak ustawić GitHub Enterprise? Jak zrobić naprawdę fajne, zaawansowane rzeczy, połączyć się ze skanowaniem kodu i zrobić to dobrze, żeby faktycznie wykorzystywać. Szkolenie intensywne, dwa dni, ale faktycznie można powiedzieć, że niemal od zera do faktycznie bohatera i takich mega zaawansowanych rzeczy w GitHubie. No a co tam Ty będziesz robił?

[00:01:08.630] **Łukasz Kałużny:** Dobra, 24 czerwca - Model Context Protocol Masterclass, czyli tutaj jest jednodniówka, po której będziecie wymięci jak szmata za przeproszeniem.

[00:01:22.280] **Szymon Warda:** Po każdym szkoleniu właściwie.

[00:01:23.510] **Łukasz Kałużny:** Tak, ale będzie nieźle wypakowane wiedzą, bo przejście od zera do bohatera w praktyce przez McP. Czyli mówimy, że jest to istotne i chcę pokazać w jaki sposób powinno się to programować, w jaki sposób to kodować. Dla tych, którzy słabiej czują się może z kodowania, to poziom wejścia jest taki, że Python i TypeScript na poziomie: umiem napisać z tutoriala endpoint REST-owy, bo to jest poziom, który jest mniej więcej potrzebny, żeby w ogóle zrozumieć ten protokół prawidłowo.

[00:01:56.690] **Szymon Warda:** Albo wyvibe'uję coś tam po drodze.

[00:01:59.030] **Łukasz Kałużny:** Tak.

[00:01:59.510] **Szymon Warda:** Dobrze, to dzisiaj?

[00:02:01.340] **Łukasz Kałużny:** Dzisiaj biedahosting, czyli miejsce na nasze side projecty, MVP i inne wesołe zabawki. I inspiracją jest wpis, który podrzucił Oskar Dudycz pod Continuous Deployment właśnie z Docker Composem, korzystając z GitHub Actions. To był taki w ogóle początek. Zalinkujemy ten wpis, go zobaczycie. Jest tam użyty z Tailscalem i po dyskusji z Oskarem tak wyszło, że w sumie taki biedahosting to jest rzecz, której do projektów każdy, jeżeli robi jakieś tam zabawki, kombinuje sobie na boku, potrzebuje, bo nie będzie płacił pełnej opłaty za chmurę ani za pełen dedykowany serwer.

[00:02:43.310] **Szymon Warda:** To jest coś, co pamiętam, że było mega normalne bym powiedział sobie, jak ja powiedzmy studia i po studiach tak naprawdę, że coś tam zawsze ktoś coś tam próbował postawić. Ciekawy jestem jak to popularne jest teraz? Czy faktycznie ludzie stawiają takie biedahostingi, bo mają jakieś side projecty? Chyba trochę to umarło.

[00:03:01.520] **Łukasz Kałużny:** Zacznijmy jak bardzo... Inaczej, zacznijmy może od tematu homelabów, bo kiedyś... Inaczej, Ty zapewne miałeś dużego homelaba, jeżeli kojarzę. Miałeś na pewno.

[00:03:14.270] **Szymon Warda:** Miałem prawie od zawsze.

[00:03:16.190] **Łukasz Kałużny:** Tak. Ja szukam gdzieś na blogu, wrzucimy zdjęcia jak będzie, jeszcze jak zajmowałem się, gdzieś pewnie to znajdę, jak zajmowałem się jeszcze bardzo mocno onpremem, to miałem też całego laba, stawiałem klaster Hyper-V na laptopach, inne... O, znalazłem, miałem chyba dwa laptopy HP, microserver i jeszcze do tego wrzuconego, z tego co pamiętam, właśnie patrzę, taką stację Della roboczą dużą, stacja T5500 z Xeonem i w 2013 roku miało 32 GB RAM-u w domu. I dyski SAS-owe, tak. I korzystałem już wtedy z Nested Virtualization, bo odpalałem tam XenServery, vSphere'y, no i Hyper-v NAT-y, więc Wam gdzieś wrzucę. Zdjęć widzę tutaj nie ma, ale coś tam wrzucimy na ekran. I historycznie jeszcze gdzieś miałem, to mam, nie wyciągnę teraz działającej do kamerki, ale też wrzucę Wam zdjęcie, jest na blogu opis, mam taki mały klaster na pięciu Raspberry Pi Kubernetesa, K3s-a.

[00:04:23.720] **Szymon Warda:** To ja miałem [niesłyszalne 00:04:24], ISA, hostowałem strony, repozytorium kodu, jeszcze wtedy to był SVN tak naprawdę. I jeszcze różne narzędzia do skanowania kodu, itd. Te wszystkie rzeczy, które sobie policzyłem.

[00:04:35.360] **Łukasz Kałużny:** Szymon i mieliśmy dość homelabów.

[00:04:40.730] **Szymon Warda:** Znaczy może wyjaśnijmy, bo homelaby, homelaby to jest po prostu komputer, który stoi pod biurkiem.

[00:04:44.780] **Łukasz Kałużny:** Albo dużo komputerów.

[00:04:46.250] **Szymon Warda:** Albo dużo komputerów.

[00:04:47.330] **Łukasz Kałużny:** Niektórzy mają szafy rack'owe, szafy blade'owe i inne zabawki...

[00:04:55.340] **Szymon Warda:** Mam taką.

[00:04:55.730] **Łukasz Kałużny:** Ale masz tam tylko już router i NAS-a.

[00:05:01.280] **Szymon Warda:** Spot. Ale tak, zgadza się. Czyli sposób na eksperymentowanie, bo kiedyś ciężko było sobie poeksperymentować. Łukasz, czy masz teraz homelaba?

[00:05:12.200] **Łukasz Kałużny:** Widzisz, tak i nie. Technicznie poza zabawami z Raspberry Pi pod wysoką dostępność, mój setup kończy się na routerze i NASie, więc nie bezpośrednio.

[00:05:27.080] **Szymon Warda:** Wiesz co mnie przekonało do tego, żeby nie mieć homelaba?

[00:05:29.990] **Łukasz Kałużny:** Rachunki za prąd?

[00:05:30.860] **Szymon Warda:** Rachunki za prąd. Wiesz ile kosztuje trzymanie urządzenia 60-watowego, które chodzi 24h, rocznie?

[00:05:39.200] **Łukasz Kałużny:** Ile?

[00:05:39.470] **Szymon Warda:** Około 250-300 zł.

[00:05:41.600] **Łukasz Kałużny:** Tak? Liczyłeś?

[00:05:43.040] **Szymon Warda:** Tak, policzyłem to.

[00:05:44.750] **Łukasz Kałużny:** No więc lecimy.

[00:05:47.330] **Szymon Warda:** Taki komputerek, o którym Ty mówisz, który ma 32 GB RAM-u, Xeon, itd., on już je trochę więcej niż 60 watów.

[00:05:52.670] **Łukasz Kałużny:** Tylko wiesz, to było tyle lat temu, że cena za prąd była pomijalna wtedy przy tym, nie ten problem. Dobra, może przejdźmy sobie w ogóle do: jakie mamy opcje, jak sobie popatrzycie na to co robimy? Bo powiedzieliśmy sobie właśnie już o serwerach w domu, więc to odhaczyliśmy. Inaczej, jeżeli ktoś się nie próbuje uczyć sieci, jakiejś ciężkiej wirtualizacji, to to nie ma sensu, o tak. Czyli te serwery w domu totalnie z mojej perspektywy odpadają. Szkoda...

[00:06:23.600] **Szymon Warda:** Ja bym się nie zgodził z jedną rzeczą, serwery w domu na x86 czy też na x64 nie mają sensu z racji na rzeczy prądowe. Do home automation, itd., wszystko co stoi na Raspberry, tam możemy sobie [niesłyszalne 00:06:39].

[00:06:39.860] **Łukasz Kałużny:** Ale rozmawiamy o tym, że... Tak, tylko że gadamy, też mam tes Raspberry, którego, nie liczę, na homelaba, bo go nieregularnie nie utrzymuję, nie korzystam. Ale wiesz, tylko home automation to jest trochę inny cel niż homelab.

[00:06:54.530] **Szymon Warda:** Też tam jest dużo eksperymentów, DNS-y, wchodzisz dość szybko w te [niesłyszalne 00:06:57].

[00:06:59.360] **Łukasz Kałużny:** Inaczej, tylko po tych eksperymentach rodzina może chcieć Cię zabić. Wiesz o tym?

[00:07:04.730] **Szymon Warda:** Tak, albo może po prostu nie móc wyłączyć światła w pokoju.

[00:07:08.030] **Łukasz Kałużny:** Tak, dokładnie. Dobra, jak teraz tak popatrzymy sobie na opcje jakie mamy. Ja sobie spisałem tutaj i też dzięki społeczności na Discordzie poleciało też parę innych polecajek, więc zostawimy je w linkach i możecie sobie też zerknąć na kanał na Discordzie. To tak, pierwsza opcja, w sumie jedna z dwóch moich ulubionych, to są tanie trashowe VPS-y, jeżeli popatrzymy.

[00:07:35.300] **Szymon Warda:** Ja bym się nie zgodził.

[00:07:37.760] **Łukasz Kałużny:** Zaraz dam Ci dojść do głosu. Jeżeli tak, aktualnie moim ulubionym jest Mikrus od Unknowa, od Kuby Mrugalskiego, taka platforma. Zrobił też fajne wideo w ogóle jak to działa pod spodem, jak wygląda ten cały model. I tutaj to, co mi się podoba w tym, w całości, że 4 GB RAM-u, 40 GB dysku kosztuje 197 zł za rok.

[00:08:07.250] **Szymon Warda:** To jest bardzo mało.

[00:08:08.930] **Łukasz Kałużny:** Tak, przeliczając jeszcze na Euro, czyli tak, to jest tam około 4 euro, jak sobie popatrzymy. To jest jedna z takich opcji. Jest moim ulubionym. Są jeszcze podrzucane na Discordzie, ja to kojarzę. Jak sobie zerknę to jest NETCAP. Co tutaj jeszcze było? Contabo, więc jest parę takich rozwiązań cebulowych. Contabo chyba wychodzi najtaniej.

[00:08:38.630] **Szymon Warda:** Dobra, to teraz ja powiem. Ja mam trochę droższego VPS-a, bo potrzebowałem trochę więcej, głównie miejsca na dysku, do hostowania GoGita i on tam żyje. Dla mnie to jest pytanie podstawowe: czy to jest do eksperymentów, czy do utrzymywania czegoś, co ma żyć faktycznie? Bo mój projekt Cookie, który już nie jest utrzymywany od dość długiego czasu, ale żyje, działa w jakiś tam sposób powiedzmy, właśnie jest na VPS-ie. I dla mnie jest sens takich właśnie projektów, side projektów jest to, żeby sobie czasu nie rozwalić. A jak na przykład załóżmy Twój dostawca VPS-a mówi Ci, że no to za tydzień kończy się i my już rezygnujemy z tej usługi, musisz przenosić wszystko, no to nie jest dobra opcja.

[00:09:17.660] **Łukasz Kałużny:** Wiesz co, przy VPS-ie ja sobie pójdę, bo mam na to w notatkach punkty jak to postawić, jak ja stawiam to na tanim VPS-ie. Więc chętnie się podzielę tą wiedzą, bo to jest jedna z obaw, którą też dotknąłem. I wiesz co, można też powiedzieć, jak lecimy o VPS-ach, o tak zwanej cebula-bieda-plus. Mają dwie rzeczy. Raczej się tak nie krzaczą, to jest pierwsza rzecz. Można się dostać do supportu. I trzecia, chyba najważniejsza i będziecie wiedzieć o czym mówimy, nie palą im się data center.

[00:09:55.400] **Szymon Warda:** Tudzież też mają jakieś ujednolicone API dostępowe i raczej do tego się dostaniesz, masz gwarancję, że to będzie działało.

[00:10:02.900] **Łukasz Kałużny:** Więc taka bieda-plus, która będzie bardziej na MVP i rzeczy, które chcemy bardziej spróbować, sprawdzić, wystawić, to ja tutaj dwa takie popularne zastosowania. Pierwsze, chyba numer dwa w świecie startupowym w Stanach, czyli DigitalOcean. Pierwsze było Heroku, którego tutaj nie wymieniamy, ale to zaraz do tego sobie przejdziemy dlaczego. I Lightsail od AWS-a. I to są chyba dwie stabilne usługi. Tutaj wchodzimy troszkę drożej, bo taki VPS będzie kosztował z 10-15. Odpowiedniki do tych tanich to takie rzędu 2-3 razy więcej za miesiąc.

[00:10:45.710] **Szymon Warda:** Warte dla spokoju duszy, że tak powiem.

[00:10:48.200] **Łukasz Kałużny:** Tak, więc to jest to. Ty na czym trzymasz swoje, jak możesz zrobić ten?

[00:10:53.930] **Szymon Warda:** Ja jak trzymam GoGita, to trzymam na jakimś bieda-polskim-hostingu mimo wszystko, bo cenowo wychodziło mi z racji właśnie na wielkość dysku, potrzebowałem około 1 TB na dysk.

[00:11:03.950] **Łukasz Kałużny:** Więc tak, więc poszedłeś...

[00:11:05.540] **Szymon Warda:** [Niesłyszalne 00:11:06] powycinało wszystko.

[00:11:07.370] **Łukasz Kałużny:** Dobra, potem co, słuchaj, z biedahostingów co jeszcze mamy takiego ciekawego? To tu są vendor specific technologie, wchodzimy. To są free tier od hyperscalerów.

[00:11:20.990] **Szymon Warda:** Które są dla części usług compute'owych.

[00:11:23.540] **Łukasz Kałużny:** Tak, dokładnie. Dla bazodanowych też są, więc jest tego sporo. Więc to jest takie coś, że piszemy natywnie na ich PaaS serverlessa.

[00:11:34.250] **Szymon Warda:** Właśnie, bo chciałem to doszczegółowić, czy mówisz o czystym free tierze, czy mówisz o serverlessie, który finalnie jak mamy mały ruch może być bardzo mały.

[00:11:42.940] **Łukasz Kałużny:** Mówię o free tierach, ewentualnie free tierach na serverlessie i innych usługach. Rozkładam to po prostu na entry, bo zauważ, że część cloudów ma teraz tak, że masz na przykład do powiedzmy, z tego korzystam w AWS-ie, do tysiąca maili masz za free miesięcznie, a potem musisz płacić te grosze za każdego, za każdą paczkę setki na przykład. Czyli w ten sposób. U mnie tam za AWS-a, patrzyłem specjalnie, płacę 30 centów rachunku.

[00:12:09.850] **Szymon Warda:** To ja za Azure, bo tam trzymam jedną rzecz, ale to dojdziemy, bo widzę, że mamy to w notatkach, czemu płacę akurat kilka euro...

[00:12:18.040] **Łukasz Kałużny:** Za storage, wiemy o tym.

[00:12:20.320] **Szymon Warda:** Za storage, tak.

[00:12:21.280] **Łukasz Kałużny:** Tak. Dobra, i to są dostawcy. Tam zaraz sobie pójdziemy w detale. Rzecz, którą słuchajcie, świadomie pomijamy, jest dużo różnych platform, o których wspomnieliśmy: Heroku, poleciały, tylko właśnie nie widzę teraz na wątku na Discordzie od kogo, więc przepraszam, ale było wrzucone też inne... A, Mateusz D. właśnie, że Vercel, Supabase i inne właśnie takie platformy już aplikacyjne czy wspominane wcześniej Heroku pomijamy, bo my tego na co dzień, Ty Szymon chyba też z tego w ogóle nie korzystasz.

[00:12:54.890] **Szymon Warda:** Nie.

[00:12:55.280] **Łukasz Kałużny:** Więc z tego w ogóle nie korzystamy, więc pomijamy.

[00:12:59.300] **Szymon Warda:** Ciekawa oferta dla ludzi, którzy siedzą w jednym stosie dla postawienia prostych rzeczy i eksperymentów z językiem. To jest ciekawa języka, ciekawa alternatywa.

[00:13:10.370] **Łukasz Kałużny:** Dobra. Statyczne strony, z tego bardzo korzystamy.

[00:13:14.480] **Szymon Warda:** Najlepsza opcja.

[00:13:15.140] **Łukasz Kałużny:** Najlepsza, tak. W tym miejscu wlatuje sobie nawet hosting Pato. W ten sposób strona Pato, mój blog, Twój blog w pewnym sensie korzysta z jednej z opcji, które wymienimy. Czyli pierwsza, to są GitHub Pages.

[00:13:30.530] **Szymon Warda:** Które są absolutnie fenomenalne.

[00:13:32.270] **Łukasz Kałużny:** Tak. Drugą rzeczą, to są Cloudflare Pages, słuchaj Szymon.

[00:13:38.330] **Szymon Warda:** Tak, albo inna opcja po prostu Cloudflare, który stoi przed GitHub Pages.

[00:13:43.610] **Łukasz Kałużny:** Tak, też, można właśnie wszystkie połączenia. Ale mówię o Cloudflare Pages, bo jest jeden feature, teraz sobie zerknąłem na to, który jest warty uwagi. Mianowicie potrafisz możesz zapiąć się do repozytorium na GitHubie z tego darmowego Cloudflare Pages. Jeżeli robisz pull requesty to wystawia automatycznie również strony preview pod domeną preview.

[00:14:05.240] **Szymon Warda:** To to jest przyjemne bym powiedział.

[00:14:07.250] **Łukasz Kałużny:** Bo tego nie masz w tym. Więc statyczne strony plus królowe hostingu czyli S3, Blob Storage czy inne usługi do object storage'u schowane za Cloudflerem, a jak jesteśmy w AWS ie za CloudFrontem, żeby się ładnie to wystawić.

[00:14:24.710] **Szymon Warda:** Ustalmy, postawienie Cloudflare'a i trzymanie DNS-u w Cloudflarze i posiadanie całego keszowania, rozkładania w Cloudflarze to jest takie must have dla takich biedastron. To po prostu musi być. Jak coś wystawiamy publicznie, to jest dobry pomysł. Wiesz co, dla mnie S3 tak, czy tam Azure Blob Storage tak, Pages są lepsze.

[00:14:46.730] **Łukasz Kałużny:** Okej, z zaszłości historycznej, bo korzystałem z Hugo na blogu...

[00:14:52.190] **Szymon Warda:** Stary już.

[00:14:53.420] **Łukasz Kałużny:** Raczej wersja, którą mam, binarki na blogu, pomińmy, nie będę się przyznawał jak jest stara. Inaczej, to ja korzystam u siebie na swojego prywatnego bloga, na którym praktycznie nic już nie piszę. Korzystam z S3, wrzucam po prostu, mam skrypcik do synchronizacji S3 i wystawiam go Cloudflarem.

[00:15:18.110] **Szymon Warda:** Pamiętam jak mnie namawiałeś na to, żeby przejść na Hugo i dzięki Bogu tego nie zrobiłem.

[00:15:22.340] **Łukasz Kałużny:** Inaczej, Hugo się ciągle rozwija, to jest ciągle on going.

[00:15:27.230] **Szymon Warda:** Hugo nie jest złe. Jekyll jest łatwiejszy.

[00:15:30.730] **Łukasz Kałużny:** Dobra, w tamtym momencie czasu bym się kłócił. Teraz tak, Pato też stoi na Jekyllu na GitHub Pages. W tamtym momencie miał dla mnie, ten Rabi był, pracując wtedy na Windowsie, to była zmora, dlatego przeszedłem na Hugo, bo była jedna binarka, wszystko działało. Dobra, przejdźmy sobie teraz do technikaliów, czyli w ogóle moje podejście jak ja hostuję między innymi tego bota, którego i PatoAI, tego Hala900 i zabawki wokół pato, jak ja podchodzę do tego na tanim VPS-ie do hostowania? Więc pierwszą rzeczą jest to, jak ja to wszystko buduję i deploy'uję. I mianowicie jest tutaj pierwszy element, nie mam żadnego Kubernetesa.

[00:16:18.250] **Szymon Warda:** I słusznie.

[00:16:19.000] **Łukasz Kałużny:** Tak, nie mam żadnego Kubernetesa. I teraz tak dla chętnych to tak, bo te pytania się pojawiały, tutaj Marek Próchniak nam wrzucił komentarz do notatek właśnie o: może minicube na VPS-ie, czy szarpnąć się na postawienie jakiegoś K8s-a? Nie, nie, nie.

[00:16:37.450] **Szymon Warda:** Szkoda cykli CPU powiem tak.

[00:16:39.370] **Łukasz Kałużny:** Tak, szkoda w ogóle życia i sensu życia na to. Jeżeli ktoś już musi, ktoś już bardzo chce, to jest tak K3s, Flux CD i nie stawianie całego CNCF-u. Nie potrzebujesz tam Grafany, Elastica i innych rzeczy. I taka rzecz, już ciekawostka, na K3s-ie jest protokół również obsługiwany do VPN-ów WireGuard wbudowany natywnie i wrzuciłem linka, można sobie zrobić distributed, potraktować tani VPS-y jako distributed multicloud z wykorzystaniem. Ale nie róbcie tego, szkoda życia.

[00:17:17.830] **Szymon Warda:** Ja raz spiąłem mojego starego VPS-a z moim serwerem domowym po to, żeby serwer domowy liczył pewne rzeczy, jako background worker służył. Nie róbcie tego absolutnie. To jest głupi pomysł.

[00:17:29.590] **Łukasz Kałużny:** Dobra, i teraz co ja robię, jeżeli chodzi o GitHub Actions? Czyli tak, każdą usługę mam opakowaną w Dockera w moim przypadku i buduję, i teraz ważne, dockery buduję na GitHub Actions w ramach free tieru i przechowuję obrazy, korzystam z cache, który GitHub Actions daje, więc to reklamy do Szymona, tych elementów, które są, będziecie mogli zobaczyć na szkoleniu. I trzeci element, który jest, to korzystam jako repo obrazów, również korzystam z tego repo GitHub'owego. Trzymam obraz w repozytorium wbudowanym. I to jest taki pierwszy krok. Druga rzecz...

[00:18:06.580] **Szymon Warda:** Ja się tylko odwołam, bo to jest ważne, bo były propozycje jeszcze używania Jenkinsa jako CI/CD.

[00:18:13.810] **Łukasz Kałużny:** A, właśnie, to też od Marka, szkoda życia.

[00:18:17.380] **Szymon Warda:** Nie, nie o to chodzi. Budowanie kodu na słabym VPS-ie, gdzie masz mało cykli, potrafi zabić stronę, odpalenie testów, czegokolwiek. Nie warto tego robić. Utrzymywanie i co więcej posiadanie wszystkich jajek w jednym koszyczku nie jest dobrym pomysłem. Wierzcie mi, bo będziecie mieli tam Jenkinsa, za chwilę wylądujecie tam z jakimś repo kodu, itd., całą bajką. To jest zły pomysł, bo jak nagle zignorujecie jednego maila od Waszego dostawcy, to okaże się, że macie okrągłe nic. Nie stawiajcie, na tym biedahostingu powinno być minimum, które musicie mieć i nie stawiajcie nic więcej. A już na pewno to, o czym mówiłeś Ty, żadnej Grafanyz zarąbiecie ten procesor.

[00:19:01.960] **Łukasz Kałużny:** Tak, Prometheus i inne rzeczy. Dobra i wracając do tego, mamy to i ja Wam po prostu skrypt, który loguje się na tego VPS-a w GitHub Actions, loguję się, odpalam skrypt deployment'owy. I teraz chyba rzecz, którą nie wiem, Ty możesz mieć uczulenie na to, ja mam inne do tego podejście, wszystkie aplikacje na jednym VPS-ie, które deploy'uję, trzymam po pierwsze w monorepo, naprawdę nie bawię się w to i wszystkie usługi są spisane w Docker Composie.

[00:19:32.800] **Szymon Warda:** I tu się nie zgodzę, bo o ile Docker Compose ma jakieś tam opcje monitorowania czy te kontenery chodzą, to to bywa różnie. Ja dużo bardziej polecałbym odpalenie, to co możemy oczywiście, jako natywne zainstalowane usługi. Mamy pełen monitoring i nie musimy zbierać tych logów, wszystko widzimy. Aplikacje, odpalenie w narzędziach, bo i tak będziemy musieli coś mieć, co będzie stało przed tym, jakieś AIS-y, nginx'y, cokolwiek co będzie to monitorowało i [niesłyszalne 00:20:01].

[00:20:01.900] **Łukasz Kałużny:** Dobra. Szymon, teraz ja się z Tobą totalnie w ogóle nie zgadzam się, bo ja w tym miejscu mam tak, mam to w następnych elementach, więc do tego sobie pójdziemy. To temat, przechodząc od razu do jak ja to monitoruję, jak to wygląda. Po pierwsze Docker. Sam Docker File masz health check'a do restartów i innych rzeczy.

[00:20:23.900] **Szymon Warda:** Tak są.

[00:20:24.920] **Łukasz Kałużny:** I działają. Docker Compose, jak zrobisz restart always, zreboot'ujesz serwer, kontenery wstają. Trzecia, która część jest, mówisz o ruchu wchodzącym. Ja mam w Docker Compose, używam, korzystam z dwóch rozwiązań naprzemiennie, które tam wezmę w zależności, który syf akurat jest deploy'owany, na którym tym, która z zabawek, to korzystam z Caddy'ego. I to jest pierwsza rzecz, czyli wystawiam sobie poprzez Caddy tam gdzie muszę się, Caddy jest tam gdzie muszę się dostawać bezpośrednio. Jedna rzecz z Caddy'm, która jest, to jest wbudowany let's encrypt w środek. On ma wbudowanego let's encrypta. I to jest jedna rzecz. Druga rzecz, z której korzystam, jeżeli nie potrzebuję wystawiać bezpośrednio, to jest z Traffica, ponieważ on też potrafi się po labelach w Docker Compse odczytać i dynamicznie skonfigurować jak Ingress na Kubernetes'ie.

[00:21:30.280] **Szymon Warda:** Zgadza się, fajnie to brzmi. Zobacz ile masz elementów budulcowych i ile trzeba tam dorzucić. Przewaga Twojego rozwiązania jest taka, że łatwo możesz potencjalnie wziąć to i przenieść i masz trochę mniej konfiguracji. U mnie jest taka, że po prostu odpalam parę skryptów i się generalnie samo instaluje i nie muszę na to patrzeć praktycznie nigdy.

[00:21:50.380] **Łukasz Kałużny:** Wiesz co, ja tylko robię...

[00:21:51.700] **Szymon Warda:** Czekaj, warstwę Docker Compose'a, która mimo wszystko potrafi się zwalić.

[00:21:57.010] **Łukasz Kałużny:** Dobra, ja wkleiłem linka, ocenicie, ile to jest, jeżeli chodzi o takie wystawianie, to jest dodatkowe per serwis trzy linijki kodu w tym Docker Compose i tyle. Więc ocenicie. Dajcie znać w komentarzach albo na Discordzie czy natywne podejście Szymona, robimy walkę, czy moje.

[00:22:17.960] **Szymon Warda:** Żeby nie było, moje jest po to, żeby mieć jak najmniej elementów ruchomych.

[00:22:21.890] **Łukasz Kałużny:** Moje jest takie, że robię, instaluję Dockera na nowym serwerze, wrzucam klucz SSH do GitHuba do secretów i deploy'uję.

[00:22:29.810] **Szymon Warda:** I śmiga.

[00:22:30.770] **Łukasz Kałużny:** Dobra i jak wystawiamy rzeczy na świat, kurde i mam teraz problem, bo obydwoje korzystamy z Cloudflare'a, tu się akurat zgadzamy, że wystawiamy, zawsze aplikacja idzie przez reverse proxy na Cloudflerze.

[00:22:44.090] **Szymon Warda:** Dokładnie tak.

[00:22:45.200] **Łukasz Kałużny:** Dobra, i tu Piotrek wrzucił mi jedną rzecz, żeby: po co mam proxy? Po co mam wystawiać Cloudflare'a? Że Cloudflarem wystawiać, jak można skorzystać z tuneli cloudflare'owych. Inaczej, i teraz tak, z Piotrkiem zgodzę się jakbym wystawiał z domu czy jakiś tych, to ten tunel cloudflare'owy jest spoko. Jak i tak to jest VPS z publicznym adresem, to mogę sobie kliknąć: weź forwarduj mi ten ruch do serwera przez Cloudflare'a, jakbym trzymał DNS-a w Cloudflarze i nie ma sensu dodawać następnego klocka. Więc Piotrek, jeżeli hostujemy w domu, to się z Tobą zgadzam, czy gdzieś tam w tym. Jak mamy z publicznym IP-kiem...

[00:23:24.160] **Szymon Warda:** Nie ma sensu.

[00:23:24.850] **Łukasz Kałużny:** Nie ma sensu, to jest...

[00:23:26.020] **Szymon Warda:** Za dużo zabawy i jeszcze kolejny element ruchowy, który może się potencjalnie popsuć i możemy sobie utrudnić dostęp do tego. Nie ma sensu.

[00:23:31.720] **Łukasz Kałużny:** Tak. Dobra, kolejna rzecz, szczęśliwi backupów nie robią.

[00:23:37.390] **Szymon Warda:** Tu się nie zgodzimy w jednym punkcie, ale dobrze. No powiedz, co tam masz?

[00:23:41.320] **Łukasz Kałużny:** Dobra, ja żeby mieć monitoring backupu, wywołuję, mam skrypt, który chodzi raz w nocy i to co trzeba z tych Actions, z tego VPS-a poprzez Actions robi skrypt do backupu, który się wykonuje. Więc jak się sfailuje dostaje powiadomienie z workera, że job się wyłożył. Mam status, więc ja robię w ten sposób. I mam dwa podejścia do tego, dwa podejścia. Pierwsze jest takie, że tam gdzie mam mało tego, walę jakieś backupy różnicowe i inne takie rzeczy. Mam to w totalnej pompie i po prostu robię dumpa bazy i innych rzeczy, .tar, .gz i wrzucam na S3. I dlaczego na S3? Bo za nią płacę i mam podpiętą kartę i działa tam blog, więc to nie zginie. I to jest pierwsza rzecz.

[00:24:32.510] **Szymon Warda:** Można łatwo ustawić rule, żeby to szło do Archive czy tam Iceberga i [niesłyszalne 00:24:35].

[00:24:37.400] **Łukasz Kałużny:** Tak, żeby szło dalej. Druga rzecz, jak mam i mam też projekcik gdzie mam tak jak Ty więcej danych, może nie tak dużo jak Ty, o tak, to nie jest ta skala, ale ten. To tutaj polecam taki sofcik, on się nazywa Air Clone. Czyli to jest air sync dla chmury, dla storage cloudowych. Air sync dla storage cloudowych. Jak zobaczycie lista jest potężna tego co wspiera, naprawdę duża. I w tym miejscu, słuchajcie, i ciągle jest wydawane, rozwijane, i są, jak potrzebujecie tanio, naprawdę tanio miejsca, do backupów polecam mieć takie, które podepniecie pod kartę kredytową, to jest bardzo ważna rzecz, by dostać powiadomienie, że nie udało się zrobić płatności, że płatność była, wiecie, że jest. I dwa takie, Backblaze, czyli ta usługa od tanich backupów. Mają też storage zgodny z S3 i publikują te fajne raporty o dyskach. To jest też taka ciekawa rzecz. Albo storage od Cloudflare, czyli R2, też zgodna z S3. Ja po prostu... Mi nie robi...

[00:25:40.630] **Szymon Warda:** Miałem.

[00:25:41.440] **Łukasz Kałużny:** Co miałeś?

[00:25:42.430] **Szymon Warda:** Miałem odtworzenie z Backblaze'a.

[00:25:44.830] **Łukasz Kałużny:** Wolno.

[00:25:46.150] **Szymon Warda:** Nie chodzi o to, że wolno, ich soft do pobierania tego recovery jest tak beznadziejny, wywala się i co więcej, jeszcze powiem Ci jedną rzecz, Backblaze niestety nie masz pewności czy te wszystkie pliki są dobre, bo jeżeli im się coś wywali to nie zawsze wiesz... Jak im się wywali i oni nie pobiorą tego, co zginęło, to masz przerąbane. Tak że ja z Backblazem mam kosę.

[00:26:11.290] **Łukasz Kałużny:** Ale Ty korzystałeś z ich softu, prawda?

[00:26:13.630] **Szymon Warda:** Korzystałem z ich softu.

[00:26:14.890] **Łukasz Kałużny:** A widzisz, to dlatego. Ja tutaj korzystam z API S3, czyli nie mam ich softu do odtwarzania.

[00:26:21.640] **Szymon Warda:** Bo Ty rozróżniasz dwie rzeczy, bo jest Backblaze for business i Backblaze osobisty. I for business może być niegłupi, faktycznie, oni są bardzo tani, a ten do osobistego backupu i pobierania wersji, itd., totalna padaka. Tak że tego bym bardzo mocno mimo wszystko nie polecał. For business? Tak, może być, ale to jest zupełnie inna usługa.

[00:26:40.720] **Łukasz Kałużny:** Raczej to jest, bo u nich to jest po prostu to się nazywa, to jest B2Cloud Storage, czyli po prostu tanie API S3. Z Cloudflerem po prostu działa i też jest zgodne z S3. Dlatego ja polecam tego Rclone'a do tej części.

[00:26:56.920] **Szymon Warda:** Tu się możemy zgodzić, tak, to faktycznie działa nieźle.

[00:26:59.350] **Łukasz Kałużny:** Dobra, teraz temat, który jest problematyczny i często... Powiedz mi jak często miałeś secrety scommitowane w repo z lenistwa?

[00:27:09.250] **Szymon Warda:** Secrety scommitowane w repo? Tak, zdarzało się, jak najbardziej.

[00:27:11.470] **Łukasz Kałużny:** Do prywatnego repozytorium. Dobra, i...

[00:27:14.740] **Szymon Warda:** Wiesz, też mówimy o projektach, które się zaczynały lat temu dużo, więc trochę inne podejście było do wielu rzeczy.

[00:27:20.890] **Łukasz Kałużny:** Tak, dokładnie. I słuchajcie, ja mam dwa podejścia. Pierwsze takie tam, słuchaj Szymon, niedawno z lenistwa się odkryłem, że od roku korzystam nadal ze scommitowanego jakiegoś klucza API. Jak musiałem go zmienić, to odkryłem, że leżał po prostu w kodzie i tyle. Jak to szybki projekt, który sobie ciągle stoi. Więc ja sobie podzieliłem to na tryb super cebula i tryb zdroworozsądkowy. Super cebula polega na tym, że secrety wciskam sobie na mojego VPS-a jako envy, po prostu buduję sobie plik z tego, z secretów w GitHub Actions, które też będziesz pokazywał. Czyli w jaki sposób wrzucać. To jest tryb super cebula.

[00:28:06.430] **Szymon Warda:** To doprecyzujmy, secrety w GitHub Actions czy masz w secretach GitHub Actions'ów, nie są one zacommitowane normalnie, w apply CI/CD.

[00:28:13.330] **Łukasz Kałużny:** Tak, trzymam je, dokładnie, trzymam je i buduję sobie z tego plik .NFT, czyli ten nfile. I to jest pierwsza rzecz. Druga rzecz, do której dojrzałem niedawno, korzystałem z tego lokalnie, ale nigdy nie korzystałem z tym. Jeżeli ktoś płaci za 1Passworda, korzystacie z 1Passworda, nie wiem jak inne password managery. Ty Szymon masz urazę do 1Passworda, nie wiedzieć czemu. To słuchajcie, jest tam, bardzo mocno postawili na developer CLI. Czyli 1Password zrobił naprawdę świetne narzędzie deweloperskie i jest ono rozbite na dwa elementy. Po pierwsze, macie 1Password CLI, OP CLI, gdzie na swojej stacji się logujecie normalnie i macie całość i możecie wygenerować konto serwisowe, które ma na przykład nadane uprawnienia tylko do jednego konkretnego volta do odczytu. To jest taka bardzo istotna rzecz. Drugi element, to jak bardziej robimy MVP i idziemy w kierunku komercyjnym. Jest normalnie Secret Server, który prox'uje nas do Volta, a ja wykorzystuję to, żeby skrócić tą historię. Jest takie coś jak generowanie plików albo wciskanie zmiennych środowiskowych w locie. Więc ja zostawię do tego linki. Więc jak ja odpalam sobie tam proces, to wstrzykują się kontem serwisowym te wszystkie secrety z mojego 1Passworda, które są przewidziane dla side projectów.

[00:29:42.670] **Szymon Warda:** Ja bym powiedział tak, nie używamy 1Passworda albo secrety GitHubowe, albo jeżeli korzystamy z S3 i BLOB-a czy jakiekolwiek innego providera, a pewnie z jakiejś tam usługi będziemy korzystali, która jest tania, do backupów, itd., poleciałbym właśnie z providera secretów właśnie...

[00:30:00.460] **Łukasz Kałużny:** Natywnie.

[00:30:02.150] **Szymon Warda:** Natywnie. Czemu? Żeby nie wprowadzać nowego API, nowego providera, nowej zabawki, bo za rok, kiedy to tego projektu wrócicie, to już nie będziecie pamiętali co.

[00:30:11.870] **Łukasz Kałużny:** Wiesz co, inaczej, jest, wiesz, jedna ważna rzecz, ja z 1Passworda korzystam na co dzień, więc to nie jest...

[00:30:18.800] **Szymon Warda:** Też na co dzień.

[00:30:19.280] **Łukasz Kałużny:** Co?

[00:30:20.390] **Szymon Warda:** Pytanie, co do neigo scryptujesz?

[00:30:22.490] **Łukasz Kałużny:** Przeniosłem się na wrzucanie nfile'ów w formacie, żeby nie mieć problemów. Czyli żeby lokalnie nie trzymać, żeby się przypadkiem nie pomylić, to envy też trzymam w pliku, bo on template'uje plik nfile'ów np. Ma templating plików. Więc z tego korzystam na co dzień Szymon w swoim workflow pracy, więc nie jest to nic takiego co odrzuca, bo tak, że będę musiał sobie przypominać.

[00:30:47.720] **Szymon Warda:** Jak na co dzień, to to ma sens. Ja dalej wolę mieć jak najmniej providerów, żeby nie mieć zabawki później, bo odkopywanie tych rzeczy po jakimś czasie nie jest super pomysłem.

[00:30:58.580] **Łukasz Kałużny:** Dobra i ostatni temat chyba w biedahostingach.

[00:31:03.740] **Szymon Warda:** Free tier od chmur różnych, przeróżnych.

[00:31:07.010] **Łukasz Kałużny:** No dobra. I tak, jest sobie, jeżeli chodzi... Inaczej, Azure i Oracle mają swoje free tiery dla maszyn wirtualnych.

[00:31:22.670] **Szymon Warda:** I dla też app serwisów i innych rzeczy.

[00:31:24.590] **Łukasz Kałużny:** Tak, ale mówię teraz od VMK, bo jest tam, popularne było swego czasu, i w Google też jest, było polowanie na te. Najśmieszniejsze były zawsze w Oracle'u. I tutaj właśnie Damian Kędroń nam wrzucił komentarz, że właśnie prawdziwe 'always free' u Oracle'a to jest 1/8 OCPU 1GB RAM-u. Podobne do Azure'a tak naprawdę. W zamian za użeranie się z nimi i około 16 zł za miesiąc, bo za storage się jednak płaci.

[00:31:55.220] **Szymon Warda:** Sporo, bym powiedział.

[00:31:55.520] **Łukasz Kałużny:** I komentarz i to prawda, że czasem maszynki nie można podnieść, bo się skończyły.

[00:32:02.010] **Szymon Warda:** Z tym się trzeba liczyć, bo ustalmy, też właśnie... To na podsumowaniu powiemy za chwilę właściwie. Co mamy jeszcze? Mamy jeszcze całe serverlessy, o których mówiliśmy, funkcje kontenera, APS-y, itd. I ja bym szedł bardziej chyba mimo wszystko w tym kierunku. Jeżeli ktoś... Pytanie, co chcemy zrobić? Pouczyć się administracji czy postawić aplikację, żeby było, jakiegoś bloga, itd.? To są zupełnie inne.

[00:32:26.490] **Łukasz Kałużny:** Tak, i to są zupełnie inne zabawy. Jak popatrzymy sobie, idąc, nie wiem w ogóle, jak to wygląda w Google, bo nie jestem z tym w ogóle w żaden sposób, to nie jest moje podejście. Za to offering, który jest dostępny w AWS-ie i w Google, ten free tierowy, jest od diabły duży, który jest. On jest podzielony teraz, niestety ma jedną bardzo dużą wadę, jest podzielony na always free i na free przez pierwsze 12 miesięcy. To jest taka rzecz, którą trzeba być świadomy, jak mówią o free tierach. I cebula mode polega na tym, że zamykamy konto i otwieramy nowe po 12 miesiącach, jeżeli dalej coś ma tam działać w tych. I one są do siebie bardzo zbliżone. I z tych always free to są w okolicach miliona wywołań na jakiejś lambdzie, functions, miliona komunikatów na kolejkach, bazy NoSQL-owe typu 25 GB miesięcznie. Więc tego warto sobie zobaczyć, bo takich rzeczy jest we wszystkim na tych free tierach, bardzo jest sporawo różnych elementów, które dostajemy.

[00:33:36.630] **Szymon Warda:** Znaczy moja uwaga odnośnie tego, jeżeli lecimy w serverlessa, to warto jest sobie albo zrobić prepaid, podpiąć kartę prepaidową, albo ustawić sobie budżety, żebyśmy mieli monitorowanie ile właśnie wydajemy, bo zdarza się popłynąć, szczególnie jak robimy coś, o czym zapominamy i potem nagle nam przyjdzie dość niewesoły rachunek.

[00:33:59.490] **Szymon Warda:** A były takie historie.

[00:34:01.440] **Łukasz Kałużny:** Internet jest tym wytapetowany. Ja od tego mam... Inaczej, mam kartę wirtualną i dedykowane konto. Tylko że ona się przedstawia się, nie jest to już Revolut, tylko w banku, kartę wirtualną bez plastiku, ale przedstawia się jako zwykła debetowa. Bo nie wiem jak teraz, kiedyś był już problem z podpinaniem Revoluta do tych wszystkich usług cloudowych niestety. I słuchajcie, i takie podejście, które lecimy, to są, weźmy na przykładzie serverlessa w Azure, co możecie zrobić? To są 3 usługi, ja bym powiedział, 3 zestawy usług. Czyli Compute i tu jest functions, functions container appy, albo app service, ten developerski i to jest taki pierwszy, czyli tam hostujemy. Potem jest warstwa storage'u i na tym można byłoby zakończyć pisanie aplikacji, podobnie w AWS-ie. W Azure storage jest chyba najbardziej niedocenianą usługą, bo ma przecież pięknego, prostego PUP/SUB-a i ma NoSQL-owe, columnwide'owe tables.

[00:35:09.600] **Szymon Warda:** Które są super tanie nawet przy wielkim rozmiarze, masz kolejki. Ogólnie na połączeniu powiedzmy sobie App Service plus serverless plus storage można postawić niezłą aplikację.

[00:35:22.590] **Łukasz Kałużny:** Tak, więc to idzie świetnie. I ostatni tier, to taka zwykła baza danych, czyli właśnie tak jak wspomnieliśmy, czy to w AWS, bożesz, ich Dynamo DB, czy w Microsofcie Cosmos DB, bo jest tam free tier, czy teraz poszedł serverlessowy SQL Database na free tierze również.

[00:35:43.830] **Szymon Warda:** Tak, ale jeszcze dorzucając, bo mówimy teraz właśnie o tych compute'ach, itd. Pamiętajmy o tym np., że monitorowanie, Grafana też ma swojego free tiera. Większość tych providerów, jak chcielibyśmy korzystać z jakichś konkretnych usług, ma swojego free tiera, bo ma swoje chmury, więc oczywiście chcą nas namówić na to, żebyśmy z nich korzystali. Tak że da radę to wszystko pożenić. Oczywiście tam jest trochę mniejszy, głównie jest czas przechowywania tych metryk i innych rzeczy. Mamy ograniczenie, jeżeli chodzi o miejsce, itd. I się musimy pogodzić z tym, że to wszystko śmiga po ruchu publicznym. No ale dla naszych cebula planów to raczej nie robi to większego problemu, nie oszukujmy się.

[00:36:21.490] **Łukasz Kałużny:** Raczej z Discorda z dyskusji uczciwa oferta to 5 dolców/euro za miesiąc. To jest uczciwy offering.

[00:36:32.980] **Szymon Warda:** Płacimy za to czasem. Dobra, to teraz tak trochę podsumowując to, to zapytam się tak, czy warto i dla kogo? Bo to są dwa pytania.

[00:36:41.530] **Łukasz Kałużny:** Zacząłbym "dla kogo".

[00:36:44.920] **Szymon Warda:** Dokładnie.

[00:36:45.340] **Łukasz Kałużny:** To jest chyba w tym... Inaczej, jeżeli są dwie rzeczy, dla kogo taki zewnętrzny ten? Jeżeli developujesz i nie chcesz wystawiać aplikacji na świat, tylko bawisz się, nie ma sensu tego dotykać moim zdaniem, tego cebula mode. Więc tutaj to wykluczam. A idąc, że dla kogo? Jeżeli wystawiasz ten swój side project dla rodziny, dla kogoś na świat, chcesz to pokazać, wystawić do internetu, whatever, to tak. Druga rzecz, próbujesz się nauczyć administracji, devopsowania i innych takich rzeczy z kawałkiem kodu.

[00:37:21.060] **Szymon Warda:** A ja bym właśnie rozszerzył. Właśnie, jak chcesz się nauczyć, nic nie nauczy tak człowieka jak co działa, jak internet działa, jak wystawienie czegoś publicznego. Jak musisz to wszystko zainstalować, administrować, zrozumieć, to masz problemy wydajnościowe, postawić, itd., masz realny przekrój przez wszystko od administracji, przez aplikacje, bazy danych, itd. To jest kopalnia wiedzy. Jeżeli nie dotkniesz czegoś publicznego, nie zrozumiesz i nie ogarniesz. Tak że dla mnie to jest taki trochę must have dla ludzi, którzy faktycznie chcą się rozwijać, żeby może nawet nie będą administratorami baz danych, ale żeby rozumieli, jak to w ogóle działa i zrozumienie tych problemów, które wystąpią.

[00:38:00.180] **Łukasz Kałużny:** Jeszcze od M. Kunikow jest link właśnie z tym z update'ami o self-host taki. I na zasadzie jest duża gama osób, która chce hostować w sensie każdą aplikację w ramach Privacy u siebie.

[00:38:19.830] **Szymon Warda:** Nie ma to żadnego sensu.

[00:38:20.310] **Łukasz Kałużny:** Inaczej, szanuję ich zdanie, okej, mi już szkoda na to życia.

[00:38:29.040] **Szymon Warda:** Można się z tym zarąbać. Naprawdę ilość problemów, która będzie wynikała z providera, bo ilość zabawek, które tam trzeba połączyć, żeby to działało...

[00:38:37.290] **Łukasz Kałużny:** Te wszystkie self-hosty, ja wiem, to się tylko tak wydaje.

[00:38:40.890] **Szymon Warda:** To się wydaje. Jak się to ustawi, to jest fajne. Tam co chwilę się coś psuje.

[00:38:46.080] **Łukasz Kałużny:** Ale potem z tymi open source'ami... Inaczej, dobra, chociaż do NAS-a zapomniałem jak się nazywa, ten soft do NAS-a...

[00:38:54.090] **Szymon Warda:** TrueNAS.

[00:38:54.570] **Łukasz Kałużny:** Co?

[00:38:54.840] **Szymon Warda:** TrueNAS.

[00:38:56.040] **Łukasz Kałużny:** Właśnie nie, oprócz TrueNAS-a ten własny, podobny do Synology. Kurde bij, zabij, nie free NAS, nie TrueNAS... Nieważne, zapomniałem nazwy, nie przypomnę sobie i tyle. Więc od tej strony nie ma sensu. W sensie są softy, które są oczywiście dojrzałe, które się nawet skomercjalizowały częściowo, ale własne self-hosted, no nie, ja mam akurat tutaj po prostu, no nie.

[00:39:25.650] **Szymon Warda:** Ja tu dorzucę, self-hosted open source i ma sens, jeżeli stawiamy to na dedykowanym hardware od producenta.

[00:39:36.360] **Łukasz Kałużny:** A, wiem co, Nextcloud. Jest dojrzały, bo aż musiałem to wyszukać. Dobra, ale wiesz, to teraz tak, wracając, własny self-hosted, to nie, dziękuję. Inaczej, do firmy, jeżeli firma mówi, że idzie w open source, spoko. Do własnych zastosowań, mam to w poważaniu, o tak. I słuchaj, lecąc do podsumowania, warto czy nie warto?

[00:40:01.920] **Szymon Warda:** Dla mnie jest to konieczne dla tych, którzy chcą się czegoś nauczyć. Przejście przez taką ścieżkę zdrowia, bo to będzie ścieżka zdrowia, utrzymywanie czegoś co coś liczy i coś robi i monitorowanie, nauczenie się wszystkiego co aplikacja zrobi i będzie żyła, i ustalanie backupów, itd., jest konieczne, żeby chociaż rozumieć cały proces wytwarzania aplikacji i życia jej.

[00:40:24.960] **Łukasz Kałużny:** I wiesz co, tutaj polecę takim cytatem z Bartoszewskiego z jakiegoś, pamiętam, nie pamiętam, czy to był TED, jakieś wystąpienie, ale to świetnie podsumowuje. Są w życiu rzeczy, które warto i są takie, które się opłaca. Są, które się opłaca i nie zawsze to co warto się opłaca, nie zawsze to co się opłaca warto. I chyba taką filozofią trzeba to podsumować.

[00:40:49.470] **Szymon Warda:** No, jak projekt wypali, to w pewnym momencie warto przejść już na coś konkretnego i zapłacić więcej [niesłyszalne 00:40:54] czas.

[00:40:54.870] **Łukasz Kałużny:** Tak, czyli w przypadku jeżeli chcemy coś wystawić, to w zależności od tego co robimy albo thrashowy VPS i minimalistyczny setup, żeby to się samo wdrażało z jakiegoś właśnie CI/CD GitHuba, GitLabie, whatever, co macie z free tieru. Albo free tier od dostawcy cloudowego ze świadomością jak to powinno działać.

[00:41:22.170] **Szymon Warda:** Brzmi dobrze. Dobrze, kończymy w takim razie.

[00:41:24.360] **Łukasz Kałużny:** Kończymy. Na razie.

[00:41:26.430] **Łukasz Kałużny:** Hej.

[00:41:26.610] **Łukasz Kałużny:** Trzymajcie się.

