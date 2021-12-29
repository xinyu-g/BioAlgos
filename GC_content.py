from DNA import *

def readFile(filename):
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]
    

def gc_content(seq):
    return round((seq.count('G') + seq.count('C'))/len(seq) * 100, 6)

FASTAFile = readFile('rosalind_gc.txt')

FASTADict = {}

FASTALabel = ""

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

gcDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

maxGCKey = max(gcDict, key = gcDict.get)

print(maxGCKey[1:])
print(gcDict[maxGCKey])

# print(gcDict)