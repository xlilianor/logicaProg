senha_correta = ("python123")
senha_usuario = (None)
limite_tentativas = 1

while senha_usuario != senha_correta:
    senha_usuario = input("Digite a sua senha: \n")
    if senha_usuario != senha_correta:
        print("Senha incorreta. Tente novamente.")
        limite_tentativas +=1
        if limite_tentativas == 4:
            print("Limite de tentativas atingido. Acesso Negado")
            break
    else:
        print("Senha correta! Acesso liberado")