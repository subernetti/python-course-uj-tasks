# Zadanie 3.2 
# Co jest złego w kodzie:

L = [3, 5, 4] ; L = L.sort() 
# .sort() co prawda sortuje, acz jako wynik przyjmuje None, przez co zmienna L nie będzie
# posortowaną tablicą lecz przyjmnie wartość None

x, y = 1, 2, 3 
# Nie mozna przypisać trzech wartości w taki sposób do dwóch zmiennych 
# ValueError: too many values to unpack (expected 2)

X = 1, 2, 3 ; X[1] = 4
# Zmienna X jest krotką, przez co jest niemutowalna - nie mozna modyfikowac jej elementow
# TypeError: 'tuple' object does not support item assignment

X = [1, 2, 3] ; X[3] = 4
# Odwołanie do czwartej komórki listy, która nie istnieje
# IndexError: list assignment index out of range

X = "abc" ; X.append("d")
# Stringi nie posiadają metody ".append()" 
# AttributeError: 'str' object has no attribute 'append'

L = list(map(pow, range(8)))
# Funkcja pow() wymaga co najmniej dwóch argumentów, tutaj natomiast
# nie otrzymuje ona tylu ile trzeba
# TypeError: pow() missing required argument 'exp' (pos 2)
