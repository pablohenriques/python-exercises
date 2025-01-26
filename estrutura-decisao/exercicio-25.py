"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    a) "Telefonou para a vítima?"
    b) "Esteve no local do crime?"
    c) "Mora perto da vítima?"
    d) "Devia para a vítima?"
    e) "Já trabalhou com a vítima?"
    O programa deve no final emitir uma classificação sobre a participação da pessoa
    no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
    entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

if __name__ == '__main__':
    print("Detetive IA - Responda as questões abaixo")

    a: str = input("Telefonou para a vítima? s/n:")
    b: str = input("Esteve no local do crime? s/n:")
    c: str = input("Mora perto da vítima? s/n:")
    d: str = input("Devia para a vítima? s/n:")
    e: str = input("Devia para a vítima? s/n:")
    respostas: list[str] = [a, b, c, d, e]
    numero_respostas: int = respostas.count("s")
    status_pessoa: str = ""

    if numero_respostas == 2:
        status_pessoa = "suspeita"
    elif numero_respostas == 3 or numero_respostas == 4:
        status_pessoa = "cúmplice"
    elif numero_respostas == 5:
        status_pessoa = "assassino"
    else:
        status_pessoa = "inocente"

    print(f"A pessoa é: {status_pessoa}")
