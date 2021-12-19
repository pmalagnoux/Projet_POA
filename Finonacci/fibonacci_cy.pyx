from libc.stdint cimport int64_t

def fib_cdef(int n):
    return fib_in_c(n)

cdef int64_t fib_in_c(int n):
    cdef int64_t x = 0
    cdef int64_t y = 1
    cdef int64_t z
    for i in range(1, n):
        z = x + y
        x = y
        y = z
    return y
