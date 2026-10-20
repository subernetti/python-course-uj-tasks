# Zadanie 4.6
# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która 
# może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, 
# czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

def sum_seq(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Wejscie musi byc lista lub krotka.")
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        elif isinstance(item, (float, int)) and not isinstance(item, bool):
            total += item
        else:
            raise TypeError(f"Nieprawidłowy element w sekwencji: {item!r} (typ {type(item).__name__}")
    return total


seq = [1, 2, [3, 4], (5, [6, 7]), 8]

assert sum_seq(seq) == 36
print(sum_seq(seq))