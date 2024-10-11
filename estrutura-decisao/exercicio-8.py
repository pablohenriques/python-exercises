"""
    Faça um programa que pergunte o preço de três produtos e
    informe qual produto você deve comprar, sabendo que a
    decisão é sempre pelo mais barato.
"""

if __name__ == '__main__':
    print("Produto mais barato")
    prod1: float = float(input("Digite o preço do primeiro produto:"))
    prod2: float = float(input("Digite o preço do segundo produto:"))
    prod3: float = float(input("Digite o preço do terceiro produto:"))
    prod_selecionado: float = 0.0

    if prod1 < prod2 and prod1 < prod3:
        prod_selecionado = prod1
    elif prod2 < prod3:
        prod_selecionado = prod2
    else:
        prod_selecionado = prod3

    print(f"O produto mais barato: {prod_selecionado}")
