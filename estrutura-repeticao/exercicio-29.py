"""
    O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
    Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o
    número de itens que o cliente comprou e ao lado o valor da conta.
    Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela
    de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os
    preços de 1 até 50 produtos, conforme o exemplo abaixo:
        Lojas Quase Dois - Tabela de preços
            1 - R$ 1.99
            2 - R$ 3.98
            ...
            50 - R$ 99.50
"""


if __name__ == '__main__':
    print("Automação de Preços - Lojinha")

    lista_precos: dict = {}
    valor_base: float = 1.99

    for indice in range(1, 51, 1):
        # preco: float = float(input(f"Digite o preco do produto {indice}:"))
        lista_precos[indice] = valor_base * indice

    print(f"Preço dos produtos: {lista_precos}")

