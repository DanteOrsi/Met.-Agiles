import unittest
from calculadora import sumar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):
    
    # Suma básica: 2+3, resultado esperado: 5
    def test_suma_basica(self):
        self.assertEqual(sumar(2, 3), 5)

    # Manejo de números negativos: -5 + (-2), resultado esperado: -7
    def test_numeros_negativos(self):
        self.assertEqual(sumar(-5, -2), -7)

    # Multiplicación por elemento neutro (Cero): 8*0, resultado esperado: 0
    def test_multiplicacion_cero(self):
        self.assertEqual(multiplicar(8, 0), 0)

    # División con decimales (Precisión): 5/2, resultado esperado: 2.5
    def test_division_decimales(self):
        self.assertEqual(dividir(5, 2), 2.5)

    # Caso de error, división por cero: 10/0, resultado esperado: Error o Exception
    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == '__main__':
    unittest.main()
    