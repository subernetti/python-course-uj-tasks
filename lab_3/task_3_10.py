# Zadanie 3.10
# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) 
# na liczby arabskie (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący 
# całą liczbę [funkcja roman2int()].

def roman2int(input: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    n = len(input)

    for i in range(n):
        current_val = roman_map[input[i]]

        if i + 1 < n and current_val < roman_map[input[i + 1]]:
            total -= current_val
        else: 
            total += current_val

    return total

assert roman2int("IV") == 4
assert roman2int("XI") == 11
assert roman2int("LVIII") == 58
assert roman2int("MCMXCIV") == 1994

print(roman2int("IV"))
print(roman2int("VI"))
print(roman2int("V"))

