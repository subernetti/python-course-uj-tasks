# Zadanie 4.3
# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def factorial(n):
    if n < 1:
        raise ValueError("Podane wejscie musi byc liczba naturalna inna od zera!")
    result = 1
    for i in range(1, n+1):
        result = result * i

    return result

assert factorial(1) == 1 
assert factorial(2) == 2
assert factorial(3) == 6

print(factorial(4))