import pytest
from singleListExtended import Node, SingleList  

def test_remove_tail():
    alist = SingleList()
    
    # 1. Próba usunięcia z pustej listy
    with pytest.raises(ValueError):
        alist.remove_tail()
        
    # 2. Usunięcie jedynego elementu (lista staje się pusta)
    alist.insert_tail(Node(10))
    removed = alist.remove_tail()
    assert removed.data == 10
    assert alist.is_empty() is True
    assert alist.length == 0
    assert alist.head is None
    assert alist.tail is None
    
    # 3. Usunięcie ostatniego elementu z dłuższej listy
    alist.insert_tail(Node(1))
    alist.insert_tail(Node(2))
    alist.insert_tail(Node(3))
    
    removed = alist.remove_tail()
    assert removed.data == 3
    assert alist.length == 2
    assert alist.tail.data == 2
    assert alist.tail.next is None

def test_join():
    list1 = SingleList()
    list2 = SingleList()
    
    # 1. Join pustej z pustą
    list1.join(list2)
    assert list1.is_empty() is True
    
    # 2. Join niepustej z pustą
    list1.insert_tail(Node(1))
    list1.join(list2)
    assert list1.length == 1
    assert list1.tail.data == 1
    
    # 3. Join pustej z niepustą
    list3 = SingleList()
    list4 = SingleList()
    list4.insert_tail(Node(10))
    list4.insert_tail(Node(20))
    
    list3.join(list4)
    assert list3.length == 2
    assert list3.head.data == 10
    assert list3.tail.data == 20
    assert list4.is_empty() is True
    
    # 4. Join niepustej z niepustą
    list_a = SingleList()
    list_a.insert_tail(Node("A"))
    list_a.insert_tail(Node("B"))
    
    list_b = SingleList()
    list_b.insert_tail(Node("C"))
    list_b.insert_tail(Node("D"))
    
    list_a.join(list_b)
    assert list_a.length == 4
    assert list_a.head.data == "A"
    assert list_a.tail.data == "D"
    
    # Sprawdzenie czy list_b została poprawnie wyczyszczona
    assert list_b.is_empty() is True
    assert list_b.length == 0
    assert list_b.head is None
    assert list_b.tail is None

def test_clear():
    alist = SingleList()
    
    # 1. Czyszczenie pustej listy
    alist.clear()
    assert alist.is_empty() is True
    
    # 2. Czyszczenie wypełnionej listy
    alist.insert_tail(Node(1))
    alist.insert_tail(Node(2))
    alist.clear()
    
    assert alist.is_empty() is True
    assert alist.length == 0
    assert alist.head is None
    assert alist.tail is None

def test_find_min():
    alist = SingleList()
    
    # 1. Pusta lista
    assert alist.find_min() is None
    
    # 2. Lista z kilkoma elementami
    alist.insert_tail(Node(15))
    alist.insert_tail(Node(5))
    alist.insert_tail(Node(20))
    alist.insert_tail(Node(2))
    alist.insert_tail(Node(10))
    
    min_node = alist.find_min()
    assert min_node.data == 2
    
    # 3. Minimum na samym początku
    blist = SingleList()
    blist.insert_tail(Node(1))
    blist.insert_tail(Node(5))
    assert blist.find_min().data == 1

def test_find_max():
    alist = SingleList()
    
    # 1. Pusta lista
    assert alist.find_max() is None
    
    # 2. Lista z kilkoma elementami
    alist.insert_tail(Node(15))
    alist.insert_tail(Node(5))
    alist.insert_tail(Node(25))
    alist.insert_tail(Node(2))
    alist.insert_tail(Node(10))
    
    max_node = alist.find_max()
    assert max_node.data == 25
    
    # 3. Maksimum na samym końcu
    blist = SingleList()
    blist.insert_tail(Node(5))
    blist.insert_tail(Node(100))
    assert blist.find_max().data == 100

def test_reverse():
    alist = SingleList()
    
    # 1. Odwracanie pustej listy (nie powinno rzucić błędu)
    alist.reverse()
    assert alist.is_empty() is True
    
    # 2. Odwracanie listy 1-elementowej
    alist.insert_tail(Node(10))
    alist.reverse()
    assert alist.head.data == 10
    assert alist.tail.data == 10
    
    # 3. Odwracanie standardowej listy
    blist = SingleList()
    blist.insert_tail(Node(1))
    blist.insert_tail(Node(2))
    blist.insert_tail(Node(3))
    blist.insert_tail(Node(4))
    
    blist.reverse()
    
    # Sprawdzamy wskaźniki head i tail
    assert blist.head.data == 4
    assert blist.tail.data == 1
    
    # Sprawdzamy wewnętrzne powiązania (powinno być 4 -> 3 -> 2 -> 1 -> None)
    assert blist.head.next.data == 3
    assert blist.head.next.next.data == 2
    assert blist.tail.next is None
    
    # Długość powinna pozostać bez zmian
    assert blist.length == 4