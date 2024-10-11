"""
    Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
"""

if __name__ == '__main__':
    print("Cálculo da área do círculo")
    pi: float = 3.14
    raio = float(input("Digite o raio do círculo:"))
    area_circulo = pi * (raio ** 2)
    print(f"Área do círculo: {area_circulo} U (unidades)")
