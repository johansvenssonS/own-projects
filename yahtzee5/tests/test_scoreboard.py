"""
Modul för enhetstester för scoreboard.py
"""
import unittest
import random

from src.scoreboard import Scoreboard
from src.hand import Hand

class TestScoreboard(unittest.TestCase):
    """
    Testcase för scoreboard klassen.
    """
    def setUp(self):
        """
        Funktion som sätter återkommande seeden för testen\n.
        """
        random.seed(0)

    def test_add_points(self):
        """
        Test för att lägga till poäng i en regel.
        """
        scoreboard = Scoreboard()
        hand = Hand([5,5,5,3,1])
        scoreboard.add_points("Three of a kind", hand)
        self.assertEqual(scoreboard.get_points("Three of a kind"), 19)
        print(f"{scoreboard.get_points('Three of a kind')}\n")
    def test_add_full_category(self):
        """
        Test för att lägga till poäng i en regel som redan spelats.
        """
        scoreboard = Scoreboard()
        hand = Hand([5,5,5,3,1])
        scoreboard.add_points("Three of a kind", hand)
        with self.assertRaises(ValueError) as _:
            scoreboard.add_points("Three of a kind", 1337)
