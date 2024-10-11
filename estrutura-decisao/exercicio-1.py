"""
    Faça um Programa que peça dois números e imprima o maior deles.
"""

if __name__ == '__main__':
    print("O maior número")
    numero1: int = int(input("Digite o primeiro número:"))
    numero2: int = int(input("Digite o segundo número:"))
    maior_numero: int = 0

    if numero1 > numero2:
        maior_numero = numero1
    elif numero2 > numero1:
        maior_numero = numero2

    print(f"Maior número: {maior_numero}")
