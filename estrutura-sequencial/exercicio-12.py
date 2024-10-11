"""
    Tendo como dados de entrada a altura de uma pessoa,
    construa um algoritmo que calcule seu peso ideal,
    usando a seguinte fórmula: (72.7*altura) - 58
"""

if __name__ == '__main__':
    print("Cálculo do peso ideal")
    altura: float = float(input("Digite sua altura:"))
    calculo_peso_ideal: float = (72.7*altura) - 58
    print(f"Seu peso ideal: {calculo_peso_ideal:.2f}")
