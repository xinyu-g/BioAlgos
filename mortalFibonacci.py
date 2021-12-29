def readFile(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.read().split()]


n, m = readFile('rosalind_fibd.txt')
# n,m = 6,3

def MortalFib(n, m):
    ages = [0] * m
    ages[-1] = 1 
    for _ in range(n - 1):
        newborns = sum(ages[:-1])
        ages[:-1] = ages[1:]
        ages[-1] = newborns
    return sum(ages)


print(MortalFib(n,m))