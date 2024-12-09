import unittest
from typing import List
from searchInsert import SearchInsert


class TestSearchInsert(unittest.TestCase):
    def setUp(self):
        self.solution = SearchInsert()

    def test_target_in_list(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 6), 3)

    def test_target_not_in_list(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 0), 0)

    def test_empty_list(self):
        self.assertEqual(self.solution.searchInsert([], 5), 0)

    def test_single_element_list(self):
        self.assertEqual(self.solution.searchInsert([1], 0), 0)
        self.assertEqual(self.solution.searchInsert([1], 1), 0)
        self.assertEqual(self.solution.searchInsert([1], 2), 1)

    def test_large_list(self):
        nums = list(range(1, 10001))  
        self.assertEqual(self.solution.searchInsert(nums, 5000), 4999)
        self.assertEqual(self.solution.searchInsert(nums, 10001), 10000)
        self.assertEqual(self.solution.searchInsert(nums, 0), 0)

if __name__ == "__main__":
    unittest.main()
