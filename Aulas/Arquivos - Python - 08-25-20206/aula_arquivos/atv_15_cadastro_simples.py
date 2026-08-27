nome = input("Digite o nome do aluno: ")

with open("alunos.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(nome + "\n")

print("Aluno cadastrado!")