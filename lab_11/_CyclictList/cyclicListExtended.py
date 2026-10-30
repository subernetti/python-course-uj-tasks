# Zadanie 11.5
# Na bazie list powiązanych pojedynczo lub podwójnie (to jest wygodniejsze) stworzyć klasę CyclicList, 
# która przechowuje listę cykliczną. Atrybut head może wskazywać na dowolny węzeł listy cyklicznej, 
# natomiast przez tail rozumiemy węzeł bezpośrednio poprzedzający head.

from doubleListExtended import Node, DoubleList

class CyclicList(DoubleList):
    def __init__(self):
        self.head = None   # łącze do dowolnego węzła listy
        # nie potrzeba mieć self.tail

    def is_empty(self):
        return self.head is None

    def insert_head(self, node): 
        if self.head is None:
            node.next = node.prev = node
        else:
            tail = self.head.prev
            node.next = self.head
            node.prev = tail
            tail.next = node
            self.head.prev = node
        self.head = node

    def insert_tail(self, node): 
        if self.head is None:
            node.next = node.prev = node
            self.head = node
        else:
            tail = self.head.prev
            node.next = self.head
            node.prev = tail
            tail.next = node
            self.head.prev = node

    def search(self, data):   # zwraca node lub None
        if self.head == None:
            return None
        current = self.head
        while True:
            if current.data == data:
                return current
            current = current.next
            if current is self.head:
                return None

    def remove(self, node): 
        if self.head is None:
            return 
        if node.next is node:
            self.head = None
        else: 
            node.prev.next = node.next
            node.next.prev = node.prev
            if node is self.head:
                self.head = node.next
        node.next = node.prev = None

    def join(self, other):     # scalanie dwóch list cyklicznych w czasie O(1)
        if other.head is None:
            return
        if self.head is None:
            self.head = other.head
        else:
            tail1 = self.head.prev
            tail2 = other.head.prev
            tail1.next = other.head
            other.head.prev = tail1
            tail2.next = self.head
            self.head.prev = tail2
        other.head = None

    def clear(self):    # czyszczenie listy
        self.head = None
        