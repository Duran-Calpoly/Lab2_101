import unittest
from lab2_6 import multiplication_table, get_multiples_of_three, merge_lists

class TestLab2_6(unittest.TestCase):

    # --- Tests for multiplication_table ---
    def test_table_values(self):
        result = multiplication_table()
        self.assertEqual(len(result), 144)
        self.assertEqual(result[0], 1)    # 1x1
        self.assertEqual(result[12], 2)   # 2x1
        self.assertEqual(result[-1], 144) # 12x12

    # --- Tests for get_multiples_of_three ---
    def test_multiples_1(self):
        self.assertEqual(get_multiples_of_three([3, 6, 7, 9, -3, 0]), [3, 6, 9])
    
    def test_multiples_2(self):
        # Empty result test
        self.assertEqual(get_multiples_of_three([1, 2, 4, 5]), [])

    # --- Tests for merge_lists ---
    def test_merge_1(self):
        l1 = ["Name", "Age"]
        l2 = ["Alice", 20]
        expected = [("Name", "Alice"), ("Age", 20)]
        self.assertEqual(merge_lists(l1, l2), expected)

    def test_merge_2(self):
        # Testing different lengths (zip stops at the shortest list)
        l1 = [1, 2]
        l2 = ['a', 'b', 'c']
        self.assertEqual(merge_lists(l1, l2), [(1, 'a'), (2, 'b')])

if __name__ == '__main__':
    unittest.main()