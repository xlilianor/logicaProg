def verificar_numero(numero):
    if numero > 0:  
        print ("É POSITIVO")

    elif numero < 0:
        print ("É NEGATIVO")
    else:
        print ("É ZERO")

    if numero % 2 == 0:
        print ("O NUMERO É PAR")

    else:
        print("O NÚMERO É IMPAR")

numero = int(input("Digite um número:\n"))
verificar_numero(numero)
    