"""
    Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
    A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
    Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados
    alcançadas pelo atleta em sua apresentação e depois informe a sua média,
    conforme a descrição acima informada
    (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
    As notas não são informados ordenadas.
"""


class Atleta:

    def __init__(self, nome: str, notas: list[float], melhor_nota: float, pior_nota: float):
        self.nome: str = nome
        self.notas: list[float] = notas
        self.melhor_nota: float = melhor_nota
        self.pior_nota: float = pior_nota
        self.media: float = self.__media()

    def __media(self) -> float:
        lista_temporaria: list[float] = self.notas.copy()
        lista_temporaria.remove(self.melhor_nota)
        lista_temporaria.remove(self.pior_nota)
        return sum(lista_temporaria) / len(lista_temporaria)


if __name__ == '__main__':
    lista_atletas: list[Atleta] = list()

    while True:
        nome: str = input("Digite o nome do atleta:")
        entrada_notas: str = input("Digite as notas separadas por ponto-e-vírgula:")
        notas: list = [float(x) for x in entrada_notas.split(";")]
        melhor_nota: float = max(notas)
        pior_nota: float = min(notas)
        atleta = Atleta(nome, notas, melhor_nota, pior_nota)
        lista_atletas.append(atleta)

        flag: str = input("Inserir novo atleta ? S-sim ou N-não:")
        if flag == "S":
            continue
        elif flag == "N":
            break
        else:
            print("Programa encerrado. Opção não encotrada")

    for atleta in lista_atletas:
        print(f"Nome: {atleta.nome}")
        for nota in atleta.notas:
            print(f"Nota: {nota}")
        print("Resultafo final:")
        print(f"Atleta: {atleta.nome}")
        print(f"Melhor Nota: {atleta.melhor_nota}")
        print(f"Pior Nota: {atleta.pior_nota}")
        print(f"Média: {atleta.media}")
