# Zadanie 2.12
# Zbudować string stworzony z pierwszych znaków wyrazów ze stringu line. 
# Zbudować napis stworzony z ostatnich znaków wyrazów ze stringu line.

line = "Ala ma kota"

pierwsze = "".join(word[0] for word in line.split())
ostatnie = "".join(word[-1] for word in line.split())

print(pierwsze)
print(ostatnie)