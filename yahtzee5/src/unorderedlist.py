"""Modul för en osorteradlista (DataStruktur)"""

from src.node import Node
from src.errors import MissingValue
from src.errors import MissingIndex

# from node import Node
# from errors import MissingValue
# from errors import MissingIndex



class UnorderedList():
    """Klass för en osorteradlista."""
    def __init__(self):
        self._head = None
    def append(self, value):
        """Metod för att lägga till i lista."""
        if self._head is None:
            self._head = Node(value)
        else:
            current = self._head
            while current.has_next():
                current = current.next_
            current.next_ = Node(value)

    def set(self, index, data):
        """Metod för att skriva över data på specifikt index."""
        current = self._head
        count = 0
        #try:
        while count < index:
            if current is None:
                raise MissingIndex("Positionen hittades inte!")
            current = current.next_
            count += 1
        if current is None:
            raise MissingIndex("Positionen hittades inte!")
        current.data = data
        # except MissingIndex as e:
        #     print(e)



    def size(self):
        """Metod för att hämta storlek på lista."""
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.next_
        return count

    def get(self, index):
        """Metod för att hämta data ifrån specifikt index."""
        current = self._head
        count = 0
        #try:
        while count < index:
            if current is None:
                raise MissingIndex("Positionen hittades inte!")
            current = current.next_
            count += 1
        if current is None:
            raise MissingIndex("Positionen hittades inte!")
        return current.data
        # except MissingIndex as e:
        #     print(e)

    def index_of(self, value):
        """Metod för att hitta index av specifikt värde."""
        current = self._head
        index = 0
        #try:
        while current is not None :
            if current.data == value:
                return index
            current = current.next_
            index += 1
        raise MissingValue
        # except MissingValue:
        #     raise MissingValue("Värdet hittades inte!")

    def print_list(self):
        """Metod för att printa listans innehåll."""
        current = self._head
        while current is not None:
            print(current.data)
            current = current.next_

    def remove(self, data):
        """Metod för att ta bort specifikt värde ur listan."""
        current = self._head
        tail = None
        # try:
        while current is not None:
            if current.data == data:
                if tail is None:
                    self._head = current.next_
                else:
                    tail.next_ = current.next_
                return
            tail = current
            current = current.next_
        raise MissingValue("Värdet hittades inte!")
    # except MissingValue as e:
    #     print(type(e), e)
        ## Funkade inte med Missingvalue as e,
        ## och print(e) med testerna.


# if __name__ == "__main__":
#     hej = UnorderedList()
#     hej.append("one")
#     hej.append("two")
#     hej.append("three")
#     hej.remove("three")
#     hej.print_list()
