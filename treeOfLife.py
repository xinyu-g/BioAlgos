import itertools

File = [l.strip() for l in open('rosalind_tree.txt','r').readlines()]

n = int(File[0])
edges = []

for line in File[1:]:
    node = [int(s) for s in line.split()]
    edges.append(node)

print(n-1-len(edges))

