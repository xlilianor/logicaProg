def calcular_media (nota1, nota2):
    media = ((nota1 + nota2) /2)
    return media

alunos = int(input("Digite a quantidade de alunos:\n"))

em_recuperacao = 0
aprovados = 0
reprovados = 0

for i in range(alunos):
    print(f"Aluno {i + 1}")
    nome_aluno = input("Nome: ")
    n1 = float(input("Valor da primeira nota:\n"))
    n2 = float(input("Valor da segunda nota:\n"))

    media = calcular_media(n1,n2)
    print(f"A média de {nome_aluno} é {media}\n")
    if media >= 7:
        print("APROVADO\n")
        aprovados += 1

    elif media >= 4 and media < 7:
        print("RECUPERAÇÃO\n")
        em_recuperacao += 1
    else:
        print("REPROVADO\n")
        reprovados += 1
print(f"Total de alunos APROVADOS: {aprovados}")
print(f"Total de alunos em RECUPERAÇÃO: {em_recuperacao}")
print(f"Total de alunos REPROVADOS: {reprovados}")