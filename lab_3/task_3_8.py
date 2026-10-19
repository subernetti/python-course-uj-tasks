# Zadanie 3.8
# Dla dwóch sekwencji liczb lub znaków znaleźć:
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

A = [1,2,2,3]
B = [2,3,4]

A = set(A)
B = set(B)

punkt_A = list(A & B)
punkt_B = list(A | B)

assert punkt_A == [2,3]
assert punkt_B == [1,2,3,4]

print(f"Podpunkt a) {punkt_A}")
print(f"Podpunkt b) {punkt_B}")

