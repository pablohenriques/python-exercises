"""
    Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
    representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
    alto e número do aluno mais baixo, junto com suas alturas.
"""

if __name__ == '__main__':
    print("Dados alunos")
    dados_alunos: dict = {
        1: 1.90,
        2: 1.95,
        3: 1.85,
        4: 1.89,
        5: 1.70,
        6: 1.75,
        7: 1.65,
        8: 1.85,
        9: 1.80,
        10: 2.00
    }

    indice_maior_aluno: int = max(dados_alunos, key=dados_alunos.get)
    indice_menor_aluno: int = min(dados_alunos, key=dados_alunos.get)

    print(f"Maior aluno. Índice: {indice_maior_aluno}: {dados_alunos[indice_maior_aluno]}")
    print(f"Maior aluno. Índice: {indice_menor_aluno}: {dados_alunos[indice_menor_aluno]}")
