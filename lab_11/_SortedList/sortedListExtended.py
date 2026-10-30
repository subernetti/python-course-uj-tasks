# Zadanie 11.4
# Na bazie list powiązanych pojedynczo lub podwójnie stworzyć klasę SortedList, która
# przechowuje listę stale posortowaną. Największy element jest na początku listy (head).

### !!!!  DO DOKONCZENIA  !!! ### 

from singleListExtended import SingleList


class SortedList(SingleList):
    """Lista posortowana malejąco: największy element jest w head."""

    def insert(self, node):
        """Wstawia węzeł na właściwe miejsce. Np. L.insert(Node(3))."""
        if self.is_empty() or node.data >= self.head.data:
            self.insert_head(node)
            return

        prev = self.head
        while prev.next is not None and prev.next.data > node.data:
            prev = prev.next

        node.next = prev.next
        prev.next = node
        if node.next is None:
            self.tail = node
        self.length += 1

    def remove(self):
        """Zwraca węzeł z elementem największym (head) lub None dla pustej listy.
        Długość listy zmniejsza się o jeden węzeł.
        """
        if self.is_empty():
            return None
        return self.remove_head()

    def merge(self, other):
        """Scala posortowaną listę other do self. Po operacji other jest pusta."""
        while not other.is_empty():
            self.insert(other.remove())
