"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
 - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 - A mensagem "Reprovado", se a média for menor do que sete;
 - A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

if __name__ == '__main__':
    print("Aprovação do aluno")
    nota1: float = float(input("Digite a primeira nota:"))
    nota2: float = float(input("Digite a segunda nota:"))
    media: float = (nota1 + nota2) / 2

    if media == 10:
        print(f"Nota: {media}. Aprovado com distinção!")
    elif media >= 7:
        print(f"Nota: {media}. Aprovado.")
    else:
        print(f"Nota: {media}. Reprovado.")
