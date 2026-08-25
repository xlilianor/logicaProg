senha_correta = ("python123")
senha_usuario = (None)
limite_tentativas = 0

while senha_usuario != senha_correta:
    senha_usuario = input("Digite a sua senha: \n")
    if senha_usuario != senha_correta:
        print("Senha incorreta. Tente novamente.")

        if limite_tentativas == 2:
            print("Limite de tentativas atingido. Acesso Negado")
            break
    else:
        print("Senha correta! Acesso liberado")
    limite_tentativas += 1