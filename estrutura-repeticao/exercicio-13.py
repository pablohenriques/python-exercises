"""
    Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
    número. Não utilize a função de potência da linguagem
"""
if __name__ == '__main__':
    print("Potência de um número")
    base: float = float(input("Digite o número base:"))
    expoente: int = int(input("Digite o número expoente:"))
    resultado: float = 1

    if expoente < 0:
        base = 1/base
    for _ in range(abs(expoente)):
        resultado *= base

    print(f"{base} elevado a {expoente} é {resultado}")
