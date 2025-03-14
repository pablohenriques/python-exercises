"""
    Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
    votar e ao final mostrar o número de votos de cada candidato.
"""

if __name__ == '__main__':
    condicao = True
    total_votos: int = 0
    candidato1: int = 0
    candidato2: int = 0
    candidato3: int = 0

    while condicao:
        voto: int = int(input("Digite 1, 2 ou 3 para o seu candidato:"))
        total_votos += 1

        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1

        validacao: str = input("Continuar eleição: S-sim ou N-não:")

        if validacao == "N":
            condicao = False

    print(f"Total votos: {total_votos}")
    print(f"Candidato 1: {candidato1}")
    print(f"Candidato 2: {candidato2}")
    print(f"Candidato 3: {candidato3}")


