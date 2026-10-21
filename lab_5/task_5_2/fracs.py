# Zadanie 5.2
# Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. 
# Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik]. 
# Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions. 
# Można wykorzystać funkcję fractions.gcd() [Py2, zwraca liczby dodatnie lub ujemne] lub math.gcd() 
# [Py3, zwraca liczby nieujemne] implementującą algorytm Euklidesa.

#from fractions import gcd   # Py2
from math import gcd   # Py3

# Ujednolicenie konwencji ((-1, 2) zamiast (1,-2))
def _simplify(frac1, frac2):
    if(frac2 == 0):
        raise ZeroDivisionError("Mianownik w ulamku nie moze byc rowny zeru.")
    
    if(frac2 < 0):
        frac1 = -frac1
        frac2 = -frac2
    
    x = gcd(frac1, frac2)
    return [frac1 // x, frac2 // x]

# Dodatkowa obsluga bledow
def _validate_input(frac):
    if not (isinstance(frac, (list, tuple)) and len(frac) == 2):
        raise ValueError("Ulamek musi byc list/tuple o rozmiarze 2.")
    
    if not (isinstance(frac[0], int) and isinstance(frac[1], int)):
        raise TypeError("Licznik i mianownik to musza byc liczby calkowite.")
    
    if isinstance(frac[0], bool) or isinstance(frac[1], bool):
        raise TypeError("Licznik/mianownik nie moze byc typu <bool>.")
    
    if frac[1] == 0:
        raise ZeroDivisionError("Nie wolno dzielic przez zero.")


def add_frac(frac1, frac2):         # frac1 + frac2
    _validate_input(frac1)
    _validate_input(frac2)
    numerator = frac1[0] * frac2[1] + frac1[1] * frac2[0]
    denominator = frac1[1] * frac2[1]
    return _simplify(numerator, denominator)

def sub_frac(frac1, frac2):         # frac1 - frac2
    _validate_input(frac1)
    _validate_input(frac2)
    numerator = frac1[0] * frac2[1] - frac1[1] * frac2[0]
    denominator = frac1[1] * frac2[1]
    return _simplify(numerator, denominator)


def mul_frac(frac1, frac2):         # frac1 * frac2
    _validate_input(frac1)
    _validate_input(frac2)
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    return _simplify(numerator, denominator)

def div_frac(frac1, frac2):         # frac1 / frac2
    _validate_input(frac1)
    _validate_input(frac2)
    numerator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]
    return _simplify(numerator, denominator)


def is_positive(frac):              # bool, czy dodatni
    _validate_input(frac)
    return (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0)

def is_zero(frac):                  # bool, typu [0, x]
    _validate_input(frac)
    return frac[0] == 0


def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    _validate_input(frac1)
    _validate_input(frac2)
    diff = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    if (frac1[1] * frac2[1]) < 0:
        diff = -diff
    if diff > 0:
        return 1
    elif diff < 0:
        return -1
    return 0

def frac2float(frac):               # konwersja do float
    _validate_input(frac)
    return frac[0] / frac[1]

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-1, 2], [1, 2]), self.zero)
        self.assertEqual(add_frac([1, -2], [1, 3]), [-1, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 2], [1, 2]), self.zero)
        self.assertEqual(sub_frac([1, 3], [1, 2]), [-1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [2, 3]), [1, 3])
        self.assertEqual(mul_frac([-1, 2], [-2, 3]), [1, 3])
        self.assertEqual(mul_frac([3, 4], self.zero), self.zero)

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 4]), [2, 1])
        self.assertEqual(div_frac([1, 2], [-1, 4]), [-2, 1])
        with self.assertRaises(ZeroDivisionError):
            div_frac([1, 2], self.zero)

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertTrue(is_positive([-1, -2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([1, -2]))
        self.assertFalse(is_positive(self.zero))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertTrue(is_zero([0, -5]))
        self.assertFalse(is_zero([1, 2]))
        self.assertFalse(is_zero([-3, 4]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([-1, 2], [1, -2]), 0)
        self.assertEqual(cmp_frac([-1, 2], [1, 2]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([-1, 4]), -0.25)
        self.assertEqual(frac2float(self.zero), 0.0)

    def test_invalid_input(self):
        with self.assertRaises(ZeroDivisionError):
            add_frac([1, 0], [1, 2])
        with self.assertRaises(TypeError):
            add_frac([1.5, 2], [1, 2])
        with self.assertRaises(TypeError):
            add_frac([True, 2], [1, 2])
        with self.assertRaises(ValueError):
            add_frac([1], [1, 2])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy