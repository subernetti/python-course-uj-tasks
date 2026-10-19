# Zadanie 3.6
# Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, 
# a potem go wypisać. Liczby kratek w wierszach (y) i kolumnach (x) mają być zapisane w osobnych 
# zmiennych jako parametry. Przykładowy prostokąt składający się 2 × 4 pól ma postać:

#+---+---+---+---+   (x = 4, y = 2)
#|   |   |   |   |
#+---+---+---+---+
#|   |   |   |   | 
#+---+---+---+---+

x = input("Podaj dlugosc prostokata: ")
y = input("Podaj szerokosc prostokata: ")

try: 
    x = int(x)
    y = int(y)
    if x < 1 or y < 1:
        raise ValueError
except ValueError:
    print("Błąd! Rozmiary muszą być dodatnimi liczbami całkowitymi.")
    exit()

pozioma = "+" + ("---+" * x)
pionowa = "|" + ("   |" * x)

wynik = (pozioma + "\n" + pionowa + "\n") * y + pozioma

print(wynik)