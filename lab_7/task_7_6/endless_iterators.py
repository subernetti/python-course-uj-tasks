# Zadanie 7.6
# Stworzyć następujące iteratory nieskończone:
# (a) zwracający 0, 1, 0, 1, 0, 1, ...,
# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].

import random

# (a) 
def endless_zeros_and_ones():
    val = 0
    while True:
        yield val
        val = 1 - val 


# (b) 
def endless_random_directions():
    directions = ("N", "E", "S", "W")
    while True:
        yield random.choice(directions)


# (c) 
def endless_weekdays():
    day = 0
    while True:
        yield day
        day = (day + 1) % 7  

import itertools

print("Podpunkt (a):", list(itertools.islice(endless_zeros_and_ones(), 10)))

print("Podpunkt (b):", list(itertools.islice(endless_random_directions(), 10)))

print("Podpunkt (c):", list(itertools.islice(endless_weekdays(), 16)))

    