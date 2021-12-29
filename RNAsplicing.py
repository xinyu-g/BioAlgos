from DNA import *

FASTAFile = [l.strip() for l in open('rosalind_splc.txt', 'r').readlines()]
introns = False
FASTALabel = ''
SpliceDict = {}
for line in FASTAFile:
    if '>' in line:
        if not introns:
            FASTALabel = 'sequence'
        else:
            FASTALabel = line
        SpliceDict[FASTALabel] = ''
        introns = True
    else:
        SpliceDict[FASTALabel] += line

sequence = SpliceDict.get('sequence')
for k,v in SpliceDict.items():
    if k != 'sequence':
        index = sequence.find(v)
        sequence = sequence[:index] + sequence[index + len(v):]
    # print(sequence)

RNA_seq = transcription(sequence)
protein_seq = translate(RNA_seq)

for seq in protein_seq:
    print(seq, end='')