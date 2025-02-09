"""
    Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50
"""

if __name__ == '__main__':
    print("Números Ímpares")

    for n in range(1, 51, 1):
        if n % 2 !=0:
            print(f"Número Ímpar: {n}")
