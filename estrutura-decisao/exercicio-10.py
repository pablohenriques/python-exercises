"""
    Faça um Programa que pergunte em que turno você estuda.
    Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
    Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""


if __name__ == '__main__':
    print("Mensagens do dia")
    print("Horários de Estudo:")
    print("\tm - matutino")
    print("\tv - vespertino")
    print("\tn - noturno")
    horario_estudo: chr = input("Horário de Estudo (m, v, n): ")

    if horario_estudo == 'm':
        print("Bom dia!")
    elif horario_estudo == 'v':
        print("Boa tarde!")
    elif horario_estudo == 'n':
        print("Boa noite!")
    else:
        print("Horário Inválido!")
