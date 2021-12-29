import math
File = [l.strip() for l in open('rosalind_prob.txt','r').readlines()]

seq = ''
GC_content = []
for line in File:
    if '0' in line:
        for num in line.split():
            GC_content.append(float(num))
    else:
        seq += line

A = seq.count('A')
T = seq.count('T')
G = seq.count('G')
C = seq.count('C')
res = []
for freq in GC_content:
    GC_freq = freq/2
    AT_freq = (1-freq)/2
    prob = (A+T)*math.log10(AT_freq) + (G+C)*math.log10(GC_freq)
    res.append(prob)

for num in res:
    print(num, end = ' ')