senha_correta = "python123"
senha_usuario = input("Digite a sua senha: \n")
limite_tentativas = 0

while senha_usuario != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha_usuario = input("Digite a sua senha: \n")
    limite_tentativas +=1
    if limite_tentativas == 2:
        print("O Limite de Tentativas foi Atingido. Acesso negado.")
if senha_usuario == senha_correta:
    print("Senha correta. Acesso permitido.")
