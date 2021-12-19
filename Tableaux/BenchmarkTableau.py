# coding=utf-8
import os
import time
from numpy import mean
def benchTableau():
    tests = [('Jython (py)', 'jython Tableaux\Tableau.py'),
            ('Jython (class)', 'jython Tableaux\Tableau$py.class')]

    data = []
    plotting = True
    for label, cmd in tests:
        ret = []
        print("%s..." % label)
        for i in range(3):
            t1 = time.time()
            result = os.popen(cmd).read()
            taken = time.time() - t1
            ret.append(taken)
        taken = mean(ret)
        data.append((taken, label))

    data.sort()
    data.reverse()
    result = []
    for d,l in data:
        result.append((l.ljust(30), ("%.3f" % d).ljust(10), 'sec'))
    return result

'''
if plotting:
    data, labels = zip(*data)
    from pylab import array, bar, yticks, xticks, show, grid, arange, xlabel, ylabel, title

    xlocations = array(range(len(data))) + 0.5
    width = 0.5
    bar(xlocations, data, width=width)
    yticks(arange(0, max(data) + 1, .5))
    grid()
    xticks(xlocations, labels)
    xlabel("Python Interpeter / Platform")
    ylabel("Time (sec)")
    title("Creation d'un Tableau de 1000000 à valeurs")
    show()
'''