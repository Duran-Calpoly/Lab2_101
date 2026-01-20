import unittest
from lab2_3 import alphabetize_two, repeat_string, swap_ends

class TestLab2_3(unittest.TestCase):

    # --- Tests for alphabetize_two ---
    def test_alpha_1(self):
        # Standard alphabetical order
        self.assertEqual(alphabetize_two("apple", "banana"), "apple banana")

    def test_alpha_2(self):
        # Reverse order input
        self.assertEqual(alphabetize_two("zebra", "apple"), "apple zebra")
        
    def test_alpha_3(self):
        # Identical words
        self.assertEqual(alphabetize_two("dog", "dog"), "dog dog")

    # --- Tests for repeat_string ---
    def test_repeat_1(self):
        self.assertEqual(repeat_string("Hi", 3), "HiHiHi")

    def test_repeat_2(self):
        self.assertEqual(repeat_string("!", 5), "!!!!!")

    def test_repeat_3(self):
        self.assertEqual(repeat_string("No", 0), "")

    # --- Tests for swap_ends ---
    def test_swap_1(self):
        self.assertEqual(swap_ends("cat"), "tac")

    def test_swap_2(self):
        self.assertEqual(swap_ends("Python"), "nythoP")

    def test_swap_3(self):
        # Testing a single character string
        self.assertEqual(swap_ends("A"), "A")

if __name__ == '__main__':
    unittest.main()