"""Modul för kö till yathzee"""

from src.players import Player


class Queue:
    """Klass till kö i yathzee."""
    def __init__(self):
        self._items = []

    def is_empty(self):
        """Metod som kollar om kön är tom."""
        return not self._items 

    def enqueue(self, item):
        """Metod som lägger till objekt i kön."""
        self._items.append(item)

    def dequeue(self):
        """Metod som tar bort objekt i kön."""
        try:
            return self._items.pop(0)

        except IndexError:
            return "Empty list."

    def peek(self):
        """Metod som kollar på första objektet i kön."""
        return self._items[0]

    def size(self):
        """Metod som kollar storleken på kön."""
        return len(self._items)

    def to_list(self):
        """Metod som konverterar kön till lista."""
        items_list = []
        for item in self._items:
            items_list.append(item.to_dict())
        return items_list
    @classmethod
    def from_list(cls, lst):
        """Metod som konverterar lista till kö."""
        que = cls()
        for item in lst:
            player = Player.from_dict(item)
            que.enqueue(player)
        return que
