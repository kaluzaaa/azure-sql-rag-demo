# 166.mp3

[00:00:00.000] **Szymon Warda:** Jeżeli każdy robi po swojemu moduły i nie mamy takiej standaryzacji, czyli każdy na własnym koncie, to obstawiam, że całkowicie leży pilnowanie kosztów, infrastruktury, tagowanie, kto za co płaci i tak dalej.

[00:00:12.660] **Łukasz Kałużny:** 80% use case'ów będzie taka sama. 20%, darujcie sobie, nie ma co sprawdzać.

[00:00:18.630] **Szymon Warda:** Często zaczynamy, przepraszam, pozdrawiam wszystkich przedszkolaków, od dupy strony. Czyli zaczynamy od technologii, a nie od standardów i nie od tego, żebyśmy mieli co self-service'ować.

[00:00:29.370] **Łukasz Kałużny:** Czy zespoły chcą standaryzacji, czy będą walczyć?

[00:00:43.530] **Szymon Warda:** Cześć, czołem, kluski z rosołem. Słuchacie Patoarchitektów. Prowadzą Szymon Warda...

[00:00:47.730] **Łukasz Kałużny:** I Łukasz Kałużny. Wszystkie linki do tego odcinka, dacie sobie radę, znajdziecie gdzieś tu w opisie czy na stronie pod tym samym numerem co odcinek po slashu. A dzisiaj mamy pytanie z Discorda, które padło nam na tapet i nas zainteresowało. Mianowicie od użytkownika Dogo.

[00:01:12.980] **Szymon Warda:** Pozdrawiamy.

[00:01:14.060] **Łukasz Kałużny:** Tak, i to jest takie klasyczne pytanie, z którymi się spotykamy: platform engineering, od czego zacząć?

[00:01:22.640] **Szymon Warda:** I pytanie: czy jest potrzebne, bym powiedział.

[00:01:24.590] **Łukasz Kałużny:** Właśnie, tak, czy jest potrzebny. I tak naprawdę problemy, które się pojawiły, skracając całe pytanie, to jest brak self-service'u, bo każdy zespół pisze własne rozwiązania. Chaos w deploymentach, bo każdy zespół wdraża na swoim koncie AWS-owym. Bałagan organizacyjny. Robi się burdel, cytując. Długi czas wdrożeń od commita do feature'a u klienta miesiące, lata.

[00:01:54.080] **Szymon Warda:** To jest dziwne, bo z reguły jak zespoły mają osobne konta, to z reguły właśnie ten czas jest krótszy, czyli wdrażają szybciej. Więc tu takie dwie rzeczy nam nie grają za bardzo.

[00:02:03.460] **Łukasz Kałużny:** Tak, ale do tego jeszcze przejdziemy sobie. Frustracja biznesu, długie cykle wpływają na konkurencyjność. Brak standardów, każdy robi po swojemu. I jak popatrzymy stos technologiczny, bo ten kontekst jest istotny, produktowy SaaS, 2, 3 flagowe produkty. To jest dla mnie taki red flag, że SaaS i 2, 3 produkty często, ale to już zostawmy. Cloud w postaci AWS-a IaC, Terraform, CI/CD, Jenkins z migracją w trakcie na GitHuba i GitHub Actions. Automatyzacja trochę tu, trochę tam, czyli fragmentaryczna. Zespół 700 osób w firmie, 200-250 inżynierów, programistów, DevOpsów. To jest ciekawa statystyka.

[00:02:49.060] **Szymon Warda:** To ja mam pytania od słuchacza, bo to jest też ważne. Czyli w ogóle od czego wychodzimy? Pierwsze, czy to dobra motywacja do budowania platformy? Drugie, czy to właściwe podejście w sytuacji na rozwiązanie problemów? I czy faktycznie potrzebują platformy? No i w ogóle jakaś prośba o rady praktyczne, jak w ogóle by to ugryźć?

[00:03:10.710] **Łukasz Kałużny:** Więc stąd mamy ten odcinek. Stwierdziliśmy, że to bardzo dobry temat, żeby go omówić. I słuchajcie, jeżeli byśmy, zaczniemy chyba tak jak konsultacyjnie, czyli w sumie powiedzieć sobie, realnie nazwać problemy. Bo to nie jest teraz problem, że potrzebujemy platformy czy nie. Prawdopodobnie można byłoby skrócić tą rozmowę do tego: potrzebujecie platformy, ale... I tutaj będzie bardzo długi, bardzo długi wywód, ale zobaczmy, jakie mamy problemy. Po pierwsze, jest ten chaos z Terraformem, czyli każdy zespół sobie coś pisze. Oznacza to, że governance w ogóle w tym momencie jeszcze nie istnieje, nie ma żadnej standaryzacji.

[00:03:53.730] **Szymon Warda:** Ale też security prawdopodobnie też leży.

[00:03:56.580] **Łukasz Kałużny:** Tak. I to co powiedziałaś powiedziałeś teraz właśnie security, to drugi problem. Każdy wdraża na swoim koncie AWS. Czyli prawdopodobnie Organization Landing Zone, setup cały nie istnieje. Do tego pewnie potem elementy, które są w AWS-ie. Jesteśmy bardziej Azure'owi, więc AWS-a to tak z pamięci trzeba walić. Ale tam było Guard Rails, Service Control Policies prawdopodobnie nie istnieją, nie są używane. I zostanie standardowe pytanie, czy faktycznie potrzeba tylu kont?

[00:04:30.450] **Szymon Warda:** Dla mnie jeszcze tu się świeci kolejna rzecz. Jeżeli każdy robi po swojemu moduły i nie mamy takiej standaryzacji, czyli każdy na własnym koncie, to obstawiam, że całkowicie leży pilnowanie kosztów infrastruktury, tagowanie, kto za co płaci i tak dalej.

[00:04:45.330] **Łukasz Kałużny:** Wyciągnąłeś mi to z ust. To jest w ogóle jeszcze nienazwany problem.

[00:04:50.310] **Szymon Warda:** Kolejna rzecz, która jestem pewien, że występuje, publicznie wystawione usługi, ponieważ nie ma zestawionych tuneli, ludzie dostają się do baz danych publicznie i to całkowicie połączenie developerów z AWS-em leży.

[00:05:05.260] **Łukasz Kałużny:** Nawet jeżeli są DevOpsi.

[00:05:06.850] **Szymon Warda:** (...) publiczne prawdopodobnie.

[00:05:09.010] **Łukasz Kałużny:** Dobra i Twój ulubiony problem.

[00:05:12.430] **Szymon Warda:** Tak, długie cykle wydawnicze, miesiące, lata od commitu do klienta. To jest absurdalne w kontekście SaaS-a. Nie wyobrażam sobie takiej sytuacji. Ale co mnie bardzo dziwi, to jest to, że skoro zespoły mają wysoką autonomię, bo mają własne konta, tak by wynikało, to co tam się dzieje, że mają takie długie cykle wydawnicze.

[00:05:33.760] **Łukasz Kałużny:** Raczej to taki ten określając 5 Why Moment, trzeba zacząć drążyć, co jest przyczyną.

[00:05:40.390] **Szymon Warda:** Tak. I tu trzeba zaznaczyć od razu, bo to mogą być dwie rzeczy i trzeba to podzielić. Może to być długi cykl wydawniczy, developerski, a może też to być po stronie samych Opsów, DevOps'ów, nazwijmy to tej części infrastrukturalnej.

[00:05:53.770] **Łukasz Kałużny:** Chciałbym zacząć się zakładać, o co tam chodzi.

[00:05:56.630] **Szymon Warda:** Jedno i drugie.

[00:05:57.860] **Łukasz Kałużny:** W którym, tak jedno i drugie to jest jedno. Jeżeli mam rację, to piwo w takim razie tak zwane. Czy przypadkiem tam u Was nie zbudowaliście rozproszonego monolitu na wielu kontach AWS?

[00:06:13.940] **Szymon Warda:** Możliwe. Dla mnie druga rzecz, że z racji, że jest dużo zespołów, to wprowadzili sprawdzenia i cały zestaw podpisów...

[00:06:22.130] **Łukasz Kałużny:** Regresji.

[00:06:22.970] **Szymon Warda:** Musi się na co zgodzić. I to czeka na wszystkich na quality gate nazwijmy to.

[00:06:29.210] **Łukasz Kałużny:** Quality gate albo testy regresyjne, które zlecą, stoją w kolejce.

[00:06:33.860] **Szymon Warda:** Oczywiście, że tak.

[00:06:34.910] **Łukasz Kałużny:** Tak.

[00:06:35.240] **Szymon Warda:** Dokładnie.

[00:06:35.600] **Łukasz Kałużny:** Dobra, no i nasz ostatni ukochany problem, który jest najgorszą motywacją moim zdaniem.

[00:06:44.660] **Szymon Warda:** Brak self-service. I o co chodzi? No bo mówimy sobie, że ok, fajnie, miejmy platformę i tak dalej, czyli twórzmy rzeczy dla własnej konsumpcji. To jest świetny pomysł, tylko bardzo kłopotliwy pomysł. Czemu? Z tego prostego powodu, że musi być taka chęć wewnętrzna, to jest po pierwsze. A po drugie to jest to, że często zaczynamy, przepraszam, pozdrawiam wszystkich przedszkolaków, od dupy strony. Czyli zaczynamy od technologii, a nie od standardów i nie od tego, żebyśmy mieli co self-service'ować. Będziemy self-service'owali płatki śniegu, to nie zadziała ogólnie rzecz biorąc, to umrzemy przez tysiąc cięć.

[00:07:25.830] **Łukasz Kałużny:** Dobra i teraz przejdźmy sobie do czegoś, co można nazwać taką checklistą, czyli czy w ogóle jest sens rozmawiać o kierunku, bo to chyba każdy...

[00:07:34.830] **Szymon Warda:** Ja bym to inaczej ujął, bo w każdej organizacji, a szczególnie dużej, wiedza się roznosi przez legendy. Ten powiedział, ten powiedział i rosną takie mity ogólnie rzecz biorąc. I checklista służy też temu, żeby ułożyć rzeczy w liczby. To jest pierwsza rzecz. Czyli realnie mówimy ok, tak to wygląda. Mówimy na przykład załóżmy: o, mamy cykl wydawniczy miesiące, lata. Liczby, konkretne liczby. Załżmy, że to są dwa miesiące, co już nie jest taką złą wartością. Nie jest też rewelacją, ale też nie jest taka zła. Druga rzecz, która jest bardzo ważna, to jest robimy inwentaryzację stanu obecnego. Bo jeżeli chcemy coś zmieniać i poprawiać, to musimy udowodnić, o ile poprawiliśmy. Musimy pokazać wartość wniesioną przez nasze czynności.

[00:08:15.590] **Łukasz Kałużny:** Dobra, ja bym Wiesz co, rzuciłbym tą checklistę, którą sobie zrobiliśmy. Czyli tak, zacznijmy sobie od reality check infrastruktury. Czyli ile jest kont  AWS-owych i dlaczego? I to będzie taka pierwsza rzecz. Druga rzecz, jak mówimy o standaryzacji.

[00:08:35.330] **Szymon Warda:** Jeszcze bym dorzucił - ile one kosztują?, każde konto. Żeby były (...) liczby, dolary są dobrą wartością.

[00:08:40.940] **Łukasz Kałużny:** Tak. Następny element, kłania się zasada Pareto i ona się sprawdza. 80% use case'ów będzie taka sama, 20%, darujcie sobie, nie ma co sprawdzać. Jakie macie najczęstsze usługi i patterny w organizacji w kontekście Terraforma i infry?

[00:08:58.970] **Szymon Warda:** AWS, więc maszyny wirtualne.

[00:09:02.930] **Łukasz Kałużny:** Przestań już szydzić, wiesz o tym, że będą lambdy, inne rzeczy, może EKS-iki, ECS-y on Fargate, więc nie szydźmy. Dobra, gdzie faktycznie są bottlececki? To co właśnie Szymon powiedział wcześniej. Co oznacza ten bottleneck faktyczny i w którym jest miejscu?

[00:09:23.300] **Szymon Warda:** Tak, z czego wynika i jak to dokładnie wygląda, żebyśmy mieli w miarę rozpisane na konkretnych przykładach. I to jest ważne, niech to nie będzie na zasadzie ogólniki, tylko weźmy sobie dwie, trzy sytuacje i prześledźmy tego commita, ten feature najlepiej. Najlepszy by był feature, któremu biznes chciał mieć. I potem biznes marudzi, że to weszło długo. I weźmy te punkty, które bolą i tam wsadźmy palca w tą ranę i zacznijmy grzebać z czego to wynikało.

[00:09:46.670] **Łukasz Kałużny:** A potem posypmy jeszcze solą.

[00:09:49.130] **Szymon Warda:** Tak, bo to będzie zrozumiane tak naprawdę przez biznes, bo musimy mieć ten w tym momencie (...).

[00:09:54.760] **Łukasz Kałużny:** Teraz dwa najgorsze pytania z reality checku od infrastrukturalnego, bo są jeszcze gorsze. Czy już są jakieś właśnie shared modules? Czy ludzie może na przykład shared modules też uważają za copy paste pomiędzy projektami? Bo to też jest swego rodzaju współdzielenie.

[00:10:11.050] **Szymon Warda:** Gwarantuję Ci. Wiesz jakie są shared modules? Są takie, że zespoły zrobiły swoje i w swoich projektach reużywają pewnych modułów.

[00:10:21.280] **Łukasz Kałużny:** Tak, słuchaj, ale to też jest bardzo dobre wyjście w ogóle.

[00:10:24.820] **Szymon Warda:** To jest, tak, dobry punkt.

[00:10:26.410] **Łukasz Kałużny:** Dobra, kolejny element - kto faktycznie może podejmować decyzje o narzuceniu standardów?

[00:10:33.310] **Szymon Warda:** I ja dwojako, bo tutaj słowo, może się przyczepię, bo to jest taka opcja, kto może, a kto realnie podejmuje? Bo pamiętajmy o tym, co mówiliśmy, nie pamiętam w którym odcinku, ale mówiliśmy o tym, że każda organizacja ma kilka wymiarów. Ten teoretyczny, komunikacyjny i faktyczny. Czyli kto ma tą miękką moc sprawczą na wpływanie na kolejne zespoły. Jak będziemy się opierali na teoretycznym rozkładzie uprawnień mocy, kto co może zrobić, to polegniemy. Musimy znać realny, kto na co ma realnie wpływ, mimo że tytuł może nie świadczyć o tym.

[00:11:08.880] **Łukasz Kałużny:** Dobra. Kolejny element, to jest chyba jeden z najważniejszych i największych problemów, bo przechodzimy do tego, czy organizacja w ogóle jest gotowa? I to jest w ogóle...

[00:11:22.320] **Łukasz Kałużny:** Ale (...) szara, część jest, część nie jest.

[00:11:24.420] **Łukasz Kałużny:** Tak i infrastrukturę zostawmy, to są proste rzeczy. Teraz przechodzimy do trudnych. Czy zespoły chcą standaryzacji, czy będą walczyć? I to jest taka rzecz, którą trzeba sobie politycznie rozgryźć w organizacji.

[00:11:37.920] **Szymon Warda:** Ja bym to zmienił, bo to jest tak, część zespołu będzie chciało, więc trzeba wybrać tych, którzy chcą i potem robić powolny roll out, żeby mieć...

[00:11:46.350] **Łukasz Kałużny:** Resztę zmusić, tak.

[00:11:47.370] **Szymon Warda:** Biding, że tak powiem.

[00:11:48.720] **Łukasz Kałużny:** Tak, ale trzeba zobaczyć, czy zaczynamy od 1 vs 10 na przykład. Od czego zaczynamy?

[00:11:57.050] **Szymon Warda:** To też wynika z tego, że większość zespołów będzie uważała, że jeżeli użyjemy naszych standardów, to my to chcemy ustandaryzować, bo narzucimy reszcie.

[00:12:06.110] **Łukasz Kałużny:** Dokładnie. Trzeba mieć naprawdę twardy tyłek przy wdrażaniu czegoś takiego. Następna rzecz, to jest business impact faktycznie tego chaosu. To co było wcześniej powiedziane, legendy miejskie, które krążą po firmie, to jest follow the money i zobaczmy, czy uda nam się przekonać, że faktycznie mamy problem.

[00:12:28.250] **Szymon Warda:** Ten business impact, czyli wpływ na biznes, jest bardzo ważny z prostego powodu, wdrażanie jakichkolwiek standardów oznacza przerabianie istniejącego kodu. A to oznacza kilka rzeczy - koszt pieniężny, czasowy i regresja, która wystąpi. Bo zamieniając to spaghetti na jakieś standardy będą problemy i będzie narzekanie. Więc jeżeli nie udowodnimy czemu my to robimy, czyli po co i jaki będzie z tego zysk, to to się nie uda.

[00:12:54.600] **Łukasz Kałużny:** I teraz ważne, z naszego doświadczenia 99% przypadków to jest migracja infry i stawiania tego od zera nowymi rzeczami. Nie wierzcie w to, że to wmigrujecie i zrobicie. Nie.

[00:13:08.280] **Szymon Warda:** Tym bardziej, że to jest Terraform, więc (...) rozwali się plik stanu. Nie ma opcji.

[00:13:13.830] **Łukasz Kałużny:** Tak. Albo migrowanie istniejących do nowych modułów zasobów, darujcie sobie, to nigdy się nie skończy. Dobra.

[00:13:20.340] **Szymon Warda:** To jest zbyt dużo roboty.

[00:13:21.510] **Łukasz Kałużny:** Dobra i teraz jeżeli popatrzymy, to są trzy istotne pytania. Pierwsze jest o finansowanie. Czy jest w organizacji przestrzeń na, prawdopodobnie w tej skali zaczynałbym dwie, trzy osoby, które będą inicjalnym platform teamem przy tej skali, tak patrząc na liczby, to jest pewnie z 5-8 osób patrząc się lub odpowiedni format gildii z kontrybucją i to też jest przy mniejszej...

[00:13:51.100] **Szymon Warda:** Grupie.

[00:13:52.390] **Łukasz Kałużny:** Wiem, że nie wierzysz, ale core musi być teamu platformowego. Bardziej mówię jako gildie Szymon przez ręce do pracy. Czyli, że na przykład mamy i z zespołu na przykład jest ktoś oddelegowywany na przykład do pisania Terraforma na dwa, trzy sprinty. Zdarzają się takie rzeczy, co działa w zależności od organizacji. W tej, o której opisujemy, prawdopodobnie to nie zadziała.

[00:14:15.940] **Szymon Warda:** Ja, nie, wydzielone osoby. Gildia jest fajna na ustalenie, w jakim kierunku idziemy, żeby był taki, znowu to, o czym mówiłeś, (...), czyli zgoda wszystkich albo zgoda większości. To się zgodzę, bo to będziemy musieli od góry do dołu płynąć. Ale musimy mieć wydzieloną osobę. Takie problemy z takim pisaniem, że jest oddelegowana osoba, to jest to, że to nie jest jej kawałek kodu. Zawsze biznes będzie ważniejszy, będą wchodziły jakieś zmiany, poprawki, bugi, na których tylko ona się zna i tak dalej. Ten czas będzie szarpany. Jak czas będzie szarpany, jakość będzie niska, nie zadziała według mnie.

[00:14:48.280] **Łukasz Kałużny:** Dobra, idziemy. Następna część. Ile pracy? To jest taki, to jest "SRE" book od Google'a. Jest kontrowersyjna w pewnych miejscach, ale tam jest też zmierzenie sobie, ile tej pracy to jest taki powtarzalny toil, czyli właśnie takie powtarzalne, ręczne czynności, bo rzeczy nie zostały spięte ze sobą w żaden sposób.

[00:15:10.600] **Szymon Warda:** Czyli ile czasu...

[00:15:12.400] **Łukasz Kałużny:** Tracimy.

[00:15:13.150] **Szymon Warda:** Na papierki.

[00:15:14.140] **Łukasz Kałużny:** Tak, przypominam, jest taka, zalinkuję to, jest macierz, kiedy automatyzujemy, kiedy nie automatyzujemy. Taka bardzo prosta czteroelementowa macierz, więc sobie zobaczycie. I ostatnie z gotowości organizacji: czy management będzie popierał wymuszanie standardów?

[00:15:36.430] **Szymon Warda:** Ja bym tego tak nie ujął, bo same standardy jako takie nie są wartością, ustalmy.

[00:15:41.710] **Łukasz Kałużny:** Implementacja ich jest wartością.

[00:15:43.630] **Szymon Warda:** Tak, implementacja i zyski, które możemy z tego mieć. Bo załóżmy to jest, standardy nam otwierają pewne możliwości do robienia rzeczy łatwiej globalnie typu security, typu właśnie budżety, typu cały governance. Też obsługuje się łatwiej. Więc pytanie jest takie: czy ktoś chce ogarnąć bałagan w firmie przez wdrożenie standardów, które umożliwią mu wdrożenie innych narzędzi? To bardziej w tym kierunku. Czyli mówiąc realnie, to musi być ktoś wysoko postawiony, pewnie C-Level, CTO by się przydał.

[00:16:12.860] **Łukasz Kałużny:** Musi być... Inaczej, nie oszukujmy się, ktoś z boardu musi być sponsorem całej inicjatywy. Nawet specjalnie nie mówię CTO. W tym miejscu specjalnie nie mówię CTO.

[00:16:23.870] **Szymon Warda:** No ale to C musi być gdzieś tam.

[00:16:25.790] **Łukasz Kałużny:** Tak musi być C. Dobra, i teraz najgorsza część, którą rynek olewa z bardzo prostej przyczyny, bo platformę budujemy dla naszej własnej zabawy, nie dla uzyskania celów. I pierwsze będą, to są takie kryteria sukcesu. Czyli co oznacza sukces? Czy to jest krótszy lead time, czy może patrząc się na pytanie naszego słuchacza, developer happiness, developer experience?

[00:16:56.960] **Szymon Warda:** Doskonale wiesz, że na starcie będzie masa narzekań.

[00:17:00.410] **Łukasz Kałużny:** Tak, zdaję sobie sprawę.

[00:17:02.780] **Szymon Warda:** Nie, nie optymalizowałbym w kierunku szczęścia, bo każdy ma inaczej.

[00:17:08.360] **Łukasz Kałużny:** Ale to trochę mówi, wiesz, o tym, czym się kierujemy, co jest naszą motywacją.

[00:17:14.510] **Szymon Warda:** Musi być świetny UX, User Experience. To się zgadzam. Tylko mówimy bardziej długofalowo, bo początki mogą być różne.

[00:17:20.750] **Łukasz Kałużny:** Będzie dramat.

[00:17:22.490] **Szymon Warda:** Będzie narzekanie.

[00:17:23.540] **Łukasz Kałużny:** Dobra, kolejne. Jak będziecie mierzyć czy platforma działa?

[00:17:29.120] **Szymon Warda:** Dobre.

[00:17:30.170] **Łukasz Kałużny:** I do tego sobie przejdziemy. Ja tutaj podpowiem jedną z takich rzeczy, chyba najprostszą metryką to będzie to, co znajduje się w Dorze. Tak patrząc się na jedną z metryk, które można sprawdzić albo wyciągnąć część z Dory, o tak i to sobie na razie zostawmy.

[00:17:47.810] **Szymon Warda:** Ja co do Dory mam takie lekkie, tak, ale nie w krótkiej fazie.

[00:17:52.310] **Łukasz Kałużny:** Dobra, wiesz, to definicja sukcesu, dlatego w dłuższym okresie. Dobra i ostatnie takie w tym, które jest success definition, które trzeba zmierzyć. Kim są faktycznie user'zy naszej potencjalnej platformy i czego do diabła oni potrzebują?

[00:18:11.600] **Szymon Warda:** To jest super ważne i to jest niesamowicie ważne, jeszcze raz to podkreślę. Czemu? Ano dlatego, że jeżeli posadzimy tych dwóch, trzech developerów w zespole platformowym, to będą z reguły ludzie, którzy mają wysokie mniemanie o sobie i prawdopodobnie słusznie, bo są inteligentni, dlatego ich tam wybraliśmy, bo to muszą być dobrzy ludzie. Problem jest taki, że jak oni zaczną pisać dokumenty albo cokolwiek innego, to często to wynika z takiej wersji, że chcemy się pochwalić, jacy jesteśmy mądrzy. Musimy mieć określone persony, kto korzysta i do kogo piszemy i jak to wygląda i do kogo kierujemy te produkty. Więc to jest naprawdę bardzo ważne. Główne potrzeby na starcie.

[00:18:49.260] **Łukasz Kałużny:** Trzeba powiedzieć...

[00:18:50.400] **Szymon Warda:** Szybkie wygrane.

[00:18:51.480] **Łukasz Kałużny:** Chyba to jest rzecz, która jest najgorsza przy platformach, platforma wymaga product managementu.

[00:18:58.800] **Szymon Warda:** Reklamy, releasów, świętowania tego wszystkiego, czego inżynierzy z reguły nie lubią, jest to bardzo konieczne, szczególnie na starcie, kiedy będzie różnie.

[00:19:09.720] **Łukasz Kałużny:** Dobra, i teraz najważniejsze, kiedy w ogóle olejcie platformę? To będzie chyba 6 punktów. Po pierwsze, każdy zespół twierdzi, że jest unikalnym płatkiem śniegu i on inaczej nie będzie mógł żyć.

[00:19:27.960] **Szymon Warda:** Dla mnie jest tak, że każdy zespół twierdzi, że cechy unikalne. Dla mnie faktycznie jest unikalne, że każdy zespół ma inną technologię. Wtedy koszty ujednolicenia nie mają sensu, albo...

[00:19:37.680] **Łukasz Kałużny:** Tutaj już mówimy o AWS-ie, więc być może wiesz, w usługach. Ale polećmy sobie dalej. I to jest połączone z następnym punktem, że management nie jest za tym, żeby to standaryzować i będzie też bronił zespołów i innych rzeczy powyżej przed na przykład wejściem na platformę. I to będzie już oznaczało, te dwa punkty oznaczają, że to jest inicjatywa oddolna i ona się nie powiedzie, jeżeli nie macie umocowania politycznego.

[00:20:08.250] **Szymon Warda:** Jeżeli macie w firmie biegać z pustymi teczkami i nie ma czasu na nic innego, to nie ma, platforma nie ma sensu.

[00:20:14.970] **Łukasz Kałużny:** Kolejny punkt, on jest standardowy, pojawia się powinien w sumie chyba pierwszy, budowanie platformy po to, żeby zbudować platformę.

[00:20:22.290] **Szymon Warda:** Nasze stare dobre CV Driven Development.

[00:20:25.170] **Łukasz Kałużny:** Tak. Tutaj nie ma nic do dodania. Kolejny red flag, nie ma capacity na platform team.

[00:20:32.070] **Szymon Warda:** To się nie uda, tak.

[00:20:35.460] **Łukasz Kałużny:** Tak. Kolejne, próbujemy rozwiązać ludzkie problemy, często procesowe, przez technologię.

[00:20:46.280] **Szymon Warda:** Technologia pomaga, ale bez rozmowy z ludźmi, bez ustaleń, bez takich trudnych, nudnych czasami albo nawet burzliwych spotkań nie zrobimy tego. Nie ma opcji.

[00:20:56.690] **Łukasz Kałużny:** Rekomendujemy 5 why i wrócenia sobie, co jest w ogóle problemem. No i taki ostatni punkt, który się zdarza Szymon, w ogóle nader często, mamy zespoły, które naprawdę aktywnie walczą, żeby być unikalne poprzez jakąkolwiek... Inaczej, albo nasz standard, albo nasz brak standaryzacji, albo nic.

[00:21:18.080] **Szymon Warda:** Miałem sytuację, że zespoły aktywnienie walczyły i była kwestia tego, dla mnie jest kwestia pokazania wartości, że może: a po co mamy robić, mamy duży backload i tak dalej. Okej, słuchajcie, nie musicie, nie musicie, nie musicie tego robić. Ale jakbyście korzystali z naszych modułów, to na przykład macie automatyczne liczenie budżetów. I nagle jest takie, nie prowadzisz dalszej dyskusji, przekonywania, tylko wiesz, że to będzie wartość, jeżeli użyjesz. Zostawiasz i czekasz. I jak odpowiednio duża kula śnieżna wartości się zbierze, to oni stwierdzą, że może byśmy skorzystali. Dla mnie to jest fajnie, to co, znowu, ja to bardzo lubię, to co Steve Ballmer mówi na swoich prelekcjach, to jest to, że a bit of success. Czyli powodujemy, żeby łatwiej było robić rzeczy dobrze, tak jak my chcemy, a trochę trudniej pozostałe. Nagle ludzie przekonają się, że jednak będzie nam tak łatwiej.

[00:22:14.060] **Łukasz Kałużny:** Wiesz co, to właśnie takie walczenie takimi feature'mi. Mi się przypomina też taka rzecz i to akurat jest po "SRE" bookiem, ale z Google'a. To jest tak, jak tam mam znajomego, który dość mocno siedzi przy kluczowych usługach w GCP, jednej z kluczowych kawałków. I on na przykład, dla niego bainem, że trzeba przestrzegać, używać wbudowanych frameworków, innych rzeczy jest to, że po fazie hypercare'a, po release on nie będzie już na oncallu.

[00:22:49.680] **Szymon Warda:** Dokładnie tak. To jest jeden z elementów. Jeżeli używasz naszych usług, no to w tym momencie zespół platformowy, (...) przejmuje. A jeżeli nie, jeżeli chcesz robić po swojemu, stare okej, to ok, nie ma problemu, ale Ty się tym zajmujesz. To działa, bardzo dobrze działa.

[00:23:05.940] **Łukasz Kałużny:** To jest jeden z tych, dobra. I słuchajmy, przejdźmy teraz do takich pytań i odpowiedzi na te pytania, na problemy, bo to jest trochę dużo takich elementów. No i pierwsze jest w ogóle podstawowe pytanie: czy potrzebujecie platformy?

[00:23:23.310] **Szymon Warda:** Pewnie tak.

[00:23:24.660] **Łukasz Kałużny:** To jest już skala, w której, bo to zawsze powtarzamy skalę i prawdopodobnie, jeżeli mamy tam około setki aktywnych developerów, 150, spokojnie warto. Jeżeli, teraz jest kluczowa rzecz, niestety trzeba mieć capacity na platform team. To jest taka rzecz, o której trzeba sobie powiedzieć. Jeżeli mamy capacity na etaty, to ta skala tutaj podana 200-250 inżynierów, tak, robimy, zaczynamy budować platformizację naszej infrastruktury.

[00:23:58.440] **Szymon Warda:** Ja jeszcze jedną rzecz dodam, przy tej ilości developerów zakładam, że są osobne zespoły OPS-we, są osobne zespoły do security i tak dalej. Może też z tych zespołów wyłonić ludzi, którzy będą będą członkiem platform teamu. To nie muszą być nowe rekrutacje, bo ten platform team finalnie ułatwi robotę wszystkim tym takim zespołom, które są później.

[00:24:20.580] **Łukasz Kałużny:** Przykład, jeden z naszych klientów rekrutuje sobie do takiego teamu, sobie bezpieczników, żeby mieć ich bezpośrednio w teamie. To taki jeden z przykładów.

[00:24:30.540] **Szymon Warda:** (...) moduły, ta wiedza musi być.

[00:24:32.400] **Łukasz Kałużny:** Dobra. I to będzie taka pierwsza rzecz. Problem, który macie realnie tutaj w tym dogo, patrząc w tym, to jest w ogóle cała kwestia standaryzacji tych modułów terraformowych. I to jest rzecz, jak sobie popatrzymy na to wszystko, do tego jeszcze przejdziemy potem, co można zrobić, ale na początku ten problem jest w zupełnie innym miejscu i to chyba na razie jeszcze tak zostawmy. Dobra, drugi punkt jeszcze, który trzeba sobie powiedzieć, to jest chyba Szymon, kurde, już wyświechtane przez Ciebie na prezentacji, wymęczone, więc Tobie to zostawię.

[00:25:11.100] **Szymon Warda:** Zdefiniujmy czym jest ta platforma, której potrzebujemy? Bo jeżeli wrzucicie sobie backstage i odtrąbicie sukces, to coś się nie uda. Nie, ten backstage jest naprawdę wisienką na torcie i tyle. To gdzie się ma zacząć? Platforma to przede wszystkim standardy. Standardy, standardy, bo potem można pewne rzeczy mieć wspólne i dalej lecieć. Dalej lecimy, standardy, które potem mamy self-service i potem robimy wokół tego governance i tak dalej. Co jest dalej ważne? Nie porywajmy się, nie budujmy tego backstage'u. Czemu? Waszym API do waszej platformy będzie ten GitHub Actions. Macie resueable workflows, macie własne akcje i nie należy się ich bać, bo własne akcje w GitHub actions są super proste. Korzystajmy z tego.

[00:25:57.020] **Łukasz Kałużny:** Ja mam jedno przemyślenie o backstage'u. To jest troszkę w kontrze, że backstage... Może inaczej, można zacząć używać, można go wrzucić nawet na początku Szymon, to jest taka rzecz, która mi... Dobra, ale, i teraz jest ale, nie powinno tam się znaleźć zero grama custom code.

[00:26:21.800] **Szymon Warda:** Wiesz co? Dla mnie backstage to jest takie szybkie odtrąbienie sukcesu: mamy, mamy, mamy i się cieszymy z czegoś, co właściwie nie mamy. Jest to ryzykowne, bo za chwilę się odtrąbi sukces i za chwilę motywacja do dalszej pracy poleci na łeb na szyję.

[00:26:36.860] **Łukasz Kałużny:** Dobra, polećmy sobie teraz dalej, czyli faktyczne bottlenecki.

[00:26:43.350] **Szymon Warda:** Tak. Czyli musimy zająć się: czemu to robimy? To metoda, o której tu już mówiłeś: 5 razy why. Właśnie to założyć sobie (...) to wymyślił. Czyli właściwie dojść po co? Jaka jest motywacja tego? I musimy tą motywację znaleźć, żeby mieć ładne przesłanie do biznesu: czemu my to robimy i jakie z tego będą zyski? Jak to będzie wyglądało? I nie oszukujmy się, że to będzie trwało długo.

[00:27:07.860] **Łukasz Kałużny:** Tak, ja bym tutaj poleciał tak, można sobie zadać pytania: co faktycznie trwa te miesiące? Czy to jest infra provisioning? Czy może właśnie approvale z biznesu, z testów i innych rzeczy? Czy to są te testy, czy to są testingi, czy deploymenty? I tutaj jedną z takich rzeczy, zarekomendowałbym odcinek z Kingą na temat Dora Metrics, jak w Pracuj.pl na przykład mierzą. I tam było słowo też wspomniane o ankietowaniu, o takim pierwszym podejściu. Wiem, że tego Szymon nienawidzisz jako taki zobaczenie stanu.

[00:27:41.700] **Szymon Warda:** Dla mnie to będzie wyglądało trochę inaczej. Wywiady. Zrobić trzy, cztery wywiady z zespołami i zrobić dokładną, znaczy w miarę taką analizę, żebyśmy na przykładzie konkretnych sytuacji, konkretnych feature'ów zobaczyli czemu to tyle trwało i czy faktycznie tyle trwało. Czyli po prostu nie na jednym, nie na dwóch, ale cztery, jakbyśmy ugryźli, to będzie w porządku, bo w tym momencie będziemy mogli uogólnić tak naprawdę, jakieś tam średnie powyciągać. Jakbyśmy jeszcze załóżmy dorwali na przykład dwa zespoły do czegoś takiego, takich wywiadów, super. Żeby nie było, Dora Metrics świetne, ale jak uporządkujemy. To nie jest na start wdrożenie, po prostu Dora Metrics, znowu, odtrąbienie sukcesu, nie tędy droga.

[00:28:22.770] **Łukasz Kałużny:** Dobra, dobra. Następnie z tym, idąc dalej to problem z Terraformem. Inaczej, ja bym powiedział, że tu będą dwa główne elementy. Inaczej i znowu się założę, może ręki nie dam sobie uciąć, ale prawdopodobnie 80% kodu u wszystkich to jest to samo. To są te same przypadki napisane w każdym miejscu zupełnie inaczej, w każdym zespole zupełnie inaczej zaimplementowane. Jeżeli człowiek nie wędrował, który to robił, albo nie był podkradany pomiędzy repo kod.

[00:28:58.190] **Szymon Warda:** Tak, co więcej, nie ma pewnie z innymi standardami tagowania, innymi standardami, jeżeli chodzi o bezpieczeństwo, o sieciówkę, o dostępy, o wystawienie, o środowiska developerskie. Wszystko tam będzie inne. Czyli mnie jedna rzecz martwi, to mogły być zakupy, czyli firma kupiła produkty od innych i mamy teraz wiele kont AWS-owych (...).

[00:29:20.210] **Łukasz Kałużny:** To jest już cięższy element.

[00:29:22.850] **Szymon Warda:** Ale dalej realne przy tej skali developerów do ogarnięcia.

[00:29:26.090] **Łukasz Kałużny:** Context is the king jak zawsze. No i przy tej chorobie, to będzie w ogóle walka z syndromem not invented here przy zespołach. Czyli że może mamy swoje share'owane moduły, ale share'owane organizacji są już złe, bo nie spełniają naszej abstrakcji, naszego wymarzonego flow.

[00:29:44.980] **Szymon Warda:** Ale wiesz do czego to prowadzi? Bo to jest ważny element. Bo jeżeli będziemy chcieli zadowolić wszystkich, to powstaną moduły do infrastruktury, które będą tylko przelotkami, które nie będą nic standaryzowały. Więc to jest też bardzo ważne, żeby po prostu, będziemy jeszcze rozmawiali o tym, jak to wdrażać. Bo jest sposób jak (...) standardy. Bo punktem są te standardy, bo to mamy standardy i potem wdrożymy moduły, które spełniają te standardy. Nie inaczej. To jest bardzo ważne. I jeszcze do tego wrócimy jak to zrobić, bo jest na to sposób taki bardzo mocno prawniczy, bym powiedział.

[00:30:17.080] **Łukasz Kałużny:** Dobra, to co? Lecimy. Co można byłoby zrobić, takie cztery w sumie kroki, które można byłoby zastanowić się przy tym, rozważyć jako taki plan działania. Pierwsze, sprzątanie, organizacja w AWS-owych i governance wokół tego. I te przygotowanie to są jakiś blueprint właśnie landing zone z guide trialsami, control policies. I najgorsza rzecz, która jest przy tym i to jest w ogóle, czyli ta centralna główna architektura z landing zone, czyli ile Wy potrzebujecie kont, jak zrobić sieciówkę, IAM-a i inne te rzeczy w uporządkowanym świecie. I to jest najcięższe... Inaczej, to zadanie będzie ciężkie.

[00:31:07.780] **Szymon Warda:** A ja się (...) ciężkie, bo tu mam dwa komentarze do tego. To jest zdanie, które nie jest takie ciężkie, bo ono realnie nie będzie potencjalnie dotykało istniejącego kodu. Niewielkie ryzyko regresji i widzimy wartość. Można powiedzieć, że dostęp do rzeczy jest bezpieczny i tak dalej.

[00:31:26.080] **Łukasz Kałużny:** Dlatego budujemy zwykle nową infrę tutaj.

[00:31:28.900] **Szymon Warda:** Dokładnie tak. Więc ryzyko regresji i wpływu na biznes - niewielkie. Dużo robienia, można przepiąć, ale ok. Czemu to jest takie krytyczne? Ano dlatego, że będziemy mieli to wszystko w organizacji, to możemy nagle robić raporty po całej organizacji, a nie musimy robić raportu, sprawdzeń, polityk w kontekście, guardrails'ów dla każdego konta osobno. Nam robota późniejsza robi się łatwiejsza i pokazujemy jak to wygląda. I też możemy  w tym momencie, jak wdrożymy takie standardy, możemy je łatwo egzekwować i tak dalej. Super ważny krok. Drugi krok, lecisz. Ja się z tym nie zgodzę co jest na ekranie.

[00:32:04.740] **Łukasz Kałużny:** Co?

[00:32:05.460] **Szymon Warda:** Ja się z tym nie zgodzę, więc powiedz o co chodzi.

[00:32:08.340] **Łukasz Kałużny:** Ale zastanowienie się i podejście do tego, żeby zacząć budować wspólne moduły terraformowe, czyli zidentyfikować 80% tych use case'ów, które da się wystandaryzować.

[00:32:23.280] **Szymon Warda:** Czekaj, czekaj, to jedno słowo ominąłeś, to jest bardzo ważne, żeby mieć rejestr modułów terraformowych.

[00:32:29.760] **Łukasz Kałużny:** Inaczej Szymon, rejestr repo. Repo, raczej dla mnie moduł... Przepraszam, dobra, to też bardzo ważne. Dla mnie są tylko dwa scenariusze takie z tym, że nie moduł registry, tylko tak realnie to jest repo. Przy Waszej skali prawdopodobnie najlepsze będzie, nie chcę teraz wchodzić dlaczego, jak, ale prawdopodobnie kawałek dedykowanych różnych repo. Czyli prawdopodobnie repo per moduł, żeby łatwo wersjonować, tagować, release'ować. Ale współdzielone repozytorium gitowe, do których będą trafiać moduły.

[00:33:11.180] **Szymon Warda:** Tak, ustalmy, nie repozytorium, w sensie nie rejestr, w sensie nie wypychany, taki z artefaktami, bo ten narzut na robienie tego wszystkiego na starcie zbyt duży, to musi być repo. Ja na starcie bym zaczął też od jednego repo, bo na starcie będzie dużo zmian. Jak to się ładnie ustabilizuje, to potem konkretny moduł, przeniesienie do własnego repo, super pomysł. Ale to to samo co mówimy odnośnie systemów. Nie dzielmy na starcie za bardzo, bo będzie dużo zmian, a jak się to ustabilizuje, przenosimy, wydzielamy, super.

[00:33:39.460] **Łukasz Kałużny:** Dobra. Tu się z Tobą nie zgodzę, bo... Inaczej, przy modułach się z Tobą nie zgodzę współdzielonych, zacząłbym od razu przy tej skali.

[00:33:48.070] **Szymon Warda:** Ok, mamy inne podejście, jak najbardziej jestem za.

[00:33:50.380] **Łukasz Kałużny:** Dobra. No i wymuszenie przez review standardów.

[00:33:55.570] **Szymon Warda:** Tak. Ja bym jeszcze tu kilka rzeczy dorzucił, bo to jest trochę trudniejsze takie wdrożenie. Raczej posiadanie tego (...) zespołu, żeby wszyscy zaczęli korzystać, to jest takie trochę. Musimy wymyślić, musimy dać wartość, czemu te moduły mają być wykorzystywane. I to jest kilka rzeczy. To jest to przede wszystkim, że zasady zdejmą, o czym mówiliśmy, zdejmą pewne narzuty, koszta zespołów i w tym momencie przenosimy. Kolejna rzecz to jest to, że to wdrożenie takich modułów musi być etapowe. To nie jest to, że zespół platformowy wymyśla jak to powinno być bez jakiegokolwiek połączenia z innym zespołem, albo jak to jest wykorzystywane i nagle ta gildia na szczycie wieży mówi jak powinno być, a potem zespoły mówią: ale to kurna się nie aplikuje w ogóle. Więc moja propozycja jest taka: bierzecie zespół 2 na bazie tego co oni, jak oni wykorzystują, jakieś standardy zrobicie, takie dość wysokie i potem oni zaczynają używać i robicie taki etapowy rollout tego wszystkiego, żeby coraz więcej, coraz więcej, coraz więcej. Co jest super ważne tutaj? To jest to, z mojej perspektywy to jest to, żeby mieć jakieś miejsce, gdzie ludzie mogą zgłaszać problemy, to czego potrzebują. I to jest bardzo ważne, żeby to ująć w liczby, bo będziecie mieli dwie grupy. Małą głośną grupę narzekaczy, którzy krzyczą bardzo, są mniejszością, krzyczą o coś i cichą większość dla niektórych sytuacji. I trzeba umieć balansować jedno z drugim tak naprawdę, bo to jest super ważne, bo lepiej mieć to w liczbach i powiedzieć czemu na przykład ten feature (...) nie jest dorzucany. Robienie przelotek, takich po prostu modułów, które nic nie mają, żadnej wartości - bez sensu. Nie róbcie tego, to będzie przerąbane.

[00:35:32.710] **Łukasz Kałużny:** No dobra, to idziemy słuchajcie do...

[00:35:35.500] **Szymon Warda:** Jeszcze mam parę rzeczy, bo to jest wręcz, przewalczyłem bardzo dużo rzeczy. Musicie mieć (...), w sensie pokazać co jest do zrobienia jeżeli chodzi, czemu to (...)? Liczenie automatycznych właśnie security, governance'u, kosztów i tak dalej i tak dalej, żeby ludzi zachęcać do tego. Kolejną rzeczą to jest to, to jest jak teraz motywować. Nie ma nic lepszego niż tak zwane peer pressure, social pressure, czyli robienie załóżmy raportów raz w miesiącu: ile, jakie jest wykorzystanie, kto korzysta, kto z tego nie korzysta i tak dalej. Takie pałowanie można powiedzieć. Też działa i działa bardzo dobrze, o ile mamy (...) jeżeli chodzi o management.

[00:36:13.990] **Łukasz Kałużny:** Wracamy do red flag, które były.

[00:36:16.270] **Szymon Warda:** Tak, dokładnie. Dlatego, że ludzie nie chcą być gorsi od innych zespołów. Jak ułożymy to, że ok, ten moduł jest fajny i tak dalej, a Wy tego nie robicie...

[00:36:25.480] **Łukasz Kałużny:** Dobra, za dużo o Terraformie. Niektórzy powiedzieli, że to jest passe. Powinieneś zrobić crossplane'a, service operatory i wszystko tworzyć przez API z Kubernetesa, bo prawdziwa platforma...

[00:36:38.030] **Szymon Warda:** Jakaś forma pliku tekstowego, nieważne jaka.

[00:36:41.150] **Łukasz Kałużny:** Dobra. I krok trzeci słuchajcie, bo tak jak pewnie słyszycie, zajmujemy się tym na co dzień, więc jeżeli macie takie problemy, to zapraszamy do kontaktu. I teraz rzecz, którą Szymon tutaj uwielbia i padła, w szczególności szkolić z tego i tych interfejsów. Ma świetne 2-3 dniowe szkolenie: Github Actions jako platform interface, bo padło tutaj konkretnie właśnie Action też oprócz Jenkinsa w opisie stosu.

[00:37:11.540] **Szymon Warda:** Mamy kilka rzeczy. Mamy tak zwane reasonable workflows, czyli robimy templatki. I to jest świetne z tego prostego powodu, że możemy sobie obudować odnośnie budowania. Ludzie widzą te, szczególnie kod do CI/CD jako taki, coś co musi być, ale nikt na to nie zwraca większej uwagi, więc chętnie wezmą gotowce. Własne akcje w GitHubie się pisze bardzo łatwo. To nie jest jakaś taka anomalia, używanie i budowanie własnych tooli, załóżmy (...) security scanning i inne rzeczy, własna akcja i dzięki temu korzystają osobno. Dzięki temu mamy kontrolę jak to wygląda, jak się konfiguruje i tak dalej. Już mamy workflowy, czyli w tym momencie ludzie klikają, my customizujemy kawałek dalej. Bardzo ważne do akcji typu budowanie, skanowanie, wypuszczanie, dzięki temu będziemy mieli tagowanie, wysyłanie rzeczy do Grafany odnośnie adnotacji. Wszystko możemy ładnie zrobić. Wdrażacie na samym starcie, nawet jeżeli robimy to bardzo proste, ale musi być wartość w każdym z tych rzeczy. No i w tym momencie mamy wszystkie approval'e, zgody i tak dalej. Możemy robić qualitygate, które są ważne tak naprawdę w dłuższym, szczególnie w kontekście produkcji i spisaniu procesu, który istnieje w organizacji.

[00:38:20.690] **Łukasz Kałużny:** Dobra i ostatni, którego kochasz i nienawidzisz w tym miejscu, czyli rozpoczęcie mierzenia i iteracja, bo to jest już tam krok czwarty, który się powinien w pewnym momencie... Mierzenie powinno się w miarę szybko pojawić, nie pokazywanie i wyciąganie. Powinno to być wyciąganie wniosków, a nie bat na czarownice, o czym powtarzamy. I żadnych jego mać KPI na początku, bo skończy się malowaniem trawy. Czyli Szymonie, oddaję Ci głos.

[00:38:52.390] **Szymon Warda:** Żeby nie było, widzę sens i wartość Dora Metrics. Nie wdrażajmy od razu wielkiej kobyły na start, bo jak spędzimy 2 miesiąc na wdrożeniu Dora, to tam się nie uda. Etapowo. Myślmy czego potrzebujemy i bierzmy z tych standardów dorowych. W sensie, to znowu, nie wdrażamy Dory dla Dory, tylko wdrażamy Dorę, bo potrzebujemy z niej czegoś. To jest super ważne. I przede wszystkim mierzenie tego czasu, żeby pokazywać nasz sukces jaki odnosimy, bo musimy pokazać. Doskonale wiesz, praktycznie, że coś się dzieje, coś jest lepiej, czyli że obniżamy jakąś metrykę, że jest szybciej i tak dalej. Ale to nie jest to, co powiedziałeś, to nie jest to, że pałujemy o to developerów, tutaj mówimy w organizacjach.

[00:39:33.000] **Łukasz Kałużny:** Tutaj chyba byłyby dwie metryki, o których można powiedzieć. Tam z Dory to są dwie metryki. Z Dory to jest tak naprawdę lead time from commit to production. To będzie taka pierwsza metryka. Jeżeli macie wziąć jedną, to tylko ta z Dory.

[00:39:49.620] **Szymon Warda:** Pokazujcie jej rozrzut, żeby to nie była po prostu jedna liczba, najlepiej powiedzmy mediana, tego typu rzeczy są dobrym pomysłem.

[00:39:56.340] **Łukasz Kałużny:** Tak. Rozrzut taki jak pewnie znacie, piękny rozrzut kropeczkami na wykresie na osi. Tak i drugi to jest ile? I to jest zawsze powiedziane sobie ile teamów, usług, aplikacji, serwisów korzysta z platformy na ileś. Czyli jeżeli powiedzmy, weźmy naszego Szymon klienta, który ma tam 280 mikroserwisów, czyli na przykład, że procent, że w tym momencie na przykład z tej infrastruktury współdzielonej platformy korzysta na przykład 40 z 280 serwisów. Nie powiedziałbym o zespołach, ale serwisach.

[00:40:33.920] **Szymon Warda:** Wydaje mi się serwisów... To jest ten mail, o którym mówiłem. Tak, to jest raportowanie, żeby widoczne było, co się dzieje. To jest trochę narzutu, ale to właśnie jest ta robota produktowa, która powinna się odbywać, release notes, jak i inne rzeczy. Tego tam trochę jest.

[00:40:48.110] **Łukasz Kałużny:** Dobra i chyba przejdźmy do ulubionej rzeczy.

[00:40:51.530] **Szymon Warda:** Czekaj, bo jeszcze jedna odnośnie standardów, bo to jest super ważne. Tutaj hint jak mi się to udaje z reguły robić standardy. To trzeba robić etapowo. W pierwszym poziomie robi się taką konstytucję, ogólniki, które będą po prostu, które się zgadzamy, że mamy testować i tak dalej. Czyli takie rzeczy niezmienne. I potem coraz niżej, takie można powiedzieć, ustawy, czyli jak to konkretnie robimy. Czyli konstytucja mówi, co chcemy, ustawy mówią, jak to chcemy i konkretne liczby, narzędzia i tak dalej. Rzecz bardzo ważna, wymiksujcie się z tego jak najszybciej. To konstytucja musi być odgórna, ale potem ustawy niech będą te grupy, gildie produktowe, żeby to nie wynikało od jednej osoby, bo ludzie będą czuli, że okej, narzucone, na czym by tam, zrobimy to byle jak, żeby tylko było, czyli będziemy oszukiwali metryki. Musi ludziom zależeć. Musimy ująć w to, żeby ludziom w końcu zależało i żeby wiedzieli, po co to właściwie robią. Kolejna rzecz to jest to, że ustawcie czas akceptacji, czyli mówimy dokument leci, macie na wdrożenie poprawek czy na wdrożenie uwag powiedzmy dwa tygodnie. Jak nie zrobicie, to jest niejawna zgoda. Najważniejsze to jest to, żeby nie bawić się w opcję liberum veto, czyli że musimy wszystkich zaspokoić. Zaspokoimy większość, sensowne. Zawsze ktoś będzie marudził. Nie przeciągamy tych standardów miesiącami tylko dlatego, że ktoś ma jakąś jedną uwagę odnośnie przecinka, albo jakichś pierdół. To będzie się działo. Marudy zawsze istnieją, ludzie z uwagami, którzy nie chcą coś robić, a tylko marudzą, będą istnieli. Nie przejmujmy się, trzeba zrobić przecinaki w tej sytuacji. Istotna rzecz, ownership, musi być poczucie wartości, że ludzie widzą, że to oni (...). Jak widzicie trochę z tym przewalczyłem.

[00:42:28.090] **Łukasz Kałużny:** Tak, dobra. I ostatnia część: czego nie robić? I chyba tak, problemy z platformą są takie: bardzo proste 4 elementy, nie budujemy od razu mega portalu, pierwsze. Druga sprawa, tych wszystkich unikatowych płatków śniegu nie przymuszamy do standardów, raczej szukamy osób, które skorzystają, niż że będziemy zaganiać na siłę. Nie wyjdzie, będziecie tylko walczyć, tracić czas. Biznes i pieniądze są najważniejsze. Jeżeli pokażecie na nich, że to będzie działać, to będzie sukces. Jest wartość, to będzie sukcesem. Jeżeli to olejecie, to wszyscy inni oleją waszą platformę. I rzecz typowo produktowa: user research. I bez tego to znowu będą tylko coś, co zniknie.

[00:43:20.500] **Szymon Warda:** Tak i teraz wzorce, generalnie takie anty wzorce organizacyjne, że każdy jest unikalny, że będziemy właśnie budować wielkie tam jakieś tam wiesz, daleko, daleko i potem narzucimy to ludziom, tam dużymi widłami zrzucimy te platformy. Albo inna opcja, że budujemy platformę, w której mamy dużo roboty, czyli generalnie mało automatyzacji, czyli tylko sobie dorzucamy roboty, że zespół platformy będzie musiał tylko rosnąć, rosnąć, rosnąć, rosnąć, żeby spełnić pewne wymagania. To tak nie działa. On rośnie do pewnego poziomu, potem jest na stałej wartości, dlatego że ma automatyzację. Tu jest wartość.

[00:43:53.880] **Łukasz Kałużny:** No dobra, więc polećmy sobie teraz takie take away, żeby to podsumować, odpowiedzi. Czyli tak, potrzebujecie platformy przy tej skali.

[00:44:05.190] **Szymon Warda:** Tak na 99% potrzebujecie platformy. Tak.

[00:44:06.240] **Łukasz Kałużny:** Tak. Nie potrzebujecie od razu IDP, tylko IDP portalu na początku, tylko to jest jakiś krok potem. Kolejny element, to powiedziałbym wprost, problem jest tutaj w ogóle zupełnie zarządczy, governance'owy i zarządczy w rozumieniu zarządzania biznesem i technologią.

[00:44:26.550] **Szymon Warda:** Też ludzie w technologii, bo to jest bardzo ważne..

[00:44:28.710] **Łukasz Kałużny:** I ludźmi, tak, procesem. Czyli to są te wszystkie rzeczy, o których mówimy bardzo ładnie: zarządcze. I to jest trochę problem CTO, do czego się dopuściło prawdopodobnie w tym, a nie technologiczny, bo tutaj sobie też powiedzmy. Kolejna rzecz, bardzo dobre MVP platformy, to jest GitHub Actions i moduły terraformowe. I ten zaczątek będzie bardzo dobrą rzeczą. Ale w ogóle przede wszystkim trzeba posprzątać, zrobić i zaprojektować budowę organizacji AWS-owej od początku, przed całym tym self-servicem i innymi rzeczami, zastanowić się czy posprzątać. I teraz powiem rzecz, która jest, nie chcę o niej rozmawiać, jest kontrowersyjna. Być może współdzielone moduły i zrobienie tylko tego MVP na zasadzie GitHub Actions, moduły, to będzie koniec waszej platformy i wszyscy będą czuli się szczęśliwi.

[00:45:22.290] **Szymon Warda:** Jest to bardzo realne. Dla mnie, ja bym dorzucił jeszcze jedno, standardy i developerskie i spisane gdzieś. Faktycznie, to Wam się przyda. Nawet jeżeli platformy nie zrobicie, standardy Wam się przydadzą. Mogą być ogólniki, ale żeby coś było, do czego można się później odwołać. Bo była taka opcja, że: na to się umówiliście, więc czemu teraz robicie inaczej? No to generalnie to już motywuje, że tak powiem.

[00:45:46.740] **Łukasz Kałużny:** Dobra i w sumie na tym kończymy. Jeżeli macie podobne pytania, zapraszamy na Discorda. Zaczniemy, w ogóle jak będą się pojawiać tego typu ciekawe pytania, będziemy losowali i co jakiś czas wrzucali odcinek, jeżeli będą się nadawały do zrobienia w wersji publicznej.

[00:46:05.550] **Szymon Warda:** Dajcie znać czy Wam się takie odcinki podobają w ogóle, taka forma? Nam się podobało.

[00:46:09.570] **Łukasz Kałużny:** Dobra, dzięki. Na razie.

[00:46:11.490] **Szymon Warda:** Na razie. Hej.

