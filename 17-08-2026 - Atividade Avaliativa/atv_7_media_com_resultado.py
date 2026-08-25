# Recebimento dos Valores de média
nota1 = float(input("Digite o valor da sua primeira nota:\n "))
nota2 = float(input("Digite o valor da segunda nota:\n "))
nota3 = float(input("Digite o valor da sua terceira nota:\n "))

#Criação da Função
def retorno_media(n1, n2, n3): #função nome retorno_media recebendo 3 valores)
    media = (n1 * 3 + n2 * 3 + n3 * 4) / 10 # Variavel que vai receber o valor da media
    return media
media_final = retorno_media(nota1, nota2, nota3) #o calculo
print("A media da suas notas é: \n")

if(media_final >= 7.0):
    print("Parabéns! Você está APROVADO!")
elif(media_final >= 4.0 and media_final <7.0):
    print("Você está em RECUPERAÇÃO!")
elif(media_final <4.0):
    print("VOCÊ ESTÁ REPROVADO")