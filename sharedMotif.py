def readFile(filename):
    with open(filename, 'r') as f:
        return (l.strip() for l in f.readlines())

FASTAFile = readFile('rosalind_lcsm.txt')
FASTADict = {}

FASTALabel = ""

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

seqList = [v for k,v in FASTADict.items()]

sorted_seqList = sorted(seqList, key = len)
# shortest_seq = sorted_seqList[0]
# comp_seqList = sorted_seqList[1:]
motif = ""

# method one: search all possibilities
# for i in range(len(shortest_seq)):
#     for j in range(1, len(shortest_seq)):
#         m = shortest_seq[i:j+1]
#         shared = False 
#         for seq in comp_seqList:
#             if m in seq:
#                 shared = True
#             else:
#                 shared = False
#                 break
#         if shared and len(m) > len(motif):
#             motif = m

# method two: binary search

def shared_substr(seq, seqs):
    for sequ in seqs:
        if seq not in sequ:
            return False
    return True

def com_substr(seqs, length):
    shortest_seq = seqs[0]
    l = len(shortest_seq)
    for i in range(l-length+1):
        substr = shortest_seq[i:i+length]
        if shared_substr(substr, seqs):
            return substr
    return ""

def longest_com_substr(seqs):
    shortest_seq = seqs[0]
    l = 0
    r = len(shortest_seq)

    while l+1<r:
        mid = int((l+r) / 2)
        if com_substr(seqs, mid) != "": 
            l = mid
        else:
            r = mid
    
    return com_substr(seqs, l)

motif = longest_com_substr(sorted_seqList)

print(motif)


        