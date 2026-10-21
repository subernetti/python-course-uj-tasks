# Zadanie 5.2
# Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. 
# Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik]. 
# Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions. 
# Można wykorzystać funkcję fractions.gcd() [Py2, zwraca liczby dodatnie lub ujemne] lub math.gcd() 
# [Py3, zwraca liczby nieujemne] implementującą algorytm Euklidesa.

#from fractions import gcd   # Py2
from math import gcd   # Py3

def add_frac(frac1, frac2): pass        # frac1 + frac2

def sub_frac(frac1, frac2): pass        # frac1 - frac2

def mul_frac(frac1, frac2): pass        # frac1 * frac2

def div_frac(frac1, frac2): pass        # frac1 / frac2

def is_positive(frac): pass             # bool, czy dodatni

def is_zero(frac): pass                 # bool, typu [0, x]

def cmp_frac(frac1, frac2): pass        # -1 | 0 | +1

def frac2float(frac): pass              # konwersja do float

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

    def test_sub_frac(self): pass

    def test_mul_frac(self): pass

    def test_div_frac(self): pass

    def test_is_positive(self): pass

    def test_is_zero(self): pass

    def test_cmp_frac(self): pass

    def test_frac2float(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy