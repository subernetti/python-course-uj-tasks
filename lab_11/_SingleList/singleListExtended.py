# Zadanie 11.1
# Do klasy SingleList dodać nowe metody.

class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.data == other.data

    def __ne__(self, other):
        if not isinstance(other, Node):
            return False    
        return not self == other
    

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):   # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node
    
    def remove_tail(self):    # klasy O(n)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.
        if self.head is None:
            raise ValueError("Lista jest pusta!")
        
        if self.head == self.tail:
            removed_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_node
        
        current = self.head
        while current.next != self.tail:
            current = current.next

        removed_node = self.tail
        current.next = None
        self.tail = current
        self.length -= 1

        return removed_node

            

    def join(self, other):    # klasy O(1)
        # Węzły z listy other są przepinane do listy self na jej koniec.
        # Po zakończeniu operacji lista other ma być pusta.
        if other.head == None:
            return
        if self.head == None:
            self.head = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            self.tail = other.tail
        self.length += other.length
        other.clear()



    def clear(self):    # czyszczenie listy
        self.head = None
        self.tail = None
        self.length = 0