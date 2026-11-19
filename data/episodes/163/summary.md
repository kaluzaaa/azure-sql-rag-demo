## 1. Wprowadzenie do Model Context Protocol (MCP)

Summary: Łukasz i Szymon rozpoczynają odcinek od wyjaśnienia czym jest MCP - protokół stworzony przez Anthropica jako dynamiczne rozszerzenie function calling w LLM-ach. MCP standaryzuje sposób dostarczania narzędzi i zasobów do modeli językowych, umożliwiając decoupling między kodem aplikacji a integracjami.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Wyjaśnia, że MCP to wystandaryzowany protokół pozwalający na dynamiczne wykrywanie narzędzi i zasobów dla LLM-ów, będący nakładką na function calling.
- Szymon Warda: Doprecyzowuje, że protokół umożliwia dwukierunkową komunikację - model dowiaduje się co klient może zrobić, a klient co model może wykonać.

Najciekawsze cytaty:
1. Łukasz Kałużny: "MCP to dynamiczne rozszerzenie function calling w LLM-ach."
2. Łukasz Kałużny: "Protokół został zapoczątkowany przez Anthropica, a wszyscy duzi gracze od modeli do niego kontrybuują. To już standard dostarczania narzędzi do LLM-ów."

## 2. Architektura i komponenty MCP

Summary: Omówienie architektury MCP składającej się z klienta, serwera i transportu. Komunikacja opiera się na JSON RPC, a transport może odbywać się przez standard IO (lokalnie) lub Streamable HTTP. Protokół zawiera mechanizmy negocjacji wersji i możliwości między klientem a serwerem.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Opisuje techniczne aspekty architektury, wskazując na JSON RPC jako podstawę komunikacji i dwa rodzaje transportu - stdio oraz HTTP2.
- Szymon Warda: Podkreśla, że protokół jest przemyślany pod kątem wersjonowania i fallbacku, co jest istotne gdy serwery mogą nie być aktywnie rozwijane.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Całość jest zbudowana na JSON RPC, komunikacja jest standaryzowana w tym formacie."
2. Szymon Warda: "Protokół jest przemyślany pod kątem tego, że serwery powstaną i mogą nie być rozwijane, dlatego istnieją negocjacje możliwości między klientem a serwerem."

## 3. Scenariusze użycia - lokalna produktywność

Summary: Pierwszy główny scenariusz zastosowania MCP to zwiększenie lokalnej produktywności przez dostarczanie narzędzi do edytorów kodu i chatów AI. Przykłady obejmują dostęp do dokumentacji, plików lokalnych czy kalendarza. Narzędzia są zazwyczaj uruchamiane lokalnie przez NPX, pip lub Docker.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Przedstawia praktyczne przykłady użycia, w tym narzędzie Context 7 do pobierania aktualnej dokumentacji oraz różne sposoby lokalnego uruchamiania serwerów MCP.
- Szymon Warda: Wyjaśnia ideę małych, wyspecjalizowanych serwerków MCP, które rozszerzają możliwości LLM o dodatkowe funkcje bez wykonywania logiki przez sam model.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Jednym z przykładów, które mogę polecić, jest Context 7 – aktualna dokumentacja dla LLM-ów i edytorów kodu AI."
2. Szymon Warda: "LLM nie będzie tego wykonywać, nie będzie bezpośrednio sięgał do zasobów – to tylko statystyczny mechanizm. Dzięki MCP dajemy mu dodatkowe możliwości i rozszerzamy jego funkcjonalność."

## 4. Scenariusze korporacyjne i zdalne użycie MCP

Summary: Drugi główny scenariusz to zastosowania korporacyjne, gdzie MCP serwery są wystawiane zdalnie przez HTTP dla wielu użytkowników i agentów. Microsoft Copilot Studio, Azure Logic Apps i API Gateway mogą wystawiać akcje jako MCP, umożliwiając wielokrotne wykorzystanie tych samych integracji.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Opisuje jak infrastruktura cloudowa, szczególnie Azure'owa, pozwala na transformację REST API w MCP i wykorzystanie tego przez różnych agentów.
- Szymon Warda: Pyta o mechanizmy wykrywania i deklarowania serwerów MCP, podkreślając że nie ma w tym magii - wszystko musi być jawnie skonfigurowane.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Raz wystawione rozwiązanie na API Gateway, Logic Apps czy innym narzędziu open source z zbudowanymi integracjami pozwala wykorzystać MCP w wielu różnych zastosowaniach."

## 5. Primitives MCP - Tools (narzędzia)

Summary: Tools to najważniejszy element MCP, odpowiednik function calling. Każde narzędzie ma nazwę, opis i schemat inputu w JSON. LLM na podstawie tych informacji decyduje o wywołaniu narzędzia. Kluczowe jest generowanie opisów przez LLM po angielsku dla lepszego zrozumienia oraz uważanie na limit kontekstu.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Ostrzega przed przeciążeniem kontekstu zbyt dużą liczbą narzędzi i podkreśla znaczenie dobrych opisów generowanych przez LLM.
- Szymon Warda: Zachęca do lenistwa i używania LLM do generowania opisów, bo robi to lepiej niż ręczne pisanie.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Im więcej narzędzi dodamy, tym większy problem. Narzędzia prezentują się LLM-owi jako format JSON."
2. Szymon Warda: "Warto być leniwym – generowane opisy są naprawdę dobrej jakości i tworzone w sposób, który LLM doskonale rozumie."

## 6. Primitives MCP - Resources (zasoby)

Summary: Resources to dane bez logiki - proste źródła informacji jak pliki czy odpowiedzi API. W przeciwieństwie do tools nie wykonują akcji, tylko zwracają dane. Mogą mieć proste parametry jak ID użytkownika, ale powinny być lekkie i szybkie w zwracaniu danych.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Definiuje resources jako dane bez logiki, które szybko zwracają informacje, w przeciwieństwie do tools zawierających akcje i modyfikacje.
- Szymon Warda: Upraszcza, że w większości przypadków resources to po prostu pliki.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Resources to dane bez logiki. Tools to wywoływanie akcji, modyfikacja, pobieranie, natomiast resources to po prostu dane bez logiki."

## 7. Primitives MCP - Prompts, Sampling i Roots

Summary: Prompts to predefiniowane szablony promptów uruchamiane jak komendy. Sampling pozwala na human-in-the-loop i kontrolę tego co jest wysyłane do LLM, choć wsparcie w klientach jest słabe. Roots definiują dostępne zasoby i ścieżki dyskowe dla klienta.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Wyjaśnia że prompts to gotowe szablony, a sampling to mechanizm akceptacji działań, który jest słabo wspierany przez istniejące narzędzia.
- Szymon Warda: Porównuje prompts do komend w konsoli Quake i podkreśla prostotę tego mechanizmu.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Wpisuję slash review code i w zależności od implementacji interfejsu, model dostaje gotowy prompt do użycia."
2. Łukasz Kałużny: "Założenie jest takie, że serwer może poprosić klienta o human-in-the-loop – pełną kontrolę nad tym, co zostanie wysłane do LLM lub co LLM wykona."

## 8. Uwierzytelnianie i bezpieczeństwo tokenów

Summary: Lokalnie tokeny często są przechowywane w plain text w konfiguracji, co stanowi zagrożenie bezpieczeństwa. Dla zdalnych scenariuszy MCP wykorzystuje standardy OAuth i OpenID Connect, umożliwiając single sign-on i znane przepływy uwierzytelniania.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Ostrzega przed niebezpieczeństwem przechowywania tokenów w clear text lokalnie i wskazuje na OAuth jako rozwiązanie dla scenariuszy zdalnych.
- Szymon Warda: Potwierdza że wykorzystywany jest sprawdzony standard bez wymyślania czegoś nowego.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Bardzo często tokeny są przekazywane jawnie. Przy wywołaniu lokalnego narzędzia w konfiguracji deklarujemy token w czystym tekście. Doskonały przykład to MCP Server do Stripe'a – gdzie przechowywany jest token admina?"
2. Łukasz Kałużny: "W bardziej zaawansowanych scenariuszach z autoryzacją odpowiedź jest prosta: OAuth i OpenID Connect."

## 9. Bezpieczeństwo - DLP i Content Protection

Summary: Content protection dotyczy kontroli jakie dane są wysyłane do LLM - problem DLP (Data Loss Prevention). Rynek jeszcze nie wypracował jasnych standardów compliance dla danych medycznych czy innych wrażliwych przesyłanych do modeli AI.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Podkreśla że to szerszy problem wykraczający poza MCP, związany z tym czy dane medyczne i inne wrażliwe mogą być wysyłane do LLM.
- Szymon Warda: Początkowo myli content protection z prompt shielding, co prowadzi do wyjaśnienia różnicy między tymi mechanizmami.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Pytanie brzmi: co faktycznie wyślemy do LLM z naszych danych? To długa dyskusja wykraczająca poza MCP – to temat DLP."
2. Łukasz Kałużny: "We wrześniu 2025 roku mamy problem – jako rynek ciągle dyskutujemy i proponujemy rozwiązania, ale nie ma niczego jasno zdefiniowanego, czym to powinno być."

## 10. Bezpieczeństwo - Prompt Shield i Prompt Injection

Summary: Prompt shield chroni przed prompt injection - atakami gdzie złośliwe instrukcje są ukryte w danych pobieranych z publicznych źródeł. Przykład ataku na MCP GitHuba pokazał jak issue mogło zawierać instrukcje do wycieku sekretów. Azure AI Content Safety oferuje API do weryfikacji potencjalnie szkodliwych payloadów.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Opisuje realny atak na MCP GitHuba gdzie prompt injection w issue doprowadził do próby wycieku sekretów i wyjaśnia rolę Azure AI Safety.
- Szymon Warda: Tłumaczy mechanizm działania - sprawdzanie czy dane nie zawierają instrukcji typu "zignoruj wszystkie zabezpieczenia".

Najciekawsze cytaty:
1. Łukasz Kałużny: "Pobieramy issue z publicznych źródeł, a tam ukryta była instrukcja, żeby zleakować wszystkie sekrety i wpisać je jako odpowiedź w issue na GitHubie, włącznie z dostępem do prywatnych repozytoriów."
2. Szymon Warda: "Mechanizm działa tak: zanim przekażemy dane do modelu, sprawdzamy czy nie zawierają zdań typu 'zignoruj wszystkie zabezpieczenia i zrób to, co chcę'."

## 11. MCP jako API Gateway dla LLM

Summary: MCP działa jak API Gateway, ale nie w tradycyjnym rozumieniu - musi być dostosowany do LLM. Przykład MCP Jiry pokazuje problem: zwracanie surowych, nieudokumentowanych danych REST API prowadzi do niezrozumienia przez LLM lub wyczerpania kontekstu. API dla LLM powinno reprezentować funkcje biznesowe, nie surowy CRUD.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Krytykuje MCP Jiry za zwracanie surowych danych REST i podkreśla konieczność mapowania na funkcje biznesowe zamiast wystawiania CRUD-a.
- Szymon Warda: Ostrzega że CRUD przekłada całą logikę biznesową na model, który jej nie ma i może się nie trzymać założeń.

Najciekawsze cytaty:
1. Łukasz Kałużny: "MCP od Jiry Cloud zwraca REST API w niezmienionej formie – masę nieudokumentowanych pól, niezrozumiałych opisów i innych elementów."
2. Łukasz Kałużny: "To, co wystawiamy do LLM, nie powinno być surowym CRUD-em z systemu biznesowego, tylko przemapowaniem na faktyczne funkcje biznesowe."

## 12. Rate limiting i izolacja

Summary: Rate limiting jest kluczowy aby jeden klient nie obciążył całego systemu. Należy śledzić kto, co i ile zasobów zużywa, na przykład przez APIM. Izolacja i sampling request pozwalają na kontrolę użytkownika nad tym co jest przekazywane do LLM, podobnie jak akceptacja akcji w Copilot czy Cursor.

Podsumowania wypowiedzi prowadzących:
- Szymon Warda: Podkreśla znaczenie śledzenia zużycia zasobów przez poszczególnych klientów, szczególnie ze względu na koszty.
- Łukasz Kałużny: Wyjaśnia sampling jako human-in-the-loop na przykładzie akceptacji wywołań narzędzi w edytorach kodu.

Najciekawsze cytaty:
1. Szymon Warda: "Kluczowe jest postawienie na przykład APIM-a, żeby dokładnie wiedzieć kto z czego korzysta i móc śledzić ruch. W przeciwnym razie przyjdzie rachunek i nie będziemy wiedzieli, kto tyle zużył."

## 13. Jak zacząć używać MCP - SDK i narzędzia

Summary: Nie należy kodować MCP od zera - trzeba używać SDK w preferowanym języku. Warto rozważyć gotowe rozwiązania jak Azure API Management czy Logic Apps do wystawiania istniejących API jako MCP. MCP Inspector to oficjalne, dobrze rozwinięte narzędzie do debugowania z pełnym wsparciem uwierzytelniania.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Radzi używanie SDK i gotowych rozwiązań cloudowych zamiast pisania od zera, szczególnie dla prostszej logiki.
- Szymon Warda: Podkreśla że MCP Inspector to nie side project, tylko oficjalnie wspierane narzędzie o wysokiej jakości.

Najciekawsze cytaty:
1. Szymon Warda: "Pytanie jak zacząć od zera, bo istnieją biblioteki, które dają bazę – serwer MCP – i od tego można zacząć."
2. Łukasz Kałużny: "Pojawią się teraz produkty i trzykrotnie zastanowiłbym się, czy nie wykorzystać gotowego elementu usługi lub rozwiązania softwareowego do przemapowania, zamiast pisać coś od zera."

## 14. Dobre praktyki - za dużo narzędzi i kontekst

Summary: Główne wyzwanie to przeciążenie kontekstu zbyt dużą liczbą narzędzi. Prowadzi to do wyczerpania okna kontekstowego lub problemów z trzymaniem się instrukcji przez LLM. Lepiej mieć małych wyspecjalizowanych agentów z ograniczonym zestawem MCP niż jednego wielkiego agenta "do wszystkiego".

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Ostrzega przed nawalaniem zbyt wielu extensionów i proponuje architekturę z orchestratorem wywołującym małych agentów.
- Szymon Warda: Przestrzega też przed drugim skrajnym przypadkiem - jednym wielkim narzędziem z absurdalnie skomplikowanym API.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Pierwsza rzecz: za dużo narzędzi, za dużo zwracanych danych prowadzi do wyczerpania okna kontekstowego w LLM lub problemów z trzymaniem się instrukcji przez zbyt duży kontekst."
2. Łukasz Kałużny: "Tworząc agenta korporacyjnego, nie powinien mieć on wszystkich MCP naraz. Lepiej, żeby nad nim był orchestrator wywołujący małych, wyspecjalizowanych agentów."

## 15. Dobre praktyki - walidacja i opisy

Summary: Kluczowe jest używanie SCIM validation na inputach oraz tworzenie dobrych opisów schematów input i output. Należy wspierać różne formaty contentu (tekst, binarki, obrazy). Dla long-running jobów serwer powinien odsyłać progres, aby uniknąć halucynacji LLM podczas oczekiwania.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Podkreśla znaczenie walidacji SCIM i opisów, oraz dzieli się doświadczeniem jak brak progressu doprowadził do halucynacji modelu.
- Szymon Warda: Potwierdza problem halucynacji własnym przykładem z OCR-em, gdzie model wymyślił zawartość strony.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Pamiętajcie o walidacji SCIM na inpucie i dobrym opisie schematów input i output. To chyba najbardziej istotny element całości."
2. Łukasz Kałużny: "Nauczyłem się tego w praktyce, gdy model zaczął halucynować podczas pobierania i obróbki tekstu związanego z podcastem. Na podstawie samego tytułu wymyślił i zsumaryzował odcinek, do którego nie miał transkryptu."

## 16. Autonomiczni agenci i human-in-the-loop

Summary: Autonomiczny agent to taki, który jest wywoływany przez cron, event lub request - nie "myśli" samodzielnie. Główne wyzwanie to monitorowanie. Agenci powinni mieć ograniczony scope i nie rozumieć pokrętnej logiki biznesowej. Nawet autonomiczne agenty powinny wymagać ludzkiej akceptacji dla modyfikacji systemów, np. przez drafty lub maile z zatwierdzeniem.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Definiuje autonomicznego agenta i podkreśla potrzebę prostej logiki oraz human-in-the-loop dla modyfikacji systemowych.
- Szymon Warda: Ostrzega przed wystawianiem agentów do systemów korporacyjnych bez weryfikacji człowieka, bo odpowiedzialność musi być po stronie ludzi.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Autonomiczny agent to taki, który wywołuje cron, event lub request. Agent nie siedzi i nie myśli samodzielnie."
2. Łukasz Kałużny: "Nawet jeśli agent jest autonomiczny i samodzielny, na koniec dnia powinien być zaimplementowany człowiek w procesie."

## 17. Bezpieczeństwo autonomicznych agentów - przypadek EchoLeak

Summary: Przypomnienie luki Zero-Click w Copilocie (EchoLeak) pokazuje, że nawet twórcy technologii mają problemy z bezpieczeństwem. Tym bardziej należy być ostrożnym z własnymi agentami budowanymi modnymi frameworkami LLM-owymi.

Podsumowania wypowiedzi prowadzących:
- Łukasz Kałużny: Przywołuje przykład luki EchoLeak jako ostrzeżenie, że jeśli duzi gracze mają problemy, to małe zespoły tym bardziej powinny być ostrożne.
- Szymon Warda: Zauważa że dokumentacja dotycząca bezpieczeństwa płatności się rozwija i jest coraz lepsza.

Najciekawsze cytaty:
1. Łukasz Kałużny: "Przypomnę lukę Zero-Click w Copilocie, nazwaną EchoLeak. To doskonały przykład, że jeśli twórcy technologii sobie z tym nie radzą, to co dopiero agent zbudowany modnym frameworkiem LLM-owym."
