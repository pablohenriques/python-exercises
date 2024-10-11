"""
    Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

if __name__ == '__main__':
    print("Número negativo ou positivo")
    numero: int = int(input("Digite um valor: "))

    if numero > 0:
        print(f"Número {numero} é positivo")
    elif numero < 0:
        print(f"O número {numero} é negativo")
    else:
        print(f"O número {numero} é igual a zero")
