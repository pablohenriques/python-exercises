import math
import unittest
from typing import Tuple


def calcular_tinta(area: float) -> Tuple:
    litros_necessarios = area / 3
    latas_necessarias = math.ceil(litros_necessarios / 18)
    preco_total = latas_necessarias * 80
    return latas_necessarias, preco_total


if __name__ == '__main__':
    resultado = calcular_tinta(10)
    print(resultado)


class TestCalculo(unittest.TestCase):
    pass

    def test_calculo_simples(self):
        resultado = calcular_tinta(10)
        self.assertEquals(resultado[0], 1)
        self.assertEquals(resultado[1], 80)

    def test_calculo_intermediario(self):
        resultado = calcular_tinta(50)
        self.assertEquals(resultado[0], 3)
        self.assertEquals(resultado[1], 240)

