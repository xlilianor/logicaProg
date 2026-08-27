while True:
    print("""
    ===== MENU =====

    1 - Cadastrar aluno
    2 - Listar alunos
    0 - Sair
    """)

    opcao = int(input("Escolha: "))

    match opcao:
        case 1:
            nome = input("Nome: ")

            with open("alunos.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(nome + "\n")

            print("Aluno cadastrado!")

        case 2:
            with open("alunos.txt", "r", encoding="utf-8") as arquivo:
                for aluno in arquivo:
                    print(aluno.strip())

        case 0:
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida.")