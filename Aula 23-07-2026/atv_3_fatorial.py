fatorial = int(input("Digite um numero para calcular o fatorial: "))
valores = 1
for contador in range(1, fatorial+1):
    print(f"{valores} * {contador} = {valores * contador}")
    valores *= contador
print(f"{fatorial}! = {valores}")