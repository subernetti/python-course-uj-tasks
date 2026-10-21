# Zadanie 6.3 
# W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami. Prostokąt 
# jest określony przez podanie dwóch wierzchołków, lewego dolnego i prawego górnego. Boki 
# prostokąta są równoległe do osi układu współrzędnych. Napisać kod testujący moduł rectangles.

from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Wymagane: x1 < x2 oraz y1 < y2 (lewy dolny i prawy górny wierzchołek).")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):    # obsługa rect1 == rect2
        if not isinstance(other, Rectangle):
            return False
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        if not isinstance(other, Rectangle):
            return False
        return self.pt1 != other.pt1 or self.pt2 != other.pt2

    def center(self):           # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):             # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):       # przesunięcie o (x, y)
        shift = Point(x, y)
        self.pt1 = self.pt1 + shift
        self.pt2 = self.pt2 + shift


# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase): 

    def setUp(self):
        self.r1 = Rectangle(1, 2, 4, 6)
        self.r2 = Rectangle(1, 2, 4, 6)
        self.r3 = Rectangle(0, 0, 2, 2)

    def test_init_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 2, 1, 6)   # x1 >= x2
        with self.assertRaises(ValueError):
            Rectangle(1, 6, 4, 2)   # y1 >= y2
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, 1)   # zdegenerowany punkt

    def test_str(self):
        self.assertEqual(str(self.r1), "[(1, 2), (4, 6)]")
        self.assertEqual(str(self.r3), "[(0, 0), (2, 2)]")

    def test_repr(self):
        self.assertEqual(repr(self.r1), "Rectangle(1, 2, 4, 6)")
        self.assertEqual(repr(self.r3), "Rectangle(0, 0, 2, 2)")

    def test_eq(self):
        self.assertTrue(self.r1 == self.r2)
        self.assertFalse(self.r1 == self.r3)
        self.assertFalse(self.r1 == "nie_prostokat")
        self.assertFalse(self.r1 == (1, 2, 4, 6))

    def test_ne(self):
        self.assertTrue(self.r1 != self.r3)
        self.assertFalse(self.r1 != self.r2)

    def test_center(self):
        # Środek (1, 2) do (4, 6) to (2.5, 4.0)
        self.assertEqual(self.r1.center(), Point(2.5, 4.0))
        # Środek (0, 0) do (2, 2) to (1.0, 1.0)
        self.assertEqual(self.r3.center(), Point(1.0, 1.0))

    def test_area(self):
        # szerokość = 3, wysokość = 4 -> pole = 12
        self.assertEqual(self.r1.area(), 12)
        # szerokość = 2, wysokość = 2 -> pole = 4
        self.assertEqual(self.r3.area(), 4)

    def test_move(self):
        self.r1.move(2, -1)
        self.assertEqual(self.r1, Rectangle(3, 1, 6, 5))
        self.r3.move(-1, -1)
        self.assertEqual(self.r3, Rectangle(-1, -1, 1, 1))


if __name__ == "__main__":
    unittest.main()