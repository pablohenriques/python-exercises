"""
    Faça um Programa que leia três números e mostre o maior deles
"""

if __name__ == '__main__':
    print("Maior número")
    n1: int = int(input("Digite o primeiro número:"))
    n2: int = int(input("Digite o segundo número:"))
    n3: int = int(input("Digite o terceiro número:"))

    maior_numero: int = 0

    if n1 > n2 and n1 > n3:
        maior_numero = n1
    elif n2 > n3:
        maior_numero = n2
    else:
        maior_numero = 3

    print(f"Maior número da sequência [{n1}, {n2}, {n3}]: {maior_numero}")
