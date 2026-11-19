## 1. Wprowadzenie do tematu platform engineering

Summary: Prowadzący przedstawiają pytanie od użytkownika Discord o platform engineering i wstępnie identyfikują główne problemy: brak self-service'u, chaos w deploymentach na wielu kontach AWS, długie cykle wdrożeniowe trwające miesiące lub lata, oraz brak standardów w organizacji liczącej 700 osób, w tym 200-250 inżynierów.

Podsumowania speakerów:
- Szymon Warda: Zwraca uwagę na paradoks sytuacji, gdzie zespoły z oddzielnymi kontami AWS powinny wdrażać szybciej, a nie wolniej, sygnalizując że problem może leżeć gdzie indziej.
- Łukasz Kałużny: Przedstawia szczegółowy kontekst problemu, opisując stos technologiczny (AWS, Terraform, Jenkins/GitHub Actions) oraz skalę organizacji z 2-3 produktami SaaS.

Najciekawsze cytaty:
1. Szymon Warda: "Cześć, czołem, kluski z rosołem. Słuchacie Patoarchitektów."
2. Łukasz Kałużny: "Platform engineering - od czego zacząć? I pytanie: czy w ogóle jest potrzebne?"
3. Szymon Warda: "To dziwne, ponieważ zwykle gdy zespoły mają osobne konta, czas wdrożenia jest krótszy - wdrażają szybciej. Więc te dwie rzeczy nam tu nie pasują."

## 2. Identyfikacja rzeczywistych problemów organizacyjnych

Summary: Prowadzący analizują głębsze przyczyny problemów wykraczające poza technologię. Identyfikują brak governance, problemy z security, prawdopodobny brak kontroli kosztów i tagowania, oraz możliwość publicznie wystawionych usług. Pojawia się hipoteza o rozproszonym monolicie na wielu kontach AWS.

Podsumowania speakerów:
- Łukasz Kałużny: Systematycznie wymienia problemy governance'owe, wskazując na brak Landing Zone, Guard Rails i Service Control Policies w AWS.
- Szymon Warda: Diagnozuje problemy z pilnowaniem kosztów infrastruktury, tagowaniem i prawdopodobnie publicznie wystawionymi usługami z powodu braku standaryzacji.

Najciekawsze cytaty:
1. Szymon Warda: "Jeżeli każdy tworzy własne moduły bez standaryzacji - każdy na własnym koncie - obstawiam, że całkowicie leży pilnowanie kosztów infrastruktury, tagowanie, rozliczanie odpowiedzialności i tak dalej."
2. Łukasz Kałużny: "Czy przypadkiem nie zbudowaliście u siebie rozproszonego monolitu na wielu kontach AWS?"
3. Szymon Warda: "Jestem pewien, że występuje kolejny problem: publicznie wystawione usługi. Ponieważ nie ma zestawionych tuneli, ludzie łączą się z bazami danych publicznie."

## 3. Analiza długich cykli wydawniczych

Summary: Prowadzący drążą temat absurdalnie długich cykli wydawniczych (miesiące do lat) w kontekście SaaS-a. Podejrzewają, że problem może wynikać zarówno z części developerskiej, jak i infrastrukturalnej, prawdopodobnie przez quality gates, testy regresyjne i kolejki oczekiwania.

Podsumowania speakerów:
- Szymon Warda: Wskazuje na paradoks wysokiej autonomii zespołów przy jednoczesnych długich cyklach, sugerując problemy z quality gates i podpisami wymagającymi zgód wielu osób.
- Łukasz Kałużny: Proponuje użycie metody 5 Why do zidentyfikowania prawdziwych przyczyn problemu i zakłada się o piwo co do źródła problemu.

Najciekawsze cytaty:
1. Szymon Warda: "Długie cykle wydawnicze - miesiące, lata od commitu do klienta - to absurd w kontekście SaaS-a. Nie wyobrażam sobie takiej sytuacji."
2. Łukasz Kałużny: "To moment na zastosowanie metody 5 Why - trzeba zacząć drążyć, co jest prawdziwą przyczyną."
3. Szymon Warda: "Długi cykl może wynikać z procesu developerskiego, ale również z części infrastrukturalnej - Ops, DevOps, nazwijmy to tej warstwy."

## 4. Problem braku self-service i złej motywacji

Summary: Prowadzący omawiają najgorszą motywację do budowania platformy - brak self-service. Podkreślają, że budowanie platformy dla własnej konsumpcji wymaga wewnętrznej chęci zespołów i że często organizacje zaczynają od technologii zamiast od standardów, co prowadzi do porażki.

Podsumowania speakerów:
- Szymon Warda: Ostrzega przed rozpoczynaniem "od dupy strony", czyli od technologii zamiast od standardów, co prowadzi do self-service'owania płatków śniegu.
- Łukasz Kałużny: Identyfikuje brak self-service jako najgorszą motywację do budowania platformy.

Najciekawsze cytaty:
1. Szymon Warda: "Często zaczynamy - przepraszam, pozdrawiam wszystkich przedszkolaków - od niewłaściwej strony. Czyli od technologii, a nie od standardów i nie od tego, co faktycznie będziemy udostępniać przez self-service."
2. Szymon Warda: "Jeśli będziemy oferować self-service dla płatków śniegu, to po prostu nie zadziała - umrzemy przez tysiąc cięć."
3. Łukasz Kałużny: "Ostatni ulubionym problem, który jest moim zdaniem najgorszą motywacją: brak self-service."

## 5. Checklista reality check infrastruktury

Summary: Prowadzący przedstawiają szczegółową checklistę do oceny stanu obecnego organizacji. Podkreślają znaczenie konkretnych liczb zamiast legend organizacyjnych oraz konieczność inwentaryzacji jako punktu wyjścia do mierzenia poprawy. Checklista obejmuje konta AWS, koszty, najczęstsze use case'y i bottlenecki.

Podsumowania speakerów:
- Szymon Warda: Argumentuje za znaczeniem liczb i konkretnych danych, aby przeciwdziałać mitom organizacyjnym i móc udowodnić wartość zmian.
- Łukasz Kałużny: Przedstawia zasadę Pareto (80/20) dla use case'ów i podkreśla znaczenie identyfikacji najczęstszych usług i patternów.

Najciekawsze cytaty:
1. Szymon Warda: "W każdej organizacji, szczególnie dużej, wiedza rozprzestrzenia się przez legendy. Ktoś komuś powiedział, ktoś dalej przekazał - i tak rosną mity organizacyjne."
2. Łukasz Kałużny: "80% use case'ów będzie identycznych. Te 20% - darujcie sobie, nie ma sensu ich sprawdzać."
3. Szymon Warda: "Jeśli chcemy coś zmieniać i poprawiać, musimy udowodnić, o ile poprawiliśmy. Musimy pokazać wartość wniesioną przez nasze działania."

## 6. Identyfikacja bottlenecków i ich źródeł

Summary: Prowadzący szczegółowo omawiają metodologię identyfikacji rzeczywistych bottlenecków w procesie dostarczania oprogramowania. Rekomendują metodę 5 Why i śledzenie konkretnych feature'ów od commita do produkcji, aby zrozumieć gdzie faktycznie leżą problemy - czy w infra provisioning, approval'ach, testach czy deploymentach.

Podsumowania speakerów:
- Szymon Warda: Zaleca przeprowadzenie wywiadów z zespołami i szczegółową analizę 3-4 konkretnych feature'ów, aby zrozumieć rzeczywiste przyczyny opóźnień.
- Łukasz Kałużny: Proponuje systematyczne zadawanie pytań o to, co faktycznie trwa miesiące i w którym miejscu procesu występują problemy.

Najciekawsze cytaty:
1. Szymon Warda: "Weźmy dwie, trzy konkretne sytuacje i prześledźmy całą ścieżkę tego commita, najlepiej konkretnego feature'a. Najlepszy byłby feature, którego biznes naprawdę potrzebował."
2. Szymon Warda: "Weźmy te punkty, które bolą, włóżmy w tę ranę palec i zacznijmy drążyć, z czego to faktycznie wynikało."
3. Łukasz Kałużny: "Co faktycznie trwa te miesiące? Czy to provisioning infrastruktury? A może approval'e z biznesu, z testów i innych obszarów?"

## 7. Pytania o shared modules i strukturę organizacyjną

Summary: Prowadzący zadają kluczowe pytania o istniejące shared modules, które mogą być zarówno prawdziwymi współdzielonymi modułami, jak i tylko copy-paste między projektami. Podkreślają znaczenie identyfikacji osób mających realną moc sprawczą w organizacji, nie tylko formalną.

Podsumowania speakerów:
- Łukasz Kałużny: Pyta o istnienie shared modules i wskazuje, że nawet copy-paste między projektami jest formą współdzielenia.
- Szymon Warda: Zwraca uwagę na różnicę między teoretycznym a faktycznym rozkładem uprawnień i mocy w organizacji.

Najciekawsze cytaty:
1. Szymon Warda: "Shared modules? Są takie, że zespoły stworzyły własne rozwiązania i w swoich projektach ponownie wykorzystują pewne moduły."
2. Szymon Warda: "Kluczowe jest zidentyfikowanie, kto ma tę nieformalną moc sprawczą, kto może wpływać na kolejne zespoły. Jeśli będziemy opierać się na teoretycznym rozkładzie uprawnień, to polegniemy."
3. Łukasz Kałużny: "Czy już istnieją jakieś shared modules? Czy może ludzie za shared modules uważają również copy-paste między projektami?"

## 8. Gotowość organizacji do standaryzacji

Summary: Prowadzący przechodzą do najtrudniejszych pytań dotyczących gotowości organizacji. Kluczowe jest ustalenie, czy zespoły chcą standaryzacji czy będą walczyć, oraz czy jest przestrzeń na wydzielony platform team. Podkreślają, że część zespołów będzie chciała, część nie, i trzeba zacząć od tych chętnych.

Podsumowania speakerów:
- Łukasz Kałużny: Identyfikuje polityczny aspekt standaryzacji i konieczność zrozumienia, od jakiej proporcji zespołów (1 vs 10) zaczynamy.
- Szymon Warda: Proponuje strategię wyboru zespołów, które chcą standaryzacji i stopniowego roll-outu, zamiast próby zadowolenia wszystkich naraz.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Czy zespoły chcą standaryzacji, czy będą przeciwko niej walczyć? To kwestia, którą trzeba sobie politycznie rozgryźć w organizacji."
2. Szymon Warda: "Część zespołów będzie chciała standaryzacji - trzeba wybrać właśnie te zespoły i następnie przeprowadzić stopniowy roll-out."
3. Szymon Warda: "Większość zespołów będzie uważała, że jeśli zastosujemy nasze standardy, to chcemy je narzucić pozostałym."

## 9. Business impact i konieczność sponsora z boardu

Summary: Prowadzący podkreślają konieczność udowodnienia wpływu chaosu na biznes i znaczenie metody "follow the money". Wyjaśniają, że wdrażanie standardów wymaga przerabiania kodu, co generuje koszty i ryzyko regresji, dlatego potrzebny jest silny sponsor na poziomie C-level.

Podsumowania speakerów:
- Szymon Warda: Argumentuje, że bez udowodnienia biznesowego celu i zysków, wdrożenie standardów się nie uda z powodu kosztów i ryzyka regresji.
- Łukasz Kałużny: Podkreśla, że ktoś z boardu musi być sponsorem inicjatywy, niekoniecznie CTO, ale ktoś na poziomie C-level.

Najciekawsze cytaty:
1. Szymon Warda: "Wdrażanie jakichkolwiek standardów oznacza przerabianie istniejącego kodu. A to oznacza kilka rzeczy: koszt pieniężny, koszt czasowy i regresję, która wystąpi."
2. Szymon Warda: "Jeżeli nie udowodnimy, dlaczego to robimy - jaki jest cel i jaki będzie z tego zysk - to się nie uda."
3. Łukasz Kałużny: "Nie oszukujmy się - ktoś z boardu musi być sponsorem całej inicjatywy."

## 10. Finansowanie i struktura platform teamu

Summary: Prowadzący omawiają potrzebę dedykowanych zasobów dla platform teamu. Przy opisywanej skali organizacji rekomendują 2-3 osoby na start, docelowo 5-8 osób, lub alternatywnie format gildii z kontrybucją. Odrzucają model oddelegowania osób na kilka sprintów jako nieskuteczny.

Podsumowania speakerów:
- Łukasz Kałużny: Sugeruje początkowy team 2-3 osobowy, docelowo 5-8 osób, lub alternatywnie format gildii z oddelegowaniem ludzi na 2-3 sprinty.
- Szymon Warda: Stanowczo sprzeciwia się modelowi oddelegowania, argumentując że biznes zawsze będzie ważniejszy i czas będzie szarpany, co obniży jakość.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Czy jest w organizacji przestrzeń na - prawdopodobnie w tej skali zaczynałbym od dwóch, trzech osób - inicjalny platform team?"
2. Szymon Warda: "Problem z oddelegowaniem polega na tym, że to nie jest kod danej osoby. Biznes zawsze będzie ważniejszy."
3. Szymon Warda: "Gdy czas będzie szarpany, jakość spadnie - według mnie to nie zadziała."

## 11. Pomiar toil i powtarzalnej pracy ręcznej

Summary: Prowadzący odnoszą się do koncepcji "toil" z książki SRE Google'a - powtarzalnych, ręcznych czynności wynikających z braku integracji systemów. Rekomendują zmierzenie ile czasu tracimy na "papierki" i używanie macierzy decyzyjnej do określenia, kiedy automatyzować.

Podsumowania speakerów:
- Łukasz Kałużny: Wprowadza koncepcję toil z SRE book i zapowiada zalinkowanie macierzy decyzyjnej dotyczącej automatyzacji.
- Szymon Warda: Potwierdza znaczenie mierzenia czasu traconego na powtarzalne czynności manualne.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Ile tej pracy stanowi powtarzalny toil? To koncepcja z SRE book od Google'a - książka jest kontrowersyjna w pewnych miejscach, ale zawiera właśnie pomiar tego rodzaju pracy."
2. Szymon Warda: "Czyli ile czasu tracimy na papierki."
3. Łukasz Kałużny: "Zalinkuję macierz decyzyjną określającą, kiedy automatyzujemy, a kiedy nie."

## 12. Definicja kryteriów sukcesu platformy

Summary: Prowadzący podkreślają, że platforma musi mieć jasno zdefiniowane kryteria sukcesu, nie może być budowana dla zabawy. Omawiają różne możliwe metryki sukcesu: lead time, developer happiness/experience, oraz sposób mierzenia czy platforma faktycznie działa, wskazując na metryki z Dora.

Podsumowania speakerów:
- Łukasz Kałużny: Pyta o definicję sukcesu i czy jest to krótszy lead time czy developer experience, sugerując metryki z Dora.
- Szymon Warda: Ostrzega, że na starcie będzie masa narzekań, więc nie należy optymalizować w kierunku szczęścia, choć dobry UX jest konieczny.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Najgorsza rzecz, którą rynek ignoruje z prostej przyczyny: platformę budujemy dla własnej zabawy, a nie dla osiągnięcia konkretnych celów."
2. Szymon Warda: "Na starcie będzie masa narzekań. Nie optymalizowałbym w kierunku szczęścia użytkowników, bo każdy ma inne oczekiwania."
3. Łukasz Kałużny: "Jak będziecie mierzyć, czy platforma działa?"

## 13. Identyfikacja użytkowników platformy i ich potrzeb

Summary: Prowadzący podkreślają kluczowe znaczenie zdefiniowania, kim są faktyczni użytkownicy platformy i czego potrzebują. Ostrzegają przed pułapką, w którą wpadają inteligentni inżynierowie w platform teamie - pisaniem dokumentacji pokazującej jak są mądrzy, zamiast skupienia się na potrzebach użytkowników.

Podsumowania speakerów:
- Łukasz Kałużny: Zadaje fundamentalne pytanie o identyfikację użytkowników platformy i ich rzeczywistych potrzeb.
- Szymon Warda: Ostrzega, że inteligentni inżynierowie w platform teamie często chcą się pochwalić jak są mądrzy, zamiast pisać dla określonych person.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Kim są faktyczni użytkownicy naszej potencjalnej platformy i czego oni konkretnie potrzebują?"
2. Szymon Warda: "Problem polega na tym, że gdy zaczynają pisać dokumentację lub cokolwiek innego, często wynika to z chęci pokazania, jacy są mądrzy."
3. Szymon Warda: "Musimy mieć określone persony - kto korzysta z platformy, do kogo piszemy, jak to wygląda i do kogo kierujemy te produkty."

## 14. Konieczność product managementu dla platformy

Summary: Prowadzący podkreślają, że platforma wymaga prawdziwego product managementu, włączając w to reklamy, release'y i świętowanie sukcesów - rzeczy, których inżynierowie zazwyczaj nie lubią, ale które są konieczne, szczególnie na początku wdrożenia.

Podsumowania speakerów:
- Łukasz Kałużny: Stwierdza wprost, że najgorsza rzecz przy platformach to fakt, że platforma wymaga product managementu.
- Szymon Warda: Wymienia konkretne elementy product managementu: reklamy, release'y, świętowanie, które są bardzo konieczne na starcie.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Najgorsza rzecz przy platformach: platforma wymaga product managementu."
2. Szymon Warda: "Reklamy, release'y, świętowanie - wszystko to, czego inżynierowie zazwyczaj nie lubią, jest bardzo konieczne, szczególnie na starcie, gdy sytuacja będzie różna."

## 15. Kiedy zrezygnować z budowania platformy - płatki śniegu

Summary: Prowadzący przedstawiają pierwszy red flag - sytuację, gdy każdy zespół twierdzi, że jest unikalnym płatkiem śniegu i nie może żyć inaczej. Szczególnie problematyczne jest, gdy każdy zespół używa innej technologii, co czyni koszty ujednolicenia nieuzasadnionymi.

Podsumowania speakerów:
- Łukasz Kałużny: Identyfikuje jako pierwszy red flag przekonanie każdego zespołu o swojej unikalności i niemożności funkcjonowania inaczej.
- Szymon Warda: Doprecyzowuje, że prawdziwy problem to różne technologie w każdym zespole, co czyni ujednolicenie nieopłacalnym.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Kiedy w ogóle zrezygnować z platformy? Po pierwsze: każdy zespół twierdzi, że jest unikalnym płatkiem śniegu i nie może funkcjonować inaczej."
2. Szymon Warda: "Dla mnie faktycznie problematyczne jest, gdy każdy zespół używa innej technologii. Wtedy koszty ujednolicenia nie mają sensu."

## 16. Kiedy zrezygnować - brak wsparcia managementu

Summary: Prowadzący wyjaśniają, że jeśli management nie popiera standaryzacji i będzie bronił zespołów przed wejściem na platformę, oznacza to inicjatywę oddolną, która się nie powiedzie bez umocowania politycznego. To połączone z poprzednim punktem dyskwalifikuje projekt platformy.

Podsumowania speakerów:
- Łukasz Kałużny: Łączy brak wsparcia managementu z obroną zespołów jako oznakę inicjatywy oddolnej bez umocowania politycznego.
- Szymon Warda: Potwierdza, że te dwa punkty razem oznaczają brak szans powodzenia.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Management nie popiera standaryzacji i będzie bronił zespołów przed wejściem na platformę."
2. Łukasz Kałużny: "Te dwa punkty razem oznaczają, że to inicjatywa oddolna, która się nie powiedzie bez umocowania politycznego."

## 17. Kiedy zrezygnować - brak czasu i CV-driven development

Summary: Prowadzący wymieniają kolejne red flagi: organizację bez czasu na nic ("bieganie z pustymi teczkami"), budowanie platformy dla samego budowania (CV-driven development) oraz brak capacity na platform team. To standardowe antywzorce dyskwalifikujące projekt.

Podsumowania speakerów:
- Szymon Warda: Używa obrazowego określenia "biegać z pustymi teczkami" dla organizacji bez czasu na rzeczywistą pracę.
- Łukasz Kałużny: Wymienia CV-driven development i brak capacity jako oczywiste red flagi.

Najciekawsze cytaty:
1. Szymon Warda: "Jeżeli w firmie jedyne, co można robić, to biegać z pustymi teczkami i nie ma czasu na nic innego - platforma nie ma sensu."
2. Łukasz Kałużny: "Kolejny standardowy punkt, który powinien pojawić się chyba jako pierwszy: budowanie platformy po to, żeby zbudować platformę."
3. Łukasz Kałużny: "Kolejny red flag: brak capacity na platform team. To się nie uda."

## 18. Kiedy zrezygnować - rozwiązywanie problemów ludzkich technologią

Summary: Prowadzący ostrzegają przed próbą rozwiązywania problemów ludzkich i procesowych przez technologię. Rekomendują metodę 5 Why do zidentyfikowania prawdziwych problemów. Ostatni red flag to zespoły aktywnie walczące o swoją unikalność z postawą "albo nasz standard, albo nic".

Podsumowania speakerów:
- Łukasz Kałużny: Wskazuje na próbę rozwiązywania problemów ludzkich technologią jako red flag i rekomenduje 5 Why.
- Szymon Warda: Opisuje zespoły aktywnie walczące o unikalność jako ostatni, ale istotny red flag.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Kolejna rzecz: próbujemy rozwiązać ludzkie problemy, często procesowe, przez technologię."
2. Szymon Warda: "Technologia pomaga, ale bez rozmów z ludźmi, bez ustaleń, bez tych trudnych, czasem nudnych, a nawet burzliwych spotkań, tego nie zrobimy."
3. Łukasz Kałużny: "Mamy zespoły, które aktywnie walczą o swoją unikalność - albo nasz standard, albo brak standaryzacji, albo nic."

## 19. Strategia przekonywania przez wartość zamiast wymuszania

Summary: Prowadzący przedstawiają strategię pokazywania wartości zamiast wymuszania adopcji. Szymon dzieli się doświadczeniem, jak oferowanie konkretnych korzyści (np. automatyczne liczenie budżetów) przekonuje zespoły. Wprowadza koncepcję Steve'a Ballmera: "a bit of success" - sprawianie, że robienie rzeczy właściwie jest łatwiejsze.

Podsumowania speakerów:
- Szymon Warda: Opowiada o strategii oferowania wartości i czekania, aż zespoły same zdecydują się skorzystać, zamiast przekonywania siłą.
- Łukasz Kałużny: Potwierdza strategię "walczenia feature'ami" jako skuteczną metodę adopcji.

Najciekawsze cytaty:
1. Szymon Warda: "Słuchajcie, nie musicie tego robić. Ale gdybyście korzystali z naszych modułów, mielibyście na przykład automatyczne liczenie budżetów."
2. Szymon Warda: "Sprawiamy, że łatwiej jest robić rzeczy dobrze - tak jak my chcemy - a trochę trudniej pozostałe. Nagle ludzie przekonają się, że jednak będzie im łatwiej."
3. Szymon Warda: "Nie prowadzisz dalszej dyskusji ani przekonywania - po prostu wiesz, że to będzie wartość, jeśli zespół z tego skorzysta. Zostawiasz ofertę i czekasz."

## 20. Strategia przejmowania odpowiedzialności za on-call

Summary: Prowadzący omawiają strategię z Google'a, gdzie używanie standardowych frameworków i narzędzi platformy oznacza, że po fazie hypercare platform team przejmuje odpowiedzialność za on-call. Jeśli zespół chce robić po swojemu, musi sam się tym zajmować - co bardzo skutecznie motywuje do adopcji.

Podsumowania speakerów:
- Łukasz Kałużny: Przywołuje przykład z Google'a, gdzie używanie wbudowanych frameworków oznacza brak konieczności bycia na on-callu po hypercare.
- Szymon Warda: Potwierdza skuteczność tej strategii: zespół platformowy przejmuje wsparcie dla standardowych rozwiązań, niestandardowe zespoły obsługują same.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Dla niego korzyścią z przestrzegania standardów i używania wbudowanych frameworków jest to, że po fazie hypercare nie będzie już na on-callu."
2. Szymon Warda: "Jeżeli używasz naszych usług, zespół platformowy przejmuje odpowiedzialność. A jeśli chcesz robić po swojemu - okej, nie ma problemu, ale Ty się tym zajmujesz."
3. Szymon Warda: "To działa bardzo dobrze."

## 21. Czy w ogóle potrzebna jest platforma?

Summary: Prowadzący odpowiadają na fundamentalne pytanie: przy opisywanej skali (200-250 inżynierów) platforma jest potrzebna, ale kluczowe jest posiadanie capacity na dedykowany platform team. Sugerują, że członkowie teamu mogą pochodzić z istniejących zespołów OPS i security, nie muszą być nowymi rekrutacjami.

Podsumowania speakerów:
- Łukasz Kałużny: Potwierdza, że przy skali około 100-150 aktywnych developerów platforma ma sens, ale wymaga capacity na etaty.
- Szymon Warda: Sugeruje wykorzystanie ludzi z zespołów OPS i security jako członków platform teamu, podając przykład rekrutacji bezpieczników.

Najciekawsze cytaty:
1. Łukasz Kałużny: "To już skala, przy której - bo zawsze mówimy o skali - jeżeli mamy około setki, 150 aktywnych developerów, spokojnie warto."
2. Szymon Warda: "Przy tej liczbie developerów zakładam, że istnieją osobne zespoły OPS, osobne zespoły security. Można również z tych zespołów wyłonić ludzi, którzy będą członkami platform teamu."
3. Łukasz Kałużny: "Przykładowo, jeden z naszych klientów rekrutuje do takiego teamu bezpieczników, żeby mieć ich bezpośrednio w zespole."

## 22. Definicja platformy - standardy przede wszystkim

Summary: Prowadzący definiują czym powinna być platforma, ostrzegając przed wdrożeniem samego Backstage jako "odtrąbienia sukcesu". Podkreślają, że platforma to przede wszystkim standardy, a dopiero potem self-service i governance. API do platformy powinno być GitHub Actions z reusable workflows i własnymi akcjami.

Podsumowania speakerów:
- Szymon Warda: Wyjaśnia hierarchię: najpierw standardy, potem self-service, potem governance, a Backstage to tylko wisienka na torcie. Promuje GitHub Actions jako API platformy.
- Łukasz Kałużny: Kontrowersyjnie sugeruje, że Backstage można wrzucić na początku, ale bez ani grama custom code.

Najciekawsze cytaty:
1. Szymon Warda: "Jeżeli wdrożycie Backstage i odtrąbicie sukces, to się nie uda. Backstage jest naprawdę tylko wisienką na torcie."
2. Szymon Warda: "Platforma to przede wszystkim standardy. Standardy, standardy - bo dopiero potem można mieć wspólne elementy i dalej rozwijać rozwiązanie."
3. Szymon Warda: "Waszym API do platformy będzie GitHub Actions. Macie reusable workflows, macie własne akcje - i nie należy się ich bać."

## 23. Kontrowersja wokół Backstage na początku projektu

Summary: Prowadzący dyskutują o miejscu Backstage w projekcie platformy. Szymon ostrzega, że wdrożenie Backstage to ryzykowne "szybkie odtrąbienie sukcesu", które może zabić motywację do dalszej pracy. Łukasz sugeruje, że można go użyć, ale absolutnie bez custom code.

Podsumowania speakerów:
- Szymon Warda: Ostrzega przed Backstage jako przedwczesnym ogłoszeniem sukcesu, które zabije motywację do prawdziwej pracy.
- Łukasz Kałużny: Proponuje kompromis - Backstage można wrzucić, ale bez żadnego custom code.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Można zacząć go używać, można go wrzucić nawet na początku, Szymon - ale jest jedno 'ale': nie powinno tam się znaleźć ani grama custom code."
2. Szymon Warda: "Dla mnie Backstage to takie szybkie odtrąbienie sukcesu: mamy, mamy, mamy - i cieszymy się z czegoś, czego właściwie nie mamy."
3. Szymon Warda: "To ryzykowne, bo za chwilę odtrąbi się sukces i motywacja do dalszej pracy poleci na łeb na szyję."

## 24. Identyfikacja faktycznych bottlenecków metodą 5 Why

Summary: Prowadzący szczegółowo omawiają metodę identyfikacji prawdziwych bottlenecków. Łukasz sugeruje ankietowanie i odniesienie do odcinka z Kingą o Dora Metrics. Szymon preferuje wywiady z 3-4 zespołami i analizę konkretnych feature'ów, aby zrozumieć rzeczywiste przyczyny opóźnień.

Podsumowania speakerów:
- Łukasz Kałużny: Proponuje zadawanie pytań o to, co faktycznie trwa miesiące i czy to infra provisioning, approval'e, testy czy deploymenty, oraz ankietowanie zespołów.
- Szymon Warda: Preferuje szczegółowe wywiady z zespołami na konkretnych przykładach feature'ów zamiast ankiet, ostrzegając przed przedwczesnym wdrożeniem Dora Metrics.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Co faktycznie trwa te miesiące? Czy to provisioning infrastruktury? A może approval'e z biznesu, z testów? Czy to testy, testing, czy deploymenty?"
2. Szymon Warda: "Przeprowadzić trzy, cztery wywiady z zespołami i wykonać dokładną analizę na przykładzie konkretnych sytuacji, konkretnych feature'ów - zobaczyć, dlaczego to tyle trwało."
3. Szymon Warda: "Dora Metrics są świetne, ale dopiero gdy uporządkujemy sytuację. To nie jest narzędzie na start - znowu byłoby to odtrąbienie sukcesu. Nie tędy droga."

## 25. Problem z Terraformem - 80% kodu jest identyczne

Summary: Prowadzący analizują problem z Terraformem, zakładając się, że 80% kodu u wszystkich zespołów to te same przypadki napisane zupełnie inaczej w każdym zespole. Brakuje standardów tagowania, bezpieczeństwa, sieciówki i dostępów. Pojawia się hipoteza o możliwych zakupach innych firm.

Podsumowania speakerów:
- Łukasz Kałużny: Zakłada się, że 80% kodu to te same przypadki zaimplementowane różnie, chyba że kod wędrował między zespołami.
- Szymon Warda: Wymienia brak standardów w tagowaniu, bezpieczeństwie, sieciówce i środowiskach developerskich, sugerując możliwość zakupów innych firm.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Prawdopodobnie 80% kodu u wszystkich zespołów to te same przypadki - tylko napisane w każdym miejscu zupełnie inaczej, zaimplementowane w każdym zespole na swój sposób."
2. Szymon Warda: "Prawdopodobnie brakuje standardów tagowania, standardów bezpieczeństwa, sieciówki, dostępów, wystawiania usług, środowisk developerskich. Wszystko tam będzie inne."
