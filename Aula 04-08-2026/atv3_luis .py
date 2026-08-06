import webbrowser
url1 = "https://open.spotify.com/intl-pt/track/587Lf3LyhC8smoFnNIQtn3?si=79573fca342c4c5b" #Panda - Eu te Seguro
url2 = "https://open.spotify.com/intl-pt/track/4Kqy5vH2w1uvQzd4SEBbY4?si=99dee623379e4aeb" #Cosculluela - La Boda
url3 = "https://open.spotify.com/intl-pt/track/4k3xDpAdBuM17mNNHhOZkK?si=706ecc3db8c149f8" #Lil Peep - Nutts
url4 = "https://open.spotify.com/intl-pt/track/6JV2JOEocMgcZxYSZelKcc?si=8493455fee2848f7" #Justin Timberlake - Can't Stop the Feeling

def corazon_partido (valeria, plata):
    if valeria and plata == True:
        print("Tienes un corazón feliz y plata en su bolsillo")
        webbrowser.open(url2)
    elif valeria == True:
        print("Tienes un corazón feliz pero sin plata")
        webbrowser.open(url4)
    
    elif plata == True:
        print("Tienes plata en tu bolsillo pero tu corazón está roto")
        webbrowser.open(url3)
    
    else:
        print("Tienes un corazón roto y sin plata")
        webbrowser.open(url1)

def respuesta (respuesta):
    if respuesta in ("Si", "si", "SI"):
        return True
    else:
        return False

valeria = input("¿Tienes a Valéria en tu vida? ")
plata = input("¿Tienes plata en tu bolsillo? ")

corazon_partido(respuesta(valeria), respuesta(plata))
