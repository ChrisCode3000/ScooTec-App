
import unittest
from unittest import result
import main

class TestMain(unittest.TestCase):

    def test_pricef(self):
        result = main.pricef(10)
        self.assertEqual(result, 2.79)