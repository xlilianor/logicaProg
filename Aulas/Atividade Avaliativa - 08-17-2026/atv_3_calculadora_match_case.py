num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))
operacao = input("Digite a operação a ser realizada:\n + para SOMA \n - para SUBTRAÇÃO \n * para MULTIPLICAÇÃO \n / para DIVISÃO \n")

match operacao:
    case("+"):
        resultado = num1 + num2
        print("O resultado da sua soma é:\n", resultado)
    case ("-"):
        resultado = num1 - num2
        print("O resultado da sua subtração é:\n", resultado)
    case ("*"):
        resultado = num1 * num2
        print("O resultado da sua multiplicação é:\n", resultado)
    case ("/"):
        if num2 == 0:
            print("Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print("O resultado da sua divisão é:\n", resultado)