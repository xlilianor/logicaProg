def verificar_par_impar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é PAR!")
    else:
        print(f"O número {numero} é ÍMPAR!")


def calcular_quadrado(numero):
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é {quadrado}")


def mostrar_tabuada(numero):
    print(f"\n Tabuada de {numero} \n")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")

while True:
        print("\n MENU \n")
        print("1 - Verificar se um número é par ou ímpar")
        print("2 - Calcular o quadrado de um número")
        print("3 - Mostrar a tabuada de um número")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                num = int(input("Digite um número: "))
                verificar_par_impar(num)
            case "2":
                num = int(input("Digite um número: "))
                calcular_quadrado(num)
            case "3":
                num = int(input("Digite um número: "))
                mostrar_tabuada(num)
            case "0":
                print("Encerrando o programa.\n Até logo!")
                break
            case _:
                print("Opção inválida! Escolha uma das opçẽso do menu")