import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Returns max value in a populated list, None if empty and raises ValueError if argument is Nonetype"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        
        #This tests for a large list
        lista = [i for i in range(1000)]
        self.assertEqual(max_list_iter(lista), 999)
        
        #This tests for a list of length 1
        self.assertEqual(max_list_iter([1]), 1)
        
        #This tests for a list with a repeating number
        self.assertEqual(max_list_iter([1, 3, 3]), 3)
        
        #This tests for an empty list returning None
        self.assertEqual(max_list_iter([]), None)


    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) #Used to test basic functionality
        self.assertEqual(reverse_rec([4, 7, 6, 3, 9]), [9, 3, 6, 7, 4]) #Checks functionality when numbers arent in order
        self.assertEqual(reverse_rec([]), []) #Checks empty list return

        with self.assertRaises(ValueError): #Checks if ValueError is returned
            reverse_rec(None)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 ) # Checks for basic functionality

        list_val1 = []
        self.assertEqual(bin_search(5, 2, 10, list_val1), None) #Checks for searching an empty list
        
        self.assertEqual(bin_search(8, 0, 4, [2, 5, 8, 90, 123]), 2) #Tests with a list that isnt just "1, 2, 3, 4, ..."

        big_list = [i for i in range(100)]
        self.assertEqual(bin_search(100, 0, 99, big_list), None) #Checks big list for value not present
        self.assertEqual(bin_search(9, 0, 99, big_list), 9) #Checks big list for value that is present

        with self.assertRaises(ValueError): #Checks for ValueError if int_list is NoneType
            bin_search(4, 0, 10, None)

if __name__ == "__main__":
        unittest.main()

    
