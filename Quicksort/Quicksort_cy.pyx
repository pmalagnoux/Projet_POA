
def quicksort_cy():
    fichier = open("/Users/hugoreinhardt/PycharmProjects/testProject/data.txt", "r")
    cdef int lignetemp[100]
    for i in range(1000):
        tabLine= fichier.readline()[1:-3].split(",")
        for i in range(len(tabLine)):
            lignetemp[i] = int(tabLine[i])
        quicksort(lignetemp, 0, 99)
    fichier.close()

cdef int partition(int *array, int low, int high):
    cdef int pivot = array[high]
    cdef int i = low - 1
    cdef int j, tmp
    for j in range(low, high, 1):
        if (array[j] <= pivot):
            i += 1
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp

    tmp = array[i + 1]
    array[i + 1] = array[high]
    array[high] = tmp
    return (i+1)

cdef void quicksort(int *array, int low, int high):
    cdef int pi
    if (low < high):
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)
