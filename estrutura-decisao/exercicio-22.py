"""
    Faça um Programa que peça um número inteiro e determine se ele é
    par ou impar. Dica: utilize o operador módulo (resto da divisão).
"""

if __name__ == '__main__':
    print("Número par ou ímpar")
    numero: int = int(input("Digite um número:"))
    tipo_numero: str = "ímpar"

    if numero%2==0:
        tipo_numero = "par"

    print(f"O número {numero} é {tipo_numero}")
