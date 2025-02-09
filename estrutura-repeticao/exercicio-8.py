"""
    Faça um programa que leia 5 números e informe a soma e a média dos números
"""

if __name__ == '__main__':
    print("Média dos números")
    lista_numeros: list[int] = []

    for _ in range(5):
        numero: int = int(input("Digite um número:"))
        lista_numeros.append(numero)

    soma_numeros: int = sum(lista_numeros)
    media_numeros: float = soma_numeros/len(lista_numeros)

    print(f"Soma Total: {soma_numeros} - Média Total: {media_numeros}")
