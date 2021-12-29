File = [l.strip() for l in open('rosalind_lgis.txt', 'r').readlines()]

n = int(File[0])
seq = []

for line in File[1:]:
    for num in line.split():
        seq.append(int(num))

print(len(seq))
print(n)

def findLIS(seq, n):
    rank = [1]*n
    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j]:
                rank[i] = max(rank[i], rank[j] + 1)
                # print(rank)
    res = []
    length = max(rank)
    for i in range(len(seq)-1, -1, -1):
        if length == rank[i]:
            res.append(seq[i])
            length -= 1
        
    return res[::-1]


def findDIS(seq, n):
    
    rank = [1]*n
    for i in range(1, n):
        for j in range(i):
            if seq[i] < seq[j]:
                rank[i] = max(rank[i], rank[j]+1)
                # print(rank)
    res = []
    length = max(rank)
    for i in range(len(seq)-1, -1, -1):
        if length == rank[i]:
            res.append(seq[i])
            length -= 1
        
    return res[::-1]

LIS = findLIS(seq, n)
DIS = findDIS(seq, n)
# print(seq)
for num in LIS:
    print(num, end=' ')
print()
for num in DIS:
    print(num, end=' ')

