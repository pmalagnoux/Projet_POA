
def triFusion_cy():
    fichier = open("/Users/hugoreinhardt/PycharmProjects/testProject/data.txt", "r")
    cdef int lignetemp[100]
    cdef int* tmp = []
    for i in range(1000):
        tabLine= fichier.readline()[1:-3].split(",")
        for i in range(len(tabLine)):
            lignetemp[i] = int(tabLine[i])
        triFusion(0, 99, lignetemp, tmp)
    fichier.close()

cdef void triFusion(int i, int j, int tab[], int tmp[]):
    if (j <= i):
        return
    cdef int m = (int) (i + j) / 2
    triFusion(i, m, tab, tmp)
    triFusion(m + 1, j, tab, tmp)

    cdef int pg = i
    cdef int pd = m + 1
    cdef int c

    for c in range(i, j + 1, 1):
        if (pg == m +1):
            tmp[c] = tab[pd]
            pd += 1
        elif (pd == j + 1):
            tmp[c] = tab[pg]
            pg += 1
        elif (tab[pg] < tab[pd]):
            tmp[c] = tab[pg]
            pg += 1
        else:
            tmp[c] = tab[pd]
            pd += 1

    for c in range(i, j+1, 1):
        tab[c] = tmp[c]

