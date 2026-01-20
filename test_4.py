import unittest
from lab2_4 import get_evens, find_second_largest, count_vowels

class TestLab2_4(unittest.TestCase):

    # --- Tests for get_evens ---
    def test_evens_1(self):
        self.assertEqual(get_evens(10), [0, 2, 4, 6, 8, 10])

    def test_evens_2(self):
        # Testing odd n
        self.assertEqual(get_evens(7), [0, 2, 4, 6])

    # --- Tests for find_second_largest ---
    def test_second_1(self):
        self.assertEqual(find_second_largest([10, 20, 30, 40]), 30)

    def test_second_2(self):
        # Testing duplicates - second largest should be lower than max
        self.assertEqual(find_second_largest([10, 10, 5, 2]), 5)
        
    def test_second_3(self):
        # Testing negative numbers
        self.assertEqual(find_second_largest([-10, -5, -20, -2]), -5)

    # --- Tests for count_vowels ---
    def test_vowels_1(self):
        self.assertEqual(count_vowels("apple"), 2)

    def test_vowels_2(self):
        # Case sensitivity and spaces
        self.assertEqual(count_vowels("Ice Cream"), 4)

if __name__ == '__main__':
    unittest.main()