# Zadanie 3.9
# Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. 
# Znaleźć listę zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja 
# [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].

base_seq = [[],[4],(1,2),[3,4],(5,6,7)]
result_seq = []

for sub_seq in base_seq:
    result_seq.append(sum(sub_seq))

assert result_seq == [0,4,3,7,18]
print(result_seq)
