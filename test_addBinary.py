import unittest
from addBinary import AddBinary


class TestAddBinary(unittest.TestCase):

    def setUp(self):
        self.add_binary = AddBinary()
    def test_simple_case(self):
        self.assertEqual(self.add_binary.addBinary("1010", "1011"), "10101", "Suma básica fallida")
    
    def test_with_carry(self):
        self.assertEqual(self.add_binary.addBinary("1", "1"), "10", "Caso con acarreo fallido")

    def test_large_numbers(self):
        self.assertEqual(self.add_binary.addBinary("1111", "1111"), "11110", "Suma de números grandes fallida")

    def test_zero_case(self):
        self.assertEqual(self.add_binary.addBinary("0", "0"), "0", "Caso con ceros fallido")
        self.assertEqual(self.add_binary.addBinary("0", "1010"), "1010", "Suma con cero fallida")

    def test_mixed_length(self):
        self.assertEqual(self.add_binary.addBinary("101", "1"), "110", "Caso de longitud mixta fallido")
        self.assertEqual(self.add_binary.addBinary("1", "101"), "110", "Caso de longitud mixta inversa fallido")

if __name__ == "__main__":
    unittest.main()
