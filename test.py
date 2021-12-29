from DNA import *

DNAstr = open("rosalind_dna.txt")

# rstrip() remove space
DNAseq = DNAstr.read().rstrip()

FreqDict = countNucFrequency(DNAseq)

RNAseq = transcription(DNAseq)

DNA_ReverseComplement = reverse_complement(DNAseq)

gc_content = GC_content(DNAseq)



# [::-1] reverse string

# for k, v in FreqDict.items():
#     print(v, end = ' ')
