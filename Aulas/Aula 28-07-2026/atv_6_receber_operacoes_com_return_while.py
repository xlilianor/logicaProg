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
op = "erro"
while op != "+" and op != "-" and op != "*" and op != "/" :
    op = input("Qual operação a ser realizada?")
    if op != "+" and op != "-" and op != "*" and op != "/" :
        print ("ERROR")
final = calculo(numero1, numero2, op)
print("O resultado final é: ", final)
