"""
    Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o
    valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""

if __name__ == '__main__':
    print("Valor Total Coleções")

    condicao: bool = True
    quantidade_cd: int = 0
    valor_total: float = 0

    while condicao:
        valor_cd: float = float(input("Informe o valor do CD:"))
        if valor_cd < 1:
            print("Valor inválido. Digite novamente!")
        else:
            quantidade_cd += 1
            valor_total += valor_cd

        opcao: str = input("Deseja inserir mais um cd? S-sim/N-não:")
        if opcao == "N":
            condicao = False

    valor_medio: float = valor_total/quantidade_cd

    print(f"Total de CDs: {quantidade_cd}")
    print(f"Valor total CDs: {valor_total}")
    print(f"Valor médio por CD: {valor_medio}")