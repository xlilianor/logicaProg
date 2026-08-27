def cadastrar_aluno():
    nome = input("Nome: ")

    with open("alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome + "\n")

    print("Aluno cadastrado!")


def listar_alunos():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for aluno in arquivo:
            print(aluno.strip())

while True:
    print("""
    1 - Cadastrar
    2 - Listar
    0 - Sair
    """)

    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            cadastrar_aluno()
        case 2:
            listar_alunos()
        case 0:
            break
        case _:
            print("Opção inválida.")