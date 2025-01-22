"""
    Faça um Programa para um caixa eletrônico. O programa deverá perguntar
    ao usuário a valor do saque e depois informar quantas notas de cada valor
    serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100
    reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
    O programa não deve se preocupar com a quantidade de notas
    existentes na máquina.

    a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
        notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

    b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
    três notas de 100, uma nota de 50,
    quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

if __name__ == '__main__':
    print("Caixa Eletrônico")
    valor: int = int(input("Digite o valor de saque:"))

    if valor < 10 or valor > 600:
        print("Valor excede o limite de saque")
    else:
        notas_100: int = valor // 100
        notas_50: int = (valor % 100) // 50
        notas_10: int = ((valor % 100) % 50) // 10
        notas_5: int = (((valor % 100) % 50) % 10) // 5
        notas_1: int = ((((valor % 100) % 50) % 10) % 5) // 1

        print(f""
              f"Notas de 100: {notas_100}, "
              f"50: {notas_50}, "
              f"10: {notas_10}, "
              f"5: {notas_5}, "
              f"1: {notas_1}")
