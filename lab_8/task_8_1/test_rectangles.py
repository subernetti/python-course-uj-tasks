import pytest
from points import Point
from rectangles import Rectangle


def test_init_valid():
    # Zwykłe współrzędne, w tym ujemne i zmiennoprzecinkowe
    r1 = Rectangle(0, 0, 2, 2)
    assert r1.pt1 == Point(0, 0)
    assert r1.pt2 == Point(2, 2)

    r2 = Rectangle(-5, -5, -1, -1)
    assert r2.pt1 == Point(-5, -5)

    r3 = Rectangle(0.5, 1.5, 3.5, 4.5)
    assert r3.pt2 == Point(3.5, 4.5)


def test_init_invalid():
    # Skrajne przypadki: lewy dolny punkt nie jest poniżej i na lewo od prawego górnego
    with pytest.raises(ValueError):
        Rectangle(2, 2, 0, 0)  # Odwrotna kolejność

    with pytest.raises(ValueError):
        Rectangle(0, 2, 2, 0)  # x poprawne, ale y odwrócone

    with pytest.raises(ValueError):
        Rectangle(1, 1, 1, 5)  # Szerokość 0 (linia pionowa)

    with pytest.raises(ValueError):
        Rectangle(1, 1, 5, 1)  # Wysokość 0 (linia pozioma)

    with pytest.raises(ValueError):
        Rectangle(2, 2, 2, 2)  # Zdegenerowany do punktu


def test_from_points():
    p1 = Point(-2, -3)
    p2 = Point(4, 5)
    
    # Tworzenie z krotki
    r1 = Rectangle.from_points((p1, p2))
    assert r1.pt1 == p1
    assert r1.pt2 == p2

    # Tworzenie z listy
    r2 = Rectangle.from_points([p1, p2])
    assert r2 == r1

    # Próba utworzenia z błędnie ułożonych punktów powinna również rzucić ValueError
    with pytest.raises(ValueError):
        Rectangle.from_points((p2, p1))


def test_virtual_coordinates():
    r = Rectangle(-2, 1, 4, 7)
    
    assert r.left == -2
    assert r.bottom == 1
    assert r.right == 4
    assert r.top == 7


def test_virtual_dimensions():
    r = Rectangle(-2, 1, 4, 7)
    
    assert r.width == 6
    assert r.height == 6
    
    # Skrajny przypadek: ułamki
    r_float = Rectangle(0.5, 0.5, 2.0, 3.0)
    assert r_float.width == 1.5
    assert r_float.height == 2.5


def test_virtual_points():
    r = Rectangle(-2, 1, 4, 7)
    
    assert r.bottomleft == Point(-2, 1)
    assert r.topright == Point(4, 7)
    assert r.topleft == Point(-2, 7)
    assert r.bottomright == Point(4, 1)


def test_center():
    # Środek wypadający na liczbach całkowitych
    r1 = Rectangle(0, 0, 4, 4)
    assert r1.center == Point(2.0, 2.0)

    # Środek wypadający na ułamkach
    r2 = Rectangle(0, 0, 3, 3)
    assert r2.center == Point(1.5, 1.5)
    
    # Środek dla prostokąta w ujemnych współrzędnych
    r3 = Rectangle(-5, -5, -1, -1)
    assert r3.center == Point(-3.0, -3.0)


def test_area():
    r1 = Rectangle(0, 0, 4, 5)
    assert r1.area() == 20

    r2 = Rectangle(-3, -3, 3, 3)
    assert r2.area() == 36


def test_move():
    r = Rectangle(0, 0, 2, 3)
    r.move(2, -1)
    
    assert r.left == 2
    assert r.bottom == -1
    assert r.right == 4
    assert r.top == 2
    
    # Przesunięcie o zero (brak zmiany)
    r.move(0, 0)
    assert r.left == 2
    assert r.bottom == -1


def test_equality():
    r1 = Rectangle(1, 2, 3, 4)
    r2 = Rectangle(1, 2, 3, 4)
    r3 = Rectangle(0, 0, 3, 4)

    assert r1 == r2
    assert r1 != r3
    assert not (r1 == r3)

    # Skrajny przypadek: porównanie z obiektem innej klasy
    assert r1 != "to_jest_napis"
    assert r1 != Point(1, 2)


def test_str_and_repr():
    r = Rectangle(1, 2, 3, 4)
    assert str(r) == "[(1, 2), (3, 4)]"
    assert repr(r) == "Rectangle(1, 2, 3, 4)"