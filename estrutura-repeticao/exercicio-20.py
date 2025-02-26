"""
    Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
    fatorial a números inteiros positivos e menores que 16
"""
if __name__ == '__main__':
    print("Fatorial controlado")

    num: int|str = int(input("Digite um número para o fatorial:"))
    condicao: bool = True
    cache: dict = {}
    resultado: int = 1
    mensagem: str = ""

    while condicao is not False:
        mensagem = ""

        if num < 0 or num > 15:
            break

        if num in cache.keys():
            mensagem = f"Fatorial de {num} é {cache[num]}"
        else:
            resultado = 1
            for indice in range(num, 1, -1):
                resultado *= indice
            cache[num] = resultado
            mensagem = f"Fatorial de {num} é {resultado}"

        print(mensagem)

        num = input("Digite um número para o fatorial ou F para sair:")
        if num == "F":
            condicao = False
        else:
            num = int(num)
