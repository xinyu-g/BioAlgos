import itertools
from math import pow


# n, m = [int(x) for x in open('rosalind_aspc.txt', 'r').read().split()]
n, m = 6, 3

res = 0
pool = list(range(1, n+1))
for k in range(m, n+1):
    
    com = 1
    for i in range(n, n-k, -1):
        if (com == 0 or com == 0.0):
            com = 1
        com = com * i % 1000000
    
    # base = 1
    for i in range(1, k+1):
        if (com == 0 or com == 0.0):
            com = 1
        base = 1
        for _ in range(1000000-2):
            base = base*i % 1000000
        com = com * base % 1000000
    # for _ in range(1000000-2):
    #     base = base * base % 1000000
    # com = com * base % 1000000
    res = (res + com) % 1000000
    

print(res)
