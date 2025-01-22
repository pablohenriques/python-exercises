"""
    Faça um Programa para leitura de três notas parciais de um aluno.
    O programa deve calcular a média alcançada por aluno e presentar:
    a. A mensagem "Aprovado", se a média for maior ou igual a 7,
        com a respectiva média alcançada;
    b. A mensagem "Reprovado", se a média for menor do que 7,
        com a respectiva média alcançada;
    c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""


if __name__ == '__main__':
    print("Média do aluno")
    nota_1: float = float(input("Digite a primeira nota: "))
    nota_2: float = float(input("Digite a segunda nota: "))
    nota_3: float = float(input("Digite a terceira nota: "))

    media_aluno: float = (nota_1 + nota_2 + nota_3) / 3
    mensagem_aprovacao: str = ""

    if media_aluno >= 7.0:
        if media_aluno == 10.0:
            mensagem_aprovacao = "Aprovado com distinção"
        else:
            mensagem_aprovacao = "Aprovado"
    else:
        mensagem_aprovacao = "Reprovado"

    print(f"Status do aluno (a): {mensagem_aprovacao}")
