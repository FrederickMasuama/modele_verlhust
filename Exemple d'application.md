
# E
# Exemple d'application

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


## Code Block
```python 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit```
