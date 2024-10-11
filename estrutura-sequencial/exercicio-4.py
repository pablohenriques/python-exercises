"""
    Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

if __name__ == '__main__':
    print("Digite suas notas bimestrais abaixo:")
    bimestre1 = float(input("Primeiro bimestre:"))
    bimestre2 = float(input("Segundo bimestre:"))
    bimestre3 = float(input("Terceiro bimestre:"))
    bimestre4 = float(input("Quarto bimestre:"))
    notas = (bimestre1, bimestre2, bimestre3, bimestre4)
    media = sum(notas) / 4
    print(f"Média final: {media}")
