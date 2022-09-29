from unittest import TestCase
from Calculator import Main
from tkinter import *

class TestMain(TestCase):
    def setUp(self):
        self.calculator = Main(Tk())

    def test_build(self):
        self.assertEqual(self.calculator.build(), None)

    def test_logicalc(self):
        self.assertEqual(self.calculator.logicalc("C"), None)

    def test_logicalc(self):
        self.assertEqual(self.calculator.logicalc("DEL"), None)

    def test_logicalc(self):
        self.assertEqual(self.calculator.logicalc("√"), None)

    def test_update(self):
        self.assertEqual(self.calculator.update(), None)

    # Executing the tests in the above test case class
