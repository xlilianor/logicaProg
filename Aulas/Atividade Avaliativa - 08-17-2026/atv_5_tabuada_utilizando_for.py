numero = int(input("Digite um número inteiro:\n ")) # Pede o número a ser tabuado

for i in range(1, 11): #Define o range a ser multiplicado
    resultado = i * numero
    print(f"{numero} * {i} = {numero * i}") #Formatação
    