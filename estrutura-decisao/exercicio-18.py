"""
    Faça um Programa que peça uma data no formato dd/mm/aaaa e
    determine se a mesma é uma data válida.
"""

if __name__ == '__main__':
    print("Data válida")
    dia: int = int(input("Digite o dia usando o formato de dois dígitos: "))
    mes: int = int(input("Digite o mês usando o formato de dois dígitos: "))
    ano: int = int(input("Digite o ano usando o formato de quatro dígitos: "))

    status: bool = True

    if dia < 0 or dia > 31:
        status = False
    if mes < 0 or mes > 12:
        status = False
    if ano < 0:
        status = False

    if status is False:
        print("A data informada não é válida")
    else:
        print(f"Data: {dia}/{mes}/{ano}")
