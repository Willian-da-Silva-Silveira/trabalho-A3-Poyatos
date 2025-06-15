import unittest
from unittest.mock import patch
from io import StringIO

# Mock para unidadeEscolhida
class UnidadeMock:
    unidade = "m"
    simboloArea = " m²"
    simboloVolume = " m³"

# Injetando o mock no escopo global
import builtins
builtins.unidadeEscolhida = UnidadeMock()

# Importar ou definir aqui as classes: areaQuadrado, areaRetangulo, etc.

class TestCalculos(unittest.TestCase):

    @patch('builtins.input', side_effect=["3", "4"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_area_quadrado(self, mock_stdout, mock_input):
        obj = areaQuadrado()
        obj.calcular()
        self.assertIn("A área é de 12.00 m²", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["10", "2", "3"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_volume_cubo(self, mock_stdout, mock_input):
        obj = volumeCubo()
        obj.calcular()
        self.assertIn("O volume é de 60.00 m³", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["5", "2"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_area_triangulo(self, mock_stdout, mock_input):
        obj = areaTriangulo()
        obj.calcular()
        self.assertIn("A área é de 5.00 m²", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
