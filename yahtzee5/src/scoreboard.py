"""
Modul för scoreboard klassen.
"""
from src.rules import SameValueRule, FullHouse, ThreeOfAKind #line to long
from src.rules import FourOfAKind, SmallStraight, LargeStraight, Yahtzee, Chance

class Scoreboard():
    """
    Klass för scoreboard.
    """

    def __init__(self):#reglerna defualt -1 inte använda
        self._rules = {#privat attribut, gömma poäng.
            "Ones": -1, "Twos":  -1, "Threes": -1,
            "Fours": -1, "Fives": -1, "Sixes": -1,
            "Three of a kind": -1, "Four of a kind": -1, "Fullhouse": -1, 
            "Small straight": -1, "Large straight": -1, 
            "Yahtzee": -1, "Chance": -1}
        self.rule_objects = { #dict med regler och deras funktioner som ska kallas på.
            "Ones": SameValueRule(1, "Ones"), "Twos": SameValueRule(2, "Twos"), 
            "Threes": SameValueRule(3, "Threes"), "Fours": SameValueRule(4, "Fours"), 
            "Fives": SameValueRule(5, "Fives"), "Sixes": SameValueRule(6, "Sixes"),
            "Three of a kind": ThreeOfAKind(), "Four of a kind": FourOfAKind(), 
            "Fullhouse": FullHouse(), "Small straight": SmallStraight(), 
            "Large straight": LargeStraight(),
            "Yahtzee": Yahtzee(), "Chance": Chance()
    }
    @property
    def rules(self):
        """
        Metod för att hämta privata attribut
        """
        return self._rules
    @rules.setter
    def rules(self, value):
        self._rules = value

    def get_total_points(self):
        """
        Metod för att ta fram totala poängen.
        """
        total = 0
        for points in self._rules.values():
            if points != -1:
                total += points
        return total


    def add_points(self, rule_name, hand):
        """
        Metod för att lägga till poäng till en specifik kategori.
        """
        if self._rules[rule_name] == -1:
            rule = self.rule_objects[rule_name]
            points = rule.points(hand)
            self._rules[rule_name] = points
        elif self._rules[rule_name] != -1:
            raise ValueError("Kategorin har redan poängsatts")

    def get_points(self, rule_name):
        """
        Metod för att hämta poäng för en specifik kategori.
        """
        if self._rules[rule_name] == -1:
            return -1
        return self._rules[rule_name]

    def finished(self): #all kollar att alla värden inte =! -1
        """
        Metod för att kolla om alla kategorier är poängsatta/använda.
        """
        if all(points != -1 for points in self._rules.values()):
            return True
        return False

    @classmethod
    def from_dict(cls, rules):
        """
        Metod för att skapa ett scoreboard objekt och använda ett
        dict för poängsättning.
        """
        scoreboard = cls()
        scoreboard._rules = rules
        return scoreboard

a_dict = {
    "Ones": 3,
    "Twos": -1,
    "Threes": -1,
    "Fours": 0,
    "Fives": -1,
    "Sixes": 12,
    "Three Of A Kind": -1,
    "Four Of A Kind": -1,
    "Full House": -1,
    "Small Straight": -1,
    "Large Straight": -1,
    "Yahtzee": -1,
    "Chance": 13,
}
