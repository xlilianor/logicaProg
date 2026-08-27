idade = int(input("Digite a sua idade:\n "))

if idade <12:
    print("Você é uma criança.")
elif idade >=12 and idade <=17:
    print ("Você é um adolescente.")
elif idade >=18 and idade <=59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
