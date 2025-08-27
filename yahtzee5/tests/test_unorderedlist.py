"""
Modul för enhetstester för underorderedlist.py
"""
import unittest
import random

from src.unorderedlist import UnorderedList
from src.node import Node
from src.errors import MissingIndex, MissingValue

class TestUnorderedlist(unittest.TestCase):
    """
    Testcase för Unorderedlist klassen.
    """
    def setUp(self):
        """
        Funktion som sätter återkommande seeden för testen\n.
        """
        random.seed(0)

    def test_get_exeption(self):
        """
        Test att exception lyfts om index inte finns.
        """
        uo_list = UnorderedList()
        with self.assertRaises(MissingIndex) as _:
            uo_list.get(5)


    def test_get(self):
        """
        Test att rätt värde returneras om index finns .
        """
        uo_list = UnorderedList()
        uo_list.append(10)
        self.assertEqual(uo_list.get(0), 10)

    def test_remove_exception(self):
        """
        Test att exceptions lyfts om värde saknas.
        """
        uo_list = UnorderedList()
        data1 = Node(10)
        uo_list.append(data1)
        with self.assertRaises(MissingValue) as _:
            uo_list.remove(8)


    def test_remove_result(self):
        """
        Test för att listan är korrekt efter element har tagits bort om värdet finns.
        """
        a_list = [1,2,3,4]
        uo_list = UnorderedList()
        for number in a_list:
            uo_list.append(number)
        uo_list.remove(4)
        p_list = [1,2,3]

        self.assertEqual(uo_list.print_list(), print(p_list))
