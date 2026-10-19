# Zadanie 3.1
# Czy podany kod jest poprawny skladniowo w Pythonie? Jeśli nie, to dlaczego?

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

for i in "axby": if ord(i) < 100: print (i)

for i in "axby": print (ord(i) if ord(i) < 100 else i)

# Odpowiedz:
# Błąd składniowy pojawia się w 10 linijce kodu. Dla operacji "for" po znaku dwukropka 
# nie moze znaleźć się zadna operacja złozona (tutaj: if) - chyba, ze "if" zostałoby przeniesione
# do dolnej lini wraz z tabulacją, wtedy byłoby juz poprawnie.
# Potwierdza to błąd wyświetlany po próbie uruchomionego programu:
### 
# (...), line 10
#    for i in "axby": if ord(i) < 100: print (i)
#                     ^^
#   SyntaxError: invalid syntax
# ###