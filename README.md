# Projet_POA Benchmark Python Jython Cython

# Parties

Ce projet comprte 2 branches : \
main -> Benchmark Python Cython Jython \
Test_Jython -> Benchmark Jython
# Prérequis

>Python 2 \
Python 3 \
Jython https://www.jython.org/\
Cython \
Compilateur c

# Exécution

Après avoir installé tous le necessaire, il faut modifier les chemis dans les tableaux "test" dans les fichiers Benchmark_.py. 

Il faut ensuite avec python 2 lancer le fichier setup.py qui permet de compiler les fichier cython.

Une fois cela fait on exécute le fichier BenchmarkAll.py avec python 2 et on peut lire les résultats dans Résultats.txt

Une fois cela fait On peut modifier les valeurs dans le fichier python plotPOA.py qui va afficher les courbes avec les différentes valeurs trouvé.
Pour l'éxécuter il faut absoluement Python 3 car le module matplotlib n'est disponible qu'à partir de cette version de python.

# But

Le but de cette analyse est d'illustrer les différences de performance entre Python, Cython et Jython. Pour cela nous effectuons un test de Benchmark avec divers programmes simples sollicitants plusieurs composantes  comme la mémoire, la gestion des variables et des tableaux et le calcul pur.

#
