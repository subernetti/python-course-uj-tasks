# Zadanie 7.5
# W pliku circles.py zdefiniować klasę Circle wraz z potrzebnymi metodami. Okrąg jest 
# określony przez podanie środka i promienia. Wykorzystać wyjątek ValueError do obsługi błędów. 
# Napisać kod testujący moduł circles.

from points import Point
import math


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):        # "Circle(x, y, radius)"
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        if not isinstance(other, Circle):
            return False
        return not self == other

    def area(self):            # pole powierzchni
        return math.pi * math.pow(self.radius, 2)

    def move(self, x, y):      # przesuniecie o (x, y)
        self.pt = self.pt + Point(x, y)

    def cover(self, other):    # najmniejszy okrąg pokrywający oba
        if not isinstance(other, Circle):
            raise TypeError("Argument musi być instancją Circle")

        d = (self.pt - other.pt).length()

        if d + other.radius <= self.radius:
            return Circle(self.pt.x, self.pt.y, self.radius)
        if d + self.radius <= other.radius:
            return Circle(other.pt.x, other.pt.y, other.radius)

        new_radius = (d + self.radius + other.radius) / 2.0
        
        shift = (new_radius - self.radius) / d
        new_x = self.pt.x + shift * (other.pt.x - self.pt.x)
        new_y = self.pt.y + shift * (other.pt.y - self.pt.y)

        return Circle(new_x, new_y, new_radius)
            


# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.c1 = Circle(0, 0, 5)
        self.c2 = Circle(0, 0, 5)
        self.c3 = Circle(3, 4, 2)

    def test_init_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, -1)

    def test_repr(self):
        self.assertEqual(repr(self.c1), "Circle(0, 0, 5)")
        self.assertEqual(repr(self.c3), "Circle(3, 4, 2)")

    def test_eq_ne(self):
        self.assertTrue(self.c1 == self.c2)
        self.assertFalse(self.c1 == self.c3)
        self.assertTrue(self.c1 != self.c3)
        self.assertFalse(self.c1 != self.c2)
        self.assertFalse(self.c1 == "nie_okrag")

    def test_area(self):
        self.assertAlmostEqual(self.c1.area(), math.pi * 25)
        self.assertAlmostEqual(Circle(0, 0, 0).area(), 0.0)

    def test_move(self):
        c = Circle(1, 2, 3)
        c.move(2, -1)
        self.assertEqual(c, Circle(3, 1, 3))
        c.move(0, 0)
        self.assertEqual(c, Circle(3, 1, 3))

    def test_cover_contained(self):
        # Okrąg c1 (R=5, środek 0,0) zawiera w sobie okrąg o R=1 ze środkiem (1, 1)
        inner = Circle(1, 1, 1)
        self.assertEqual(self.c1.cover(inner), self.c1)
        self.assertEqual(inner.cover(self.c1), self.c1)

    def test_cover_concentric(self):
        # Okręgi współśrodkowe
        concentric_small = Circle(0, 0, 2)
        self.assertEqual(self.c1.cover(concentric_small), self.c1)
        self.assertEqual(concentric_small.cover(self.c1), self.c1)

    def test_cover_disjoint_horizontal(self):
        # Dwa identyczne okręgi o R=1 na osi X: (0, 0) i (4, 0)
        # Najdalsze punkty to (-1, 0) i (5, 0) -> rozpiętość = 6, R = 3, środek = (2, 0)
        circle_a = Circle(0, 0, 1)
        circle_b = Circle(4, 0, 1)
        covered = circle_a.cover(circle_b)

        self.assertAlmostEqual(covered.pt.x, 2.0)
        self.assertAlmostEqual(covered.pt.y, 0.0)
        self.assertAlmostEqual(covered.radius, 3.0)

    def test_cover_intersecting(self):
        # Okręgi przecinające się
        c_a = Circle(0, 0, 2)
        c_b = Circle(3, 0, 2)
        covered = c_a.cover(c_b)
        
        # d = 3, sumaryczna rozpiętość = 3 + 2 + 2 = 7, promień = 3.5
        # Nowy środek powinien wypaść w (1.5, 0)
        self.assertAlmostEqual(covered.pt.x, 1.5)
        self.assertAlmostEqual(covered.pt.y, 0.0)
        self.assertAlmostEqual(covered.radius, 3.5)


if __name__ == "__main__":
    unittest.main()
