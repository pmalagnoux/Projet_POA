
def triInsertion_cy():
    fichier = open("/Users/hugoreinhardt/PycharmProjects/testProject/data.txt", "r")
    cdef int lignetemp[100]
    cdef int* tmp = []
    for i in range(1000):
        tabLine= fichier.readline()[1:-3].split(",")
        for i in range(len(tabLine)):
            lignetemp[i] = int(tabLine[i])
        triInsertion(lignetemp, 100)
    fichier.close()

cdef void triInsertion(int array[], int n):
    cdef int i, j, x
    for i in range(0, n - 1, 1):
        x = array[i]
        j = i
        while(j > 0 & array[j-1] > x):
            array[j] = array[j-1]
            j -= 1
        array[j] = x