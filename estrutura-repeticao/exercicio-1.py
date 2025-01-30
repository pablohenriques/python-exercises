"""
    Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
    pedindo até que o usuário informe um valor válido.
"""

if __name__ == '__main__':
    print("Mostrando uma nota")

    nota: int = int(input("Digite uma nota:"))

    while nota < 0 or nota > 10:
        nota: int = int(input("Digite uma nota:"))

    print(f"Nota digitado pelo usuário: {nota}")
