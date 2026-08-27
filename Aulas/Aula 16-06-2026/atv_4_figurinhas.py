# Recebendo os Dados
valor_pacote = float(input("Insira aqui o valor unitário do pacote de figurinha: "))
quantidade_pacotes = int(input("Insira aqui a quantidade de pacotes de figurinhas a serem adquiridos: "))

# Resolução do Calculo
total_figurinhas = valor_pacote * quantidade_pacotes

# Resultado do Calculo
print("O valor total a ser investido sera de: R$",total_figurinhas)