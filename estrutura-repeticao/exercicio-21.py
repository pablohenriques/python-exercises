"""
    Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele
    que é divisível somente por ele mesmo e por 1
"""
if __name__ == '__main__':
    print("Número Primo!")

    numero: int = int(input("Digite um número:"))
    contador: int = 0
    tipo: str = "é primo"

    for n in range(1, numero+1, 1):
        if numero % n == 0:
            contador += 1
            if contador > 2:
                tipo = "não é primo"
                break

    print(f"O número digitado: {tipo}")
