import numpy as np
import random as rd
import time

guardias = 15
sansanes = 5501
prob_perderluma = 0.3
weighted_random = [0.15, 0.15, 0.7]
weighted_elements = [0.5, 0.3, 0.1]
elements = [1,0]
pesosLuma = [0.6, 0.4]
guardiaConLuma = 1
while sansanes > 0 and guardias > 0:
    time.sleep(1)
    print("Sansanos Actuales: {0}".format(sansanes))
    print("Guardias Actuales: {0}".format(guardias))
    grupo = np.round(np.random.normal(10,5,1))
    # Si es que es la ultima oleada entonces el grupo son los ultimos sansanos
    if sansanes - grupo < 0:
        grupo = sansanes
    prob = np.random.choice(weighted_elements, 1, p=weighted_random)
    mirones = np.round(grupo*prob)
    peleadores = (grupo - mirones)[0]
    print("Peleadores: {0} - Mirones: {1}".format(peleadores, mirones))
    probGanar = np.around((1 - peleadores/100), decimals=2)
    print(probGanar)
    if guardiaConLuma:
        weights = [probGanar, np.around(1-probGanar, decimals=2)]
    else:
        probGanar = probGanar - 0.1
        weights = [probGanar, np.around(1-probGanar, decimals=2)]
    print(weights)
    guardiaGana = np.random.choice(elements,1, p=weights)
    if guardiaGana:
        if sansanes - grupo == 0:
            texto = "Perdieron los sansanos" # Final text
            print(texto)
        else:
            if guardiaConLuma:
                pierdeLuma = np.random.choice(elements, 1, p=pesosLuma)
                if pierdeLuma:
                    guardiaConLuma = 0
                    texto = "Gana guardia pero pierde la luma"
                else:
                    texto = "Gana guardia"
            else:
                texto = "Gana guardia"
            # Actualizacion de sansanos
            sansanes -= grupo
            # Escribir texto de que guardia gano, con la variable de la luma
            print(texto)

    # Si es que el guardia pierde
    else:
        guardiaConLuma = 1
        guardias -= 1
        if guardias == 0:
            print("Ganaron los sansanos")
        else:
            print("Pierde guardia")
    print("\n\n")
        # Imprimir texto de que los sansanos le ganaron al guardia
    

