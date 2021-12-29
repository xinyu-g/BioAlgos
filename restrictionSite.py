import DNA

FASTAFile = [l.strip() for l in open('rosalind_revp.txt', 'r').readlines()]
seq = ''.join(FASTAFile[1:])



def isPalindrome(seq, k):
    palindromePair = [('A', 'T'), ('T', 'A'), ('G', 'C'), ('C', 'G')]
    for i in range(len(seq)-k+1):
        sequence = seq[i:i+k]
        if all((sequence[j], sequence[k-j-1]) in palindromePair for j in range(k)):
            print(i + 1, k)

for k in range(4, 14, 2):
    isPalindrome(seq, k)
