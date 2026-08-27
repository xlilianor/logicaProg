# Recebendo váriaveis
numero1 = float(input("Digite primeiro numero para a operação: "))
numero2 = float(input("Digite segundo número para operação: "))
operacao = input("Digite o sinal da operação: +, -, /, * ")

# Resolução
match operacao:
    case "+":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 - numero2
    case "/":
        resultado = numero1 / numero2
    case "*":
        resultado = numero1 * numero2
    case _:
        print("Operação Invalida")
print(resultado)