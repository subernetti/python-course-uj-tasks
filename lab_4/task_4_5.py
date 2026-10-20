# Zadanie 4.5
# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na 
# liście od numeru left do right włącznie. Lista jest modyfikowana w miejscu (in place). 
# Rozważyć wersję iteracyjną i rekurencyjną.

def odwracanieIter(L: list, left: int, right: int):
    if not isinstance(L, list):
        raise TypeError("Pierwszy argument musi byc lista.")
    if not isinstance(left, int) or not isinstance(right, int):
        raise TypeError("Drugi i trzeci argument musza byc liczbami calkowitymi")
    
    n = len(L)
    if not 0 <= left <= right <= n:
        raise TypeError("Bledny zakres indeksow: indeksy musza miescic sie pomiedzy 0 a dlugosc_listy - 1")
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def odwracanieRek(L: list , left: int, right: int):
    if not 0 <= left < len(L) or not 0 <= right < len(L):
        raise TypeError("Blad zakresu indeksow")

    if left >= right:
        return
    
    L[left], L[right] = L[right], L[left]
    return odwracanieRek(L, left + 1, right - 1)



L1 = [1,2,3,4,5]
L2 = [0,1,2,3,4]

odwracanieIter(L1, 0, 4)
odwracanieRek(L2, 1, 3) 

assert L1 == [5,4,3,2,1]
assert L2 == [0,3,2,1,4]
