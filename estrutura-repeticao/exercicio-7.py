"""
    Faça um programa que leia 5 números e informe o maior número
"""
import sys


if __name__ == '__main__':
    print("Maior número")
    lista_numeros: list[int] = []
    maior_numero: int = -sys.maxsize - 1

    for i in range(5):
        numero: int = int(input("Informe um número:"))
        lista_numeros.append(numero)

    for n in lista_numeros:
        if n > maior_numero:
            maior_numero = n

    print(f"Maior número digitado: {maior_numero}")
