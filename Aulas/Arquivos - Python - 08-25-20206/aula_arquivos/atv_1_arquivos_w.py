arquivo = open("mensagem.txt", "w") #Cria o arquivo se não existir, se existir, manipula por substituição, apagando o conteúdo do arquivo

arquivo.write("Olá, mundo")

arquivo.close()