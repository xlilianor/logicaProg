# Perguntando Valores
dolar = float(input("Digite o preço do ingresso para Copa em Dólar Americano: "))
real = float(input("Digite o valor da cotação atual do Dólar Americano em Reais R$: "))
# Calculando o valor total convertido para o Real Brasileiro R$
valor_total_em_reais = dolar * real
# Dividindo Custos
valor_por_amigo = valor_total_em_reais / 3
print("--- RESULTADO DO PLANEJAMENTO ---")
print("O Valor total dos ingressos em Real Brasileiro é:",valor_total_em_reais)
print("O Valor que cada um dos amigos deverá pagar é:R$ ",valor_por_amigo)