"""
    Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a
    tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também
    pelo usuário, conforme exemplo abaixo:
        Montar a tabuada de: 5
        Começar por: 4
        Terminar em: 7
        Vou montar a tabuada de 5 começando em 4 e terminando em 7:
        5 X 4 = 20
        5 X 5 = 25
        5 X 6 = 30
        5 X 7 = 35
"""

if __name__ == '__main__':
    print("Tabuada customizada")

    numero_tabuada: int = int(input("Digite um número para montar a tabuada:"))
    numero_inicio_tabuada: int = int(input("Digite um número para iniciar tabuada:"))
    numero_fim_tabuada: int = int(input("Digite um número para finalizar tabuada:"))

    if numero_fim_tabuada <= numero_inicio_tabuada:
        print("Insira outros números para formar uma sequência")
    else:
        for numero in range(numero_inicio_tabuada, numero_fim_tabuada+1, 1):
            multiplicacao: int = numero * numero_tabuada
            print(f"{numero_tabuada} * {numero} = {multiplicacao}")
