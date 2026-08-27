def calculo (A,B,op):
    if(op == "+"):
        print(f"{A}+{B} ={A+B}")
    elif(op == "-"):
        print(f"{A}-{B} = {A - B}")
    elif(op == "*"):
        print(f"{A}*{B} = {A * B}")
    elif(op == "/"):
        print(f"{A}/{B} = {A / B}")
    else:
        print("ERROR")
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo número: " ))
resultado = input("Qual operação a ser realizada?")
calculo(numero1, numero2, resultado)
