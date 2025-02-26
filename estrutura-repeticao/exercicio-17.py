"""
    Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""


if __name__ == '__main__':
    print("Fatorial de um número")

    numero: int = int(input("Digite um número para fatorial:"))
    resultado: int = 1

    while numero > 1:
        resultado *= numero
        numero = numero - 1
    print(resultado)
