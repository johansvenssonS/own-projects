"""
Modul till handklassen.
"""
from src.die import Die

class Hand():
    """
    Klass till hand, amount_of_dice är hur många tärningar handen har.
    """
    AMOUNT_OF_DICE = 5

    def __init__(self, dice_values = None):
        self.dice = []
        if dice_values is None:
            i = 0
            while i < self.AMOUNT_OF_DICE:
                self.dice.append(Die())
                i +=1
        else:
            for value in dice_values:
                self.dice.append(Die(value))

    def roll(self, indexes = None):
        """
        Metod som slumpar fram värdena i handen.
        med argument så slumpar den bara de specifika indexen i handen.
        """
        if indexes is None:
            for die in self.dice:
                die.roll()
        else:
            for i in indexes:
                if 0 <= i < len(self.dice):
                    self.dice[i].roll()

    def __str__(self):
        """
        Str() metod/magisk  för objektet, som användare str() metoden hos die.
        """
        #return ", ".join(str(die) for die in self.dice) list comprehension slarv
        hand_content = []
        for die in self.dice:
            hand_content.append(str(die))
        return ", ".join(hand_content)

    def to_list(self):
        """
        Metod som returner handen som en lista av <int>.
        """
        hand_content = []
        for die in self.dice:
            hand_content.append(die.get_value())
        return hand_content
