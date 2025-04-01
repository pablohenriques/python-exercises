"""
 Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
 seguintes dados:
     a. Código da cidade;
     b. Número de veículos de passeio (em 1999);
     c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
     d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
     e. Qual a média de veículos nas cinco cidades juntas;
     f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""

import sys

if __name__ == '__main__':
    print("Estatísticas sobre carros na cidade")

    dados: dict = {
        'São José dos Campos': {
            'veiculos_passeio': 100,
            'acidentes': 20
        },
        'São Carlos': {
            'veiculos_passeio': 90,
            'acidentes': 10
        },
        'Sorocaba': {
            'veiculos_passeio': 150,
            'acidentes': 30
        },
        'Jacareí': {
            'veiculos_passeio': 80,
            'acidentes': 15
        },
        'Campos do Jordão': {
            'veiculos_passeio': 50,
            'acidentes': 2
        },
    }

    cidade_menos_acidentes: str = ""
    menor_numero_acidentes: int = sys.maxsize

    cidade_mais_acidentes: str = ""
    maior_numero_acidentes: int = -sys.maxsize - 1

    total_veiculos: int = 0
    total_acidentes_menor_2000: int = 0
    total_cidades_menos_2000: int = 0

    for k, v in dados.items():
        acidentes_cidade: int = v["acidentes"]

        if acidentes_cidade  < menor_numero_acidentes:
            cidade_menos_acidentes = k
            menor_numero_acidentes = acidentes_cidade
        elif acidentes_cidade > maior_numero_acidentes:
            cidade_mais_acidentes = k
            maior_numero_acidentes = acidentes_cidade

        if v["veiculos_passeio"] < 2000:
            total_acidentes_menor_2000 += v["acidentes"]
            total_cidades_menos_2000 += 1

        total_veiculos += v["veiculos_passeio"]

    dados_menos_acidentes: dict = dados[cidade_menos_acidentes]
    dados_mais_acidentes: dict = dados[cidade_mais_acidentes]

    media_veiculos = total_veiculos / len(dados)

    media_acidentes_menor_2000_veiculos: int = total_acidentes_menor_2000 / total_cidades_menos_2000

    print(f"Cidade com menos acidentes - {cidade_menos_acidentes}: {dados_menos_acidentes}")
    print(f"Cidade com mais acidentes - {cidade_mais_acidentes}: {dados_mais_acidentes}")
    print(f"Média de veículos - {media_veiculos}")
    print(f"Média de acidentes em cidades com menor de 2000 veículos - {media_acidentes_menor_2000_veiculos}")



