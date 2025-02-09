"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que
ele mostre os números um ao lado do outro
"""

if __name__ == '__main__':
    print("Lista de números")

    print("While:")
    numero: int = 1
    while numero <= 20:
        print(f"Número: {numero}")
        numero = numero + 1

    print("For:")
    for indice in range(1, 21, 1):
        print(f"Número: {indice}; ", end="")
