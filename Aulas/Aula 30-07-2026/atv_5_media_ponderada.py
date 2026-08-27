nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

def retorno_media(n1, n2,n3):
    media = (n1 * 3 + n2 * 3 + n3 * 4) / 10
    return media
print("A média das notas é", retorno_media(nota1, nota2, nota3))