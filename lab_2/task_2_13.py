# Zadanie 2.13
# Znaleźć łączną długość wyrazów w stringu line. Wskazówka: można skorzystać z funkcji sum().

line = "Ala ma kota"

dlugosc = sum(len(word) for word in line.split())
print(dlugosc)