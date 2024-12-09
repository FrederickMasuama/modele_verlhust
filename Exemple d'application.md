
# Exemple d'application de Verlhust

Supposons qu'on dispose des données suivantes (fictives, mais basées sur des observations réelles) sur la population de poissons dans un lac, où la population a été mesurée sur une période de 10 ans. 




## Tableau de données
![Capture d’écran verlhust_poisson](https://github.com/user-attachments/assets/682064dc-13e6-449c-b956-d1aa6c03db8d)


## objectifs
* Estimer les paramètres r(taux de croissance) et k(capacité biotique) à partir de ces données réelles. 

* Utiliser le modèle de Verlhust pour ajuster ces paramètres

## processus
Nous allons premièrement estimer r et k en utilisant une approche de regression pour ajuster le modèle Verelhust à ces données puis la modélisation en ajustant notre modèle de croissance logisdtique en utilisant les données réelles. 

## code
Voici un code Python qui fait cela en ajustant les paramètres r et K au modèle de Verhulst à l'aide de l'optimisation :


```python 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Données réelles simulées sur la population de poissons
annees = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
population = np.array([50, 60, 80, 110, 150, 180, 200, 230, 250, 270, 290])

# Fonction solution de l'équa diff de Verhulst
def logistique(t, r, K, P0):
    return K / (1 + ((K - P0) / P0) * np.exp(-r * t))

# Estimation des paramètres (r, K, P0) via courbe de régression
params, covariance = curve_fit(logistique, annees, population, p0=[0.1, 500, 50])

r_estime, K_estime, P0_estime = params
print(f"Paramètres estimés : r = {r_estime:.4f}, K = {K_estime:.0f}, P0 = {P0_estime:.0f}")

# Tracer les données et la courbe ajustée
t_eval = np.linspace(0, 10, 500)
population_fit = logistique(t_eval, r_estime, K_estime, P0_estime)

plt.figure(figsize=(10, 6))
plt.plot(annees, population, 'o', label="Données réelles", color='red')
plt.plot(t_eval, population_fit, '-', label="Modèle ajusté (Verhulst)", color='blue')
plt.title("Ajustement du modèle de Verhulst à des données réelles")
plt.xlabel("Années")
plt.ylabel("Population de poissons")
plt.legend()
plt.grid(True)
plt.show()
```

Le code nous renvoie la courbe suivant: 

![Capture d’écran verlhust_poisson_courbe](https://github.com/user-attachments/assets/735297c4-fa09-4230-a19e-aa056685ad7c)

Et nous avons les paramètres estimés : r = 0.3947, K = 318, P0 = 46

## explication des resultats et interprétation

* Le code a ajusté les paramètres r et K pour minimiser l'erreur entre les données réelles et le modèle logistique. 
* Le graphique a affiché à la fois les données et la courbe de modèle ajustée, ce qui nous a permis de voir comment le modèle de Verhulst correspond à la dynamique de la population de poissons.
* Avec r(taux de croissance de la population), k(la capacité maximale d'accueil du lac) et P0(la population initiale des poissons), le modèle logistique nous aide à visionner l'évolution de la population ainsi que les limites de leur environnement, ce qui est utile pour la gestion des ressources naturelles et la prédiction de l'évolution de la population de poissons dans un milieu limité, en l'occurence, ce lac fictif. 
