import unittest
from lengthOfLastWord import LengthOfLastWord


class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        
        self.solution = LengthOfLastWord()
    
    def test_single_word(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hola"), 4)

    def test_multiple_words(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hola mundo"), 5)
        self.assertEqual(self.solution.lengthOfLastWord("Python es genial"), 6)

    def test_trailing_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("   Hola mundo   "), 5)

    def test_only_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("    "), 0)

    def test_empty_string(self):
        self.assertEqual(self.solution.lengthOfLastWord(""), 0)

    def test_single_letter_word(self):
        self.assertEqual(self.solution.lengthOfLastWord("A"), 1)
        self.assertEqual(self.solution.lengthOfLastWord("A "), 1)

    def test_mixed_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("   Hola   "), 4)
        self.assertEqual(self.solution.lengthOfLastWord("Hola   mundo    "), 5)

if __name__ == "__main__":
    unittest.main()
