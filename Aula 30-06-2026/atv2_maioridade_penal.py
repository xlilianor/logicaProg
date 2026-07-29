#Recebendo as variaveis
from datetime import datetime
data_atual = datetime.now()
ano_atual = data_atual.year

ano_nascimento = int(input("Digite o ano do seus nascimento: "))
idade = ano_atual - ano_nascimento

if (idade < 18):
    print("Você é menor de idade")
else:
    print("Você é maior de idade")