"""Etude de la population via Verlhust"""

#IMPORTS

import numpy as np
import matplotlib as plt

#PROGRAMME

#fonction solution de l'équation différenetielle de Verlhust

def f(r, k, N_0, t) :
    return k / (1 + ((k/N_0) - 1) * np.exp(-r * t))

#corps du programme

N_0 = int(input("Quel est lme nombre initial d'individus ?"))
if N_0 == 0 :
    while N_0 == 0 :
        N_0 = int(input("Vous devez mettre une valeur différent de zéro car sinon, il n'y a aucune évolution démographique quand il n'y a pas d'invidus")
else :
    a = int(input("Veillez rentrer le taux de natalité"))
    b = int(input("Veuillez rentrer le taux de mortalité"))
    r = a - b
    t = np.array(0, 100, 100)
    p = int(input("Veuillez taper 1 si vous avez la valeur numérique de la capacité biotique \n ou 2 si vous n'avez que le coefficient de la compétition"))
    if p == 1 :
        k = int(input("Veuillez rentrer la valeur numérique de la capacité biotique"))
    else :
        c = int(input("veuillez rentrer la valeur de la compétition"))
        while c == 0 :
            c = int(input("Veuillez rentrer une valeur autre que zéro s'il vous plaît"))
        k = r/c

    z = f(r, k, N_0, t)

    #points d'équilibres
    #points de stabilité

print(z)

   

    

