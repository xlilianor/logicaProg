# Recebendo váriaveis
numero1 = float(input("Digite primeiro numero para a operação: "))
numero2 = float(input("Digite segundo número para operação: "))
operacao = input("Digite o sinal da operação: +, -, /, * ")

# Resolução

if(operacao == "+"):
    resultado = numero1 + numero2
elif(operacao == "-"):
    resultado = numero1 - numero2
elif(operacao == "/"):
    resultado = numero1 / numero2
elif(operacao == "*"):
    resultado = numero1 * numero2
else:
    resultado = "Operação Inválida"

print(resultado)