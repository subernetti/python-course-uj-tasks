# Zadanie 2.19
# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy 
# zbudować string z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe 
# będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().

L = [7, 24, 123, 5, 89]

wynik = ''.join(str(liczba).zfill(3) for liczba in L)

print(wynik)