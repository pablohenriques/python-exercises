"""
    Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                        Até 5 Kg                Acima de 5 Kg
        Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
        Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
    desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
    (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

if __name__ == '__main__':
    print("Cálculo para Kitanda")

    qtd_morango: float = float(input("Digite a quantidade de morango:"))
    qtd_maca: float = float(input("Digite a quantidade de morango:"))
    valor_total_morango: float = 0.0
    valor_total_maca: float = 0.0

    if qtd_morango > 5:
        valor_total_morango = qtd_morango * 2.20
    else:
        valor_total_morango = qtd_morango * 2.50

    if qtd_maca > 5:
        valor_total_maca = qtd_maca * 1.50
    else:
        valor_total_maca = qtd_maca * 1.80

    qtd_total_frutas: float = qtd_morango + qtd_maca
    valor_total_frutas: float = valor_total_morango + valor_total_maca

    if qtd_total_frutas > 8 or valor_total_frutas > 25:
        desconto = valor_total_frutas * 0.1
        valor_total_frutas = valor_total_frutas - desconto

    print(f"Quantidade morango: {qtd_morango} - Valor total: {valor_total_morango}")
    print(f"Quantidade maçã: {qtd_maca} - Valor total: {valor_total_maca}")
    print(f"Quantidade total: {qtd_total_frutas} - Valor total: {valor_total_frutas}")
