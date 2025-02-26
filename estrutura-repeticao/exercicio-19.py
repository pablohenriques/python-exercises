"""
    Altere o programa anterior para que ele aceite apenas números entre 0 e 1000
"""


if __name__ == '__main__':
    print("Maior, menor e soma de valores:")

    cancelamento: bool = False
    lista_numeros: list[int] = []

    while not cancelamento:
        numero: int|str = input("Digite um número ou F para cancelar:")

        if numero.isnumeric():
            numero_convertido: int = int(numero)
            if 0 < numero_convertido < 1001:
                lista_numeros.append(int(numero))
            else:
                print("Coloque ")
        else:
            if numero == "F":
                cancelamento = True

    soma_numeros: int = sum(lista_numeros)
    maior_numero: int = max(lista_numeros)
    menor_numero: int = min(lista_numeros)

    print(f"Soma dos números da sequência: {soma_numeros}")
    print(f"Maior número da sequência: {maior_numero}")
    print(f"Menor número da sequência: {menor_numero}")