import unittest
from removeDuplicates import RemoveDuplicates

class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.remove_duplicates = RemoveDuplicates()
    def test_empty_array(self):
        nums = []
        k = self.remove_duplicates.removeDuplicates(nums)
        self.assertEqual(k, 0)
        self.assertEqual(nums, [])

    def test_single_element(self):
        nums = [1]
        k = self.remove_duplicates.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        k = self.remove_duplicates.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 2, 3, 4, 5])

    def test_all_duplicates(self):
        nums = [2, 2, 2, 2, 2]
        k = self.remove_duplicates.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [2])

    def test_some_duplicates(self):
        nums = [1, 1, 2, 2, 3, 3, 4]
        k = self.remove_duplicates.removeDuplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 3, 4])

    def test_duplicates_at_end(self):
        nums = [1, 2, 3, 4, 5, 5, 5]
        k = self.remove_duplicates.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()
