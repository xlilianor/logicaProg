opcao = "s"

while opcao == "s":
    nome = input("Nome do aluno: ")

    with open("alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome + "\n")

    opcao = input("Cadastrar outro aluno? (s/n): ")