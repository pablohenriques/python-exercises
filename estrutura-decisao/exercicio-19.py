"""
    Faça um Programa que leia um número inteiro menor que 1000 e imprima a
    quantidade de centenas, dezenas e unidades do mesmo
    Observando os termos no plural a colocação do "e", da vírgula entre outros.
        Exemplo:
            326 = 3 centenas, 2 dezenas e 6 unidades
            12 = 1 dezena e 2 unidades
            Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25,
            20, 10, 21, 11, 1, 7 e 16
"""


if __name__ == '__main__':
    print("Decomposição de números")
    numero: int = int(input("Digite um número:"))

    divisao_100, resto_100 = numero//100, numero % 100
    divisao_10, resto_10 =  resto_100//10, resto_100 % 10
    divisao_1 = resto_10//1

    print(f"{divisao_100} centenas {divisao_10} dezenas {divisao_1} unidades")
