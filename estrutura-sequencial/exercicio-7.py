"""
    Faça um Programa que calcule a área de um quadrado,
    em seguida mostre o dobro desta área para o usuário.
"""

if __name__ == '__main__':
    print("Cálculo da área de um quadrado e o dobro da área")
    lado: int = int(input("Digite o lado do quadrado:"))
    area: int = lado * lado
    print(f"Área do quadrado: {area} U (unidades)")
    print(f"Dobro da área do quadrado: {area * 2} U (unidades)")
