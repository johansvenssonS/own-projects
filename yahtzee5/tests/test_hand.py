"""
Modul för enhetstester för hand.py
"""
import unittest
import random

from src.hand import Hand

class TestHand(unittest.TestCase):
    """
    Testcase för die klassen.
    """
    def setUp(self):
        """
        Funktion som sätter återkommande seeden för testen\n.
        """
        random.seed(0)
    def test_create_hand(self):
        """
        Test för att skapa objekt och läsa av dens värde.
        seed används så de blir samma random varje gång\n.
        """
        hand = Hand()
        hand_list = hand.to_list()
        excepted_value = [4, 4, 1, 3, 5]
        self.assertEqual(hand_list, excepted_value)
        #kollar exakt värde ==, användar samma randomseed(0) krav7
    def test_preset_hand(self):
        """
        Test för att skapa hand med bestämd lista av tärningar\n.
        """
        hand_arguments = [6,6,6,6,6]
        hand = Hand(hand_arguments)
        self.assertEqual(hand.to_list(), hand_arguments)
    def test_to_list(self):
        """
        Test för att se så att to_list funkar.
        """
        hand_arguments = [6,6,6,6,6]
        hand = Hand(hand_arguments)
        self.assertIsInstance(hand.to_list(), list)
        self.assertIsInstance(hand.to_list()[0], int)
    def test_roll_parameter(self):
        """
        Test för att slå om de de specifika tärningar man specificerar.
        """
        parameter_list = [0,2,4]
        hand_arguments = [1,2,3,4,5]
        hand = Hand(hand_arguments)
        hand.roll(parameter_list)
        old_hand = hand.to_list()
        seed_sequence = [4,2,4,4,1]
        self.assertEqual(old_hand,seed_sequence)
    def test_roll_silent(self):
        """
        Test för att slå om alla tärningar utan att ange parameter.
        """
        hand = Hand()
        hand.roll()
        hand_values = hand.to_list()
        seed_sequence = [4,4,3,4,3]
        ###random.seed(0) ger [4,4,3,4,3]
        ### andra random sekvensen på "första"
        self.assertEqual(hand_values, seed_sequence)
