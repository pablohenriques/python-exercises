"""
    Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

if __name__ == '__main__':
    print("Verificando se é uma vogal ou consoante")
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"
    letra: chr = input("Digite uma letra:")

    if letra in vogais:
        print(f"A letra {letra} é uma vogal")
    elif letra in consoantes:
        print(f"A letra {letra} é uma consoante")
    else:
        print("Caracter desconhecido")
