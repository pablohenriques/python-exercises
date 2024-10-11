"""
    Faça um Programa que peça a temperatura em graus Fahrenheit,
    transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9)
"""

if __name__ == '__main__':
    print("Conversão temperatura, Fahrenheit para Celsius")
    fahrenheit: int = int(input("Digite a temperatura em Fahrenheit:"))
    celsius: int = int(5 * ((fahrenheit-32)/9))
    print(f"{fahrenheit} °F são {celsius} °C")
