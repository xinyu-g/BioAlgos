def readFile(filename):
    with open(filename, 'r') as f:
        return f.read().split()






# Z Algorithm
def getZarray(s, z):
    n = len(s)

    l, r, k = 0, 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i , i

            while r < n and s[r - l] == s[r]:
                r += 1
            z[i] = r - l 
            r -= 1
        else:
            k = i - l

            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1

def search(s, t):
    com = t + '$' + s
    l = len(com)

    z = [0] * l
    getZarray(com, z)

    for i in range(l):
        if z[i] == len(t):
            print(i - len(t), end = " ")


# s = "GATATATGCATATACTT"
# t = "ATAT"
s, t = readFile('rosalind_subs.txt')
search(s, t)

