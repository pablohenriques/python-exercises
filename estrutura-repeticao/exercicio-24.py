"""
    Faça um programa que calcule o mostre a média aritmética de N notas
"""

if __name__ == '__main__':
    condicao: bool = True
    lista_numeros: list = []

    while condicao:
        numero: int|str = input("Digite um número ou cancele C:")

        if numero == "C":
            condicao = False
        else:
            lista_numeros.append(int(numero))

    tam: int = len(lista_numeros)
    media: float = sum(lista_numeros)/tam

    print(f"Média: {media}")
