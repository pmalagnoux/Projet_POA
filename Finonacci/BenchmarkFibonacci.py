import os
import time
from numpy import mean
def benchFibonacci():
    tests = [('Python (py)', 'python /Users/hugoreinhardt/PycharmProjects/testProject/Finonacci/Fibonacci.py'),
            ('Jython (-jar)', 'bash /Users/hugoreinhardt/PycharmProjects/testProject/Finonacci/FibonacciJy.sh'),
            ('Cython (c)', 'python /Users/hugoreinhardt/PycharmProjects/testProject/Finonacci/fibonacci_cython.py'),
            ('Cython (py)', 'python /Users/hugoreinhardt/PycharmProjects/testProject/Finonacci/Fibonacci.pyx')]

    data = [] 
    plotting = True
    for label, cmd in tests:
        ret = []
        print("%s..." % label)
        for i in range(10):
            t1 = time.time()
            result = os.popen(cmd).read()
            taken = time.time() - t1
            ret.append(taken)
        taken = mean(taken)
        data.append((taken, label))

    data.sort()
    data.reverse()
    result = []
    for d,l in data:
        result.append((l.ljust(30), ("%.3f" % d).ljust(10), 'sec'))
    return result