def usuarios (login,senha):
    if login == "lilian" and senha == "taylor":
        return True
    else:
        return False

nome = input("Digite o nome de usuário: ")
senha = input("Digite a senha de usuário: ")
print(usuarios(nome,senha))

while not usuarios(nome, senha):
    print("Usuário ou senha incorretos. Tente novamente.")
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha de usuário:")
else:
    print("Login realizado com sucesso.")