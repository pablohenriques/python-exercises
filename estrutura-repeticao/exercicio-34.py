"""
    Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
    entre 1 e um número inteiro informado pelo usuário.
"""
import threading
from threading import Thread


def validacao(numero: int, lista: dict) -> bool:
    contador: int = 0
    resultado: bool = True

    for n in range(1, numero + 1, 1):
        divisao: float = numero % n
        if divisao == 0:
            contador += 1
        if contador > 2:
            break

    if numero==0 or numero == 1 or contador > 2:
        resultado = False

    lista[numero] = resultado


if __name__ == '__main__':
    print("Liste de verificação de números primos")

    numero_limite: int = int(input("Digite um número limite para gerar lista:"))
    lista_resultados: dict = {}

    for n in range(numero_limite+1):
        resultado: Thread = threading.Thread(target=validacao, args=(n, lista_resultados))
        resultado.start()
        resultado.join()

    print(f"Lista: {lista_resultados}")

