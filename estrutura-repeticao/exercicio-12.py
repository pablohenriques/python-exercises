"""
    Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
    informar de qual numero ele deseja ver a tabuada.  A saída deve ser conforme o exemplo abaixo:
    Tabuada de 5:
        5 X 1 = 5
        5 X 2 = 10
        ...
        5 X 10 = 50
"""
if __name__ == '__main__':
    print("Tabuada")
    numero: int = int(input("Digite um número para tabuada:"))

    for n in range(1, 11):
        resultado: int = numero * n
        print(f"{numero} x {n} = {resultado}")
