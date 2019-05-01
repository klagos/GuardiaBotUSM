import numpy as np
import random as rd

guardias = 15
sansanes = 5501

while sansanes > 0:
    grupo = np.random.normal(10,5,1)
    print(grupo)
    sansanes-=grupo

    prob = rd.random()
    peleadores = round(grupo*prob)
    mirones = grupo - peleadores

    prob_perderluma = 0.01
    prob_ganar = 0.9