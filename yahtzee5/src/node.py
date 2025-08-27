"""
Modul för Nod klassen.
"""

class Node():
    """Klass för Noder i lista"""
    def __init__(self, data, next_= None):
        self.data = data
        self.next_ = next_

    def has_next(self):
        """Metod för att få reda på om nästa nod finns"""
        return self.next_ is not None
    