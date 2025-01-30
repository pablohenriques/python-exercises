"""
    Exercício 4 + Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento
    iniciais. Valide a entrada e permita repetir a operação
"""

if __name__ == '__main__':
    print("Crescimento Populacional Customizado")

    pop_a: int = int(input("Informe o número de habitantes da cidade A:"))
    pop_b: int = int(input("Informe o número de habitantes da cidade B:"))

    taxa_a: float = float(input("Informe a taxa de crescimento da cidade A:"))
    taxa_b: float = float(input("Informe a taxa de crescimento da cidade B:"))

    anos: int = 0

    while pop_a <= pop_b:
        pop_a += round(pop_a * taxa_a)
        pop_b += round(pop_b * taxa_b)
        anos += 1

    print(f"Pop A: {pop_a} - Pop B: {pop_b} - Anos: {anos}")
