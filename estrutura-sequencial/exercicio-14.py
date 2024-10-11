"""
    João Papo-de-Pescador, homem de bem, comprou um microcomputador para
    controlar o rendimento diário de seu trabalho. Toda vez que ele traz
    um peso de peixes maior que o estabelecido pelo regulamento de pesca do
    estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
    excedente. João precisa que você faça um programa que leia a variável peso
    (peso de peixes) e calcule o excesso. Gravar na variável excesso a
    quantidade de quilos além do limite e na variável multa o valor da multa
    que João deverá pagar. Imprima os dados do programa com as mensagens
    adequadas.
"""

if __name__ == '__main__':
    print("Cálculo pesagem de peixe")
    peso_peixe: float = float(input("Digite a pesagem do peixe:"))
    valor_excesso: float = peso_peixe - 50  
    valor_multa: float = valor_excesso * 4.0
    print(f"Valor da multa")
