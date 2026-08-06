def afiados(lilian, luis):
    if lilian and luis == True:
        print("Vocês estão prontos para Arquivos!")
    else:
        print("Vocês não estão prontos para Arquivos!")

def respuesta (resposta):
    if resposta  in ("Sim", "sim", "si", "claro", "s", "y", "yes", "oui", "ja", "da", "si", "はい", "예", "是的"):
        return True
    else:
        return False

dorneless1 = input("Digite a resposta para Lilian: ")
dorneless2 = input("Digite a resposta para Luis: ")

afiados(respuesta(dorneless1), respuesta(dorneless2))
