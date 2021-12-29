def readIntegers(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split()]

n, k = readIntegers("rosalind_fib.txt")


print(n,k)

# fibonacci: f(n) = f(n-1) + k*f(n-2)
def countRabbits(n, k):
    
    
    if (n == 1 or n == 2):
        return 1
    else:
        return (countRabbits(n-1, k) + k * countRabbits(n-2, k))


print(countRabbits(n,k))