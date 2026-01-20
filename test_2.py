import unittest
from lab2_2 import reverse_list, get_ends, get_middle

class TestLab2_2(unittest.TestCase):

    # --- Tests for reverse_list ---
    def test_reverse_1(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
    
    def test_reverse_2(self):
        self.assertEqual(reverse_list(['a', 'b']), ['b', 'a'])
        
    def test_reverse_3(self):
        self.assertEqual(reverse_list([]), [])

    # --- Tests for get_ends ---
    def test_ends_1(self):
        self.assertEqual(get_ends([10, 20, 30, 40]), [10, 40])
        
    def test_ends_2(self):
        self.assertEqual(get_ends(['red', 'blue']), ['red', 'blue'])
        
    def test_ends_3(self):
        # Testing a list with one element (first and last are the same)
        self.assertEqual(get_ends([5]), [5, 5])

    # --- Tests for get_middle ---
    def test_middle_odd(self):
        # Middle of 3 elements is index 1
        self.assertEqual(get_middle(['apple', 'banana', 'cherry']), 'banana')
        
    def test_middle_even(self):
        # Middle of 4 elements (rounded down) is index 1
        self.assertEqual(get_middle([1, 2, 3, 4]), 2)
        
    def test_middle_single(self):
        self.assertEqual(get_middle([100]), 100)

if __name__ == '__main__':
    unittest.main()