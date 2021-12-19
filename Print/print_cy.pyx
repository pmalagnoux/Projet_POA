
def printMultiple_cy(int n, char* string):
    return printMultiple(n, string)

cdef void printMultiple(int n, char* string):
    for _ in range(n):
        print(string)