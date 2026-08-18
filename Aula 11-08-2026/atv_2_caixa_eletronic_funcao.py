def verificacao (valor):
    if valor < 0:
        print("Valor inválido!")
        return False
    return True

saldo = 1000.00
opcao = None                  # Classicamente precisa inicializar uma variavel com valor zero ou None

while opcao != "4":
    opcao = input("CAIXA ELETRÔNICO: \n1 - Imprima o Saldo, \n2 - Realizar Saque, \n3 - Realizar Depósito, \n4 - Sair \n Escolha: ")

    if opcao == "1":
        print("O seu saldo atual em reais é de R$", saldo)

    elif opcao == "2":
        saque = float(input("Digite o valor que deseja sacar: "))
        if saque > saldo:
            print ("O seu saldo é insuficiente!")
        elif verificacao(saque):
            saldo -= saque
            print("Saque realizado com sucesso! \n Você sacou R$", saque, "\n O seu saldo atual é de R$", saldo)

    elif opcao == "3":
        deposito = int(input("Digite o valor que deseja deposito: R$: "))
        if verificacao(deposito):
            saldo += deposito
            print("Depósito realizado com sucesso! \n Você depositou R$", deposito, "\n O seu saldo atual é de R$", saldo)

    elif opcao == "4":
        print("Operação encerrada")
    else:
        print("Opção inválida! Tente novamente.")