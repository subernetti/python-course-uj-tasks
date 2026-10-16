# Zadanie 2.15
# Na liście L znajdują się liczby całkowite dodatnie. Stworzyć string będący ciągiem 
# cyfr kolejnych liczb z listy L.

L = [1, 2, 3, 0]

wynik = "".join(str(liczba) for liczba in L)
print(wynik)