"""
    Faça um Programa que pergunte quanto você ganha por hora e
    o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês.
"""

if __name__ == '__main__':
    print("Cálculo do salário")
    valor_hora: float = float(input("Digite o valor da hora:"))
    total_horas_trabalhadas: float = float(input("Digite o total de horas:"))
    salario_total: float = valor_hora * total_horas_trabalhadas
    print(f"Seu salário nesse mês: {salario_total}")
