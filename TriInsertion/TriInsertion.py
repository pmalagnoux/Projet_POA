# coding=utf-8
# Programme Python pour l'implémentation du tri par insertion
def tri_insertion(tab):
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)):
        k = tab[i]
        j = i - 1
        while j >= 0 and k < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = k


# Programme principale pour tester le code ci-dessus
if __name__ == '__main__':

    fichier = open("data.txt", "r")
    arr = []
    for i in range(1000):
        tabLine = fichier.readline()[1:-3].split(",")
        lignetemp = []
        for n in tabLine:
            lignetemp.append(int(n))
        arr.append(lignetemp)
    fichier.close()

    for i in range(len(arr)):
        tri_insertion(arr[i])
