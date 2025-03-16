"""
    Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
    A saída deve ser conforme o exemplo abaixo:
"""


if __name__ == '__main__':
    print("Fatorial")

    numero: int = int(input("Informe um número para o fatorial:"))
    acumulador: int = 1

    for n in range(numero, 0, -1):
        acumulador *= n

    print(f"Fatorial: {acumulador}")
