import random


# Allocation d'un tableau

def setRandomTableau(taille):
    return [random.random() for _ in range(taille)]


if __name__ == '__main__':
    print(setRandomTableau(1000000))
