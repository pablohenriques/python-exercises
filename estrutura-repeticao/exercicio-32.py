"""
    O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
    indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média
    das temperaturas.
"""


if __name__ == '__main__':
    print("Dados sobre temperaturas")

    condicao: bool = True
    temperaturas: list[float] = list()

    while condicao:
        temperatura: float = float(input("Informe o valor da temperatura em ºC:"))
        temperaturas.append(temperatura)

        opcao: str = input("Deseja inserir mais uma temperatura? S-sim/N-não:")
        if opcao == "N":
            condicao = False

    menor_temperatura: float = min(temperaturas)
    maior_temperatura: float = max(temperaturas)
    media_temperaturas: float = sum(temperaturas)/len(temperaturas)

    print(f"Menor temperatura: {menor_temperatura}")
    print(f"Maior temperatura: {maior_temperatura}")
    print(f"Temperatura média: {media_temperaturas}")
