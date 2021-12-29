n = int(open('rosalind_sset.txt', 'r').read())
# n = 3
res = 1 
for _ in range(n):
    res = res * 2 % 1000000

print(res)