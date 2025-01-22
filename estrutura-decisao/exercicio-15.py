"""
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
    equilátero, isósceles ou escaleno.
Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""

if __name__ == '__main__':
    print("Verificação Tipo Triângulo")
    lado_a: int = int(input("Digite o primeiro lado do triângulo: "))
    lado_b: int = int(input("Digite o segundo lado do triângulo: "))
    lado_c: int = int(input("Digite o terceiro lado do triângulo: "))
    tipo_triangulo: str = ""

    if lado_a == lado_b and lado_a == lado_c:
        tipo_triangulo = "Equilátero"
    elif lado_a != lado_b and lado_b != lado_c and lado_a != lado_c:
        tipo_triangulo = "Escaleno"
    else:
        tipo_triangulo = "Isóceles"

    print(f"O tipo do triângulo é: {tipo_triangulo}")
