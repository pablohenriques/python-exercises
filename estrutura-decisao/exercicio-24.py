"""
    Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
    operação ele deseja realizar. O resultado da operação deve ser acompanhado
    de uma frase que diga se o número é:
        a) par ou ímpar
        b) positivo ou negativo
        c) inteiro ou decimal
"""

if __name__ == '__main__':
    print('Operações Números')
    num1: int = int(input('Digite o primeiro número:'))
    num2: int = int(input('Digite o segundo número:'))
    opcao: str = input('Escolha uma operação: \n\ta) par/impar \n\tb) positivo/negativo \n\tc) inteiro/decimal\n:')
    status_num1: str = ''
    status_num2: str = ''
    mensagem: str = ''

    if opcao == 'a':
        if num1 % 2 == 0:
            status_num1 = 'é par'
        else:
            status_num1 = 'é ímpar'
        if num2 % 2 == 0:
            status_num2 = 'é par'
        else:
            status_num2 = 'é ímpar'
        mensagem: str = f'Número {num1}: {status_num1}. Número {num2}: {status_num2}'
    elif opcao == 'b':
        if num1 > 0:
            status_num1 = 'é positivo'
        elif num1 < 0:
            status_num1 = 'é negativo'
        else:
            status_num1 = 'é zero'
        if num2 > 0:
            status_num2 = 'é positivo'
        elif num2 < 0:
            status_num2 = 'é negativo'
        else:
            status_num2 = 'é zero'
        mensagem: str = f'Número {num1}: {status_num1}. Número {num2}: {status_num2}'
    elif opcao == 'c':
        if isinstance(num1, int):
            status_num1 = 'é inteiro'
        else:
            status_num1 = 'é decimal'
        if isinstance(num2, int):
            status_num2 = 'é inteiro'
        else:
            status_num2 = 'é decimal'
        mensagem: str = f'Número {num1}: {status_num1}. Número {num2}: {status_num2}'
    else:
        mensagem = 'Opção não encontrada. Digite novamente.'

    print(mensagem)
