#!/usr/bin/env python
# A.H.P 2023
# Biorare

from ete4 import SeqGroup
from collections import defaultdict
import json

'''
    Create a fasta file with all sequences from xenobiotic ko 
'''

clean_fasta = SeqGroup('/home/plaza/projects/biorare/results/clean_total_aa_seqs.fa')


ko2genes = json.load(open('/home/plaza/projects/biorare/results/ko2genes.json'))
print(len(ko2genes))


xenob_ko = set()
with open('/home/plaza/projects/biorare/raw/Marker_functional_genes__xenobiotics_specific.tsv') as fin:
    for line in fin:
        if not line.startswith('#'):
            info = line.strip().split('\t')
            ko = info[2]
            xenob_ko.add(ko)
print(len(xenob_ko))

miss_xenob = defaultdict(set)
fasta_xenob = open('/home/plaza/projects/biorare/results/xenob_total_aa_seqs.fa', 'w')
for ko in xenob_ko:
    ko_mems = ko2genes[ko]
    for m in ko_mems:
        seq_name = ko+'_'+m
        try:
            nuc = clean_fasta.get_seq(m)
            fasta_xenob.write('>'+seq_name+'\n'+nuc+'\n')
            
        except:
            miss_xenob[ko].add(m)
            

fasta_xenob.close()

with open('/home/plaza/projects/biorare/results/miss_ko_seqs_aa.tsv', 'w') as fout:
    for k, val in miss_xenob.items():
        fout.write(k+'\t'+','.join(list(val)))