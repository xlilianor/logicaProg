# Recebendo váriaveis
litros_vendidos = float(input("Digite o total vendido na bomba: "))
combustivel = input("Qual o tipo de combustivel. Digite A para Alcool, G para Gasolina ")
preco_alcool = 3.90
preco_gasolina = 5.50

if(combustivel == "A"):
    if(litros_vendidos < 20):
        preco_litro = preco_alcool- (preco_alcool * 0.03)
    else:
        preco_litro = preco_alcool - (preco_alcool * 0.05)

elif (combustivel == "G"):
    if(litros_vendidos < 20):
        preco_litro = preco_gasolina - (preco_gasolina * 0.04)
    else:
        preco_litro = preco_gasolina - (preco_gasolina * 0.06)

resultado = preco_litro * litros_vendidos
print(" O valor total a ser pago é de:", resultado) 