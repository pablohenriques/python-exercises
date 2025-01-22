"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
    O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

if __name__ == '__main__':
    print("Calculo equação segundo grau")
    a: int = int(input("Digite o valor de A: "))

    if a != 0:
        b: int = int(input("Digite o valor de B: "))
        c: int = int(input("Digite o valor de C: "))
        resultado_delta: int = (b*b) - 4 * a * c
        resultado_equacao: str = ""

        if resultado_delta < 0:
            resultado_equacao = "Equação não possui raízes reais"
        elif resultado_delta == 0:
            resultado_equacao = "Equação possui apenas uma raiz real"
        else:
            resultado_equacao = "Equação possui duas raizes reais"

        print(f"Possíveis resultados para equação: {resultado_equacao}")
    else:
        print("Não é uma equação de segundo grau. Digite outro valor.")
