# Zadanie 3.3
# Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3. Podać dwa rozwiązania, 
# jedno z pętlą for, drugie z pętlą while.

# Wersja z for
for i in range(31): print(i if i%3 else "")

# Inna wersja z for
for i in range(31):
    if(i%3 != 0): print(i)

# Wersja z while
j = 0
while j < 31:
    if(j%3 != 0): print(j)
    j += 1
    