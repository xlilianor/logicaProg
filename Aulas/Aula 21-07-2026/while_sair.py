opcao =""
while opcao != "Sair":
    opcao = input("Digite: Entrar, Ajuda ou Sair ") .upper()
    if opcao == "ENTRAR":
        print("Entrar")
    elif opcao == "AJUDA":
        print("Ajuda")
    elif opcao == "SAIR":
        print("Sair")
    else:
        print("Opção Digitada Inválida")