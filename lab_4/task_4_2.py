# Zadanie 4.2 
# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które 
# zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika o dane, tylko 
# korzystać z argumentów.

def make_ruler(n): 
    n = int(n)
    if n <= 0:
        raise ValueError("Błąd! Rozmiar miarki musi być dodatnią liczbą całkowitą.")

    miarkaKropki = "|"
    miarkaLiczby = "0"

    for i in range(1, n + 1):
        miarkaKropki += "....|"
        miarkaLiczby += f"{i:>5}"  

    pelnyString = miarkaKropki + "\n" + miarkaLiczby
    return pelnyString

def make_grid(rows, cols): 
    cols = int(cols)
    rows = int(rows)
    if cols < 1 or rows < 1:
        raise ValueError("Błąd! Wymiary muszą być dodatnimi liczbami całkowitymi.")
    
    pozioma = "+" + ("---+" * cols)
    pionowa = "|" + ("   |" * cols)

    wynik = (pozioma + "\n" + pionowa + "\n") * rows + pozioma

    return wynik

try:
    print(make_ruler(-1))
except ValueError as e:
    print(f"Złapano oczekiwany błąd: {e}")

try:
    print(make_grid(-1, -1))
except ValueError as e:
    print(f"Złapano oczekiwany błąd: {e}")

print(make_ruler(11))
print(make_grid(3,4))

