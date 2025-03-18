"""
    O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
    Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido
    de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o
    final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente
    forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto
    inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
        Lojas Tabajara
            Produto 1: R$ 2.20
            Produto 2: R$ 5.80
            Produto 3: R$ 0
            Total: R$ 9.00
            Dinheiro: R$ 20.00
            Troco: R$ 11.00
            ...
"""


if __name__ == '__main__':
    print("Caixa registradora")

    condicao: int = 1
    produtos: dict = {}
    identificador: int = 0

    while condicao != 0:
        preco_produto: float = float(input("Informe o preço do produto:"))

        if preco_produto == 0:
            condicao = 0
        else:
            identificador += 1
            produtos[identificador] = preco_produto

    total_produtos = sum(produtos.values())
    print(f"Valor total da compra: {total_produtos}")

    pagamento: float = float(input("Informe o valor de pagamento:"))
    print(f"Valor de pagamento: {pagamento}")

    troco = pagamento - total_produtos
    print(f"Troco: {troco}")
