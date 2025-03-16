"""
    Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
    aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se
    ele é ou não um número primo.
"""


if __name__ == '__main__':
    print("Validando números primos")

    numero: int = int(input("Digite um número para validação:"))
    contador: int = 0
    tipo_numero: str = ""

    for n in range(1, numero+1, 1):
        divisao: int = numero % n

        if divisao == 0:
            contador += 1
        if contador > 2:
            break

    if contador == 1 or contador > 2:
        tipo_numero = "não é primo"
    else:
        tipo_numero = "é primo"

    print("O número %d %s" % (numero, tipo_numero) )
