# Recebendo os dados
capacidade_estadio = int(input("Qual é a capacidade total do estádio? "))
ingressos_vendidos = int(input("Qual a quantidade total de ingressos vendidos até o momento?"))

# Calculo
assentos_livres = capacidade_estadio - ingressos_vendidos

#Resultados
print("A quantidade de assentos ainda disponiveis é de: ", assentos_livres)