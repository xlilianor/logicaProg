def usuarios (login,senha):
    if login == "lilian" and senha == "1234":
        return True
    else:
        return False
    
login = input("Digite o nome de usuário: ")
senha = input("Digite a senha de usuário:")

while not usuarios(login, senha):
    print("Usuário ou senha incorretos. Tente novamente.")
    login = input("Digite o nome de usuário: ")
    senha = input("Digite a senha de usuário:")
else:
    print("Login realizado com sucesso.")   
