def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split()]

pop = readFile('rosalind_iev.txt')

# print(type(pop))
# pop = [1, 0, 0, 1, 0, 1]

prob = [1, 1, 1, 0.75, 0.5, 0]

# k is the number of offsprings
def expectedValue(pop, prob, k):
    E = [0] * len(pop)
    for i in range(len(pop)):
        E[i] = pop[i] * prob[i]
    
    return k*sum(E)

print(expectedValue(pop, prob, 2))