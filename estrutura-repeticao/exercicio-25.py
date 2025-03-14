"""
    Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
    turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
    média calculada
"""

if __name__ == '__main__':
    condicao = True
    lista_idades: list[int] = []

    while condicao:
        idade: int = int(input("Digite a idade da pessoa:"))
        lista_idades.append(idade)
        decisao: str = input("Deseja inserir mais uma idade? S-sim; N-não:")

        if decisao == "S":
            continue
        elif decisao == "N":
            break

    media_turma: int = sum(lista_idades) // len(lista_idades)
    tipo_turma: str = ""

    if media_turma > 60:
        tipo_turma = "idosa"
    elif 25 < media_turma <= 60:
        tipo_turma = "adulta"
    else:
        tipo_turma = "jovem"

    print(f"Idades: {lista_idades}")
    print(f"Tipo turma: {tipo_turma}")
