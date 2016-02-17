import unittest
from two_sum import two_sum
class TwoSumTestSuite(unittest.TestCase):
    def test_list_range_4(self):
        result = two_sum([2, 5, 1, 7], 8)
        self.assertEqual(result,[2,3])
    def test_list_range_5(self):
        result = two_sum([7, 3, 9, 1],4)
        self.assertEqual(result, [1,3])
    def test_list_range_10(self):
        result = two_sum ([1, 3, 5, 7, 2, 9, 4, 6, 10], 5)
        self.assertEqual(result,[1,4])

if __name__ == "__main__":
    unittest.main()
