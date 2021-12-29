from math import factorial as fact

def readFile(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.read().split()]


k, N = readFile('rosalind_lia.txt')
# k, N = 2, 1

p = 0.25 

def findProb(k, N, p):
    pop = 2**k
    prob = 0
    for i in range(N, pop + 1):
        prob += (p**i)*((1-p)**(pop-i))*fact(pop)/(fact(pop-i)*fact(i))

    return prob
    
print(findProb(k, N, p))