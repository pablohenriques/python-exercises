"""
    Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
        a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
        b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
        c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
    Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
    que o usuário digite o salário inicial do funcionário.
 """
from datetime import datetime

if __name__ == '__main__':
    print("Cálculo Salário.")
    salarios: dict = dict()
    ano_atual: int = int(datetime.now().year)
    aumento_base: float = 0.015

    while True:
        nome_funcionario: str = input("Digite o nome do funcionário:")
        ano_entrada: int = int(input("Digite o ano de entrada do funcionário:"))
        salario_inicial: float = int(input("Infome o valor do salário:"))
        periodo: int = ano_atual-ano_entrada
        salario_atual: float = salario_inicial

        for ano in range(ano_entrada, ano_atual, 1):
            if ano <= 1996:
                aumento: float = salario_atual * 0.015
                salario_atual += round(aumento, 2)
            else:
                aumento: float = (salario_atual * 0.015) * 2
                salario_atual += round(aumento, 2)

        salarios[nome_funcionario] = salario_atual

        opcao: str = input("Inserir novo funcionário ? S-sim/N-não:")

        if opcao == "N":
            break

    print(f"Salários: {salarios}")
