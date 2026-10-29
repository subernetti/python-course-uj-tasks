# test_zadanie_11_3.py
import pytest

from doubleListExtended import Node, DoubleList


# ---------- funkcje pomocnicze ----------

def make_list(values):
    """Buduje listę z podanych wartości, zwraca (lista, [węzły])."""
    lst = DoubleList()
    nodes = []
    for v in values:
        node = Node(v)
        lst.insert_tail(node)
        nodes.append(node)
    return lst, nodes


def forward(lst):
    result = []
    current = lst.head
    while current is not None:
        result.append(current.data)
        current = current.next
    return result


def backward(lst):
    result = []
    current = lst.tail
    while current is not None:
        result.append(current.data)
        current = current.prev
    return result


def assert_consistent(lst, expected):
    """Sprawdza spójność listy: kolejność, wskaźniki prev/next, długość."""
    assert forward(lst) == expected
    assert backward(lst) == expected[::-1]
    assert lst.count() == len(expected)
    if expected:
        assert lst.head.prev is None
        assert lst.tail.next is None
    else:
        assert lst.head is None
        assert lst.tail is None


# ---------- find_max ----------

class TestFindMax:
    def test_empty_list(self):
        assert DoubleList().find_max() is None

    def test_single_element(self):
        lst, nodes = make_list([5])
        assert lst.find_max() is nodes[0]

    @pytest.mark.parametrize("values, expected_index", [
        ([1, 2, 3], 2),          # maksimum na końcu
        ([9, 2, 3], 0),          # maksimum na początku
        ([1, 9, 3], 1),          # maksimum w środku
        ([-5, -2, -9], 1),       # liczby ujemne
        ([1.5, 2.5, 0.5], 1),    # liczby zmiennoprzecinkowe
    ])
    def test_returns_node_with_max_data(self, values, expected_index):
        lst, nodes = make_list(values)
        assert lst.find_max() is nodes[expected_index]

    def test_duplicates_returns_first_occurrence(self):
        lst, nodes = make_list([3, 7, 7, 1])
        assert lst.find_max() is nodes[1]

    def test_does_not_modify_list(self):
        lst, _ = make_list([4, 8, 2])
        lst.find_max()
        assert_consistent(lst, [4, 8, 2])


# ---------- find_min ----------

class TestFindMin:
    def test_empty_list(self):
        assert DoubleList().find_min() is None

    def test_single_element(self):
        lst, nodes = make_list([5])
        assert lst.find_min() is nodes[0]

    @pytest.mark.parametrize("values, expected_index", [
        ([1, 2, 3], 0),          # minimum na początku
        ([3, 2, 1], 2),          # minimum na końcu
        ([3, 1, 2], 1),          # minimum w środku
        ([-5, -2, -9], 2),       # liczby ujemne
        ([1.5, 2.5, 0.5], 2),    # liczby zmiennoprzecinkowe
    ])
    def test_returns_node_with_min_data(self, values, expected_index):
        lst, nodes = make_list(values)
        assert lst.find_min() is nodes[expected_index]

    def test_duplicates_returns_first_occurrence(self):
        lst, nodes = make_list([5, 1, 1, 9])
        assert lst.find_min() is nodes[1]

    def test_does_not_modify_list(self):
        lst, _ = make_list([4, 8, 2])
        lst.find_min()
        assert_consistent(lst, [4, 8, 2])


# ---------- remove ----------

class TestRemove:
    def test_remove_middle(self):
        lst, nodes = make_list([1, 2, 3])
        lst.remove(nodes[1])
        assert_consistent(lst, [1, 3])

    def test_remove_head(self):
        lst, nodes = make_list([1, 2, 3])
        lst.remove(nodes[0])
        assert_consistent(lst, [2, 3])
        assert lst.head is nodes[1]

    def test_remove_tail(self):
        lst, nodes = make_list([1, 2, 3])
        lst.remove(nodes[2])
        assert_consistent(lst, [1, 2])
        assert lst.tail is nodes[1]

    def test_remove_only_element(self):
        lst, nodes = make_list([1])
        lst.remove(nodes[0])
        assert_consistent(lst, [])
        assert lst.is_empty()

    def test_remove_two_element_list_head(self):
        lst, nodes = make_list([1, 2])
        lst.remove(nodes[0])
        assert_consistent(lst, [2])
        assert lst.head is lst.tail is nodes[1]

    def test_remove_two_element_list_tail(self):
        lst, nodes = make_list([1, 2])
        lst.remove(nodes[1])
        assert_consistent(lst, [1])
        assert lst.head is lst.tail is nodes[0]

    def test_removed_middle_node_is_detached(self):
        lst, nodes = make_list([1, 2, 3])
        lst.remove(nodes[1])
        assert nodes[1].next is None
        assert nodes[1].prev is None

    def test_remove_by_identity_not_by_value(self):
        # Node.__eq__ porównuje dane, więc remove musi działać na tożsamości węzła
        lst, nodes = make_list([7, 7, 7])
        lst.remove(nodes[1])
        assert_consistent(lst, [7, 7])
        assert lst.head is nodes[0]
        assert lst.tail is nodes[2]
        assert lst.head.next is lst.tail

    def test_remove_all_in_order(self):
        lst, nodes = make_list([1, 2, 3, 4])
        for i, node in enumerate(nodes):
            lst.remove(node)
            assert_consistent(lst, [1, 2, 3, 4][i + 1:])
        assert lst.is_empty()

    def test_remove_all_in_reverse_order(self):
        lst, nodes = make_list([1, 2, 3, 4])
        for i, node in enumerate(reversed(nodes)):
            lst.remove(node)
            assert_consistent(lst, [1, 2, 3, 4][:3 - i])
        assert lst.is_empty()

    def test_insert_after_remove(self):
        lst, nodes = make_list([1, 2, 3])
        lst.remove(nodes[1])
        lst.insert_tail(Node(4))
        lst.insert_head(Node(0))
        assert_consistent(lst, [0, 1, 3, 4])


# ---------- clear ----------

class TestClear:
    def test_clear_non_empty(self):
        lst, _ = make_list([1, 2, 3])
        lst.clear()
        assert_consistent(lst, [])
        assert lst.is_empty()

    def test_clear_empty(self):
        lst = DoubleList()
        lst.clear()
        assert_consistent(lst, [])

    def test_clear_single_element(self):
        lst, _ = make_list([1])
        lst.clear()
        assert_consistent(lst, [])

    def test_find_after_clear(self):
        lst, _ = make_list([1, 2, 3])
        lst.clear()
        assert lst.find_min() is None
        assert lst.find_max() is None

    def test_list_usable_after_clear(self):
        lst, _ = make_list([1, 2, 3])
        lst.clear()
        lst.insert_head(Node(10))
        lst.insert_tail(Node(20))
        assert_consistent(lst, [10, 20])

    def test_remove_head_on_cleared_list_raises(self):
        lst, _ = make_list([1, 2])
        lst.clear()
        with pytest.raises(ValueError):
            lst.remove_head()