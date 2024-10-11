"""
    Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

if __name__ == '__main__':
    print("Maior e menor número")
    n1: int = int(input("Digite o primeiro número (n1):"))
    n2: int = int(input("Digite o segundo número (n2):"))
    n3: int = int(input("Digite o terceiro número (n3):"))

    maior_numero: int = 0

    if n1 > n2 and n1 > n3:
        maior_numero = n1
    elif n2 > n3:
        maior_numero = n2
    else:
        maior_numero = n3

    print(f"Maior número da sequência [{n1}, {n2}, {n3}]: {maior_numero}")

    menor_numero: int = 0

    if n1 < n2 and n1 < n3:
        menor_numero = n1
    elif n2 < n3:
        menor_numero = n2
    else:
        menor_numero = n3

    print(f"Menor número da sequência [{n1}, {n2}, {n3}]: {menor_numero}")
