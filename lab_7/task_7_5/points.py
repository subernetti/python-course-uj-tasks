# Zadanie 6.2
# W pliku points.py zdefiniować klasę Point wraz z potrzebnymi metodami. Punkty są traktowane 
# jak wektory zaczepione w początku układu współrzędnych, o końcu w położeniu (x, y). Napisać kod 
# testujący moduł points.

import math as mt # do uzycia pierwiastka kwadratowego sqrt()

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
        return(f"({self.x}, {self.y})")

    def __repr__(self):         # zwraca string "Point(x, y)"
        return(f"Point({self.x}, {self.y})")

    def __eq__(self, other):    # obsługa point1 == point2
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        if not isinstance(other, Point):
            return False
        return self.x != other.x or self.y != other.y

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        result_Point = Point(None, None)
        result_Point.x = self.x + other.x
        result_Point.y = self.y + other.y
        return ((result_Point))

    def __sub__(self, other):   # v1 - v2
        result_Point = Point(None, None)
        result_Point.x = self.x - other.x
        result_Point.y = self.y - other.y
        return ((result_Point))

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return mt.sqrt(self.x * self.x + self.y * self.y)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points


import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(3, 4)
        self.p3 = Point(1, 2)
        self.origin = Point(0, 0)

    def test_str(self):
        self.assertEqual(str(self.p1), "(1, 2)")
        self.assertEqual(str(Point(-3, 5)), "(-3, 5)")

    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(1, 2)")
        self.assertEqual(repr(Point(-3, 5)), "Point(-3, 5)")

    def test_eq(self):
        self.assertTrue(self.p1 == self.p3)
        self.assertFalse(self.p1 == self.p2)
        self.assertFalse(self.p1 == (1, 2))  # porównanie z innym typem

    def test_ne(self):
        self.assertTrue(self.p1 != self.p2)
        self.assertFalse(self.p1 != self.p3)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(4, 6))
        self.assertEqual(self.p1 + self.origin, self.p1)
        self.assertEqual(Point(-1, 5) + Point(1, -5), self.origin)

    def test_sub(self):
        self.assertEqual(self.p2 - self.p1, Point(2, 2))
        self.assertEqual(self.p1 - self.p2, Point(-2, -2))
        self.assertEqual(self.p1 - self.p1, self.origin)

    def test_mul(self):  # iloczyn skalarny
        # 1*3 + 2*4 = 3 + 8 = 11
        self.assertEqual(self.p1 * self.p2, 11)
        # Wektory prostopadłe: iloczyn skalarny = 0
        self.assertEqual(Point(1, 0) * Point(0, 1), 0)

    def test_cross(self):  # iloczyn wektorowy 2D
        # 1*4 - 2*3 = 4 - 6 = -2
        self.assertEqual(self.p1.cross(self.p2), -2)
        # 3*2 - 4*1 = 6 - 4 = 2 (antysymetria)
        self.assertEqual(self.p2.cross(self.p1), 2)
        # Wektory równoległe: iloczyn wektorowy = 0
        self.assertEqual(Point(2, 4).cross(Point(1, 2)), 0)

    def test_length(self):
        self.assertEqual(self.origin.length(), 0.0)
        self.assertEqual(self.p2.length(), 5.0)  # trójkąt 3-4-5
        self.assertAlmostEqual(Point(1, 1).length(), mt.sqrt(2))

    def test_hash(self):
        # Sprawdzenie, czy punkt może być kluczem w słowniku / elementem zbioru
        s = {self.p1, self.p2}
        self.assertIn(self.p3, s)
        self.assertEqual(len(s), 2)


if __name__ == "__main__":
    unittest.main()