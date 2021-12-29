
def readFile(filename):
    with open(filename, 'r') as f:
        return f.read().split()

s, t = readFile('rosalind_hamm.txt')

dH = 0

for i in range(len(s)):
    if (s[i] != t[i]):
        dH += 1

print(dH)