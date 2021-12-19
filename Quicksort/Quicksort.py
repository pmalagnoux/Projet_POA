import random
def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     
 
    for j in range(low, high):

        if arr[j] <= pivot:
 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 

if __name__ == '__main__':

    fichier = open("data.txt", "r")
    arr = []
    for i in range(1000):
        tabLine = fichier.readline()[1:-2].split(",")
        lignetemp = []
        for n in tabLine:
            lignetemp.append(int(n))
        arr.append(lignetemp)
    fichier.close()

    for i in range(len(arr)):
        quickSort(arr[i], 0, len(arr[i])-1)
        