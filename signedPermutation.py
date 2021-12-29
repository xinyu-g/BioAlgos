from itertools import product
n = int(open('rosalind_sign.txt','r').read().strip())
# n = 2
def printSignedPerm(permutation):
    signs = product([1,-1], repeat = len(permutation))
    # print(permutation)
    
    for sign in signs:
        # print(sign)
        signedPerm = []
        for i in range(len(permutation)):
            signedPerm.append(sign[i]*permutation[i])
        for num in signedPerm:
            print(num, end=' ')
        print()

init_perm = list(range(1, n+1))

def findPerm(permutation, l, r):
    if (l == r):
        printSignedPerm(permutation)
    else:
        for i in range(l, r+1):
            permutation[l], permutation[i] = permutation[i], permutation[l]
            findPerm(permutation, l+1, r)
            permutation[l], permutation[i] = permutation[i], permutation[l]

num = 2**n
for i in range(1, n+1):
    num = num*i

print(num)

findPerm(init_perm, 0, n-1)
