"""
Faça um programa para o cálculo de uma folha de pagamento,sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""

if __name__ == '__main__':
    print("Folha de Pagamento")
    salario_bruto: float = float(input("Digite o valor do salário:"))

    sindicato: float = 0.3
    fgts: float = 0.11
    ir: list[float] = [0.05, 0.1, 0.2]
    inss: float = 0.1
    salario_liquido: float = 0.0
    valor_ir: float = 0.0

    valor_sindicato: float = salario_bruto * sindicato
    valor_inss: float = salario_bruto * inss
    valor_fgts: float = salario_bruto * fgts
    total_descontos: float = valor_inss

    if salario_bruto <= 900:
        salario_liquido = salario_bruto
    elif salario_bruto <= 1500:
        valor_ir: float = salario_bruto * ir[0]
        total_descontos += valor_ir
        salario_liquido = salario_bruto - total_descontos
    elif salario_bruto < 2500:
        valor_ir: float = salario_bruto * ir[1]
        total_descontos += valor_ir
        salario_liquido = salario_bruto - total_descontos
    else:
        valor_ir: float = salario_bruto * ir[2]
        total_descontos += valor_ir
        salario_liquido = salario_bruto - total_descontos

    print(f"Salário Bruto: {salario_bruto}")
    print(f"IR: {valor_ir}")
    print(f"INSS: {valor_inss}")
    print(f"FGTS: {valor_fgts}")
    print(f"Total de descontos: {total_descontos}")
    print(f"Salário Líquido: {salario_liquido}")
