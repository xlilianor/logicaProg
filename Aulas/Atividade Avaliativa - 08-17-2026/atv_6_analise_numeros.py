positivos = 0
negativos = 0
zeros = 0
pares = 0
impares = 0

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número:\n "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")