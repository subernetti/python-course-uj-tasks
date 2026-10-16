# Zadanie 2.17
# Posortować wyrazy ze stringu line raz alfabetycznie, a raz pod względem długości. 
# Wskazówka: funkcja wbudowana sorted().

line = "Sortowanie Bardzo Proste Jest A Z C"
words = line.split()

alfabetycznie = sorted(words)
wedlug_dlugosci = sorted(words, key=len)

print(alfabetycznie)
print(wedlug_dlugosci)