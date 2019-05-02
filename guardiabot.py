import requests
import numpy as np
import random as rd
import time

def getAccessToken(token):
	url = "https://graph.facebook.com/v3.3/10157188782874836/accounts?access_token={0}".format(token)
	r = requests.get(url)
	return r.json()["data"][0]["access_token"]

app_properties = open("application.properties")
arch = app_properties.readlines()
access_token = getAccessToken(arch[4].split("=")[1])
app_properties.close()
guardias = 14
sansanes = 5501
prob_perderluma = 0.3
weighted_random = [0.15, 0.15, 0.7]
weighted_elements = [0.5, 0.3, 0.1]
elements = [1,0]
pesosLuma = [0.6, 0.4]
guardiaConLuma = 1
guardiaActual = 1
while sansanes > 0 and guardias > 0:
    grupo = np.round(np.random.normal(10,5,1))[0]
    textoPrincipal = "Un grupo de {0} sansano(s) se acerca(n) a combatir contra el Guardia N°{1}!!!\n{2}"
    textoActualizacion = "Sansanos restantes: {0}\nGuardias restantes:{1}"
    # Si es que es la ultima oleada entonces el grupo son los ultimos sansanos
    if sansanes - grupo < 0:
        grupo = sansanes
    prob = np.random.choice(weighted_elements, 1, p=weighted_random)
    mirones = np.round(grupo*prob)
    peleadores = (grupo - mirones)[0]
    #Actualizacion de texto principal
    probGanar = np.around((1 - peleadores/100), decimals=2)
    if mirones == 1:
    	aux = "{0} sansano se quedó mirando, por lo que los otros {1} pelearon a muerte\n\n\n".format(int(mirones[0]), int(peleadores))
    else:
    	aux = "{0} sansanos se quedaron mirando, por lo que {1} valientes pelearon a muerte\n\n\n".format(int(mirones[0]), int(peleadores))
    textoPrincipal = textoPrincipal.format(int(grupo), guardiaActual, aux)
    if guardiaConLuma:
        weights = [probGanar, np.around(1-probGanar, decimals=2)]
    else:
        probGanar = probGanar - 0.1
        weights = [probGanar, np.around(1-probGanar, decimals=2)]
    guardiaGana = np.random.choice(elements,1, p=weights)
    if guardiaGana:
        if sansanes - grupo == 0:
            texto = "   PERDIERON LOS SANSANOS, DARCY GANA :(\n" # Final text
        else:
            if guardiaConLuma:
                pierdeLuma = np.random.choice(elements, 1, p=pesosLuma)
                if pierdeLuma:
                    guardiaConLuma = 0
                    texto = "  GANA EL GUARDIA, PERO PIERDE LA LUMA!  \n"
                else:
                    texto = "  GANA EL GUARDIA!!!\n"
            else:
                texto = "  GANA EL GUARDIA!!!\n"
            # Actualizacion de sansanos
            sansanes -= grupo

    # Si es que el guardia pierde
    else:
        guardiaConLuma = 1
        guardias -= 1
        guardiaActual += 1
        if guardias == 0:
            texto = "   LOS SANSANOS LOGRARON TOMARSE EL A!!!\n"
        else:
            texto = "   LOS SANSANOS DEJAN K.O. AL GUARDIA!!!\n"
    textoActualizacion = textoActualizacion.format(int(sansanes), guardias)
    message = textoPrincipal+texto+textoActualizacion
    data = {'message': message, 'access_token': access_token}
    r = requests.post("https://graph.facebook.com/278468619769380/feed", data)
    print(r.status_code, r.reason)
    arch = open("respaldo.txt", "w")
    arch.write(str(int(sansanes))+"\n")
    arch.write(str(guardias)+"\n")
    arch.write(str(guardiaActual)+"\n")
    arch.close()
    time.sleep(1800)