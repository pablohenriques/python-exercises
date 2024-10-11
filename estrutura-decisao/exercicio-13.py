"""
    Faça um Programa que leia um número e exiba o dia correspondente da semana.
    (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

if __name__ == '__main__':
    print("Dias da semana")
    dias_semana: list[str] = [
        "domingo",
        "segunda",
        "terca",
        "quarta",
        "quinta",
        "sexta",
        "sabado"
    ]
    dia_semana: int = int(input("Digite o dia da semana em número, 0-domingo..6-sabado:"))
    print(f"Dia da semana: {dias_semana[dia_semana]}")
