"""
    Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
    que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
    escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
    mantidas as taxas de crescimento
"""
if __name__ == '__main__':
    print("Crescimento de cidades")

    cidade_a: float = 80000
    taxa_crescimento_cidade_a: float = 0.03
    cidade_b: float = 200000
    taxa_crescimento_cidade_b: float = 0.015
    anos: int = 0

    while cidade_a <= cidade_b:
        cidade_a += round(cidade_a * taxa_crescimento_cidade_a)
        cidade_b += round(cidade_b * taxa_crescimento_cidade_b)
        anos = anos + 1

    print(f"Em {anos} anos a cidade A terá o 'mesmo número/mais' habitantes que a cidade B")
