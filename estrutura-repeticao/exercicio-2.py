"""
    Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
    mostrando uma mensagem de erro e voltando a pedir as informações.
"""

if __name__ == '__main__':
    print("Cadastro de usuários")

    usuario: str = input("Digite o nome do usuário:")
    senha: str = input("Digite a senha do usuário:")

    while senha == usuario:
        print("Senha não pode ser igual ao usuário")
        senha: str = input("Digite uma nova senha:")

    print("Usuário cadastrado com sucesso.")
    print(f"Usuário: {usuario} - Senha: **********")
