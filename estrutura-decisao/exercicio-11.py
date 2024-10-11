"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o
programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""


if __name__ == '__main__':
    print("Reajuste de salário - Organizações Tabajara")
    salario: float = float(input("Digite o salário do colaborador: "))
    valor_reajuste: float = 0

    if salario <= 280:
        valor_reajuste = 0.2
    elif 280 < salario <= 700:
        valor_reajuste = 0.15
    elif 700 < salario <= 1500:
        valor_reajuste = 0.1
    elif salario > 1500:
        valor_reajuste = 0.05
    else:
        print("Salário Inválido")

    valor_aumento: float = salario * valor_reajuste
    salario_atualizado: float = salario + valor_aumento

    print(f"Salário atual: {salario}")
    print(f"Percentual de aumento: {valor_reajuste}")
    print(f"Valor do aumento: {valor_aumento}")
    print(f"Salário atualizado: {salario_atualizado}")
