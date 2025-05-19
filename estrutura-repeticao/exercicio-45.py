"""
    Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
    aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e
    a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se
    outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

    Maior e Menor Acerto
    Total de Alunos que utilizaram o sistema
    A Média das Notas da Turma

    * Gabarito
        Questão 	Resposta 	Questão 	Resposta
        1 	            A 	        6       	E
        2 	            B 	        7 	        D
        3 	            C 	        8 	        C
        4 	            D 	        9 	        B
        5 	            E 	        10 	        A
    Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes
    dos alunos usarem o programa.
"""
import random

if __name__ == '__main__':
    print('Cálculo notas')
    resposta: dict = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'E', '7': 'D', '8': 'C', '9': 'B', '10': 'A'}
    aluno1: dict = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'E', '7': 'D', '8': 'C', '9': 'B', '10': 'A'}
    aluno2: dict = {'1': 'C', '2': 'A', '3': 'A', '4': 'A', '5': 'C', '6': 'B', '7': 'C', '8': 'D', '9': 'A', '10': 'D'}
    lista_alunos: list[dict] = [aluno1, aluno2]

    notas: dict = dict()

    for aluno in lista_alunos:
        id_aluno = random.randint(100, 200)
        nota = len(aluno.items() & resposta.items())
        notas[id_aluno] = nota

    maior_nota: int = max(notas, key=notas.get) # AI help
    menor_nota: int = min(notas, key=notas.get) # AI help
    total_alunos: int = len(lista_alunos)

    print(f'Maior nota:', maior_nota)
    print(f'Menor nota:', menor_nota)
    print(f'Total alunos:', total_alunos)



