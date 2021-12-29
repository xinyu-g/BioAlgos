import itertools

def readFile(filename):
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]

FASTAFile = readFile('rosalind_grph.txt')

FASTADict = {}
FASTALabel = ""

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line[1:]
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

# FASTADict = {'Rosalind_0442': 'AAATCCC',
#         'Rosalind_0498': 'AAATAAA',
#         'Rosalind_2323': 'TTTTCCC',
#         'Rosalind_2391': 'AAATTTT',
#         'Rosalind_5013': 'GGGTGGG'}
edges = []

def isOverlap(s, t, k):
    return s[-k:] == t[:k]

k = 3

for k1, k2 in itertools.combinations(FASTADict, 2):
    v1, v2 = FASTADict[k1], FASTADict[k2]

    if isOverlap(v1, v2, k):
        edges.append([k1, k2])

    if isOverlap(v2, v1, k):
        edges.append([k2, k1])

for u,v in edges:
    print(u + " " + v)
    