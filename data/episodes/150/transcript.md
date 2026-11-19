# 150.mp4

[00:00:10.23] **Szymon Warda:** Cześć, czołem! Słuchacie Patoarchitektów. Prowadzą Szymon Warda...

[00:00:15.13] **Łukasz Kałużny:** I Łukasz Kałużny. Wszystkie linki do tego odcinka znajdziecie na Patoarchitekci.io lub gdzieś tu na dole. No Szymon, chyba zmieniłeś powitanie w swojej części.

[00:00:25.10] **Szymon Warda:** Będę teraz trochę zmieniał. Tak, dobrze, Łukaszu, ogłoszenia. Szkolenia.

[00:00:31.16] **Łukasz Kałużny:** Tak, Patoarchitekci.io/szkolenia. Jeżeli słuchacie tego w kwietniu 2025, to słuchajcie najbliższe nadchodzące to Architektura 101, w której pokazuję jak myśleć jak architekt, jak projektować systemy, o czym pamiętać, co jest nieoczywiste. A Szymon o observability z wykorzystaniem open source'u.

[00:00:57.00] **Szymon Warda:** Dokładnie tak. I jak zbudować sobie ładną platformę. To się chyba trochę będzie przewijało w dzisiejszej rozmowie. Dobrze, dzisiaj trochę taki temat, że Łukasz chciał się pochwalić co tam umie i co tam trzeba zrobić. Ale tak już mówiąc bardzo na poważnie, to pogadamy sobie o tworzeniu własnego PAS-a, ale PAS-a w tym momencie w sytuacji gdy jesteśmy na onpremie. Trochę to jest takie doświadczenie z tego, co widzimy po naszych klientach, że trochę się takiej formy buduje i to z bardzo różnych powodów. Łukasz zacznijmy, w ogóle to po co, po co w ogóle klienci wchodzą w takie rzeczy? Po co? Czemu?

[00:01:32.23] **Łukasz Kałużny:** Rozróżnijmy. Niektórzy modnie nazywają teraz to IDP i zwykle to, co myślą pod IDP, to myślą o tym, o czym mówimy, a nie z perspektywy developerskiej, czyli myślą o: zróbmy sobie hosting w onpremie, który nazwiemy, czy w cloudzie, który nazwiemy IDP. A ja tutaj mówię o tym, że... Inaczej, przez lata w mojej karierze był trend: będą oprócz chmury, to się nazywało wirtualizacją, IT zorientowanym na usługi, zaawansowanym hostingiem. Miało to kupę nazw. Potem przyszła chmura i jak zawsze w IT mamy sinusoidę, czyli porzucamy pewne technologie i pewne technologie wracają. I tu jest tak, że słuchaj, to co powiedziałeś zresztą, mamy już pewne zapytania o to pytanie jak wynieś się z chmury, jak się od niej uniezależnić, może jak z powrotem wrócić do onpremu z niektórymi aplikacjami, które chodzą stale, 24/7 i autoskalowanie za dużo tak naprawdę nie przynosi, jeżeli popatrzymy na palenie. Więc popatrzmy sobie tutaj, takie trzy motywatory, które będą. Pierwsze, to są rzeczy regulacyjne, coraz mniej, ale nadal. Tylko też to gdzieś wychodzi przy całych trendach AI-owych i innych rzeczach, że chcielibyśmy jednak mieć wszystko u siebie w Europie. I co za tym idzie? Też geopolityczne kwestie, które jak nagrywamy, no to wczoraj wieczorem wleciały wspaniałe cła ze Stanów i zaczynają się różne ciekawe rzeczy dziać. Jeżeli teraz popatrzymy, to kolejną rzeczą, która za tym idzie, to są pieniądze. I tutaj zależy jak firma jest zorganizowana, kto liczy pieniądze, bo chmura może być i droższa i tańsza, w zależności. Dyrektor finansowy jest w stanie udowodnić każdą tezę.

[00:03:30.19] **Szymon Warda:** Nie tylko dyrektor, dowolny księgowy wydaje mi się, taki kreatywny.

[00:03:34.15] **Łukasz Kałużny:** Tak. No i ostatnim takim punktem, który nam się zdarza, to jest trochę lewar negocjacyjny na zasadzie wyrośliśmy już z bajki, że ta chmura daje aż tyle rzeczy szybko i te wszystkie gotowe API zaczynają być bardzo dużym uwiązaniem u jednego vendora, więc chcemy być cloud agnostic, ale w sposób zdroworozsądkowy. Nie mówimy, że będziemy teraz już multi, że będziemy od razu multicloud, cokolwiek, tylko chcemy mieć możliwość łatwego zabrania zabawek od siebie do siebie, w inne miejsce i przez to też negocjowania ceny, czy pójścia dosłownie tam, gdzie dadzą nam taniej.

[00:04:15.08] **Szymon Warda:** Ja myślę, że bym dorzucił to, co my widzimy. To jest to, że faktycznie widzimy wynoszenie tych rzeczy, usług takich prostych, typu właśnie compute. No bo co? Stawiamy sobie Kubernetesa i śmigamy w jakiejś tam formie. A są dalej usługi, które z racji chociażby na tą georeduntantność chmury i na to załóżmy [niesłyszalne 00:04:35] i tak dalej, że one dalej tam mimo wszystko zostają albo są wynoszone na samym końcu. To jest taka ucieczka.

[00:04:42.08] **Łukasz Kałużny:** Tak, ale jak sobie popatrzysz nagle z takich elementów, nagle się okazuje, że wydajność wysokiej bazy PAS-owej potrafi być kosmicznie droga w pewnym momencie, jak porównasz za ile to zahostujesz na VM-kach na przykład w jakiś rozsądny sposób. Jak popatrzysz sobie, że każdy vendor uniemożliwia Ci wyjście, bo to jest taka rzecz, którą my już przyjmiemy za oczywistość i tłumaczymy to klientom, że żadnemu vendorowi cloudowemu nie zależy, żeby replikować się poza ich obszar. I za to dostajesz potem ciekawe, że tak powiem, opłaty, które robią marżę. Czy jak wchodzisz na poważnie w rozwiązania enterprise i networking, to zobacz ile jest podatków. Ja zawsze pokazuję ten Azure'owy podatek, gdzie Azure Service Bus kosztuje, ten standard kosztuje, wychodzi tam około 100 dolarów miesięcznie, gdzie private endpoint, czyli ten prywatny networking będzie dostępny przy ilu? Jakieś 500 ponad 500 dolarów miesięcznie za jedną instancję?

[00:05:42.08] **Szymon Warda:** Tak, często właśnie integracja z winetami i tak dalej, już są standardy albo wyżej. Dokładnie. Dobra, ale to w takim razie zacznijmy od tego, bo mówimy sobie, że tutaj platforma na onpremie i tak dalej, co dokładnie przez to rozumiemy?

[00:05:57.06] **Łukasz Kałużny:** Dobra, musimy się wrócić - czego potrzebuje tak naprawdę aplikacja, jak popatrzymy? Bo to trzeba z tej perspektywy zobaczyć. Potrzebujesz dla niej compute'a, o którym powiedziałeś i to jest taki must have, czyli gdzie chcę to trzymać. Z drugiej strony powiesz potem, że potrzebujemy, jeżeli popatrzysz, to wszystkie usługi wspomagające, czyli bazy danych, cache, storage, kolejki i potem rzeczy takie ogólnikowe, które się znajdują, czyli ta cała warstwa, której już zarządzamy aplikacją i się wspomagamy, czyli od strony jakieś repozytoria, CI/CD, logi, monitoring, jakieś być może na koniec observability, portal dostępowy, więc to są takie elementy. Więc taki core plus to co znamy z chmury jako otoczkę, że pracuje nam się przyjemnie.

[00:06:50.06] **Szymon Warda:** No ok, dobrze, to tak wymieniłeś sporo rzeczy. Teraz ja mogę zadać takie ładne pytanie - Łukasz, to co wybrać? Ale go nie zadam, bo oczywiście wiemy co wybrać, bo się wybiera Kubernetesa tak naprawdę. My widujemy faktycznie takie a la platformy budowane jeszcze na innych technologiach, powiedzmy sobie trochę niższego poziomu. Ale tak realnie na to patrząc obecnie, gdyby ktoś miał budować platformę właśnie na onpremie, to czy jest sens wybierać cokolwiek innego niż Kubernetes?

[00:07:18.23] **Łukasz Kałużny:** Szczerze?

[00:07:20.07] **Szymon Warda:** Nie.

[00:07:20.19] **Łukasz Kałużny:** Nie. Znaczy inaczej, można to zrobić, tak. Jeżeli popatrzymy w wirtualizacji, jeżeli popatrzysz się, tam były te wszystkie trendy wokół wcześniej OpenStacka, jeżeli chodzi o całe zagwozdki, chodzi o to, że musisz po prostu szybko stawiać... Inaczej, kończysz na tym, że automatyzujesz VM-ki. I tu będzie taki świetny przykład, który chciałem w ogóle rzucić i zalinkujemy, no to Basecamp i DHH. To, że wynieśli się ze swoimi produktami, Signal 37, dobrze pamiętam? Zawsze mi się myli nazwa ich firmy. Mają ileś tam usług SAS-owych i oni się wynieśli z cloudu do onprema i tam była choroba: not invented here. Inaczej, główni kontrybutorzy do Ruby'ego prawdopodobnie, jeżeli popatrzymy. I napisali, teraz to się nazywa Kamal, czyli własny stack do automatyzacji i deploymentu aplikacji Ruby, dorabiają tam jakąś bazę danych w oparciu o Dockera. Czyli nadal jest to maszyna wirtualna, automatycznie provisioningowana plus czy tego chcesz czy nie - kontenery w jakimś stopniu. Więc takie rzeczy nawet słuchaj powstają, tylko pytanie czy jest sens w wielu miejscach odkrywać koło na nowo? Bo jak powiedziałaś w tym dlaczego Kubernetes - to jest jedna rzecz. Ilość rzeczy, o których wspomnimy dzisiaj, które pojawiły się w sposób zautomatyzowany i gotowy.

[00:08:59.11] **Szymon Warda:** Kubernetes z prostego powodu, to jest to, że jest ekosystem, jest sterowany w formie kodu, który jest w miarę czytelnego Yamla.

[00:09:07.14] **Łukasz Kałużny:** Tak i jego API staje się bazą konfiguracji również, którą aplikujemy.

[00:09:11.12] **Szymon Warda:** Dokładnie tak. No bo my widujemy przecież w jednej instytucji, można powiedzieć, że takiego PAS-a, PAS-a, IaC-a nakodowanego w Ansible, bo w Ansible jest masa ludzi, którzy naprawdę potrafią cuda w Ansible robić. Tylko problem pozostaje taki, że w pewnym momencie staje się dość mocno ograniczone. Kubernetes daje nam to, że mamy tą orkiestrację, mamy to pilnowanie i tak dużo, dużo rzeczy. Tak.

[00:09:35.18] **Łukasz Kałużny:** Przy czym też trzeba podejść do tego świadomie. To jest taka jedna rzecz, którą zrobię. Jak mówimy Kubernetes, to teraz nie bierzemy obrazka CNCF-u i nie mówimy, że mamy wszystko. Tylko to jest naprawdę duży, duży cherry picking komponentów i raczej zastanawiamy się 20 razy, czy my naprawdę potrzebujemy jakiejś funkcji.

[00:09:56.14] **Szymon Warda:** Na przykład kontenerów windowsowych.

[00:10:03.16] **Łukasz Kałużny:** Tak, nie potrzebujecie kontenerów windowsowych i ogólnie powiedzmy, że budowa stosu tutaj na Windowsie, takiego PAS-owego - dobra, darujcie, napiszcie sobie skrypty w PowerShell DSC do deploymentu aplikacji rolling update też da się tym zrobić na wirtualkach i więcej nie kombinujcie.

[00:10:22.22] **Szymon Warda:** Mówiąc tak już totalnie poważnie, bo to jest też ważna uwaga, dobrze ogarnięte wirtualki nie są złym rozwiązaniem. Jeżeli mamy systemy na Windowsie, to zautomatyzowanie tego wcale nie jest takie bardzo trudne i tam nie ma co kombinować. Wirtualki naprawdę się świetnie sprawdzą. Można dużo w DSC zrobić fajnych rzeczy. Dobra, a teraz idziemy z taką rzeczą. To jest taka podstawa podstaw, ale mimo wszystko - tożsamość.

[00:10:47.06] **Łukasz Kałużny:** Dobra, potrzebujesz identity providera. I teraz masz jedno bardzo duże wymaganie. Twój identity provider musi dostarczać OIDC, bo wszystkie te usługi czy Kubernetes, czy inne rzeczy, o których powiemy, potrafią się zintegrować od tej strony, z OIDC, żeby zrobić tą federację tożsamości, podpiąć uwierzytelnianie, autoryzacje w aplikacjach. Jeżeli masz Active Directory, tam masz ADFS-a, to być może możesz wziąć sobie Keycloak, DEX-a i inne takie elementy. Czyli to są toole, które pozwalają się podpiąć do LDAP-a i wystawić go jako OIDC. Bo Microsoftowy ADFS da się, ale nie chcecie tego robić. Znowu tutaj z doświadczenia, daje radę przy dużej skali, ale z drugiej strony ilość wiedzy na ten temat w połączeniu z open sourcem jest niska z mojego doświadczenia, więc potrafi być drogą przez mękę.

[00:11:50.05] **Szymon Warda:** Ok, ale tak zapytajmy się, bo faktycznie to będzie trochę wstęp do tego, co będziemy za chwilę mówili. Mianowicie mówimy sobie o platformie, która jest PAS-owa. Ok, fajnie. A w takim razie co się dzieje w sytuacji, jak... Czy ona musi być totalnie PAS-owa? Czy na przykład mamy, w tym momencie hybryda zaczyna mieć sens? Niekoniecznie hybryda z chmurą może być, ale też z innymi powiedzmy dostarczycielami usług.

[00:12:17.07] **Łukasz Kałużny:** Wiesz co, trochę trzeba wydać założenia, po co to robimy i od czego się odcinamy.

[00:12:23.12] **Szymon Warda:** Zgadza się, ale dla mnie to też pytanie jest odnośnie ile na siebie bierzemy? Bo przechodzimy do kolejnego fragmentu, mamy repozytorium kodu i CI/CD. Czy naprawdę chcemy trzymać repo totalnie na naszych maszynach onpremowych? Zakładamy, że mamy jedno data center, bo to już jest.

[00:12:42.19] **Łukasz Kałużny:** I Szymon i widzisz i teraz jest zabawa. Pytanie jest - w którym miejscu i po co to robimy?

[00:12:47.22] **Szymon Warda:** Dokładnie, bo z tego co mówiliśmy, z racji na koszty na przykład, to używajmy GitHuba.

[00:12:53.23] **Łukasz Kałużny:** Tak, używajmy GitHuba, on może być Twoim... I właśnie, może wróćmy w ogóle po co z tym repozytorium kodu? Po czym? Czemu wspominamy najpierw identity provider, potem repozytorium kodu? Czyli identity provider, to jest dostarczenie Ci tożsamości i tam z produktów open sourceowych jeszcze, jak nie masz Active Directory, nie masz LDAP-a, to produkt, który warto rozważyć. Parę osób, które mnie zna, będzie zdziwione, że to powiem, ale jest to Keycloak, bo jest on najbardziej z open source dorobiony. Jeżeli chodzi o to jak nie chcemy, nie mamy AD, innych rzeczy, Active Directory, Google, AWS-owe, wszystkie są spoko. Czy nie wiem jak z tym, z Auth0, tudzież OctoM miała swoje duże wpadki, więc może nie polecajmy od tej strony, ale tak. I repo kodu, jeżeli popatrzycie, jest jedna rzecz, jest ono potrzebne, bo jak potem powiemy, jest ono dla Was warstwą dostępu i zarządzania taką platformą. Czyli zamiast... Ostatnią rzeczą, którą chcecie robić, to budować piękny portal dostępowy. Pierwszą warstwą są po prostu natywne UI-e, a repozytorium chcę [niesłyszalne 00:14:12], to robię na przykład pull request i pojawia mi się. Robię pull request do repozytorium i dzięki temu moja baza się na przykład stawia.

[00:14:21.01] **Szymon Warda:** Albo odpalam jakiś pipeline CI/CD, druga opcja.

[00:14:25.23] **Łukasz Kałużny:** Tak, dokładnie i to jest taka, tutaj jest taka część. Więc odpowiadając Ci, jeżeli to nie jest część geopolityczna, regulacyjna, odcinam się, to jak najbardziej można wybrać wersję hostowaną tego.

[00:14:41.05] **Szymon Warda:** Raczej będę wybierał, bo utrzymanie własnego CI/CD, jeszcze biorąc po uwagę backupy, [niesłyszalne 00:14:44] danych i tak dalej, to jest bardzo, bardzo śliskie tak naprawdę. Widziałem organizacje, w których nagle repa ginęły i były odtwarzane z loga. Nie polecam. Dobra, a w takim razie ok, mamy sam sobie CI. A co z naszym CD? No bo w momencie wchodzimy w agentów, wchodzimy w inne rzeczy, wchodzimy w networking, połączenia tych powiedzmy wyrzuconych usług z naszym deploymentem, jak w tym całym, czyli jak tą infrastrukturę zmieniać realnie?

[00:15:15.07] **Łukasz Kałużny:** Dobra i to zależy. Jest tak, że z jednej strony, no niestety, musisz mieć, jak podejdziemy sobie zaraz do Kubernetesa, potrzebujesz mieć jakąś warstwę managementową, cluster managementowy, na którym takie workery będą chodziły i tego nie przeskoczysz. Jak popatrzysz na popularne CI/CD, czy weźmiesz Jenkinsa i zapniesz go na zewnętrzne repo, czy weźmiesz GitLaba, czy weźmiesz GitHub Actions z GitHuba, bo będziesz chciał mieć to repo zdalnie, u siebie hostować, to każde z nich ma jakiś sposób integracji z Kubernetesem. Przykład GitHub Actions, ich workery, możesz podpiąć CEDA i skalować na swoim Kubernetesoe workery w Dockerze. Więc to wszystko już jest. O tak, tu nie odkrywamy koła na nowo, tu wszystko w tym miejscu jest, po prostu trzeba, znowu powiem, minimalistycznie, pragmatycznie wziąć te rekomendowane configi i z nich skorzystać. Jak popatrzysz, tam jest drugi element, który poleci, czyli co z GitOpsem? Bo tak go można...

[00:16:19.19] **Szymon Warda:** To się sprawdzi, ewidentnie.

[00:16:21.04] **Łukasz Kałużny:** Tak i to jest ten moment, kiedy ArgoCD, nie jestem aż takim fanem, ale jeżeli chodzi potem o to, że wrzucamy te manifesty i inne rzeczy na Kubernetesa, żeby deployować te komponenty na Kubernetesie, przepychać się z repo, sprawdzi się bardzo, bardzo dobrze z dwóch powodów. Jest już na tyle dojrzały, że dobrze przepycha Yamlę, Helmy, customize'y do klastrów, ma RBAC-a. I z drugiej strony daje też bardzo przyjemny dashboard, który w jednym miejscu może wszystko pokazać, stan Twoich usług w Twoim projekcie, w infrze, którą masz.

[00:16:58.08] **Szymon Warda:** Powiedziałbym jeszcze jedno, nawet Flux, na którego pluje wielokrotnie, w pewnych sytuacjach do utrzymania takich core'owych rzeczy infrastrukturalnych, to też się może sprawdzić, bo będziemy musieli mieć zespół, który to utrzymuje, to się samo nie będzie działo. Więc to, o czym mówiliśmy wielokrotnie, rozdzielenie tego, co widzą developerzy, tego, co widzą zespoły inne, nie musi to być to samo narzędzie zawsze.

[00:17:23.18] **Łukasz Kałużny:** Tak i możecie pomyśleć, że projekt Fargo zaczyna być takim Waszym resource grupą namespacem, który pokazuje wszystkie usługi.

[00:17:33.08] **Szymon Warda:** Okej, ale to teraz wchodzimy, tak dość płynnie, bo ruszyliśmy temat developerów, kto co widzi, co jest dostępem. To w takim razie jakie są warstwy naszej platformy? Czyli co ona będzie miała, czego nie będzie miała, te podstawowe komponenty?

[00:17:47.02] **Łukasz Kałużny:** Jak sobie teraz popatrzysz, to powiedzmy, że jest ta cała ciężka warstwa infrastruktury z Kubernetesem i tym, co jest pod nim. I to jest taka pierwsza i tego, co pod nim nie powinniśmy widzieć jako odbiorca takiej platformy. Potem trzeba sobie powiedzieć jak hostujemy aplikacje na Kubernetesach, w jaki sposób, co udostępniamy. Następnie te usługi, które będą już ontop tego Kubernetesa, czyli bazy danych, storage, cache, kolejki plus rzeczy, które będą gdzieś w części managementowej typu logi, monitoring, portal dostępowy, być może jeszcze jakiś provider do zarządzania secretami na takiej platformie.

[00:18:30.08] **Szymon Warda:** No dobra, ok, spoko. W takim razie to lećmy po kolei. Od najprostszego, czyli hostowanie aplikacji, czyli Kubernetesik.

[00:18:38.18] **Łukasz Kałużny:** Dobra, jeżeli chodzi tak o hostowanie, w ogóle o Kubernetesa, co wybrać? Bo to jest taki duży, duży problem. To tak, z mojego, naszego doświadczenia teraz takim way to go jest Rancher, jeżeli chodzi o...

[00:18:56.20] **Szymon Warda:** A czemu?

[00:18:57.01] **Łukasz Kałużny:** Wiesz co, z jednej strony...

[00:18:58.05] **Szymon Warda:** Bo to jest ciekawy powód.

[00:18:58.23] **Łukasz Kałużny:** Wiesz co, powód jest prosty, rozwiązuje z pudełka najwięcej problemów, które mogą się... Rozwiązuje najwięcej problemów z pudełka. Bo jeżeli popatrzysz, to mamy waniliowego Kubernetesa, mamy różne distra enterpriseowe, które takie no nie do końca są open sourceowe, mamy open shifta i do tego mamy jeszcze Tanzu, a z VMWarem robi się coraz weselej z licencjonowaniem, weszły ciekawe zmiany ostatnio. Znowu podbijają minimalne ilości core'ów. Więc tutaj, jak popatrzymy, Rancher rozwiązuje Ci, po pierwsze, problem jak zdeploy'ować klaster. Druga sprawa, przychodzi z opinionated configiem, czyli przychodzi już z wypracowanym zestawem kompatybilnych driverów Ingressa. I potem dwie rzeczy, które rozwiązuje bardzo mocno, to są upgrade'y in-place. Czyli ten upgrade zachowuje się jak w chmurze, czyli z portalu managementowego możesz dosłownie wziąć i kliknąć z upgrade'u i klaster i upgradeuje węzeł po węźle. Druga rzecz, integruje się z wirtualizacją, czyli może Ci provisioningować VM-ki. I też SUSE ma na bazie tego do wirtualizacji potem Harvestera, który się też na tym bazuje, na tym integruje. I ostatnia, najważniejsza dla mnie zaleta, to jest cały już zopiniowany, przygotowany zestaw - portal dostępowy i sposoby nadawania dostępów. Czyli dostajemy jedno miejsce, w którym nadajemy dostępy do tych wszystkich Kubernetesów, dostajemy UI-a, co wbrew pozorom, gdzie widzimy nasze aplikacje i inne rzeczy.

[00:20:46.09] **Szymon Warda:** Przydaje się.

[00:20:47.20] **Łukasz Kałużny:** I dostajemy od razu te klastry Kubernetesowe, które są wpięte w tego Ranchera i które deploy'ujemy, jak i nimi zarządzamy przez Ranchera. Ten centralny serwer robi też reverse proxy do naszych API serwerów i daje nam całą warstwę uwierzytelniania. Czyli Ty wchodzisz i tak jak w chmurze pobierasz sobie token, cubeconfig i ładujesz się i uwierzytelniasz. To jest bardzo duża istotna zaleta tutaj.

[00:21:14.20] **Szymon Warda:** Ja bym jeszcze dorzucił ostatni element, mianowicie cały pricing, czyli jak jest Rancher sprzedawany, bo on jest często liczony od klastra, więc to staje się bardziej opłacalne. Bo nie oszukujmy się, ceny są ważne, jeżeli mówimy.

[00:21:28.12] **Łukasz Kałużny:** Tak, przy czym większość... Inaczej, jak sobie popatrzymy Ranchera praktycznie, jak nie chcesz wsparcia enterpriseowego, to postawisz go z tymi wszystkimi feature'ami za darmo. To jest istotna rzecz.

[00:21:41.05] **Szymon Warda:** Dobra. Jak najlepiej hostować Kubernetesa dla prywatnego SAS-a? W co wejść dokładnie?

[00:21:49.10] **Łukasz Kałużny:** Słuchaj, gdzie będzie Ci... Inaczej, to wracamy do pierwszego przypadku, czyli co jest Twoim motywatorem. Bo tutaj to co trzeba zrobić, to po prostu policzyć kasę. Pod tym względem to jest po prostu liczenie kasy. Jeżeli jesteś w tym, jesteś w cenie, tak jak powiedzieliśmy, na przykład masz takie czysto regulacyjne, geopolityczne, że się odcinam, to zostaje Ci gdzieś lokalna, zostaje Ci w jakiś sposób kolokacji, kolokacji, w którym Ci są dostarczane serwery, albo sam je kupujesz. Z drugiej strony może gdzieś tańsi dostawcy VM-ek. To wszystko zależy od tego jak będziesz liczył te pieniądze.

[00:22:34.23] **Szymon Warda:** Czyli generalnie powiedzmy zależy od naszej skali, powiedzmy sobie. Bo tak, ustawienie tego w kolokacji będzie dobre, opłacalne inicjalnie, jeżeli chcemy, być bardziej odpowiedzialni i mamy więcej kasy, większą skalę, to po prostu mamy już taki self-hosted, to powiedzmy on na onpremise'ie, a potem możemy kombinować różne opcje hybrydowe.

[00:22:55.11] **Łukasz Kałużny:** Słuchaj, praktycznie już nikt nie ma własnej serwerowni. Więc pytanie, raczej Szymon bardziej przy tej skali jest bardziej pytanie czy kupujesz szafy?

[00:23:07.02] **Szymon Warda:** Tak, czy kupujesz całe szafy.

[00:23:08.05] **Łukasz Kałużny:** Czy kupujesz unity w szafach?

[00:23:11.18] **Szymon Warda:** To się zgadza. Dobra. A zobacz, zostaje nam [niesłyszalne 00:23:16], ładnie mówimy Kubernetes, Kubernetes, a cały czas pomijamy ten obszar, który tam istnieje i będzie istniał zawsze. Czyli mianowicie to jest ten cały bare metal, czyli gdzieś ktoś musi serwery usunąć.

[00:23:28.04] **Łukasz Kałużny:** I teraz tak, jak sobie popatrzymy, to co zrobił VMWare, to wygniótł rynek troszeczkę. I w tym, jak to postrzegać? Jeszcze dwa lata temu bym się nie zastanawiał: weźcie VMware'a, w miarę tanio da się go postawić, jest sprawdzony i nie ma co się zastanawiać.

[00:23:48.02] **Szymon Warda:** To przypomnijmy, bo VMWare zmienił po prostu licencjonowanie i cały zespół...

[00:23:52.02] **Łukasz Kałużny:** Został przejęty przez Broadcoma, a potem wycinają jak cytrynę. Teraz trochę zwolnili w wyciskaniu, ale nadal kontynuują.

[00:24:02.16] **Szymon Warda:** Dokładnie, rok temu, dwa lata temu zmienili właśnie...

[00:24:05.16] **Łukasz Kałużny:** Dwa lata,rok temu się tak zaczęło na poważnie. Dobra, i tutaj jeżeli teraz tak poleci, czy bare metal, czy warstwa wirtualizacji daje Ci to odcięcie od spodu, że tak powiem? I w szczególności, jak popatrzymy na upgrade'y i inne takie rzeczy, jest to w miarę... Bardziej odcinasz się od tego co jest na dole. Też bare metal oznacza, że jak masz goły serwer, na przykład jako worker Kubernetesa, oznacza, że hostujesz tam naprawdę dużo. I wszystko zależy od tego, jak dużo będziemy kolokować ze sobą i od skali. Czyli jak teraz popatrzymy ze względu na wygodę, to raczej jest wzięcie wirtualizacji. I jeżeli mówimy teraz o Harvesterze, o którym mówiliśmy, o Rancherze, to tutaj automatycznie z takiej wirtualizacji wpada np. Harvester i to jest jedna z takich rzeczy. To jest też właśnie bazujące pod spodem na Rancherze, jeżeli popatrzymy. Tak samo jak OpenShift, jeżeli byśmy chcieli jednak więcej zapłacić, tak jak samo OpenShift Virtualization, więc są tam, zaczynają się pojawiać rozwiązania do wirtualizacji na bazie Kubernetesa, bądź bardziej klasycznie można podejść z Proxmoxem, o którym kiedyś już wspominaliśmy, rok temu w odcinku właśnie, jak VMWare zmieniał licencjonowanie i jak do tego podejść. Więc to są takie rzeczy, które można sobie rozważyć. Powiedziałbym moje ukochane Hyper-V, którym kiedyś się zajmowałem. No ale integracje w narzędziach leżą i płaczą w tym miejscu, niestety.

[00:25:48.19] **Szymon Warda:** Jak budujecie platformę na Windowsie, to może tam być.

[00:25:52.02] **Łukasz Kałużny:** Można oskryptować to bardzo przyjemnie. O tak.

[00:25:54.12] **Szymon Warda:** To się zgadza, jak najbardziej. Znaczy będąc w windowsowym ekosystemie to jak najbardziej to będzie działało całkiem nieźle. Dobra, a teraz tak sobie wszystko ładnie gadamy, wszystko ładnie, ale pamiętajmy też o tym, że chmura to nie było tylko to, czemu idziemy do chmury. To nie jest tylko to, że nam się opłaca, to, że jest hype, choć to są częste powody. Ale to jest też to, że daje nam opcję, że w razie czego jak coś buchnie, to mamy za chwilę kolejne setki maszyn, na których możemy się przepiąć. Jak to jest z taką magiczną dostępnością, bym powiedział?

[00:26:25.05] **Łukasz Kałużny:** Ty wiesz co, może powiedzmy sobie, powiedz to klientom, którzy wynosili się z West Europe na przykład w Azure.

[00:26:30.18] **Szymon Warda:** Ustalmy, jak Ci buchnie kilkaset, kilka tysięcy maszyn, to to nie jest tak bardzo ładnie. Ale jak buchnie Ci te kilkadziesiąt.

[00:26:36.18] **Łukasz Kałużny:** Nie, mówię o brakach capacity.

[00:26:38.22] **Szymon Warda:** Tak, też są.

[00:26:40.12] **Łukasz Kałużny:** Dobra, raczej tak, z perspektywy wysokiej dostępności, znowu wróćmy na przykład do motywu kosztów. Czy faktycznie wiesz jak wygląda odpowiedź prawdziwa jak audytujesz i oceniasz? To są dwie rzeczy. Jak robimy wysokość, większość nie wykorzystuje prawidłowo availability zone w systemach, w swoich systemach, a co dopiero mówić teraz. A Szymon wiesz o tym, że jak pokazujesz ile będzie kosztować, jak wygląda architektura active, passive na cloudzie, to zostaje active z backupem po prostu tylko danych do drugiego regionu.

[00:27:24.17] **Szymon Warda:** Żeby często backupem tylko, tak.

[00:27:28.03] **Łukasz Kałużny:** Więc od tej strony słuchajcie, teraz tak, jesteście w stanie, jeżeli popatrzycie, to osiągnąć taką zwykłego deploymentu, jeżeli popatrzymy na same Kubernetesy, to jest to kurde tutaj dużo "to zależy". Bo jeżeli mówimy w obrębie gdybyś stosował AZK-ę, to prawdopodobnie jesteś w stanie osiągnąć bardzo podobne SLA. Jeżeli wykorzystujesz trzy AZK-i, to będzie Ci ciężej to zbudować. Czyli availability zone, czyli to są rozproszone trzy serwerownie, tak jak macie w AWS, w Azure, w Google, 3 zone'y, to będzie Ci to ciężej u siebie utrzymać. Tylko pytanie jest, jak często aż to tak wybucha? Bo to jest też straszymy tymi SLA. Ale Szymon, nie oszukujmy się, większość fuckupów, które jest, nie jest na warstwie tej niskiej, tylko jest najczęściej słuchaj aplikacja albo kawałek i tak Twojego softu i Twojego configu, który zrobiłeś.

[00:28:29.13] **Szymon Warda:** Wiesz co, raczej z jednej strony tak, z drugiej strony ja tu będę jednak trochę bronił, bo jednak... Tak sobie mówimy o takiej ładnej sytuacji, kiedy organizacja ma możliwości i ma zasoby ludzkie na zrobienie tego wszystkiego. Zrobienie tego dobrze jak najbardziej jest realne, tylko po prostu jest kosztowne czasowo i kwotowo, a też wielu rzeczy nie przyspieszymy za bardzo. Inną bajką jest też to, że nawet jak nam coś buchnie w Azure, to odpalamy najwyżej tego Bicepa, Terraforma, czy cokolwiek innego...

[00:28:59.01] **Łukasz Kałużny:** Gdzieś dalej.

[00:28:59.13] **Szymon Warda:** Powstanie gdzieś dalej. W kontekście onprema...

[00:29:01.15] **Łukasz Kałużny:** Tak, tylko pytanie.

[00:29:02.11] **Szymon Warda:** To już nie jest takie różowe często.

[00:29:04.07] **Łukasz Kałużny:** Pytanie, czy będziesz miał gdzieś dalej te dane?

[00:29:08.07] **Szymon Warda:** To jest już kwestia backupów i tak dalej. Jak Ci wybuchnie całe data center to pytanie, czy w ogóle poza zapukaniem do miejsca, czy jakkolwiek się do nich dostaniesz w ogóle i w inny sposób. Tak że to też nie jest takie porównywanie pomarańczy do pomarańczy, tylko tu gdzieniegdzie są pomarańcze i powiedzmy pomelo wchodzi nam w sytuację. Dobra, przechodzimy w takim razie do czegoś, co w sumie my najczęściej zalecamy. To co z hybrydą? I nie chodzi nam paznokcie w tej sytuacji.

[00:29:34.04] **Łukasz Kałużny:** Czy wiesz co z hybrydą? Raczej jeżeli robisz tak platformę, o której tutaj mówię, na przykład na bazie takiego Ranchera, jedna rzecz, która jest istotna, jak mówisz o dostępności, jeszcze do tego wracają i tak musisz gdzieś zrobić offside backup tego wszystkiego. I tutaj na przykład alternatywą, jeżeli znowu to jest tylko kasa, to prawdopodobnie robienie backupu i postawienie klastrów, a potem odtworzenie reszty configu na nich nie jest wyzwaniem.

[00:30:07.07] **Szymon Warda:** No ale doprecyzuj, rozwiązanie gdzie? Bo też zależy co Ci...

[00:30:11.11] **Łukasz Kałużny:** Przez hybrydę mówią u dostawcy cloudowego. Jak weźmiesz takiego Ranchera, pozwala Ci podpiąć na przykład zarządzane Kubernetesy. Czyli możesz nim się wziąć i spiąć, podpiąć się go. Stawiasz taki management, podpinasz do niego AKS-y, EKS-y, GKE i możesz odtworzyć to, co zbudowałeś, na przykład jeżeli mówisz w takiej sytuacji. Wiesz, jak mówisz trochę hybryda, to znowu wiesz, to jest takie wielkie, to zależy po co ja tego potrzebuję. Bo wielkim mitem raczej nie będziesz robił replikacji, traktował cloudu jako drugie data center w tym wypadku, bo pewnie może być za drogie. Albo może postanowisz, że będziesz trzymał tam pasywne rzeczy i będziesz replikował na przykład tylko tą infrę stenową.

[00:30:59.13] **Szymon Warda:** Czyli załóżmy co ja widuję i też zalecam, to jest to, żeby faktycznie te rzeczy, które wiemy jakie mają obłożenie, trzymajmy sobie nawet dla oszczędności finansowych, nawet na onpremie. A rzeczy, które mają piki, albo które żyją w cyklach powiedzmy sobie, na przykład rzeczy developerskie, testowe i tego typu rzeczy, one się na model hybrydowy nadają fenomenalnie, bo to sobie przerzucamy ładnie do chmury i płacimy tylko za ten mały wycinek. Ale tak, zgodzę się faktycznie, ta opcja, że rozpięcie na chmurę i ta opcja, że w razie jakby się coś posypało totalnie, się odpalamy tam, tak, jak najbardziej. To też jest kolejnym argumentem czemu CI albo nasze repo może niekoniecznie u nas na onpremie.

[00:31:44.09] **Łukasz Kałużny:** Tak, jeszcze bym Ci dorzucił jeden taki przypadek, jak mówimy o tej hybrydzie i o kasie. To jest rzecz, wiesz, że na rachunkach środowiska developerskie potrafią w sumie zjadać więcej niż produkcja, bo nikt tego nie wyłącza, nie stopuje, nie deeskaluje. I wiesz, to jest taka rzecz, teraz był mit, że chmura jest tania do developmentu, a ona jest tania w przypadku małych projektów i które chcesz szybko postawić.

[00:32:10.20] **Szymon Warda:** Nie, ja tu się nie zgodzę kompletnie. Ona jest tania, jeżeli te maszyny są odpowiednio wykorzystywane, jeżeli są wyłączane, jeżeli się pilnuje developerów, bo trzeba ich pilnować, a nie to, że po prostu zostawiamy sobie [niesłyszalne 00:32:23] i one właściwie się nie nudzą.

[00:32:25.01] **Łukasz Kałużny:** Wiesz, z drugiej strony PAS-ów nie wyłączysz.

[00:32:29.15] **Szymon Warda:** Tak, ale mówimy o compute'cie. Compute możemy zeskalować...

[00:32:32.16] **Łukasz Kałużny:** Tak, ale PAS robi swoje w tych rachunkach. Dobra, idźmy dalej.

[00:32:36.20] **Szymon Warda:** Dobra. Dobrze, w takim razie, ale już trochę ruszyliśmy, bo ja ruszyłem temat całego CI/CD. A co z takimi właśnie rzeczami, rzeczami właśnie typu rejestry, nugety, feedy, npm pakiety i tak dalej.

[00:32:53.19] **Łukasz Kałużny:** Dobra, opcje masz dwie. Albo korzystasz z tego tak jak korzystałaś. Druga rzecz, jeżeli popatrzymy na produkty, to masz komercyjnie, masz do tego open source. Albo jak chcesz wrzucić to wszystko do jednego worka, centralnie zarządzasz, masz na przykład od JFroga Artifactory, który to wszystko dostarcza.

[00:33:15.14] **Szymon Warda:** Który działa całkiem nieźle.

[00:33:17.02] **Łukasz Kałużny:** I powiedzmy nie jest przerażająco cenowe i jest sprawdzone... Inaczej, gdzie tego nie widzieliśmy, o tak można to powiedzieć.

[00:33:27.17] **Szymon Warda:** Wszędzie Artifactory, przysięgam.

[00:33:29.02] **Łukasz Kałużny:** Tak, dlatego mówimy, bo jak sobie popatrzymy, z drugiej strony, jeżeli nie jest to IDP i skupiamy się tylko na tej części hostingu aplikacji, to Harbor czy repozytoria, bo to repo powinieneś mieć blisko tych Kubernetesów. Więc samo repozytorium nie przeskoczysz. Może apki mogą być sobie budowane nawet SAS-owo gdzieś w cloudzie, ale kontenery muszą być, powinny być gdzieś blisko kodu. I od tej strony, tutaj bym powiedział, że open source'owych rzeczy to tutaj z CNCF-u Harbor jako repozytorium i nie ma co kombinować, o tak, pod tym względem

[00:34:08.21] **Szymon Warda:** To teraz wracamy do pytań z serii trudniejszych. No to w takim razie okej, mamy sobie ładnie opakowane wszystko w Dockery i inne rzeczy. A co z naszymi rzeczami na, powiedzmy sobie, AS-ie, czy naszymi rzeczami, które niekoniecznie są skonteneryzowane?

[00:34:23.21] **Łukasz Kałużny:** Słuchaj, inaczej, jak o tym mówimy, jak mówimy o... Jeżeli mówisz o Windowsie Szymon, jeżeli mówisz o Windowsie, olejmy, robisz maszyny wirtualne, koniec i zakończmy ten temat. Tego nie da się zrobić dobrze, jeżeli chodzi... Kontenery windowsowe, to jest, otwierasz puszkę Pandory używając ich. A w przypadku jak weźmiesz jeszcze workery Kubernetesa windowsowe, to okazuje się, że w puszce Pandory była hydra i jeszcze dodatkowa puszka Pandory.

[00:34:55.18] **Szymon Warda:** Dobra, teraz lecimy, temat, za który nam się dostanie po uszach. Mianowicie, bo odpowiedzi na te wszystkie punkty znamy, to nie jest nic nowego, ale no i mamy teraz bazy danych. No i teraz podzielmy to na dwie części. No bo wiadomo, że jak mówimy o sobie, o bazach typu właśnie bazach nierelacyjnych, no to odpowiedź jest prosta - operator.

[00:35:18.21] **Łukasz Kałużny:** No i dobra, to tak, powiedzmy sobie tutaj ja wrzucam teraz bazę do jednego worka i odpowiadam zamiast "pomidor" - operator. Ale dobra, na poważnie. Operatory, jeżeli chodzi, jeżeli teraz tak pójdziemy, jeżeli chodzi o bazę...

[00:35:38.20] **Szymon Warda:** Chodzi o wzorzec operatorów Kubernetesowych, żeby było jasne.

[00:35:42.03] **Łukasz Kałużny:** Tak, operator mówi to, że weźcie prostego Yamla, na przykład ja chcę bazę danych, ma mieć gigabajt storage'u i trzy albo dwa węzły. To operator potem z tego czegoś robi statefull sety Kubernetesowe i wdraża tą bazę danych. Czyli taki prosty opisik zamienia na całą działającą usługę jak w chmurze, tylko Ty widzisz bebechy. Czyli wrzucamy sobie customowy obiekt do Kubernetesa, który nazywamy Custom Resource Definition - CRD, aplikujemy ten customowy obiekt zasobu i z niego jest budowana, tak jak zresztą w innych rzeczach w Kubernetesie, są budowane właśnie te faktyczne zasoby, ściągane images, jest [niesłyszalne 00:36:26] cluster.

[00:36:26.21] **Szymon Warda:** Czyli bronimy się przed tym, żeby każdy developer nam nowego Helma nie instalował i nie konfigurował dalej, tylko mamy...

[00:36:32.09] **Łukasz Kałużny:** I teraz dlaczego wrzucam Szymon to do jednego worka? Bo jeżeli popatrzymy z baz danych na to, co będziesz chciał: Mongo, Postgres'a.

[00:36:43.02] **Szymon Warda:** Mongo, Postgresa, Redisa, który nie jest bazą danych. Będę chciał jakiegoś FullTextSearcha, Elastica, OpenSearcha i inne bajki, które też nie są bazami danych, żeby jasne było, ale to z reguły w ten sam worek wchodzi. Ale zapytałeś co będę chciał? SQL Server. Realny. Postgresa. Realny. [Niesłyszalne 00:37:05]

[00:37:05.06] **Łukasz Kałużny:** Na Kubernetesie, dobra. Dobra, to teraz tak, wyrzućmy SQL Server i Oracle. Postaw sobie klaster na VM-kach i dostaję kolejny i zautomatyzuj stawianie baz danych.

[00:37:16.05] **Szymon Warda:** Mówiąc bardzo prosto, po prostu miej moduł w Twoim pipelinie CD i który wyśle odpowiednie komendy w SQL-u i stworzy bazę i tak dalej. To jest proste jak budowa cepa.

[00:37:27.09] **Łukasz Kałużny:** Tak, tylko musisz zrobić dobry klaster.

[00:37:30.16] **Szymon Warda:** Tak.

[00:37:31.02] **Łukasz Kałużny:** Wcześniej. To jest wcześniej, musisz zrobić klaster i tak naprawdę wchodzisz na to, że pewnie robisz dwa klastry, bo klastry produkcyjne, developerskie. Jak pójdziemy na open source, tudzież trochę CloudSource, czyli Mongo, Elastica, czy pójdziemy do Postgres'a, czy weźmiemy jeszcze nawet Cassandrę, to na każdego z nich mamy działającego operatora. Jak popatrzymy też mamy klienta, który tak w onpremie świadczy usługi bazodanowe. Wspominaliśmy ostatnio o Postgres operatorze Cloud Native PG, który teraz trafił do CNCF-u. I to jest właśnie przykład, że sorry, Postgres w dzisiejszych czasach załatwi Ci większość problemów.

[00:38:11.06] **Szymon Warda:** Są takie moduły Postgresa, które będą zarządzały klastrem Kubernetesowym, więc można też w drugą stronę pójść.

[00:38:16.20] **Łukasz Kałużny:** Tak, albo całą chmurą. Ale jeżeli popatrzycie sobie, tak jak na przykładzie Cloud Native PG, on stawia wam klastry, pozwala zarządzać backupem, failoverem, replikacją z poziomu tego, że opisujecie to trochę jak deployment Kubernetesowy: ja chciałbym bazę danych, czy jak Yamla w jakiejś innej chmurze, czy: ja chciałbym bazę danych. Mówię o nich, o elementach, jak ja chcę i dostaję ten klaster bazodanowy.

[00:38:48.18] **Szymon Warda:** To mówimy sobie o bazach. Bazy danych nie istniałyby bez jakiegoś storage'u persystętnego. No i co? Coś idziemy poza persystentnymi wolumenami Kubernetesowymi, czy nie bawimy się już w nic?

[00:39:00.06] **Łukasz Kałużny:** Dobra. Po pierwsze, aplikacjom ich nie dajemy. To jest podstawowe, apka nie powinna widzieć persistent wolumenów. Czyli...

[00:39:09.16] **Szymon Warda:** Z wyjątkami bardzo wątpliwymi.

[00:39:10.23] **Łukasz Kałużny:** Co?

[00:39:11.14] **Szymon Warda:** Z wyjątkami bardzo wątpliwymi, typu uploady i tak dalej.

[00:39:16.02] **Łukasz Kałużny:** Tak, tylko to jest lokalny storage. To jest, Szymon, upload też powinno być operacją tymczasową.

[00:39:21.18] **Szymon Warda:** Zgadza się, ale potem finalnie musi gdzieś to przenieść mimo wszystko.

[00:39:25.02] **Łukasz Kałużny:** Tak i sobie teraz rozdzielmy trochę, że jak z memem Panie Arku, to jest dla zarządu. Czyli persistent wolumeny są dla i storage, które możemy pod spodem zrobić, jest kilka rozwiązań. Można zrobić takie rozwiązania hyper konwergentne, które wykorzystują Twój storage pod spodem, lokalny na serwerach, replikują go. Jest Longhorn. Jest, bożesz, ale mi, jest ruch na bazie SEF-a, który to automatyzuje. Inną rzeczą jest Portworx bodajże, wkleję do tego nazwę, to już bardziej komercyjne rozwiązanie, które pozwalają Ci zreplikować lokalny storage, dyski NVMena, SSD, które masz wsadzane w serwerze i zrobić w ramach klastra wspólną pulę. Wspólną pulę storage, z którego są wydzielane piwiki i replikowane. I to jest jedno podejście. Jakbyśmy powiedzieli o tych bazach danych, dlaczego ja tam mówiłem o klastrach i replikacji? Bo wtedy nie musisz mieć w ogóle współdzielonego storage'u w żaden sposób, tylko baza i to część aplikacyjna, baza danych replikuje swój stan i o to dba, co prawdopodobnie może Ci, nie będziesz tak łysieć w tym momentku albo siwieć w zależności od predyspozycji genetycznych. Jeżeli popatrzymy sobie dalej i to jest ta część infrastrukturalna, a drugie, że dla pana Areczka, czyli dla aplikacji, raczej storage obiektowy. I tutaj bym się skłaniał do czegoś, co wystawia API S3 najczęściej i w tej perspektywie to będzie sprawdzone w boju Minio.

[00:41:07.03] **Szymon Warda:** Minio polecaliśmy już chyba kilka razy, o ile pamiętam.

[00:41:09.21] **Łukasz Kałużny:** Tak, więc tutaj nie ma co w tym. Czyli rozwiązanie, które nam wystawi po prostu S3 API i te zasoby storage'owe przerobi na część obiektową. Gdybyśmy mieli własną infrę, tutaj można pomyśleć o jakiejś infrastrukturze SAN-owskiej, ale to już są, mówimy o większych inwestycjach.

[00:41:27.19] **Szymon Warda:** Tak. I z tego co pamiętam, mówimy S3. S3 z reguły kojarzę z AWS-em, ale o ile pamiętam, to teraz też Azure wspiera też.

[00:41:39.03] **Łukasz Kałużny:** Jeszcze chyba nie.

[00:41:41.01] **Szymon Warda:** Ale było głoszone, że ma być.

[00:41:42.16] **Łukasz Kałużny:** Tak, coś tam miało być robione. Wiesz co Szymon, nawet nie wchodziłem w którym to jest miejscu. Nie jest publiczny, to nie jest jeszcze żaden GA. Nie wiem czy to wyszło poza private preview.

[00:41:52.01] **Szymon Warda:** Tak, tyle, że było głośno przez chwilę.

[00:41:54.16] **Łukasz Kałużny:** Inaczej, jest, przyjął się standardem, bo tak jak mówię, nawet hardware w opremie może to mieć jako API w storage'ach obiektowych.

[00:42:01.05] **Szymon Warda:** Dokładnie. Dobra, to wchodzimy jeszcze w kolejny, żeby temat ładnie zamknąć. Backupy.

[00:42:07.03] **Łukasz Kałużny:** Dobra i tutaj backupy zależą od tego co Ty zbudowałeś.

[00:42:14.20] **Szymon Warda:** Czy coś wartościowego czy nie?

[00:42:17.07] **Łukasz Kałużny:** Nie, bardziej... To też, to w ogóle przede wszystkim, ale pierwsze nie, od komponentów, które masz i jak podchodzisz, co rozumiesz przez backup? Bo jak popatrzysz, tak, duża z tych rzeczy część powinna leżeć w repozytorium po prostu. Duża część z tej konfiguracji powinna leżeć w repozytorium, czyli właśnie configi, jak edytujemy aplikację. Ale pojawia się pytanie - co z tym Minio? Co z tymi bazami danych, o których wspomnieliśmy? I tutaj trzeba złapać jakąś strategię, gdzie to wypychać. I to jest trochę podejście, które powiedzieliśmy trochę wcześniej o hybrydzie. Trzeba się poważnie zastanowić, gdzie my i jak my do tej hybrydy podchodzimy.

[00:42:57.13] **Szymon Warda:** Czyli co, jednak ją wypychać mimo wszystko gdzieś dalej.

[00:43:01.10] **Łukasz Kałużny:** Gdzieś wypychać z dala od swojej infrastruktury i od tej serwerowni, w której jesteśmy i skupić się, jedna, to są backupy konfiguracji, żeby w miarę szybko potem to wszystko odtworzyć. Druga rzecz, to jest storage S3, o którym sobie powiedzieliśmy, to też trzeba gdzieś wypchać. I ostatni element to są te bazy danych i część z nich pozwala się backupować właśnie na jakieś S3 i inne API automatycznie, bądź zastanowić się właśnie jak to zesnapshotujemy i wyślemy to w diabły poza to.

[00:43:32.10] **Szymon Warda:** Dobra, to idziemy kolejnym krokiem budulcowym. I oczywiście mówimy o cache'ach. Więc pytanie czy chcemy tu powiedzieć coś więcej poza tym, że Redis i żeby nie zapisywać go, nie robić go persystentnym Redisem. To właściwie koniec naszych rad, jak można powiedzieć.

[00:43:47.05] **Łukasz Kałużny:** Wiesz co? Tak, to jest chyba koniec. Jedną rzeczą jest tak, że w tym. Nie wiem jaki jest stan, bo ostatnio nie robiłem porównań, bo są dwa ten, mamy, jak tam popatrzymy, mamy w sumie trzy operatory bezpłatne open source'owe dla Redisa, ale nie patrzyłem jak wypada ich teraz porównanie w tym momencie. Bo jedyna rzecz, którą trzeba powiedzieć... Inaczej Szymon, to co powiedziałeś, Redis musi nie mieć persystencji pod spodem i tego się nauczmy wreszcie. Ja wiem, że wszyscy kochają robić z tego bazę danych albo że aplikacja nie potrafi działać bez cache'a, jak padnie, zamiast po prostu zwolnić. To nie działa. To bardzo częsty przypadek. Więc pierwsze, wyrzucamy storage. Druga rzecz, pamiętamy, że trzeba tego Redisa sklastrować. Jeżeli mielibyśmy go udostępnić jako usługę, to w postaci właśnie, żeby stawiał się jako mały, dedykowany klasterek.

[00:44:47.10] **Szymon Warda:** Tak i fajnie działa, bo jest takim self healing cluster, czyli sam się umie naprawić, rozrzucić. Bardzo to fajnie działa. Dobrze. Czy mogę teraz zdjąć moją czapeckę pytającego i powiedzieć...

[00:44:58.18] **Łukasz Kałużny:** Tak.

[00:44:59.07] **Szymon Warda:** Odnośnie logów i monitorowania?

[00:45:01.03] **Łukasz Kałużny:** Dobra Szymon, co zrobimy z logami? Bo to jest konik jednak Szymona. I pierwsze, co do zbierania tych logów? Czyli rozumiem, że Elastic po prostu?

[00:45:10.12] **Szymon Warda:** Wiesz co, ja właśnie nie jestem wielkim fanem Elastica. Elastic jest super fajny, super miły i przyjemny do momentu tylko dla konsumentów. Dla tych, którzy mają go utrzymywać i widzieć ile on tam pochłania pamięci i przestrzeni, to nie do końca. Jeżeli budujemy na poważnie platformę, to z całym szacunkiem trzeba nauczyć developerów głównie i sam się wywodzę od developerki, więc to nie jest bardzo negatywna, tak to wygląda, że sorry, ale full text searcha, żeby spisać context error, nie potrzebujesz z reguły. To samo co pokazuję na szkoleniach i też doradzam klientom, spójrzmy na stos grafanowy, bo on się może naprawdę fajnie opłacić, potrafi fajnie działać i jak się ogarnie godzinną, czy też powiedzmy tak trzygodzinną prezentacją, czy warsztatami jak korzystać z języka zapytań do Loki, to po prostu potrafi śmigać i wychodzi bardzo kosztowo.

[00:46:05.20] **Łukasz Kałużny:** Szymon, ale to nie ma full text searcha.

[00:46:08.19] **Szymon Warda:** Bo z reguły go nie potrzebujesz. Analogia, znaczy taka historia, którą mieliśmy odnośnie tego. Mieliśmy klienta jednego, któremu się Elastic totalnie kładł. To tak totalnie. Co się okazało? Okazało się, że jedna osoba miała 64 dashboardy, na których miała przykłady błędów i tam takie niesamowite kwerendy do wyszukiwania właśnie po full text searchu. Super, to kładło cały klaster Elasticowy. Nie potrzebujesz full text searcha z reguły.

[00:46:33.23] **Łukasz Kałużny:** Raczej tak, tylko co musisz zrobić? To jest, lecimy trochę o rzeczy, o której wspominamy często, czyli standaryzacja. A w tym wypadku standaryzacja i strukturyzacja logów niestety, żeby je labelować, tagować.

[00:46:47.16] **Szymon Warda:** Pytanie pozostaje takie właśnie jak teraz podchodzisz? Bo jak tu już naarzuciłeś ten standard, że śmigamy w Kubernetesie, to możemy dwie formy właściwie. Albo możemy te logi po prostu pushować korzystając właśnie z Open Telemetry. Bo ustalmy, to jest super ważne. Nie zbudujemy platformy, jeżeli nie będziemy mieli standardów. A jeżeli mamy Open Telemetry, to możemy zrobić dużo bardzo fajnych rzeczy i to już praktycznie staje się wymagane. I potem lecimy log scriptingiem i zbieramy te logi tak naprawdę. To jest chyba najłatwiejsze. Ja fanem jawnego wysyłania logów z aplikacji mimo wszystko nie jestem. To się nie sprawdza na dłuższą metę. Dobra, to teraz pójdźmy sobie do monitoringu. Monitoring znowu nam ułatwia całkowicie Open Telemetry. Jeżeli mówimy, że chcemy być agnostyczni i tak dalej, to to jest jedyny wybór, bo płacenie, bycie całkowicie na onpremie i płacenie grubych setek tysięcy dolarów za narzędzia do APM-u, to chyba nie w tym kierunku chcieliśmy pójść. I w tym momencie do czego będziemy to zbierali? W sumie staje się obojętne. Prometeusz tam będzie. Czemu? Mamy Kubernetesa. Metryki z Kubernetesa ładnie zbieramy Prometeuszem, to staje się już naturalne. Druga opcja, to zostaje nam, więc też zbieramy aplikacje, dostajemy trace'y, które przydałoby się znowu...

[00:48:05.03] **Łukasz Kałużny:** Gdzieś wrzucić.

[00:48:06.02] **Szymon Warda:** Stos grafanowy spełnia też się fenomenalnie.

[00:48:10.06] **Łukasz Kałużny:** Znaczy jest takim jednym, w sensie można to, że tak powiem, z jednej paczki zbudować. I da się zrobić też bieda version anomaly detection na metrykach.

[00:48:21.03] **Szymon Warda:** Mozna zrobić, tak i ma się jeden portal wejścia. Stawiamy Grafanę i nagle w jednym miejscu wszyscy mają wejście i wszystko widzą, to co powinni widzieć. No bo problem takich platform wewnętrznych, które działy się powiedzmy lat temu ileś tam, nagle, że mieliśmy stronę Wiki albo Docsa, gdzie mieliśmy wszystkie linki do różnych systemów, które ze sobą w ogóle nie rozmawiały i w ogóle nie gadały i to było rozproszone, co tak nie może być. To musi być w jednym miejscu, żeby udawało ten portal a la chmurowy, tak.

[00:48:49.14] **Łukasz Kałużny:** No dobra, teraz taki temat, który kochamy, czyli kolejki.

[00:48:55.18] **Szymon Warda:** Kolejki i kolejki można już teraz. Znowu, operatory tu ogarną praktycznie wszystko, można powiedzieć też.

[00:49:01.09] **Łukasz Kałużny:** Tak, ja bym powiedział kolejki, zmniejszyłbym ilość do dwóch rozwiązań.

[00:49:07.21] **Szymon Warda:** Dwóch typów, bym powiedział.

[00:49:10.02] **Łukasz Kałużny:** Raczej dwóch typów. Raczej ja bym bezczelnie do dwóch produktów, które reprezentują. Jeżeli chodzi o smart brokery, no to RabbitMQ ma swój klaster operator. Czyli tak jak mówiliśmy, przychodzi z pudełka, jest utrzymywany. Jak rozmawiamy, 17 godzin temu ten, commicik wersja 12.2.1, czyli aktywnie się rozwija. O tak, to jest jedna rzecz. Druga rzecz, Kafka nie służy do bycia kolejką, ale wiemy, że takiej używacie. Więc Kafka również z operatorem.

[00:49:46.15] **Szymon Warda:** Jest i mogę powiedzieć sam stawiając ją, działa, ma się dobrze, korzystajcie.

[00:49:53.12] **Łukasz Kałużny:** Tak. Tu jest problem, jeszcze możecie trafić na artykuł: Choosing the right Kubernetes operator for Kafka, więc to jest taka rzecz. Tu jest wybór, o tak powiedzmy. Rabbit podchodzi z tym, tu jest jedyny słuszny wybór. Z Kafką warto sobie zobaczyć plusy i minusy, podejść.

[00:50:13.12] **Szymon Warda:** Dobrze Łukaszu, to teraz kiedy postawić backstage?

[00:50:20.11] **Łukasz Kałużny:** Dobra. Czyli portal dostępowy. Portal dostępowy. Dobra i teraz na poważnie. Na początku Grafana repo/CI/CD i Argo powinny być + rancherowy taki portal, powinny być po prostu tymi elementami, które są opisane powiedziane: tu masz to, jak chcesz obejrzeć swojego Kubernetesa, swoje aplikacje, to masz tu, logi, metryki masz w tej Grafanie, deployment Twoich usług PAS-owych i ich konfiguracja, tu jest repo, którym to wysyłasz, tam CI/CD. Argo, możesz sobie podejrzeć status na tych klastrach, do których nie masz dostępu. To w ten sposób wygląda, bo to co nie padło, tych klastrów powinno być minimum 4, jak popatrzymy tak zdroworozsądkowo: produkcyjny i nieprodukcyjny management, na usługi PAS-owe, takie bazodanowe, state'owe i taki techniczny na, być może z tym managementowym połączone, na monitoring + na logi.

[00:51:22.18] **Szymon Warda:** Ewentualnie hostowanie agentów CI, takie rzeczy, które służą typowo platformowe.

[00:51:27.17] **Łukasz Kałużny:** Tak i backstage, jak powiedziałeś bezczelnie, nie warto budować prawdopodobnie tego samemu, bo będzie to raczej opus magnum niż coś działającego, albo zawsze będziemy przeklinać. Lepiej dostosować sobie backstage. To jest w ogóle ostatnia rzecz, którą robimy, tak naprawdę na samym, samym końcu. To nie jest na początku, to jest na końcu.

[00:51:50.12] **Szymon Warda:** To jest fajne narzędzie, które służy inwentaryzacji tego, co zrobiliśmy, które nam, jeżeli mamy problem tego, że zaczyna się rzeczy dziać zbyt dużo, to fajnie pokazuje i buduje ładną używalność tych aplikacji, że inne zespoły nagle widzą, co można wykorzystać, co już istnieje, jakie są standardy i tak dalej. Absolutnie nie jest na starcie.

[00:52:11.21] **Łukasz Kałużny:** Tak więc jest tego tam, znajdziemy jeszcze parę innych tych. Nawet na Reddicie był kiedyś wątek z: Backstage not user friendly. I want something better.

[00:52:23.17] **Szymon Warda:** Bo nie jest do końca. Dobra, to co podsumowujemy teraz na chwilę obecną już?

[00:52:30.18] **Łukasz Kałużny:** Możemy, tak. Czyli nie budujcie własnego backstage na samym końcu, jeżeli ktoś chce, albo alternatywy, które znajdziecie.

[00:52:38.08] **Szymon Warda:** Kiedy PAS własny? Podsumowując krótko, krótko i na temat.

[00:52:41.17] **Łukasz Kałużny:** Jeżeli masz drivery, czyli chciałeś się odciąć od chmury, chciałeś się od niej uniezależnić, musisz od niej uciekać.

[00:52:50.06] **Szymon Warda:** Dobra.

[00:52:50.16] **Łukasz Kałużny:** To jest ten moment. To nie jest driver technologiczny.

[00:52:53.08] **Szymon Warda:** Ile tam jest budowania własnej platformy na onpremie?

[00:52:57.23] **Łukasz Kałużny:** Wiesz co? I tutaj po konsultancku powiem od MVP. Możesz mieć, w MVP na te wszystkie elementy możesz mieć działające w 3 miesiące, 3-4 miesiące. Jeżeli nie masz zasobów, to nieskończenie wiele. I to jest teraz tak jak powiedziałeś, w tym, ja bym poszedł jeszcze w jedną rzecz, powiedziałeś ile to zajmie, to w MVP możesz mieć w 3 miesiące, jak masz wiedzę o tych wszystkich komponentach.

[00:53:26.12] **Szymon Warda:** Albo masz kogoś, kto ci to postawi. Na przykład my.

[00:53:29.13] **Łukasz Kałużny:** Tak, dokładnie. Jeżeli teraz popatrzysz na to, to postawienie to jest jedno. Potem to trzeba utrzymywać i update'ować, czyli to, czego nie powiedzieliśmy po drodze. Tak jak z Rancherem to trochę przeminęło. Chodzi o to, że niestety trzeba to wszystko update'ować i tych technologii nie wrzuciliśmy. Tu na przykład nie powiedzieliśmy o zarządzaniu secretami, o Ingresach, load balancerach, bo tutaj jeszcze będzie dużo takiej drobnicy decyzyjnej pod spodem, która też musi się gdzieś pojawić, bo mówiliśmy o takich warstwach. Trzeba pamiętać, że to trzeba wybrać i potem jeszcze utrzymać.

[00:54:05.22] **Szymon Warda:** I jeszcze zapomniałeś o jednej rzeczy - rozwijać. To jest system, który będzie cały czas żył, będą wychodziły nowe wersje tego systemu, będziemy wdrażać nowe standardy, będziemy pewne rzeczy obudowywać. Będą wchodziły też standardy nie tylko aplikacyjne, ale też tego, co chcemy wewnątrz organizacji robić. To jest rosnący worek tego, co trzeba utrzymywać.

[00:54:26.04] **Łukasz Kałużny:** Dobra i jeden błąd, który chyba najczęściej jest popełniany. Za dużo chcemy zrobić naraz i wrzucamy z prezentacji tego diagramu CNCF-a, chcielibyśmy wszystko wrzucić na tą platformę. Więc to jest taka przestroga, że podchodzimy minimalistycznie.

[00:54:44.05] **Szymon Warda:** Raczej lepiej jest mieć mniej rzeczy i ogarniętych, ładnie zarządzanych, niż mieć cały pierdolnik i mieć z tego po prostu brak jakiejkolwiek platformy czy brak czegokolwiek, czy każdy będzie po swojemu robił. Wtedy wprowadzamy jeszcze większy bałagan i to się po prostu nie opłaca w żaden sposób.

[00:55:02.23] **Łukasz Kałużny:** Dobra.

[00:55:04.14] **Szymon Warda:** Dobrze. Przyszłość PAS-ów lokalnych.

[00:55:07.23] **Łukasz Kałużny:** Czy wiesz co, ja mam ciągle zakład, czy będę... Inaczej, przyszłość jest taka, że pytanie, czy tego będziemy potrzebować, czy będziemy po prostu projekty sobie stawiali niezależnie wszystko na jednym Kubernetesie i tyle. Wiesz, to jest takie, bo to wynika z potrzeb. To jest trochę jak z IDP.

[00:55:28.22] **Szymon Warda:** Z IDP. Wydaje mi się, że to, że rozmawiamy z reguły z dużymi instytucjami, to trochę przekrzywia nasze takie spojrzenie na to, że to się po prostu może opłacać. W instytucjach - tak. Naprawdę trzeba mieć porządną skalę, żeby to była inwestycja, która się zwróci w jakiejkolwiek formie.

[00:55:44.21] **Łukasz Kałużny:** Tak, jak masz kilkadziesiąt workerów Kubernetesowych, prawdopodobnie ma to sens.

[00:55:50.14] **Szymon Warda:** Przy 12 workerach?

[00:55:52.07] **Łukasz Kałużny:** Kilkudziesięciu. 12 to nie kilkadziesiąt.

[00:55:57.10] **Szymon Warda:** No dobrze, niech Ci będzie.

[00:56:00.06] **Łukasz Kałużny:** 50+ Szymon, 50+.

[00:56:04.08] **Szymon Warda:** 50+, to się zgodzimy w tej sytuacji, tak. Ale powiedzmy przy tych 20, to niekoniecznie.

[00:56:11.13] **Łukasz Kałużny:** Nie. I teraz pytanie, jak dużo też masz projektów? Bo jeżeli masz jedną większą, dwie, trzy aplikacje, to co mówiliśmy, to w ogóle nie ma sensu. Stawiasz współdzielony klaster i wrzucasz te wszystkie rzeczy odpowiednio od siebie izolując.

[00:56:29.11] **Szymon Warda:** Pytanie, czy jesteś w stanie przeznaczyć zespół, 2, 3 zespoły ludzi na utrzymywanie tego, co właśnie stworzysz? Prosta opcja. Dobra. Czy budowanie takiej platformy na onpremie będzie miało sens w przyszłości? Czy to się będzie rozwijało, czy się będzie zmniejszało?

[00:56:51.03] **Łukasz Kałużny:** Ja obstawiam, że będą powroty z chmur. Albo chęć odcięcia się od chmur.

[00:56:58.18] **Szymon Warda:** Ale pytanie w takim razie, odcięcie się od chmury i przejście na onprema? Czy odcięcie się od chmury i przejście bardziej do na przykład OVH, czegoś, co jest tańsze, ale śmiga na wirtualkach i tam ogarnięcie sobie tego?

[00:57:10.04] **Łukasz Kałużny:** Czy wiesz co, to zależeć będzie od potrzeb. Ja teraz powiem, zależy od ceny i tego, co nas motywuje, tak jak Ci powiedziałem wcześniej, bo to pójdzie pod motywację. Zobacz, że my rozmawiamy tutaj, to jest tylko rozwiązanie motywacji biznesowych. Technologią można budować dowolne piękne rozwiązanie, ale zawsze są jakieś inne rzeczy. I powiedzieliśmy sobie o rzeczach regulacyjnych, tych rzeczach politycznych, odcinaniu się od tego, co się dzieje. Z drugiej strony kasa i to zawsze będzie zupełnie inny driver, zawsze.

[00:57:47.13] **Szymon Warda:** Czyli kończy się na kasie mimo wszystko. Dobra, to co? Kończymy.

[00:57:52.01] **Łukasz Kałużny:** Trzymajcie się, na razie.

[00:57:53.11] **Szymon Warda:** Pa, pa. Hej.

