"""
    Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
    e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0          A
      Entre 7.5 e 9.0           B
      Entre 6.0 e 7.5           C
      Entre 4.0 e 6.0           D
      Entre 4.0 e zero          E
    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
    se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

if __name__ == '__main__':
    print("Conceitos de Aprovação")
    conceito: str = ""
    mensagem: str = ""
    nota: float = float(input("Digite a nota do aluno:"))

    if 9.0 < nota <= 10:
        conceito = "A"
    elif 7.5 < nota <= 9.0:
        conceito = "B"
    elif 6.0 < nota <= 7.5:
        conceito = "C"
    elif 4.0 < nota <= 6.0:
        conceito = "D"
    else:
        conceito = "E"

    if conceito == "A" or conceito == "B" or conceito == "C":
        mensagem = "APROVADO"
    else:
        mensagem = "REPROVADO"

    print(f"Status do aluno: {mensagem}")
