import unittest
from lab2_5 import map_word_lengths

class TestLab2_5(unittest.TestCase):

    def test_map_1(self):
        # Standard case
        input_list = ["apple", "bat", "cherry"]
        expected = {"apple": 5, "bat": 3, "cherry": 6}
        self.assertEqual(map_word_lengths(input_list), expected)

    def test_map_2(self):
        # Testing empty strings
        input_list = ["", "a", "abc"]
        expected = {"": 0, "a": 1, "abc": 3}
        self.assertEqual(map_word_lengths(input_list), expected)

    def test_map_3(self):
        # Testing duplicates (Dictionaries handle unique keys)
        input_list = ["dog", "cat", "dog"]
        expected = {"dog": 3, "cat": 3}
        self.assertEqual(map_word_lengths(input_list), expected)

if __name__ == '__main__':
    unittest.main()