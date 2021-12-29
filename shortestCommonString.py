import itertools
FASTAFile = [l.strip() for l in open('rosalind_long.txt', 'r').readlines()]
FASTADict = {}
FASTALabel = ''
for line in FASTAFile:
    if '>'in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ''
    else:
        FASTADict[FASTALabel] += line

strings = []
for k,v in FASTADict.items():
    strings.append(v)

# print(strings)

def overlap(a, b, min_length = 3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

def scs(ss):
    shortest_sup = None 
    for ssperm in itertools.permutations(ss):
        # print(ssperm)
        sup = ssperm[0]
        for i in range(len(ss)-1):
            olen = overlap(ssperm[i], ssperm[i+1], min_length = 1)
            sup += ssperm[i+1][olen:]
        if shortest_sup == None or len(sup) < len(shortest_sup):
            shortest_sup = sup
    return shortest_sup

def pick_max_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0
    for a, b in itertools.permutations(reads, 2):
        olen = overlap(a, b, min_length = k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, best_olen

def greedy_scs(reads, k):
    read_a, read_b, olen = pick_max_overlap(reads, k)
    while olen > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_max_overlap(reads, k)
    return ''.join(reads)

print(greedy_scs(strings, 1))