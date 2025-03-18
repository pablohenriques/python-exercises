"""
    Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o
    mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua
    altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
    Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais
    gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""

if __name__ == '__main__':
    print("Dados da academia")

    condicao: bool = True
    dados_clientes: dict = {}

    media_altura: float = 0
    media_peso: float = 0

    menor_altura: float = 999
    maior_altura: float = 0
    maior_peso: float = 0
    menor_peso: float = 999

    cod_maior_cliente: int = 0
    cod_menor_cliente: int = 0
    cod_mais_pesado_cliente: int = 0
    cod_mais_magro_cliente: int = 0

    while condicao:
        dados: str = input("Digite no padrão, 'código,altura,peso':")

        if dados.isnumeric() and int(dados) == 0:
            condicao = False
        else:
            cliente: list = dados.split(",")
            dados_clientes[cliente[0]] = [float(cliente[1]), float(cliente[2])]

    for k, v in dados_clientes.items():

        if float(v[0]) > maior_altura:
            maior_altura = v[0]
            cod_maior_cliente = k

        if float(v[0]) < menor_altura:
            menor_altura = v[0]
            cod_menor_cliente = k

        if float(v[1]) > maior_peso:
            maior_peso = v[1]
            cod_mais_pesado_cliente = k

        if float(v[1]) < menor_peso:
            menor_peso = v[1]
            cod_mais_magro_cliente = k

    media_altura = sum([v[0] for v in dados_clientes.values()]) / len(dados_clientes)
    media_peso = sum([v[1] for v in dados_clientes.values()]) / len(dados_clientes)

    print(f"Cliente mais alto {cod_maior_cliente}: {dados_clientes[cod_maior_cliente]}")
    print(f"Cliente mais baixo {cod_menor_cliente}: {dados_clientes[cod_menor_cliente]}")
    print(f"Cliente mais pesado {cod_mais_pesado_cliente}: {dados_clientes[cod_mais_pesado_cliente]}")
    print(f"Cliente mais magro {cod_mais_magro_cliente}: {dados_clientes[cod_mais_magro_cliente]}")
    print(f"\nMédia de altura dos clientes: {media_altura}")
    print(f"\nMédia de peso dos clientes: {media_peso}")
