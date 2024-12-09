import unittest
from isPalindrome import IsPalindrome

class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.isPalindrome = IsPalindrome()

    def test_positive_palindrome(self):
        print("")
        print("Caso donde el número es un palíndromo positivo")
        self.assertTrue(self.isPalindrome.isPalindrome(121))

    def test_positive_non_palindrome(self):
        print("")
        print("Caso donde el número no es un palíndromo positivo")
        self.assertFalse(self.isPalindrome.isPalindrome(123))

    def test_negative_number(self):
        print("")
        print("Caso donde el número es negativo y no debería ser un palíndromo")
        self.assertFalse(self.isPalindrome.isPalindrome(-121))

    def test_zero(self):
        print("")
        print("Caso especial de cero, que es palíndromo")
        self.assertTrue(self.isPalindrome.isPalindrome(0))

    def test_large_palindrome(self):
        print("")
        print("Caso con un número grande que es un palíndromo")
        self.assertTrue(self.isPalindrome.isPalindrome(1234321))

    def test_large_non_palindrome(self):
        print("")
        print("Caso con un número grande que no es un palíndromo")
        self.assertFalse(self.isPalindrome.isPalindrome(1234567))


if __name__ == '__main__':
    unittest.main()