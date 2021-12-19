from libc.stdlib cimport calloc, free

def nb_premier_cy(int limit):
    return nb_premier(limit)

cdef nb_premier(int limit):
    cdef int i, j
    cdef char *buff = <char *> calloc(limit, 1)
    for i in range(2, limit, 1):
        if (buff[i] != 1):
            for j in range(i+i, limit, i):
                buff[j] = 1
    for i in range(2, limit, 1):
        if (buff[i] != 1):
            print(i)
    free(buff)