"""
    Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
    divisível
"""
if __name__ == '__main__':
    print("Número Primo ou seu divisores")

    numero: int = int(input("Digite um número:"))
    contador: int = 0
    divisores: list = []
    tipo: str = "é primo"

    for n in range(1, numero+1, 1):
        if numero % n == 0:
            divisores.append(n)
            contador += 1

    if contador > 2:
        tipo = "não é primo"

    print(f"O número {numero} {tipo}")
    print(f"Divisores: {divisores}")
