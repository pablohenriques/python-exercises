"""
    Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa
    deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o
    funcionamento, o estilo e o número de testes (divisões) executados.
"""

if __name__ == '__main__':
    print("Lista de números primos")
    numero: int = int(input("Digite um número para a lista de números:"))
    divisoes: dict = {}


    for n in range(1, numero+1, 1):
        contador: int = 0
        numero_divisoes: int = 0
        tipo: str = "é número primo"
        for d in range(1, n+1, 1):
            numero_divisoes += 1
            if n%d == 0:
                contador += 1
            if contador > 2:
                tipo = "não é número primo"
                break
        divisoes[n] = (numero_divisoes, tipo)

    for k, v in divisoes.items():
        print(f"Número: {k}. Divisões: {v[0]}. Tipo: {v[1]}")
