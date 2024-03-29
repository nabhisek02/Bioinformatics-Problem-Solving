#DNA Toolkit File

from structures import *

# Check the sequence to make sure it is a DNA String
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()     # The lowercase and uppercase letters are not same in ASCII table
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    # return dict(collections.Counter(seq))


# For optimization of the python code
import collections

#def countNucFrequency(seq):
    #return dict(collections.Counter(seq))

def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine with Uracil"""
    return seq.replace("T", "U")

def reverse_complement(seq):
   """Swapping adenine with thymine and guanine with cytosine. 
   Reversing newly generated string"""
   # return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]   # you can use this version or,

   # More Pythonic solution. A little bit faster solution.
   mapping = str.maketrans('ATCG', 'TAGC')             
   '''The str.maketrans() function is a static method that creates a translation table. 
   Here, it maps 'A' to 'T', 'T' to 'A', 'C' to 'G', and 'G' to 'C'.'''
   return seq.translate(mapping)[::-1]

def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


def gc_content_subsec(seq, k=20):
    """GC Content in a DNA/RNA sub-sequence length k. k=20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):    # range(start, stop, step); In this case, start is 0, stop is len(seq) - k + 1, and step is k.
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res
