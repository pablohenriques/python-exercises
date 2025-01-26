"""
    Um posto está vendendo combustíveis com a seguinte tabela de descontos:
        a) Álcool:
            b) até 20 litros, desconto de 3% por litro
            c) acima de 20 litros, desconto de 5% por litro
        d) Gasolina:
            e) até 20 litros, desconto de 4% por litro
            f) acima de 20 litros, desconto de 6% por litro
    Escreva um algoritmo que leia o número de litros vendidos,
        o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o
        valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do
        álcool é R$ 1,90.
"""

if __name__ == '__main__':
    print("Cálculo combustível")
    tipo: str = input("Digite o tipo de combustível, A-álcool ou G-gasolina:")
    valor_final: float = 0.0

    if tipo == "A":
        qtd_combustivel: int = int(input("Informe a quantidade de combustível:"))
        valo_total: float = qtd_combustivel * 1.90
        if valor_final <= 20:
            valor_final: float = valo_total - (valo_total*0.03)
        else:
            valor_final: float = valo_total - (valo_total*0.05)
        print(f"Quantidade combustível: {qtd_combustivel} - Valor total (com desconto): {valor_final}")
    elif tipo == "G":
        qtd_combustivel: int = int(input("Informe a quantidade de combustível:"))
        valo_total: float = qtd_combustivel * 2.50
        if valor_final <= 20:
            valor_final: float = valo_total - (valo_total*0.04)
        else:
            valor_final: float = valo_total - (valo_total*0.06)
        print(f"Quantidade combustível: {qtd_combustivel} - Valor total (com desconto): {valor_final}")
    else:
        print("Combustível não identificado.")
