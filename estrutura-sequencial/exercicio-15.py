"""
    Faça um Programa que pergunte quanto você ganha por hora e o
    número de horas trabalhadas no mês. Calcule e mostre o total do seu
    salário no referido mês, sabendo-se que são descontados 11% para o
    Imposto de Renda, 8% para o INSS e 5% para o sindicato,
    faça um programa que nos dê:
        a) salário bruto.
        b) quanto pagou ao INSS.
        c) quanto pagou ao sindicato.
        d) o salário líquido.
        e) calcule os descontos e o salário líquido, conforme a tabela abaixo:

            + Salário Bruto : R$
            - IR (11%) : R$
            - INSS (8%) : R$
            - Sindicato ( 5%) : R$
            = Salário Liquido : R$

        Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

if __name__ == '__main__':
    print("Cálculo valores salários")
    horas_trabalhos: int = int(input("Digite sua horas de tabralho:"))
    valor_hora: int = int(input("Digite o valor da hora:"))
    salario_bruto: int = horas_trabalhos * valor_hora
    valor_inss: float = (salario_bruto * 0.08)
    valor_sindicato: float = (salario_bruto * 0.05)
    valor_ir: float = (salario_bruto * 0.11)
    salario_liquido = salario_bruto - (valor_inss + valor_sindicato + valor_ir)
    print(f"Salário Bruto: {salario_bruto}")
    print(f"Valor do Inss: {valor_inss}")
    print(f"Valor Sindicato: {valor_sindicato}")
    print(f"Salário Líquido: {salario_liquido}")
