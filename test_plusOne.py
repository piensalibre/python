import unittest
from plusOne import PlusOne


class TestPlusOne(unittest.TestCase):
    def setUp(self):
        
        self.solver = PlusOne()

    def test_no_carry(self):
        
        self.assertEqual(self.solver.plusOne([1, 2, 3]), [1, 2, 4])

    def test_single_digit_no_carry(self):
        
        self.assertEqual(self.solver.plusOne([5]), [6])

    def test_single_digit_carry(self):
        
        self.assertEqual(self.solver.plusOne([9]), [1, 0])

    def test_with_carry(self):
        
        self.assertEqual(self.solver.plusOne([4, 3, 9]), [4, 4, 0])

    def test_full_carry(self):
        
        self.assertEqual(self.solver.plusOne([9, 9, 9]), [1, 0, 0, 0])

    def test_empty_list(self):
        
        self.assertEqual(self.solver.plusOne([]), [1])

    def test_zero(self):
        
        self.assertEqual(self.solver.plusOne([0]), [1])


if __name__ == '__main__':
    unittest.main()
