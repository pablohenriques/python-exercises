"""
    Faça um programa que calcule o número médio de alunos por turma.
    Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
    As turmas não podem ter mais de 40 alunos
"""
if __name__ == '__main__':
    print("Número médio alunos por turma")

    condicao: bool = True
    turmas: dict = {}
    identificador: int = 1


    while condicao:
        quantidade_aluno: int = int(input("Digite a quantidade de alunos da turma:"))

        if quantidade_aluno > 40:
            print("Quantidade de alunos não permitda. Digite novamente.")
        else:
            turmas[identificador] = quantidade_aluno
            identificador += 1

        verificacao: str = input("Deseja continuar ? S-sim, N-não:")

        if verificacao == "N":
            condicao = False

    total_turmas: int = len(list(turmas.keys()))
    total_alunos: int = sum(list(turmas.values()))
    media_turmas: float = total_alunos/total_turmas

    print(f"Total de Turmas: {total_turmas}")
    print(f"Total de Alunos: {total_alunos}")
    print(f"Media de alunos por turma: {media_turmas}")
