import unittest
from operations import soma

class TestOperacoes(unittest.TestCase):

    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -4), -5)

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
