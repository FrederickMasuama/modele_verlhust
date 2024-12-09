
# Modèle de verlhust : modèle logistique


Ce projet vise à faire l'étude d'une croissance en utilisant le modèle logistique. 
Cette croissance peut être démographique, propagation d'une maladie, adoption d'une technologie, exploitation des ressources naturelles ...

Contrairement au modèle de Malthus qui ne prend en compte aucune contrainte ou perturbation, celui-ci considère les contraintes et perturbations del'environnement encapsulées dans ce que nous appelons "la capacité biotique" : ce qui peut être traduit comme le maximum de croissance que peut tolérer l'environnement. 

Ainsi vous pourrez voir la courbe globale de croissance, l'intervalle de temps dans lequel la croissance commence à ralentir et celui dont elle devient statique. 




## A propos du code

Le code fait usage de deux librairies python : numpy et matplotlib.pyplot 
L'équation différentielle que génère le modèle logistique est résolue à la main car elle est simple, de la forme << y' = a y + b $y^2$ >> 

Sur un intervalle de temps allant de 0 à 100 considéré comme jours, semaines, années... selon la mesure de temps ayant fournie le taux de croissance intrinsèque, le programme retourne un longue tableau listant les valeurs à chaque instant t ainsi qu'un graphe de la courbe de croissance globale. 

Enfin, pour tester le code, vous aurez besoin, en plus de la capacité biotique, des taux croissance et décroissance que nous avons référencé comme taux de naissance et de mortalité.

## Equation du modèle

Le modèle logistique est bâti en partant du modèle de Malthus ainsi on a: 

$$ N'(t) = rN(t)x(1 - \frac{N(t)}{k}) $$

avec 
* r = taux de croissance intrinsèque = a - b
* a = taux de croissance (natalité)
* b = taux de décroissance (mortalité)
* k = capacité biotique = r/c
* c = le coefficient de compétition et/ou contraintes
* N_0 = valeur initiale

Après resolution à la main, nous avons la solution suivante, à l'équation différentielle: 

$$ N(t) = \frac{k}{1 + (\frac{k}{N_0} -1)exp(-rt)} $$     



