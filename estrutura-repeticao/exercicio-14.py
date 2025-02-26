"""
    Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
    números impares
"""
import random

if __name__ == '__main__':
    print("Número pares e ímpares")
    lista_numeros: list[int] = [random.randrange(0, 100) for _ in range(10)]
    quantidade_numeros_pares: int = 0
    quantidade_numeros_impares: int = 0

    for n in lista_numeros:
        if n % 2 == 0:
            quantidade_numeros_pares += 1
        else:
            quantidade_numeros_impares += 1

    print(f"Lista: {lista_numeros}")
    print(f"Quantidade Números Pares: {quantidade_numeros_pares}")
    print(f"Quantidade Números Ímpares: {quantidade_numeros_impares}")
