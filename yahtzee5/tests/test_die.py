"""
Modul för enhetstester för die.py
"""
import unittest
import random

from src.die import Die

class TestDie(unittest.TestCase):
    """
    Testcase för die klassen.
    """
    def setUp(self):
        """
        Funktion som sätter återkommande seeden för testen.
        """
        random.seed(0)
    def test_create_die(self):
        """
        Test för att skapa objekt och läsa av dens värde.
        seed används så de blir samma random varje gång.\n
        """
        die = Die()
        excepted_value = random.randint(Die.MIN_ROLL_VALUE, Die.MAX_ROLL_VALUE)
        self.assertEqual(die.get_value(), excepted_value)
        #kollar exakt värde ==, användar samma randomseed(0) krav7
    def test_preset_die(self):
        """
        Test för att skapa tärning med bestämt värde(2).\n
        """
        die2 = Die(2)
        self.assertEqual(die2.get_value(), 2)

    def test_highnumber_die(self):
        """
        Test för att se hur klassen hanterar input av höga värden.\n
        """
        die100 = Die(100)
        self.assertEqual(die100.get_value(), 6)
    def test_lownumber_die(self):
        """
        Test för att se hur klassen hanterar input av låga värden.\n
        """
        die100 = Die(-100)
        self.assertEqual(die100.get_value(), 1)

    def test_die_roll(self):
        """
        Test för att se så att nytt värde tilldelas vid roll()
        Ny seed i testet så att de inte blir samma som linje 17.\n
        """
        die_rand = Die()
        first_value = die_rand.get_value()
        random.seed(1) #update seeden så de inte använder samma
        die_rand.roll()
        new_value = die_rand.get_value()
        self.assertNotEqual(first_value, new_value)
        #kollar exakta värden != , ny randomseed(1) krav7
    def test_die_name(self):
        """
        Test för att se så att tärningen får rätt namn kontra dens värde.\n
        """
        die = Die()
        die_value = die.get_value()
        list_of_names = ["one", "two", "three", "four", "five", "six"]
        test_name = list_of_names[die_value -1]
        self.assertEqual(die.get_name(), test_name )
    def test_die_eq(self):
        """
        Test för att se att __eq__() returnerar rätt vid jämförelse med ett annat Die objekt.\n
        """
        die = Die(1)
        die2 = Die(1)
        self.assertTrue(die == die2)
        self.assertEqual(die,die2)
if __name__ == "__main__":
    unittest.main()
