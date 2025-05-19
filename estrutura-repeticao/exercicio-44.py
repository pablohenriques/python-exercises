"""Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

    1, 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco

Faça um programa que calcule e mostre:

    O total de votos para cada candidato
    O total de votos nulos
    O total de votos em branco
    A percentagem de votos nulos sobre o total de votos
    A percentagem de votos em branco sobre o total de votos

Para finalizar o conjunto de votos tem-se o valor zero. """


if __name__ == '__main__':
    print('Eleições')
    votos: dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}

    while True:
        opcao: int = int(input('Informe o número de um candidato, 5-nulo, 6-branco ou "0" para sair:'))

        if opcao not in (1, 2, 3, 4, 5, 6):
            break
        else:
            votos[str(opcao)] += 1

    total_votos: int = sum([n for n in votos.values()])
    porcentagem_brancos: float =  (votos['6'] / total_votos) * 100
    porcentagem_nulos: float =  (votos['5'] / total_votos) * 100

    print(f'Total votos em branco: {votos["6"]}')
    print(f'Total votos nulos: {votos["5"]}')
    print(f'Votos - 1:{votos["1"]} - 2:{votos["2"]} - 3:{votos["3"]} - 4:{votos["4"]}')
    print(f'% votos nulos: {porcentagem_nulos}')
    print(f'% votos brancos: {porcentagem_nulos}')
