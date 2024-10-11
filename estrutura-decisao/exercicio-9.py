"""
 Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

if __name__ == '__main__':
    print("Números descrescentes")
    n1: int = int(input("Digite o primeiro número:"))
    n2: int = int(input("Digite o segundo número:"))
    n3: int = int(input("Digite o terceiro número:"))

    maior_numero: int = 0
    meio_numero: int = 0
    menor_numero: int = 0
    if n1 > n2 and n1 > n3:
        maior_numero = n1
        if n2 > n3:
            meio_numero = n2
            menor_numero = n3
        else:
            meio_numero = n3
            menor_numero = n2

    elif n2 > n1 and n2 > n3:
        maior_numero = n2
        if n1 > n3:
            meio_numero = n1
            menor_numero = n3
        else:
            meio_numero = n3
            menor_numero = n1
    elif n3 > n2 and n3 > n1:
        maior_numero = n3
        if n2 > n1:
            meio_numero = n2
            menor_numero = n1
        else:
            meio_numero = n1
            menor_numero = n2
    elif n1 == n2:
        pass

    print(f"Números em ordem decrescente: {maior_numero}, {meio_numero}, {menor_numero}")
