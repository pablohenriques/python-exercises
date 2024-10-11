"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
    a - Para homens: (72.7*h) - 58
    b - Para mulheres: (62.1*h) - 44.7
"""

if __name__ == '__main__':
    print("Cálculo do peso ideal")
    altura: float = float(input("Digite sua altura:"))
    peso_ideal_homem: float = (72.7*altura) - 58
    peso_ideal_mulher: float = (62.1*altura) - 44.7
    print(f"Peso ideal (homem): {peso_ideal_homem}")
    print(f"Peso ideal (mulher): {peso_ideal_mulher}")
