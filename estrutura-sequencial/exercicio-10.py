"""
    Faça um Programa que peça a temperatura em graus Celsius,
    transforme e mostre em graus Fahrenheit.
    F = (C * 9/5) + 32
"""

if __name__ == '__main__':
    print("Conversor de graus, Celsius para Fahrenheit")
    celsius: int = int(input("Digite o valor da temperatura em °C:"))
    fahrenheit: int = int((celsius*(9/5) + 32))
    print(f"{celsius} °C são {fahrenheit} °F")
