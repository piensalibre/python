import unittest
from typing import List
from twoSum import TwoSum  # Asegúrate de cambiar "tu_archivo" al nombre del archivo donde esté tu clase TwoSum.

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.TwoSum = TwoSum()

    def test_case_basico(self):
        print("")
        print("Probando el caso básico...")
        self.assertEqual(self.TwoSum.twoSum([2, 7, 11, 15], 9), [0, 1], "El resultado esperado es [0, 1]")
    
    def test_con_numeros_negativos(self):
        print("")
        print("Probando con números negativos...")
        self.assertEqual(self.TwoSum.twoSum([-1, -2, -3, -4, -5], -8), [2, 4], "El resultado esperado es [2, 4]")

    def test_con_ceros_y_negativos(self):
        print("")
        print("Probando con ceros y números negativos...")
        self.assertEqual(self.TwoSum.twoSum([0, 4, 3, 0], 0), [0, 3], "El resultado esperado es [0, 3]")
    
    def test_multiple_pares(self):
        print("")
        print("Probando con múltiples pares...")
        self.assertEqual(self.TwoSum.twoSum([3, 3, 4, 5], 6), [0, 1], "El resultado esperado es [0, 1]")

    def test_con_un_solo_numero(self):
        print("")
        print("Probando con un solo número en la lista...")
        self.assertEqual(self.TwoSum.twoSum([5], 10), [])

    def test_sin_solucion(self):
        print("")
        print("Probando sin solución...")
        self.assertEqual(self.TwoSum.twoSum([3, 3, 4, 5], 20), [])
        

if __name__ == "__main__":
    unittest.main()
