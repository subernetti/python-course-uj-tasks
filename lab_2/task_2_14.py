# Zadanie 2.14
# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w stringu line.

line = "Kot ma Ale ale Ala nie ma kotkow"
words = line.split()

najdluzszy = max(words, key=len)
dlugosc = len(najdluzszy)

print(najdluzszy)
print(dlugosc)