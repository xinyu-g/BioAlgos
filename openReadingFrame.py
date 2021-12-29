import itertools

DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}

DNA_Complement = {"A": "T", "C": "G", "T": "A", "G": "C"}

def readFile(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

FASTAFile = readFile('rosalind_orf.txt')
seq = ''.join(FASTAFile[1:])

def translation(seq, init_pos = 0):
    return ''.join(DNA_Codons[seq[pos:pos+3]] for pos in range(init_pos, len(seq) - 2, 3))

def reverse_complement(seq):
    return ''.join(DNA_Complement[nuc] for nuc in seq)[::-1]

def find(s, ch):
    return [i for i, l in enumerate(s) if l == ch]

def findIndex(start, stop):
    combination = itertools.product(start, stop)
    return [(m,n) for (m,n) in combination if m < n]




def readingFrame(seq):
    reverseSeq = reverse_complement(seq)
    proteinReadingFrame = []
    for i in range(3):
        ProteinSeq_1 = translation(seq, i)
        ProteinSeq_2 = translation(reverseSeq, i)
        start_1 = find(ProteinSeq_1, 'M')
        stop_1 = find(ProteinSeq_1, '_')
        start_2 = find(ProteinSeq_2, 'M')
        stop_2 = find(ProteinSeq_2, '_')
        combination_1 = findIndex(start_1, stop_1)
        combination_2 = findIndex(start_2, stop_2)
        for m,n in combination_1:
            proteinReadingFrame.append(ProteinSeq_1[m:n])
        for m,n in combination_2:
            proteinReadingFrame.append(ProteinSeq_2[m:n])
    return proteinReadingFrame
        
proteinReadingFrame = [proteinSeq for proteinSeq in readingFrame(seq) if '_' not in proteinSeq]
ProteinList = set(proteinReadingFrame)
for protein in ProteinList:
    print(protein)



        




        

    



