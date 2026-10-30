# Zadanie 11.3
# Do klasy DoubleList dopisać nowe metody.

class Node:
    """Klasa reprezentująca węzeł listy dwukierunkowej."""

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
            return not self == other
    
class DoubleList:
    """Klasa reprezentująca całą listę dwukierunkową."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node   # stary head
            self.head = node        # nowy head
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.tail:
            node.prev = self.tail
            self.tail.next = node   # stary tail
            self.tail = node        # nowy tail
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def remove_head(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        elif self.head is self.tail:   # length == 1
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.head.prev = None   # czyszczenie
            node.next = None   # czyszczenie
            self.length -= 1
            return node

    def remove_tail(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        elif self.head is self.tail:   # length == 1
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None   # czyszczenie
            node.prev = None
            self.length -= 1
            return node   
        
    def find_max(self): 
        # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
        if self.is_empty():
            return None
        
        current = self.head.next
        max_node = self.head
        while current is not None:
            if current.data > max_node.data:
                max_node = current
            current = current.next
        
        return max_node


    def find_min(self): 
        # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.
        if self.is_empty():
            return None
        
        current = self.head.next
        min_node = self.head
        while current is not None:
            if current.data < min_node.data:
                min_node = current
            current = current.next
        
        return min_node

    def remove(self, node): 
        # Usuwa wskazany węzeł z listy (węzeł należy do listy).
        if node is self.head:
            self.remove_head()
        elif node is self.tail:
            self.remove_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None
            self.length -= 1
 
    def clear(self):    # czyszczenie listy
        self.head = None
        self.tail = None
        self.length = 0