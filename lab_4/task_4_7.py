# Zadanie 4.7
# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, 
# a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. Napisać funkcję 
# flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. 
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, 
# wykonać przez isinstance(item, (list, tuple)).

# sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
# print(flatten(sequence))   # [1,2,3,4,5,6,7,8,9]

def flatten(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Wejscie musi byc lista lub krotka.")
    total = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total.extend(flatten(item))
        else:
            total.append(item)
    return total

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
assert flatten(sequence) == [1,2,3,4,5,6,7,8,9]