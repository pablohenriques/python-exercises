"""
    O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                        Até 5 Kg                Acima de 5 Kg
        File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
        Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
        Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
    porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
    cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
    e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e
    quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
if __name__ == '__main__':
    print("Organizações Tabajara tum dum dum dum")

    preco_primeira_carne: float = 0.0
    preco_segunda_carne: float = 0.0

    cartao: str = input("Cliente usará cartão Tabajara? S-Sim/N-Não:")
    primeiro_tipo_carne: str = input("Digite o primeiro tipo de carne, FD-Filé Duplo, A-Alcatra, P-Picanha:")
    qtd_primeira_carne: float = float(input("Digite a quantidade (Kg) de carne:"))

    if primeiro_tipo_carne == "FD":
        if qtd_primeira_carne > 5:
            preco_primeira_carne = 5.80
        else:
            preco_primeira_carne = 4.90
    elif primeiro_tipo_carne == "A":
        if qtd_primeira_carne > 5:
            preco_primeira_carne = 6.80
        else:
            preco_primeira_carne = 5.90
    elif primeiro_tipo_carne == "P":
        if qtd_primeira_carne > 5:
            preco_primeira_carne = 7.80
        else:
            preco_primeira_carne = 6.90
    else:
        print("Essa opção de carne não está disponível!")

    segundo_tipo_carne: str = input("Digite o segundo tipo de carne, FD-Filé Duplo, A-Alcatra, P-Picanha:")
    qtd_segunda_carne: float = float(input("Digite a quantidade (Kg) de carne:"))

    if segundo_tipo_carne == "FD":
        if qtd_segunda_carne > 5:
            preco_segunda_carne = 5.80
        else:
            preco_segunda_carne = 4.90
    elif segundo_tipo_carne == "A":
        if qtd_segunda_carne > 5:
            preco_segunda_carne = 6.80
        else:
            preco_segunda_carne = 5.90
    elif segundo_tipo_carne == "P":
        if qtd_segunda_carne > 5:
            preco_segunda_carne = 7.80
        else:
            preco_segunda_carne = 6.90
    else:
        print("Essa opção de carne não está disponível!")

    total_primera_carne: float = qtd_primeira_carne * preco_primeira_carne
    total_segunda_carne: float = qtd_segunda_carne * preco_segunda_carne
    total_valor: float = total_primera_carne + total_segunda_carne

    desconto: float = 0.0
    valor_com_desconto: float = total_valor
    if cartao == "S":
        desconto = (total_valor * 0.05)
        valor_com_desconto = total_valor - desconto

    print("*********************************************************************")
    print("**************************Mercado Tabajara***************************")
    print(f"{primeiro_tipo_carne} - {qtd_primeira_carne}: {total_primera_carne}")
    print(f"{segundo_tipo_carne} - {qtd_segunda_carne} : {total_segunda_carne}")
    print(f"Desconto: {desconto}")
    print(f"Valor com desconto: {valor_com_desconto}")
    print(f"Total: {total_valor}")
    print("*********************************************************************")
