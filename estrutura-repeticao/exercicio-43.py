"""
    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser
    pago por ‘item’ (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o
    pedido deve ser encerrado. O cardápio de um café é o seguinte:
    Especificação	Código	Preço
    Cachorro Quente	100	    R$1,20
    Bauru Simples	101	    R$1,30
    Bauru com ovo	102	    R$1,50
    Hambúrguer	    103	    R$1,20
    Cheeseburguer	104	    R$1,30
    Refrigerante	105	    R$1,0
"""


if __name__ == '__main__':
    print("Conta de lanchonete")
    produtos: dict = {
        100: {'preco': 1.20, 'especificacao': 'Cachorro Quente'},
        101: {'preco': 1.30, 'especificacao': 'Bauru Simples'},
        102: {'preco': 1.50, 'especificacao': 'Bauru com Ovo'},
        103: {'preco': 1.20, 'especificacao': 'Hambúrguer'},
        104: {'preco': 1.30, 'especificacao': 'Cheeseburguer'},
        105: {'preco': 1.00, 'especificacao': 'Refrigerante'},
    }
    lista_produtos: dict = dict()
    total: float = 0

    while True:
        opcao: str = input("Inserir produto - I ou Finalizar - F?:")

        if opcao == "F":
            break

        cod_produto: int = int(input("Informe o código do produto:"))
        qtd_produto: int = int(input("Informe quantos produtos foram consumidos:"))
        total_parcial: float = produtos[cod_produto]['preco'] * qtd_produto
        lista_produtos[f'{produtos[cod_produto]["especificacao"]}'] = {
            'quantidade': qtd_produto,
            'total': total_parcial
        }

    for k,v in lista_produtos.items():
        total += v['total']

    [
        print(f'\nProduto: {k}. Quantidade: {v['quantidade']}. Valor: {v['total']}\n')
        for k,v in lista_produtos.items()
    ]

    print(f'Valor total: {total}')
