# import numpy as np

def readFile(filename):
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]

FASTAFile = readFile('rosalind_cons.txt')

FASTADict = {}
FASTALabel = ""

for line in FASTAFile:
    
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line



matrix = [list(v) for k,v in FASTADict.items()]


hor = len((matrix[0]))
ver = len(matrix)

print(hor, ver)

# for i in range(ver):
#     print(len(matrix[i]))
def countNucFrequency(seq):
    FreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    for nuc in seq:
        FreqDict[nuc] += 1
    return FreqDict

FreqDict = {'A': [], 'C': [], 'G': [], 'T': []}


for i in range(hor):
    seq = ""
    for j in range(ver):
        seq += matrix[j][i]
        tempDict = countNucFrequency(seq)
    for k,v in FreqDict.items():
        FreqDict[k].append(tempDict[k])
        

l = len(FreqDict.get('A'))
concensus = ""


for i in range(l):
    maxloc = 0
    key = ""
    for k,v in FreqDict.items():
        
        freq = FreqDict[k][i]
        if maxloc < freq:
            maxloc = freq
            key = k
        # print(key)
    concensus += key
        # maxv = max(FreqDict[k][i])
        # print(maxv)
        # maxNuc = max(FreqDict, key = gcDict.get)
        # max_value = max(FreqDict[k][i])  # maximum value
        # max_keys = [k for k, v in dic.items() if v == max_value]


print(concensus)   

for k,v in FreqDict.items():
    print(k + ':', end = " ")
    for num in v:
        print(num, end = " ")
    print('')
        





         


