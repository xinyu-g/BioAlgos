import math

n, k = [int(x) for x in open('rosalind_pper.txt', 'r').read().split()]
# n,k = 21,7

res = 1
print(res)
for i in range(n, n-k, -1):
    print(i)
    res = (res * i) % 1000000

print(res)