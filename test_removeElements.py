import unittest
from typing import List
from removeElements import RemoveElements



class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.solution = RemoveElements()
    
    def test_example_case(self):
        nums = [3, 2, 2, 3]
        val = 3
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [2, 2])
    
    def test_no_occurrences(self):
        nums = [1, 2, 3, 4]
        val = 5
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 3, 4])
    
    def test_all_occurrences(self):
        nums = [7, 7, 7, 7]
        val = 7
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])
    
    def test_mixed_occurrences(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 3, 0, 4])
    
    def test_empty_list(self):
        nums = []
        val = 1
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])
    
    def test_single_element_match(self):
        nums = [1]
        val = 1
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])
    
    def test_single_element_no_match(self):
        nums = [2]
        val = 1
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [2])


if __name__ == "__main__":
    unittest.main()
