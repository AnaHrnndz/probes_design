#!/usr/bin/env python
# A.H.P 2023
# Biorare


from ete4 import SeqGroup
from collections import defaultdict
import json

'''
    Create a fasta file with all nucleotide sequences from xenobiotic ko 
'''

clean_fasta = SeqGroup('/home/plaza/projects/biorare/results/clean_total_nuc_seqs.fn')


ko2genes = json.load(open('/home/plaza/projects/biorare/results/ko2genes.json'))
print(len(ko2genes))


# xenob_ko = set()
# with open('/home/plaza/projects/biorare/raw/Marker_functional_genes__xenobiotics_specific.tsv') as fin:
    # for line in fin:
        # if not line.startswith('#'):
            # info = line.strip().split('\t')
            # ko = info[2]
            # xenob_ko.add(ko)
# print(len(xenob_ko))

xenob_ko = json.load(open('/home/plaza/projects/biorare/results/xenob_ko2path_descp.json'))

miss_xenob = defaultdict(list)

fasta_xenob = open('/home/plaza/projects/biorare/results/xenob_total_nuc_seqs_2.fn', 'w')
for ko in xenob_ko.keys():
    ko_mems = ko2genes[ko]
    for m in ko_mems:
        seq_name = ko+'_'+m
        try:
            nuc = clean_fasta.get_seq(m)
            fasta_xenob.write('>'+seq_name+'\n'+nuc+'\n')
           
        except:
            miss_xenob[ko].append(seq_name)
            

fasta_xenob.close()

with open('/home/plaza/projects/biorare/results/miss_xenob_ko_2.tsv', 'w') as fout:
    for ko, seqs in miss_xenob.items():
        fout.write(ko+'\t'+','.join(seqs)+'\n')

# with open('/home/plaza/projects/biorare/results/miss_xenob_genes_2.tsv', 'w') as fout:
    # fout.write('\n'.join(miss_xenob))
