"""Etude de croissance démographique par le modèle de Verlhust
                    - Croissance logistique -                 """

#IMPORTS

import numpy as np
import matplotlib.pyplot as plt

#PROGRAMME

#fonction solution de l'équation différenetielle de Verlhust

def f(r, k, N_0, t) :
    return k / (1 + ((k/N_0) - 1) * np.exp(-r * t))

#données

N_0 = int(input("Quel est le nombre initial d'individus ?"))
coeff_nat = float(input("Veillez rentrer le taux de natalité"))
coeff_mort = float(input("Veuillez rentrer le taux de mortalité"))
k = float(input("Veuillez rentrer la valeur numérique de la capacité biotique"))
r = coeff_nat - coeff_mort
t = np.linspace(0, 100, 100)

#résolution

z = f(r, k, N_0, t)

#affichages

print(z)
plt.plot(t,z, label = f"r={r}, k={k}, N_0={N_0}")
plt.title("Modèle de Verhulst (croissance logistique)")
plt.xlabel("Temps")
plt.ylabel("Population")
plt.legend()
plt.show()
