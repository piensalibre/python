import unittest
from isValid import IsValid

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.isvalid = IsValid()
    
    def test_empty_string(self):
        self.assertTrue(self.isvalid.isValid(""))

    def test_single_pair_parentheses(self):
        self.assertTrue(self.isvalid.isValid("()"))
        self.assertTrue(self.isvalid.isValid("{}"))
        self.assertTrue(self.isvalid.isValid("[]"))

    def test_mixed_valid_pairs(self):
        self.assertTrue(self.isvalid.isValid("()[]{}"))
        self.assertTrue(self.isvalid.isValid("{[()()]}"))
        self.assertTrue(self.isvalid.isValid("([{}])"))

    def test_invalid_mixed_pairs(self):
        self.assertFalse(self.isvalid.isValid("(]"))
        self.assertFalse(self.isvalid.isValid("([)]"))
        self.assertFalse(self.isvalid.isValid("{[(])}"))

    def test_unbalanced_open_brackets(self):
        self.assertFalse(self.isvalid.isValid("("))
        self.assertFalse(self.isvalid.isValid("{["))
        self.assertFalse(self.isvalid.isValid("[{"))

    def test_unbalanced_close_brackets(self):
        self.assertFalse(self.isvalid.isValid(")"))
        self.assertFalse(self.isvalid.isValid("]}"))
        self.assertFalse(self.isvalid.isValid("]}{"))

if __name__ == '__main__':
    unittest.main()
