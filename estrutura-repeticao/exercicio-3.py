"""
    Faça um programa que leia e valide as seguintes informações:
        Nome: maior que 3 caracteres;
        Idade: entre 0 e 150;
        Salário: maior que zero;
        Sexo: 'f' ou 'm';
        Estado Civil: 's', 'c', 'v', 'd';
"""
if __name__ == '__main__':
    print("Cadastro de pessoa")

    nome: str = input("Digite um nome:")
    idade: int = int(input("Digite idade:"))
    salario: int = int(input("Digite um salário:"))
    sexo: str = input("Digite o sexo:")
    estado_civil: str = input("Digite o estado cívil:")
    validador: int = 0

    while validador < 5:
        if len(nome) < 3:
            nome = input("Digite novamente um nome acima de três letras:")
        else:
            validador += 1
        if idade < 0 or idade > 150:
            idade = int(input("Digite idade entre 0 e 150:"))
        else:
            validador += 1
        if salario < 0:
            salario = int(input("Digite salário acima de 0:"))
        else:
            validador += 1
        if sexo not in ["f", "m"]:
            sexo = input("Digite f-Feminino ou m-Masculino:")
        else:
            validador += 1
        if estado_civil not in ["s", "c", "v", "d"]:
            estado_civil = input("Digite estado cívil, s-solteiro, c-casado, d-divorciado, v-viúvo/viúva:")
        else:
            validador += 1

    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estado_civil}")
