"""
Modul för tärningar 
"""
import random

class Die():
    """
    Tärningsklass 
    """
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6
    ##_value = None

    def __init__(self, _value = None):
        if _value is None:
            self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)
        elif self.MIN_ROLL_VALUE <= _value <= self.MAX_ROLL_VALUE:
            self._value = _value
        elif _value > self.MAX_ROLL_VALUE:
            self._value = self.MAX_ROLL_VALUE
        elif _value < self.MIN_ROLL_VALUE:
            self._value = self.MIN_ROLL_VALUE

    def get_name(self):
        """
        Metod som returnerar tärningens värde till sträng/namn.
        """
        list_of_names = ["one", "two", "three", "four", "five", "six"]
        name = list_of_names[self._value -1]
        # if self._value == 1:
        #     name = "one"
        # elif self._value == 2:
        #     name = "two"
        # elif self._value == 3:
        #     name = "three"
        # elif self._value == 4:
        #     name = "four"
        # elif self._value == 5:
        #     name = "five"
        # elif self._value == 6:
        #     name = "six"
        return name
    def get_value(self):
        """
        Metod som returnerar tärningens värde.
        """
        return self._value

    def roll(self):
        """
        Metod som slumpar fram tärningens värde 1-6.
        """
        self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)

    def __str__(self):
        """
        Str() metod för objeketet, returnerar värdet i en f-string.
        """
        return f"{self._value}"
    def __eq__(self, other):
        """
        Metod för att jämföra två tärningar eller med ett heltal.
        (==)
        """
        if isinstance(other, Die):
            return self._value == other._value
        return self._value == other
