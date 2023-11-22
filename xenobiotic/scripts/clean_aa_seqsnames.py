#!/usr/bin/env python
# A.H.P 2023
# Biorare

from ete4 import SeqGroup

'''
    Clean aa seqs names
'''

fasta = SeqGroup('/home/plaza/projects/biorare/raw/total_aa_seqs.fa')
print(len(fasta))

clean_fasta = open('/home/plaza/projects/biorare/results/clean_total_aa_seqs.fa', 'w')
for num, (name, seq, _) in enumerate(fasta):
    clean_name = name.split(' ')[0]
    clean_fasta.write('>'+clean_name+'\n'+seq+'\n')
    
clean_fasta.close()