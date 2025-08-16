"""
    Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
    No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
    O seu resultado fica sendo a média dos três valores restantes.
    Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
    informe a média dos saltos conforme a descrição acima informada
    (retirar o melhor e o pior salto e depois calcular a média).
    Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução,
    portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta.
"""
class Atleta:

    def __init__(self, nome: str, saltos: list[float], media: float, melhor: float, pior: float):
        self.nome = nome
        self.saltos = saltos
        self.media = media
        self.melhor = melhor # melhor salto
        self.pior = pior     # pior salto


if __name__ == '__main__':
    lista_saltadores: list = list()

    while True:
        nome = input("Informe o nome do atleta ou digite 'Enter' para sair:")

        if len(nome) < 1:
            break
        else:
            lista_temporaria: list[float] = []
            lista_saltos: list[float] = []
            for _ in range(5):
                valor_salto: float = float(input("Informe o valor do salto:"))
                lista_temporaria.append(valor_salto)
            lista_saltos = lista_temporaria.copy()
            melhor_salto: float = max(lista_temporaria)
            pior_salto: float = min(lista_temporaria)
            lista_temporaria.remove(melhor_salto)
            lista_temporaria.remove(pior_salto)
            media_saltador: float = sum(lista_temporaria) / len(lista_temporaria)
            lista_saltadores.append(Atleta(nome, lista_temporaria, media_saltador, melhor_salto, pior_salto))

    for atleta in lista_saltadores:
        print(f'Atleta: {atleta.nome}\n')
        numero_salto: int = 1
        for salto in atleta.saltos:
            print(f"Salto: {numero_salto}: {salto}")
            numero_salto += 1
        print(f'Melhor salto: {atleta.melhor}')
        print(f'Pior salto: {atleta.pior}')
        print(f'Média: {atleta.media}\n')
        print('Resultado Final')
        print(f'{atleta.nome}: {atleta.media}')
