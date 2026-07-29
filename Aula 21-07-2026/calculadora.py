operacao = ""
multiplicador = ""

while operacao != "SAIR":
    operacao = input("Digite um valor para ser o multiplicador: ou Sair para encerrar o calculo ").upper()
    if operacao == "SAIR":
        print("Encerrando o programa...")
    else:
        multiplicador = int(input("Digite um valor para ser o multiplicado: "))
        resultado = int(operacao) * multiplicador
        print("Resultado: ", resultado)