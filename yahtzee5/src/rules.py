"""
Modul till reglerna för yatzy.
"""
from abc import ABC, abstractmethod


class Rule(ABC):
    """
    Klass för regler till yatzy.
    """
    @abstractmethod
    def points(self, hand):
        """
        Abstrakt metod för undre klasser att ärva.
        """
        #passW0107: Unnecessary pass statement

class SameValueRule(Rule):
    """
    Klass för regler som kollar efter samma värde på tärningarna.
    """
    def __init__(self, value, name):
        self.value = value
        self.name = name

    def points(self, hand):
        """
        Metod för att är räkna ut poäng för tärningar med samma värde.
        """
        points = 0
        for die in hand.dice:
            if die.get_value() == self.value:
                points += self.value
        return points
class Ones(SameValueRule):
    """
    Klass för regeln Ones.
    """
    def __init__(self):
        super().__init__(1, "Ones")
class Twos(SameValueRule):
    """
    Klass för regeln Twos.
    """
    def __init__(self):
        super().__init__(2, "Twos")

class Threes(SameValueRule):
    """
    Klass för regeln Threes.
    """
    def __init__(self):
        super().__init__(3, "Threes")

class Fours(SameValueRule):
    """
    Klass för regeln Fours.
    """
    def __init__(self):
        super().__init__(4, "Fours")

class Fives(SameValueRule):
    """
    Klass för regeln Fives.
    """
    def __init__(self):
        super().__init__(5, "Fives")

class Sixes(SameValueRule):
    """
    Klass för regeln Sixes.
    """
    def __init__(self):
        super().__init__(6, "Sixes")


class ThreeOfAKind(Rule):
    """
    Klass för regeln tretal.
    """
    def __init__(self):
        self.name = "Three Of A Kind"
    def points(self, hand):
        """
        Metod för att räkna ut poäng för tärningar med tretal.
        """
        value_dict = {}
        for die in hand.dice:
            die_value = die.get_value()
            if die_value in value_dict:
                value_dict[die_value] += 1
            else:
                value_dict[die_value] = 1
        for dices in value_dict.values():
            if dices >= 3:
                points = 0
                for die in hand.dice:
                    points += die.get_value()
                return points
        return 0

class FourOfAKind(Rule):
    """
    Klass för regeln fyrtal.
    """
    def __init__(self):
        self.name = "Four Of A Kind"
    def points(self, hand):
        """
        Metod för att räkna ut poäng för tärningar med fyrtal.
        """
        value_dict = {}
        for die in hand.dice:
            die_value = die.get_value()
            if die_value in value_dict:
                value_dict[die_value] += 1
            else:
                value_dict[die_value] = 1
        for dices in value_dict.values():
            if dices >= 4:
                points = 0
                for die in hand.dice:
                    points += die.get_value()
                return points
        return 0

class FullHouse(Rule):
    """
    Klass för regeln kåk.
    """
    def __init__(self):
        self.name = "Full House"
    def points(self, hand):
        """
        Metod för att räkna ut poäng för tärningar med kåk.
        """
        value_dict = {}
        for die in hand.dice:
            die_value = die.get_value()
            if die_value in value_dict:
                value_dict[die_value] += 1
            else:
                value_dict[die_value] = 1
        har_tretal = False
        har_par = False
        for count in value_dict.values():
            if count == 3:
                har_tretal = True
            elif count == 2:
                har_par = True
            if har_tretal and har_par:
                return 25
        return 0

class SmallStraight(Rule):
    """
    Klass för regeln liten stege.
    """
    def __init__(self):
        self.name = "Small Straight"
    def points(self, hand):
        """
        Metod för att räkna ut poäng för liten stege.
        """
        v_d = {} #value_dict line-too-long
        for die in hand.dice:
            die_value = die.get_value()
            if die_value in v_d:
                v_d[die_value] += 1
            else:
                v_d[die_value] = 1
        if 1 in v_d and 2 in v_d and 3 in v_d and 4 in v_d:
            return 30
        if 2 in v_d and 3 in v_d and 4 in v_d and 5 in v_d:
            return 30
        if 3 in v_d and 4 in v_d and 5 in v_d and 6 in v_d:
            return 30
        return 0

class LargeStraight(Rule):
    """
    Klass för regeln stor stege.
    """
    def __init__(self):
        self.name = "Large Straight"
    def points(self, hand):
        """
        Metod för att räkna ut poäng för stor stege.
        """
        v_d = {} #value_dict line-too-long
        for die in hand.dice:
            die_value = die.get_value()
            if die_value in v_d:
                v_d[die_value] += 1
            else:
                v_d[die_value] = 1
        if 1 in v_d and 2 in v_d and 3 in v_d and 4 in v_d and 5 in v_d:
            return 40
        if 2 in v_d and 3 in v_d and 4 in v_d and 5 in v_d and 6 in v_d:
            return 40
        return 0
class Yahtzee(Rule):
    """
    Klass för regeln yatzy.
    """
    def __init__(self):
        self.name = "Yahtzee"
    def points(self, hand):
        """
        Metod för att räkna ut poäng för yatzy.
        """
        value_dict = {}
        for die in hand.dice:
            die_value = die.get_value()
            if die_value in value_dict:
                value_dict[die_value] += 1
            else:
                value_dict[die_value] = 1
        for dices in value_dict.values():
            if dices >= 5:
                return 50
        return 0
class Chance(Rule):
    """
    Klass för regeln chans.
    """
    def __init__(self):
        self.name = "Chance"
    def points(self, hand):
        """
        Metod för att räkna ut poäng för chans.
        """
        points = 0
        for die in hand.dice:
            points += die.get_value()
        return points
