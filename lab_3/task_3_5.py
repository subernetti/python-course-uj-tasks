# Zadanie 3.5
# Napisać program rysujący "miarkę" o zadanej długości. Długość miarki (x) 
# ma być zapisana w osobnej zmiennej jako parametr. Należy prawidłowo obsłużyć 
# liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). 
# Należy zbudować pełny string, a potem go wypisać.

#|....|....|....|....|....|....|....|....|....|....|....|....|   (x = 12)
#0    1    2    3    4    5    6    7    8    9   10   11   12

x = input("Podaj rozmiar miarki (liczba dodatnia calkowita): ")
try: 
    x = int(x)
    if x <= 0:
        raise ValueError
except ValueError:
    print("Błąd! Podano błędny rozmiar miarki.")
    exit()

miarkaKropki = "|"
miarkaLiczby = "0"

for i in range(1, x + 1):
    miarkaKropki += "....|"
    miarkaLiczby += f"{i:>5}"  

pelnyString = miarkaKropki + "\n" + miarkaLiczby
print(pelnyString)