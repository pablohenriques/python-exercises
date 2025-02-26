"""
    Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores
"""
if __name__ == '__main__':
    print("Maior, menor e soma de valores:")

    cancelamento: bool = False
    lista_numeros: list[int] = []

    while not cancelamento:
        numero: int|str = input("Digite um número ou F para cancelar:")

        if numero.isnumeric():
            lista_numeros.append(int(numero))
        else:
            if numero == "F":
                cancelamento = True

    soma_numeros: int = sum(lista_numeros)
    maior_numero: int = max(lista_numeros)
    menor_numero: int = min(lista_numeros)

    print(f"Soma dos números da sequência: {soma_numeros}")
    print(f"Maior número da sequência: {maior_numero}")
    print(f"Menor número da sequência: {menor_numero}")
