def readFile(filename):
    with open(filename, 'r') as f:
        return f.read().split()

s,t = readFile('rosalind_subs.txt')

def getZarray(s,t):
    concat = t + '$' + s

    n = len(concat)
    z = [0] * n
    l, r, k = 0, 0, 0

    for i in range(1, n):
        
        
        if i > r:
            l, r = i, i
            while r < n and concat[r - l] == concat[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and concat[r - l] == concat[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z

z = getZarray(s,t)

for i in range(len(z)):
    if z[i] == len(t):
        print(i - len(t), end = " ")




    
    
    