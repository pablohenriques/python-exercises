"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
"""

if __name__ == '__main__':
    lista_numeros: list[int] = list()

    while True:
        numero: str = input("Digite um número para a sequência de números ou 'S' para sair:")

        if numero == "S":
            break

        lista_numeros.append(int(numero))

    lista_numeros_invertida: list[int] = list()
    tam_lista: int = len(lista_numeros) - 1
    for indice in range(tam_lista, -1, -1):
        numero_indice: int = lista_numeros[indice]
        lista_numeros_invertida.append(numero_indice)

    print("-------------------------------------------")
    print(f"lista          : {lista_numeros}")
    print(f"lista invertida: {lista_numeros_invertida}")