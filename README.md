# Metoda tworzenia miar zastępowalności składników przy uwzględnieniu celu zamiany - wersja 1

## Wprowadzenie

W niniejszym opracowaniu rozważa się problem opracowania metody definiowania miary zastępowalności składników
spożywczych w przepisach kulinarnych zgodnej z wymaganiami zdefiniowanymi przez użytkownika. Zakłada się, że
zdefiniowanie jednej miary, która jednocześnie pokryłaby wszystkie możliwe wymagania jest niemożliwe, ponieważ składnik,
który w jednym zastosowaniu jest substytutem niebudzącym zastrzeżeń (np. zastępienie schabu polędwicą wieprzową przy
braku ograniczeń dietetycznych), w innym będzie nie do przyjęcia (np. zastępienie schabu polędwicą wieprzową w diecie
wegańskiej).

W przedstawionej wersji przyjęto następujące założenia:

* zamianie poddawany jest jeden składnik na raz, a nie grupa składników;
* wynikiem zamiany jest jeden składnik, a nie grupa składników;
* nie rozważa się ilości produktów;
* nie uwzględnia się przepisu, na potrzeby którego dokonywana jest zamiana;
* miara powinna być oferować użytkownikowi wyjaśnialność decyzji, w szczególności unikając złożonych modeli typu *czarna
  skrzynka* czy wykorzysytwania wektorów zanurzeń.

W toku prac zidentyfikowano kilka wymiarów, które mogą wpływać na zamienianie składników. Należy zaznaczyć, że nie jest
to lista wyczerpująca ani zakorzeniona w studiach literaturowych. Wymiary, poza wyjaśnieniem, opisane są też wprowadzaną
twardością ograniczenia. Wyróżnia się
*ograniczenie twarde* tzn. takie, którego naruszenie powoduje, że potencjalny subsytut jest nieprzydatny z punktu
widzenia użytkownika, np. zastąpienie schabu polędwicą wieprzową w diecie wegańskiej; oraz
*ograniczenie miękkie* tzn. takie, które może być lepiej lub gorzej spełnione, np. zastąpienie cukru białego miodem w
diecie cukrzycowej. Wskazuje się też czy dana cecha jest wyłącznie cechą składnika (*cecha własna*), czy cechą składnika
w kontekście przepisu (*cecha kontekstowa*).

* *Funkcja/właściwość* Niektóre składniki przepisów charakteryzują się specyficznymi cechami czy właściwościami, które
  muszą zostać zachowane podczas zamiany. Przykładowo *proszek do pieczenia* pełni zazwyczaj funkcję środka
  spulchniającego, która musi zostać zachowana podczas zamiany. Ograniczenie twarde; cecha kontekstowa.
* *Kluczowe właściwości organoleptyczne* Niektóre składniki wprowadzają konkretne właściwości organoleptyczne kluczowe z
  punktu widzenia niektórych przepisów. Przykładowo, w przepisie na *stek z tuńczyka* zastąpienie *polędwicy z
  tuńczyka* *fasolą z puszki*
  (bez dodatkowego procesu mającego na celu przerobienie fasoli) jest niedopuszczalne. Ograniczenie twarde; cecha
  kontekstowa.
* *Drugorzędne właściwości organoleptyczne* Zamiana powinna w miarę możliwości zachowywać smak, zapach całego przepisu
  itp. Ograniczenie miękkie; cecha kontekstowa.
* *Dopuszczalność* Proponowany składnik musi być akceptowalny dla konsumenta, np. zastąpienie schabu polędwicą wieprzową
  w diecie wegańskiej nie jest dopuszczalne. Ograniczenie twarde; cecha własna.
* *Preferencja dietetyczna* Wszyscy różnimy się preferencjami smakowymi, wyborami dietetycznymi itp. Przykładowo,
  fleksitarianie preferują niespożywanie mięsa, ale mięso nie jest dla nich składnikiem niedopuszczalnym. Ograniczenie
  miękkie; cecha własna.
* *Brak współwystępowania* Przypuszcza się, że produkty często występujące razem w przepisach nie są swoimi
  zastępnikami. Ograniczenie miękkie; cecha własna (ale wynikająca ze zbioru danych).
* *Współdzielony kontekst* Przypuszcza się, że produkty występujące często razem z takimi samymi zbiorami składników
  mogą być swoimi zastępnikami. Ograniczenie miękkie; cecha własna (ale wynikająca ze zbioru danych).
* *Wartości odżywcze* Sumaryczna wartość odżywcza przepisu powinna zostać zachowana. Ograniczenie miękkie; cecha
  własna (w ogólności cecha kontekstowa, ale w świetle przyjętych założeń o zamienianiu jednego składnika na raz staje
  się własna)
* *Dostępność* Składniki róznią się dostępnością sezonową i geograficzną. Ograniczenie miękkie; cecha własna (ale
  zależna od miejsca i czasu wykorzystania).
* *Kategoria* Przypuszcza się, że produkty z tej samej kategorii (np. mąki) są raczej lepszymi zastępnikami dla zadanego
  produktu niż produkty z zupełnie innej kategorii. Ograniczenie miękkie; cecha własna.
* *Nazwa* W przypadku składników nowoczesnych nazwa może wprost wskazywać czego jest to zastępnik (np. *wegański boczek*
  jako zastępnik *wędzonego boczku*). Niestety, należy zwrócić uwagę, że w przypadku składników tradycyjnych nazwa może
  być myląca (np. *mąka ziemniaczana* nie koniecznie dobrym zastępnikiem *mąki pszennej*). Ograniczenie miękkie; cecha
  własna.

Z punktu widzenia miary istotne są wyłącznie ograniczenia miękkie, ponieważ składniki niespełniające ograniczeń twardych
w ogóle nie powinny być rozważane jako możliwe zastępniki. Ponadto, ze względu na przyjęte założenia, na aktualnym
etapie mogą zostać uwzględnione wyłącznie cechy własne produktów. Pozostawia to następujące cechy: *Drugorzędne
właściwości organoleptyczne*, *Preferencja dietetyczna*, *Brak współwystępowania*, *Współdzielony kontekst*, *Wartości
odżywcze*, *Dostępność*, *Kategoria*, *Nazwa*.

W przedstawionym rozwiązaniu wykorzystano wyłącznie następujące cechy: *Preferencja dietetyczna*, *Wartości odżywcze*,
*Kategoria*. Pozostałe cechy zostały w bieżącej wersji pominięte z następujących powodów:

* *Drugorzędne właściwości organoleptyczne* Planowano integrację z FlavorDB, która póki co okazuje się niemożliwa ze
  względu na problemy z dostępnością usługi.
* *Brak współwystępowania*, *Współdzielony kontekst* Na obecnym etapie zbiór danych TASTEset nie jest powiazany z
  ontologią FoodOn.
* *Dostępność* Na wczesnym etapie projektu podjęto decyzję o całkowitym pominięciu tej cechy jako zbyt skomplikowanej do
  zamodelowania.
* *Nazwa* Ontologia FoodOn nie obfituje w nowoczesne produkty, które zyskałyby w ten sposób. Z drugiej strony
  porównywanie nazw wymaga zwykle dość skomplikowanych miar, co mogłoby stać w sprzeczności z założeniem o
  wyjaśnialności miary.

Przedstawiona metoda tworzenia miar nie jest zamknięta na wprowadzanie nowych cech i kolejne wersje mogą wykorzystywać
wymienione powyżej cechy.

## UTA

### Wprowadzenie do metody UTA

Jako bazę dla zaproponowanej metody tworzenia miar wykorzystano metodę wielokryterialnego wspomagania decyzji UTA [4].
Bardziej szczegółowe, a przystępnie napisane wprowadzenie do UTA można znaleźć w [5], poniżej natomiast przedstawiono
podsumowanie najważniejszych aspektów. Ze względu na spodziewane grono odbiorców raportu zapożycza się stosowane w
uczeniu masznowym pojęcia, m.in., *parametru* jako wartości liczbowej dobieranej automatycznie w procesie optymalizacji
oraz *hiperparametru* jako parametru konfiguracyjnego zwyczajowo ustawianego przez użytkownika. Należy podkreślić, że
nie są to terminy zwyczajowo stosowane w kontekście metod wielokryterialnego wspomagania decyzji.

UTA zakłada, że istnieje pewien zbiór obiektów (wariantów) opisanych cechami liczbowymi. Każda z cech może być albo
maksymalizowana albo minimalizowana (hiperparametr), znana jest też jej wartość najlepsza i najgorsza (hiperparamter). W
UTA cechy transformowane są za pomocą niemalejących/nierosnących, nieujemnych funkcji odcinkami liniowych, tworząc
tzw. *cząstkowe funkcje użyteczności*, przy czym liczba odcinków dla każdej z funkcji jest hiperparametrem, natomiast
wartości współczynników kierunkowych i wyrazów wolnych są parametrami. Dla kryterium maksymalizowanego funkcja jest
niemalejąca, natomiast dla kryterium minimalizowanego - nierosnąca.

Cząstkowe funkcje użyteczności są sumowane (po wszystkich cechach) do *globalnej funkcji użyteczności* `U`, przy czym
wprowadza się dodatkowy czynnik regularyzacyjny wymagający, aby globalna funkcja użyteczności dla szutcznego obiektu
składającego się wyłącznie z najgorszych wartości cech wynosiła 0, natomiast dla sztucznego obiektu składającego się
wyłącznie z najlepszych wartości cech wynosiła 1.

Zakłada się ponadto, że pomiędzy niektórymi obiektami znana jest relacja preporządku, pełniąca rolę odpowiednika zbioru
uczącego: dla dwóch obiektów `a`, `b` wiadomo albo, że `a` jest preferowany nad `b`, co powinno zostać odwzorowane przez
globalną funkcję użyteczności jako `U(a) > U(b)`, albo że są nierozróżnialne, co powinno zostać odwzorowane
jako `U(a) = U(b)`.

W odróżnieniu od metod uczenia maszynowego zamiast optymalizacji gradientowej stosuje się reprezentację jako problem
matematycznego programowania liniowego i rozwiązuje przy wykorzystaniu tzw. solwerów. Należy zaznaczyć, że nie jest to
reprezentacja w formie całkowitoliczbowego programowania liniowego i w związku z tym znalezienie rozwiązania odbywa się
w czasie wielomianowym.

Wynikiem działania UTA jest globalna funkcja użyteczności `U`, która definiuje preporządek na wszystkich rozważanych
wariantach: `a` jest preferowane nad `b` jeżeli `U(a) > U(b)` albo `a` jest nierozróżnialne z `b` jeżeli `U(a) = U(b)`.

### Implementacja - klasa `uta.RawUTA`

Konsultacja z prof. Miłoszem Kadzińskim wykazała, że nie ma ogólnie przyjętej, powszechnie używanej biblioteki metod
wspomagania decyzji w Pythonie. W związku z prostotą UTA podjęto decyzję o samodzielnej implementacji przy wykorzystaniu
solwera cvxpy [6]. Implementacja dostępna jest w klasie `uta.RawUTA` w pliku [uta/rawuta.py](uta/rawuta.py). Konstruktor
klasy `RawUTA` przyjmuje dwa argumenty:

* `features` typu `Sequence[Tuple[int, float, float]]` - Sekwencja (np. lista) opisująca hiperparametry cech w formie
  trójek, składających się kolejno z: liczby odcinków liniowych, wartości najgorszej, wartości najlepszej.
* `same_tier_is_equivalent` typu `bool` - Parametr konfiguracyjny wskazujący jak interpretować argumenty opisanej
  poniżej metody `add`.

Obiekt klasy `RawUTA` w ramach publicznego API oferuje trzy metody:

* Dwuargumentową metodę `add` dodającą informacje o znanej relacji preporządku o następujących argumentach:
    * `reference_ranking` typu `Sequence[Collection[Any]]`, stanowiące sekwencję kolekcji identyfikatorów obiektów.
      Obiekty z kolekcji `reference_ranking[i]` są preferowane nad obiektami z kolekcji `reference_ranking[j]` dla
      wszystkich `j>i`. Jeżeli `same_tier_is_equivalent` było ustawione na `True`, to obiekty w obrębie
      kolekcji `reference_ranking[i]` (dla każdego `i`) są uznawane za nierozróżnialne; w przeciwnym razie nie są
      dodawane żadne ograniczenia dotyczące par obiektów z tej samej kolekcji `reference_ranking[i]`.
    * `variants` typu `Mapping[Any, Sequence[float]]` stanowiące odwzorowanie między identyfikatorami obiektów używanymi
      w `reference_ranking`, a wartościami cech w tym samym porządku, który był użyty w arugmencie `features`
      konstruktora.

  Metodę `add` można wywoływać wielokrotnie w celu dodania kolejnych informacji o znanej relacji preporządku, przy czym
  należy zaznaczyć, że `add` polega na globalnej unikalności identyfikatorów w `reference_ranking`, tzn. w przypadku
  odwołania do obiektu z tym samym identyfikatorem w kolejnych wywołaniach `add` oczekuje się, że wartości w `variants`
  przypisane temu identyfikatorowi będą identyczne, a dodawane relacje spójne między sobą.
* Bezargumentową metodę `solve`, którą należy wywołać po wszystkich wywołaniach `add` w celu rozwiązania problemu
  programowania liniowego.
* Jednoargumenowej metody `U`, której jedyny argument to sekwencja wartości cech opisujących obiekt, dla którego ma być
  obliczona wartość globalnej funkcji użyteczności `U`. Zwracany jest obiekt typu `cp.Expression`, którego wartość
  liczbową można odczytać za pomocą pola `value`.

Testy jednostkowe oparte na [5], a zarazem przykłady użycia klasy `uta.RawUTA` znajdują się w
pliku [uta/test/test_rawuta.py](uta/test/test_rawuta.py).

### Implementacja - klasa `uta.UTA`

Klasa `uta.RawUTA` ma stosunkowo niewygodny interfejs. W związku z tym wprowadzono klasę `uta.UTA` zdefiniowaną w
pliku [uta/uta.py](uta/uta.py) oraz wykorzystywane przez nią klasy `uta.FeatureSet` oraz `uta.FeatureDescriptor`
zdefiniowane w pliku [uta/FeaturerSet.py](uta/FeaturerSet.py). `uta.FeatureDescriptor` to `dataclass`, której rolą jest
przechowywanie informacji pojedynczej cesze: nazwie (pole `name` typu `str`), liczbie odcinków w funkcji odcinkami
liniowej (pole `n` typu `int`), wartości najgorszej (pole `worst` typu `float`) oraz najlepszej (pole `best`
typu `float`).

`uta.FeatureSet` to klasa abstrakcyjna, którą klasa `uta.UTA` wykorzystuje do pozyskiwania wartości cech. Głównym
elementem klasy jest metoda `compute`, która przyjmuje jako jedyny argument identyfikator obiektu, a zwraca listę cech
liczbowych typu `List[float]`. Ta metoda domyślnie rzuca wyjątek `NotImplemented` i musi zostać zaimplementowana w
klasach pochodnych. `uta.FeatureSet` udostępnia tez jedno pole `descriptors` typu `List[FeatureDescriptor]`, które klasa
pochodna powinna wypełnić listą obiektów typu `uta.FeatureDescriptor` o identycznej długości co lista wartości zwracana
przez `compute`. W końcu udostępniona jest metoda `compute_batch` która przyjmuje jako argument listę identyfikatorów, a
zwraca listę list cech `List[List[float]]`, domyślnie wywołując `compute` dla każdego identyfikatora i łącząc zwracane
listy cech w jedną listę dwuwymiarową. Implementacje mogą przeciążyć `compute_batch` jeżeli mają możliwość bardziej
efektywnego jednoczesnego obliczania cech dla wielu obiektów na raz, np. przez zapytanie SPARQL wykorzystujące słowo
kluczowe `VALUES`.

Klasa `uta.UTA` ma API bardzo zbliżone do tego oferowanego przez `uta.RawUTA` z następującymi różnicami:

* Argument `features` konstruktora jest typu `List[FeatureSet]`, zostaje zapisany jako pole `features`.
* Metoda `add` nie ma argumentu `variants`, który nie jest potrzebny, ponieważ obliczanie wartości cech jest
  odpowiedzialnością obiektów z pola `features`.
* Metoda `U` przyjmuje identyfikator lub listę identyfikatorów obiektów, których cechy są obliczane za obiektów z
  pola `features`. Zwracana jest wartość liczbowa funkcji `U` jeżeli przekazano jeden identyfikator lub lista wartości
  liczbowych funkcji `U` jeżeli przekazano listę identyfikatorów.

### Implementacja - klasa `uta.RelativeUTA`

Zaobserwowano, że założenie o istnieniu jednego, globalnego rankingu składników może nie być adekwatnym modelem dla
miary zastępowalności składników. Wprowadzono w związku z tym pewną modyfikację API klasy `uta.UTA` oraz dodatkową,
specjalizowaną implementację klasy `uta.FeatureSet` nazwaną `uta.RelativeFeatureSet`. Obie klasy są zaimplementowane w
pliku [uta/RelativeUTA.py](uta/RelativeUTA.py).

`uta.RelativeFeatureSet` przyjmuje jako argument konstruktora obiekt klasy `uta.FeatureSet` oraz poza standardowym
interfejsem `uta.FeatureSet` udostępnia pole `reference`, które domyślnie ma wartość `None`, a które musi zostać
ustawione na identyfikator obiektu przed każdym wywołaniem metody `compute` lub `compute_batch`.
`uta.RelativeFeatureSet` zamiast obliczać wartości cech w sposób bezwzględny (np. wartość energetyczna danego składnika
wyrażona w kcal), oblicza jako cechy wartość bezwzględną różnic między cechami obiektu przekazanego jako argument do
funkcji `compute` oraz obiektu, którego identyfikator jest w polu `reference`. Takie podejście umożliwia implementację
opisanej we wstępie koncepcji zachowywania wartości odżywczej. Zakłada się, że brak różnicy jest zawsze najlepszą
możliwą wartością.

`uta.RelativeUTA` jest owinięciem (ang. wrapper) klasy `uta.UTA` z następującymi różnicami:

* Argument konstruktora `features` jest przekazywany bezpośrednio w górę, natomiast `same_tier_is_equivalent` jest
  zawsze ustawione na `False`.
* Metoda `add` przyjmuje trzy argumenty: identyfikator obiektu referencyjnego `reference`, listę identyfikatorów
  obiektów lepszych od referencyjnego `better` oraz listę obiektów gorszych `worse`. `reference` jest ustawione jako
  wartość pola `referencje` wszystkich obiektów klasy `uta.RelativeFeatureSet` na liście `features`, a pozostałe dwa
  argumenty są łączone jako dwuwymiarowa lista `[better, worse]` i przekazywane do metody `uta.UTA.add`.
* Metoda `U` przyjmuje jako pierwszy argument `reference` identyfikator obiektu referencyjnego, który jest
  wykorzystywany tak samo jak w metodzie `add`. Drugi argument i wartość zwracana mają identyczną semantykę jak
  w `uta.UTA.U`.
* Wprowadzona jest pomocnicza metoda `recommend`, która przyjmuje dwa argumenty: `reference` o semantyce j.w.
  oraz `variants` stanowiący kolekcję identyfikatorów. Zwracana jest para typu `Tuple[Any, float]`, której pierwszy
  element to element kolekcji `variants` dla którego wartość funkcji `U` jest największa (przy ustalonym `reference`), a
  drugi arugment to wartość funkcji `U`. Ta funkcja pełni rolę rekomendera, który dla zadanego obiektu `reference` ma
  wybrać najlepszą alternatywę z kolekcji `variants`.

Testy jednostkowe i zarazem przykłady użycia znajdują się w
pliku [uta/test/test_RelativeUTA.py](uta/test/test_RelativeUTA.py). Testy integracyjne wraz z mniej abstrakcyjnymi
przykładami użycia znajdują się w plikach [test_diabetes.py](test_diabetes.py), [test_glutenfree.py](test_glutenfree.py)
oraz [test_vegetarian.py](test_vegetarian.py).

## Reprezentacja wiedzy

### Wykorzystane grafy wiedzy

Zakłada się, że każdy rozważany składnik jest identyfikowany za pomocą identyfikatorów (IRI) encji z grafu wiedzy. W
bieżącej wersji przyjęto, że centralną częścią grafu wiedzy jest ontologia FoodOn i składniki są identyfikowane za
pomocą IRI z jej przestrzeni nazw. Wczytywanie FoodOn zostało zaimplementowane w postaci metody `foodon` w
pliku [helpers.py](helpers.py), która nie przyjmuje argumentów, a zwraca obiekt klasy `owlready2.Ontology` biblioteki
owlready2 [3] zawierający wczytaną ontologię. FoodOn oraz importowane przez niego ontologie są domyślnie pobierane z
Internetu, natomiast dla zwiększenia efektywności wykorzystywany jest wbudowany w bibliotekę owlready2 mechanizm
budowania pamięci podręcznej w katalogu `ontologies`.

Dodatkowo z FoodOn powiązano [WikiFCD](https://wikifcd.wiki.opencura.com/), graf wiedzy integrujący tabele wartości
odżwyczych pochodzące z różnych źródeł do współnej reprezentacji. Mimo początkowych nadziei, że WikiFCD jest mocno
zintegrowane z FoodOn okazało się, że tak nie jest i jednocześnie a) wiele składników w WikiFCD nie jest oznaczonych
identyfikatorami z FoodOn; b) wiele składników z FoodOn występuje w WikiFCD, ale nie ma przypisanych żadnych informacji
o wartościach odżywczych.

W pliku [wikifcd2foodon.json](wikifcd2foodon.json) znajdują się wszystkie powiązania między encjami WikiFCD oraz FoodOn,
wygenerowane 29.06.2022 za pomocą następującego zapytania SPARQL zadanego do
końcówki [https://wikifcd.wiki.opencura.com/query/](https://wikifcd.wiki.opencura.com/query/):

```sparql    
    PREFIX p: <http://wikifcd.wiki.opencura.com/prop/>    
    PREFIX ps: <http://wikifcd.wiki.opencura.com/prop/statement/> 
    SELECT *    WHERE {
        ?item p:P309/ps:P309 ?foodon.
    }
```

Łącznie jest 1145 powiązań, podczas gdy w FoodOn samych podklas klasy *food product* `FOODON_00001002` jest 13989 (patrz
kod w załączniku I). Co więcej, jak wspomniano wcześniej, niektóre z istniejących powiązań są bezużyteczne do zbierania
informacji o wartościach odżywczych. Przykładowo, encja *sorghum kernel* `FOODON_03309978` jest odwzorowana
w [http://wikifcd.wiki.opencura.com/entity/Q569378](http://wikifcd.wiki.opencura.com/entity/Q569378). Niestety, WikiFCD
nie oferuje żadnych informacji o wartościach odżywczych dla tej encji.

Żeby rozwiązać oba problemy zaproponowano tymczasowe rozwiązanie polegające na ręcznym odwzorowywaniu identyfikatorów
FoodOn i WikiFCD w formie pliku tekstowego [wikifcd2foodon.tsv](wikifcd2foodon.tsv). Podczas wczytywania pliku linie
puste, linie składające się wyłącznie z białych znaków oraz linie, w których pierwszy nie-biały znak to `#` są
ignorowane. Pozostałe linie dzielone są po białych znakach i uwzględniane są wyłącznie pierwsze dwa elementy wynikające
z podziału. Oczekuje się, że pierwszy element będzie identyfikatorem z WikiFCD, albo w formie pełnego IRI, albo w formie
wyłącznie części lokalnej (ang. local part, [1]), w tej sytuacji jest uzupełniany o
prefiks `http://wikifcd.wiki.opencura.com/entity/` do utworzenia pełnego IRI. Analogicznie, dla drugiego elementu
oczekuje się, że jest to albo pełne IRI encji z FoodOn, albo część lokalna, która zostaje uzupełniona
prefiksem `http://purl.obolibrary.org/obo/`. Odwzorowania w [wikifcd2foodon.tsv](wikifcd2foodon.tsv) mają priorytet nad
tymi zgromadzonymi w [wikifcd2foodon.json](wikifcd2foodon.json), tzn. w razie odwzorowania encji z FoodOn w obu plikach
uwzględniane jest to z `[wikifcd2foodon.tsv](wikifcd2foodon.tsv).

Integracja z WikiFCD została zaimplementowana w formie klasy `WikiFCD` w pliku [WikiFCD.py](WikiFCD.py). Wczytywanie
odwzorowań z plików odbywa się w bezparametrowym konstruktorze klasy, natomiast pobieranie informacji z WikiFCD odbywa
się za pomocą operatora `[]`, którego jedynym argumentem jest łańcuch znaków (`str`) stanowiący pełne IRI encji z
FoodOn. Zwracana wartość to albo `None` jeżeli nie znaleziono odwzorowania dla encji i w związku z tym nie można pobrać
danych z `WikiFCD`, albo para typu `Tuple[rdflib.URIRef, rdflib.Graph]`, gdzie pierwszy element pary to IRI z WikiFCD
odczytany z odwzorowań wczytanych w konstruktorze, a przedstawiony jako obiekt klasy `URIRef` biblioteki rdflib [2], a
drugi element to graf RDF zawierający fragment WikiFCD opisujący encję, której IRI zostało zwrócone jako pierwszy
element pary.

Klasa `WikiFCD` nie operuje na zrzucie WikiFCD, zamiast tego komunikuje się bezpośrednio z kopią WikiFCD dostępną w
Internecie. Dla zwiększenia efektywności klasa `WikiFCD` tworzy pamięć podręczną zawierającą pobrane fragmenty grafów,
domyślnie znajdującą się w katalogu `wikifcd`, który jest tworzony w konstruktorze. Nie zaimplementowano mechanizmu
usuwania niepotrzebnych bądź nieaktualnych wpisów z pamięci podręcznej. Pamięć podręczna zorganizowana jest w formie
nieskompresowanych plików w formacie Turtle (z rozszerzeniem `ttl`), o nazwach odpowiadających częściom lokalnym
identyfikatorom z WikiFCD.

Na dzień 11.07.2022 ostatni udany dostęp do Internetowej kopii WikiFCD był 04.07.2022, od tego czasu zwracany jest kod
błędu HTTP 503 Service Temporarily Unavailable.

### Transformacja do postaci wektora liczbowego

## Bibliografia

[1]: https://www.w3.org/TR/turtle/

[2]: https://rdflib.readthedocs.io/

[3]: https://owlready2.readthedocs.io/

[4]: Jacquet-Lagréze, E. and J. Siskos, “Assessing a Set of Additive Utility Functions for Multicriteria Decision
Making: The UTA Method,” Eur J of Oper Res, 10(2), 1982, 151-164.

[5]: http://www.cs.put.poznan.pl/imaslowska/wd/lab9/Metoda%20UTA.pdf

[6]: https://www.cvxpy.org/

## Załącznik I: Zliczanie podklas klasy `FOODON_00001002`

```python
from helpers import foodon

queue = [foodon().search_one(iri="http://purl.obolibrary.org/obo/FOODON_00001002")]
visited = set()
while len(queue) > 0:
    e = queue.pop(0)
    if e not in visited:
        visited.add(e)
        queue += e.descendants()
print("Visited", len(visited))
```