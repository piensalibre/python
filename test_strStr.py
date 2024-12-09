import unittest
from strStr import StrStr

class TestStrStr(unittest.TestCase):

    def setUp(self):
        self.strStr = StrStr()


    def test_found(self):
        
        self.assertEqual(self.strStr.strStr("hello", "ll"), 2)
        self.assertEqual(self.strStr.strStr("abcdef", "cd"), 2)
        self.assertEqual(self.strStr.strStr("hayneedle", "needle"), 3)
    
    def test_not_found(self):
        
        self.assertEqual(self.strStr.strStr("aaaaa", "bba"), -1)
        self.assertEqual(self.strStr.strStr("abcdef", "gh"), -1)
    
    def test_empty_needle(self):
        
        self.assertEqual(self.strStr.strStr("hello", ""), 0)
        self.assertEqual(self.strStr.strStr("", ""), 0)
    
    def test_empty_haystack(self):
        
        self.assertEqual(self.strStr.strStr("", "a"), -1)
        self.assertEqual(self.strStr.strStr("", ""), 0)
    
    def test_both_empty(self):
        
        self.assertEqual(self.strStr.strStr("", ""), 0)


if __name__ == "__main__":
    unittest.main()
