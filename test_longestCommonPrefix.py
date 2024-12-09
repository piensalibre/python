import unittest
from longestCommonPrefix import LongestCommonPrefix

class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.longest_common_prefix = LongestCommonPrefix()
    
    def test_common_prefix_exists(self):
        self.assertEqual(self.longest_common_prefix.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
    
    def test_no_common_prefix(self):
        self.assertEqual(self.longest_common_prefix.longestCommonPrefix(["dog", "racecar", "car"]), "")
    
    def test_single_string(self):
        self.assertEqual(self.longest_common_prefix.longestCommonPrefix(["single"]), "single")
    
    def test_empty_string_list(self):
        self.assertEqual(self.longest_common_prefix.longestCommonPrefix([]), "")
    
    def test_all_strings_identical(self):
        self.assertEqual(self.longest_common_prefix.longestCommonPrefix(["test", "test", "test"]), "test")
    
    def test_mixed_case(self):
        self.assertEqual(self.longest_common_prefix.longestCommonPrefix(["Case", "Casual", "Cast"]), "Cas")
    
    def test_prefix_empty(self):
        self.assertEqual(self.longest_common_prefix.longestCommonPrefix(["abc", "def", "ghi"]), "")
    
    def test_all_strings_empty(self):
        self.assertEqual(self.longest_common_prefix.longestCommonPrefix(["", "", ""]), "")
    
    def test_prefix_partial_match(self):
        self.assertEqual(self.longest_common_prefix.longestCommonPrefix(["abcde", "abc", "abcdef"]), "abc")


if __name__ == "__main__":
    unittest.main()