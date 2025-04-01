"""
    Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor
    dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo:
        Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
        1                       0
        3                       10
        6                       15
        9                       20
        12                      25
    Exemplo de saída do programa:
     Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
        R$ 1.000,00         0                   1               R$  1.000,00
        R$ 1.100,00         100                 3               R$    366,00
        R$ 1.150,00         150                 6               R$    191,67
"""
if __name__ == '__main__':
    print("Juros e parcelas")

    valor: float = float(input("Informe o valor da dívida:"))
    parcelas: int = int(input("Informe o número de parcelas:"))
    juros: float = 0
    valor_final: float = 0

    tabela_juros: dict = {1: 0.0, 3: 0.10, 6: 0.15, 9: 0.20, 12: 0.25}

    for k, v in tabela_juros.items():

        if k == parcelas:
            juros = tabela_juros[k] * valor
            valor_final = valor + juros
            break

    valor_parcela: float = round((valor_final / parcelas),2)

    print(f"Valor dívida: {valor}")
    print(f"Juros: {juros}")
    print(f"Quantidade de parcelas: {parcelas}")
    print(f"Valor parcela: {valor_parcela}")