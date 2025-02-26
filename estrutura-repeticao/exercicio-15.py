"""
    A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
    Faça um programa capaz de gerar a série até o n−ésimo termo
"""


if __name__ == '__main__':
    print("Fibonacci")

    anterior: int = 0
    proximo: int = 1
    auxiliar: int = 0

    numero: int = int(input("Digite um número para a sequência:"))

    for _ in range(numero):
        print(f"N: {anterior}")
        auxiliar = proximo
        proximo = anterior + proximo
        anterior = auxiliar
