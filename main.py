# DNA Toolset/code trsting file

from DNAToolkit import *
from utilities import colored

# Lets create a random DNA string so that we can test our function

rndDNAStr ="ATTTCGT"

print(validateSeq(rndDNAStr))

rndDNAStr1 = "ATTTCGTX"
print(validateSeq(rndDNAStr1))

rndDNASTR2 = "ATTccGgT"
print(validateSeq(rndDNASTR2))

# Lets generate a random DNA string and dont write by hand

import random
randDNAStr4 = ''.join([random.choice(DNA_Nucleotides)         # ''.join() is a method that takes a list of strings and concatenates them into a single string. The '' at the beginning is the separator (in this case, an empty string), which means there will be no characters between the elements of the list when they are joined.
                      for nuc in range(50)])

DNAStr = validateSeq(randDNAStr4)
print(countNucFrequency(DNAStr))


print(transcription(DNAStr))

# Annotate all the steps so that we can know what is happening in each step

print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))
print(f'[3] + DNA/RNA Transcription: {transcription(colored(DNAStr))}\n')

print(reverse_complement(DNAStr))



print(f"[4] + DNA String + Reverse Complement:\n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"5' {colored(reverse_complement(DNAStr))} 3'\n")



print(f'[5] + GC Content: {gc_content(DNAStr)}%\n')
# use online tool like ENDMEMO GC content calculator to validate your results

print(
    f'[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')

print(
    f'[7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr, 0)}\n') ## Either specify "init_pos = 0" or 
## in the main.py use "{translate_seq(DNAStr, 0)}\n')" If we cahnge this "0" to "5" then we will get shorter output because
## it will start counting from sixth position.


print(
    f'[8] + Codon frequency (L): {codon_usage(DNAStr, "L")}\n')



print('[9] + Reading_frames:')
for frame in gen_reading_frames(DNAStr):
    print(frame)

test_rf_frame = ['L', 'M', 'T', 'A', 'L', 'V', 'V',
                 'L', 'L', 'R', 'R', 'G', 'S', '_', 'G', 'H']

print(proteins_from_rf(test_rf_frame))

# Example 1

print('\n[10] + All prots in 6 open reading frames:')
for prot in all_proteins_from_orfs(NM_000207_3, 0, 0, True):
    print(f'{prot}')

# Example 2
    
print('\n[10] + All prots in 6 open reading frames:')
for prot in all_proteins_from_orfs(AB468090_1, 0, 0, True):
       print(f'{prot}')


# Example 3

print('\n[10] + All prots in 6 open reading frames:')
for prot in all_proteins_from_orfs(JF909299_1, 0, 0, True):
       print(f'{prot}')


