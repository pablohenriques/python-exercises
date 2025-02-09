""" Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por
eles"""

if __name__ == '__main__':
    print("Intervalo de Números")

    n1: int = int(input("Digite o início do intervalo:"))
    n2: int = int(input("Digite o fim do intervalo:"))
    condicao: int = 1
    limite: int = n2

    if n1 == 0 and n2 > 0:
        condicao = 1
        limite += 1
    elif n1 == 0 and n2 < 0:
        condicao = -1
        limite -= 1
    elif n1 > 0 and n2 == 0:
        condicao = -1
        limite -= 1
    elif n1 < 0 and n2 == 0:
        condicao = 1
        limite += 1
    elif (n1 < 0 and n2 < 0) and n1 > n2:
        condicao = -1
        limite -= 1
    elif (n1 < 0 and n2 < 0) and n1 < n2:
        condicao = 1
        limite += 1
    elif (n1 > 0 and n2 > 0) and n1 < n2:
        condicao = 1
        limite += 1
    elif (n1 > 0 and n2 > 0) and n1 > n2:
        condicao = -1
        limite -= 1
    elif n1 > 0 and n2 < 0:
        condicao = -1
        limite -= 1
    elif n1 < 0 and n2 > 0:
        condicao = 1
        limite += 1

    for i in range(n1, limite, condicao):
        print(i)