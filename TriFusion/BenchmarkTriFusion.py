import os
import time
from numpy import mean
def benchTriFusion():
    tests = [('jython (py)', 'jython TriFusion\TriFusion.py'),
            ('jython (class)', 'jython TriFusion\TriFusion$py.class')]

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