"""
    Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
    seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido
    um número negativo.
"""

if __name__ == '__main__':
    print("Entrada e análise de números")

    intervalos_numeros: dict = {
        "0-25": [],
        "26-50": [],
        "51-75": [],
        "76-100": [],
    }

    while True:
        numero: int = int(input("Digite um número:"))

        if numero < 0:
            break

        if 0 <= numero <= 25:
            intervalos_numeros["0-25"].append(numero)
        elif 26 <= numero <= 50:
            intervalos_numeros["26-50"].append(numero)
        elif 51 <= numero <= 75:
            intervalos_numeros["51-75"].append(numero)
        elif 76 <= numero <= 100:
            intervalos_numeros["76-100"].append(numero)

    for k, v in intervalos_numeros.items():
        print(f"Intervalo {k}: {v}")
