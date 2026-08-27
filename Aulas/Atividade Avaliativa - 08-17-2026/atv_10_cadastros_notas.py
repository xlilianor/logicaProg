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
    print(f"A média do aluno é {media}")
    if media >= 7:
        situacao = "APROVADO"
        aprovados += 1
    elif media >= 4 and media <= 6:
        situacao = "RECUPERAÇÃO"
        em_recuperacao += 1
    else:
        situacao = "REPROVADO!"
        reprovados += 1

print(f"Aluno: {nome_aluno}")
print(f"Média ")