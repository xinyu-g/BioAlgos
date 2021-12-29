def readFile(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.read().split()]
        # return f.read().split()

k, m, n = readFile('rosalind_iprb.txt')
# k, m, n = 2, 2, 2

t = k + m + n



# homozygous dominant
pk1 = round(k/t,5)
pk = round(k/(t-1), 5)
pk2 = round((k-1)/(t-1), 5)

# heterozygous
pm1 = round(m/t, 5)
pm = round(m/(t-1), 5)
pm2 = round((m-1)/(t-1), 5)

# homozygous recessive
pn1 = round(n/t, 5)
pn = round(n/(t-1), 5)
pn2 = round((n-1)/(t-1), 5)

# mating results in dominant allele 
pd = pk1*pk2 + pk1 * pm + pm1 * pk + pk1 * pn + pn1 * pk + pm1*pm2*0.75 + pm1*pn*0.5 + pn1*pm*0.5
print(pd)

# alternatively calculate mating results in recessive allele
pr = pm1*pm2*0.25 + pm1*pn*0.5 + pn1*pm*0.5 + pn1*pn2
print(1-pr)


