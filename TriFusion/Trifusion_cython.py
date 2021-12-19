import random

import Trifusion_cy


arr = [random.randint(0, 100000) for _ in range(100000)]
tmp = []
n = len(arr)
Trifusion_cy.triFusion_cy()

print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])