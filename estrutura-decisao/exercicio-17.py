"""
    Faça um Programa que peça um número correspondente a um determinado ano e
    em seguida informe se este ano é ou não bissexto.
"""

if __name__ == '__main__':
    print("Descobrindo Ano Bissexto")
    ano: int = int(input("Digite o ano: "))
    ano_bissexto: bool = False
    calculo_ano_divisivel_4: float = ano%4
    calculo_ano_divisivel_100: float = ano%100
    calculo_ano_divisivel_400: float = ano%400

    if calculo_ano_divisivel_4 == 0.0:
        if calculo_ano_divisivel_100 != 0.0:
            ano_bissexto = True
        elif (calculo_ano_divisivel_100 == 0.0 and
              calculo_ano_divisivel_400 == 0.0):
            ano_bissexto = True
        else:
            ano_bissexto = False
    else:
        ano_bissexto = False

    print(f"{ano} é um ano bissexto: {ano_bissexto}")
