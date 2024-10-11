"""
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    a - o produto do dobro do primeiro com metade do segundo.
    b - a soma do triplo do primeiro com o terceiro.
    c - o terceiro elevado ao cubo.
"""

if __name__ == '__main__':
    print("Cálculo de números.")
    numero_inteiro_1: int = int(input("Digite o primeiro número inteiro:"))
    numero_inteiro_2: int = int(input("Digite o segundo número inteiro:"))
    numero_real: float = float(input("Digite o número real:"))
    primeiro_calculo: float = (numero_inteiro_1*2) * numero_inteiro_2/2
    segundo_calculo: float = (numero_inteiro_1*3) + numero_real
    terceiro_calculo: float = numero_real**3
    print(f"Cálculo A: {primeiro_calculo}")
    print(f"Cálculo B: {segundo_calculo}")
    print(f"Cálculo C: {terceiro_calculo}")
