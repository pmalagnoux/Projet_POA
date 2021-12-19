import random
def generateIntTab(taille, max):
    return [random.randint(0,max) for _ in range(taille)]


def duplicateTab(tab):
    return tab[:]

def generateNtab(n, taille, max):
    return [generateIntTab(taille, max) for _ in range(n)]

def duplicateNtab(Ltab):
    return [duplicateTab(tab) for tab in Ltab]

L = generateNtab(2, 10, 10)
L2 = duplicateNtab(L)


#Creation des tableaux
L = generateNtab(1000, 100, 100)
fichier = open("data.txt", "a")
for tab in L:
    fichier.write(tab.__str__() + "\n")

fichier.close()





