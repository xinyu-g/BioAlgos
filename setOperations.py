File = [l.strip() for l in open('rosalind_seto.txt', 'r').readlines()]

res = open('setOperations.txt', 'w+')


n = int(File[0])

A = {int(s) for s in File[1][1:len(File[1])-1].split(', ') if s.isdigit()}

B = {int(s) for s in File[2][1:len(File[2])-1].split(', ') if s.isdigit()}

C = set(range(1, n+1))

AUB = A.union(B)
res.write(str(AUB) + '\n')

AnB = A.intersection(B)
res.write(str(AnB) + '\n')


A_B = A.difference(B)
res.write(str(A_B) + '\n')

B_A = B.difference(A)
res.write(str(B_A) + '\n')

Ac = C.difference(A)
res.write(str(Ac) + '\n')

Bc = C.difference(B)
res.write(str(Bc) + '\n')

res.close()









