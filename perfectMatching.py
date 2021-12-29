import math

File = [l.strip() for l in open('rosalind_pmch.txt', 'r').readlines()]

seq = ''.join(File[1:])

num_A = seq.count('A')
num_G = seq.count('G')


print(math.factorial(num_A)*math.factorial(num_G))

