with open("lista de alunos.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.readline()) #redline() lê uma linha por vez, e cada vez que é chamado, ele lê a próxima linha do arquivo.
    print(arquivo.readline())
    print(arquivo.readline())