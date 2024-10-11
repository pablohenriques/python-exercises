"""
    Faça um programa para uma loja de tintas.
    O programa deverá pedir o tamanho em metros quadrados
    da área a ser pintada. Considere que a cobertura da tinta
    é de 1 litro para cada 3 metros quadrados e que a tinta
    é vendida em latas de 18 litros, que custam R$ 80,00.
    Informe ao usuário a quantidades de latas de tinta a
    serem compradas e o preço total.
"""
import math

if __name__ == '__main__':
    print("Cálculo quantidade de litros")
    metros_quadrados: float = float(input("Digite o valor em metros quadrados:"))
    litros: float = metros_quadrados / 3.0
    quantidade_latas: float = math.ceil(litros / 18)
    valor_toral: float = quantidade_latas * 80
    print(f"Quantidade de latas: {quantidade_latas}")
    print(f"Valor total: {valor_toral} reais")
