import urllib.request as urlreq
import re

def readFile(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

ProteinList = readFile('rosalind_test.txt')

for name in ProteinList:
    proteinName = name.strip('\n')
    url = 'https://www.uniprot.org/uniprot/' + proteinName + '.fasta'
    req = urlreq.Request(url)
    response = urlreq.urlopen(req)
    page = response.read()
    start = page.decode().find('\nM')
    seq = page[start+1:].decode().replace('\n', '')
    seq = ' ' + seq
    regex = re.compile(r'N(?=[^P][ST][^P])')
    # regex = re.compile(r'N(?=[^P][ST][^P])')

    index = 0
    out = []

    while (index < len(seq)):
        

        if re.search(regex, seq[index:]) == None:
            index += 1
            break

        if re.match(regex, seq[index:]) != None:
            out.append(index)
        index += 1

    if out != []:
        print(proteinName)
        print(' '.join([str(i) for i in out]))

