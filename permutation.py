
n = int(open('rosalind_perm.txt', 'r').read().strip())
# n = 3 

def printPermutation(permutation):
    for item in permutation:
        print(item, end = ' ')
    print()

permutation = list(range(1, n + 1))

def permute(permutation, l, r):
    if l == r:
        printPermutation(permutation)
    else:
        for i in range(l, r+1):
            permutation[l], permutation[i] = permutation[i], permutation[l]
            permute(permutation, l+1, r)
            permutation[l], permutation[i] = permutation[i], permutation[l]
        
num = 1
for i in range(1, n+1):
    num = num * i

print(num)

permute(permutation, 0 , len(permutation) - 1)
    





