"""
    Faça um Programa que converta metros para centímetros.
"""

if __name__ == '__main__':
    print("Digite o valor em metros para conversão em centímetros")
    valor_metros: float = float(input("Valor metros:"))
    valor_centimetros: float = valor_metros * 100
    print(f"{valor_metros} metros são {valor_centimetros} centímetros")
