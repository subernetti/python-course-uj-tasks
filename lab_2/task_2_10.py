# Zadanie 2.10
# Mamy dany string wielowierszowy line. Podać sposób obliczenia liczby wyrazów w stringu. 
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami 
# (spacja, tabulacja, newline).

def count_words(text: str) -> int:
    return(len(text.split()))

test_string = "More is Less, Less is More"

print(count_words(test_string))