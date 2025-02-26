"""
    A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
    Faça um programa que gere a série até que o valor seja maior que 500.
"""


if __name__ == '__main__':
    print("Fibonacci")

    anterior: int = 0
    proximo: int = 1
    auxiliar: int = 0

    while anterior < 500:
        print(f"N: {anterior}")
        auxiliar = proximo
        proximo = anterior + proximo
        anterior = auxiliar
