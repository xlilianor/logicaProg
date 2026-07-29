# Recebendo os Dados
idade = int(input("Digite a sua idade: "))

# Resolução do código

if(idade < 12):
    print("Você é CRIANÇA")
elif (idade >=13 and idade <= 17):
    print ("Você é ADOLESCENTE")
elif (idade >18 and idade <= 59):
    print("Você é ADULTO")
elif (idade > 60 and idade < 120):
    print ("Você é IDOSO")
else:
    print ("Você é imortal")