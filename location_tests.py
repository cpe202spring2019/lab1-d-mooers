import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_eq(self):
        loc1 = Location("PIE", 3.14, 4.13)
        loc2 = Location("Olympia", 222, 218)
        loc3 = Location("PIE", 3.14, 4.13)
        self.assertTrue(loc1 == loc3)
        self.assertFalse(loc1 == loc2)
    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
