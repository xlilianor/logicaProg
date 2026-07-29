def calculo (A,B,op):
    if(op == "+"):
        return (A + B)
    elif(op == "-"):
        return (A - B)
    elif(op == "*"):
        return (A * B)
    elif(op == "/"):
        return (A / B)
    else:
        print("ERROR")

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo número: " ))
operacao = input("Qual operação a ser realizada?")
final = calculo(numero1, numero2, operacao)
print("O resultado final é: ", final)
