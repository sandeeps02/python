import math
L = [3, 1, 2, 4]
T = ('A', 'b', 'c', 'd')
L.sort()
counter = 0
for x in T:
    L[counter] += ord(x)
    counter += 1
    break
print(math.ceil(max(L)/min(L)))