# Zadanie 4.4
# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(n):
    if n < 1:
        raise ValueError("Błąd: Wpisz liczbe całkowitą dodatnią.")
    result = 0

    if(n == 1):
        return 0
    if(n == 2):
        return 1
    
    a = 0 
    b = 1
    for _ in range (3, n + 1):
        a, b = b, a + b
    
    return b

assert fibonacci(1) == 0
assert fibonacci(2) == 1
assert fibonacci(3) == 1
assert fibonacci(4) == 2
assert fibonacci(5) == 3
assert fibonacci(6) == 5

        