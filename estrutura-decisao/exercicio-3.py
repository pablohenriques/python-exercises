"""
    Faça um Programa que verifique se uma letra digitada é "F" ou "M".
    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

if __name__ == '__main__':
    print("Masculino ou Feminino")
    sexo: chr = input("Informe um sexo:")

    if sexo == 'M' or sexo == 'm':
        print("Masculino")
    elif sexo == 'F' or sexo == 'f':
        print("Feminino")
    else:
        print(f"Sexo {sexo}")
