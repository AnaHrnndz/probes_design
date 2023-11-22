#!/usr/bin/env python
# A.H.P 2023
# Biorare

import json
from ete4 import SeqGroup
from collections import defaultdict

'''
    Get aa fasta file for each ko

    2. Write fasta file
    3. Some ko mems are missing, it should be virus seqs
'''




clean_fasta = SeqGroup('/home/plaza/projects/biorare/results/clean_total_aa_seqs.fa')

#ko xenob mems
with open('/home/plaza/projects/biorare/results/ko2genes.json') as f:
    ko2genes = json.load(f)



code2t_name = defaultdict()
with open('/home/plaza/databases/kegg/taxonomy') as f:
    for line in f:
        if not line.startswith('#'):
            info = line.strip().split('\t')
            t_name = info[0]
            code = info[1]

miss_mems = list()
for ko, mems in ko2genes.items():
    with open('/home/plaza/projects/biorare/results/ko_aa/'+ko+'.fa', 'w') as fout:
        for m in mems:
            try:
                nuc = clean_fasta.get_seq(m)
                fout.write('>'+m+'\n'+nuc+'\n')
            except:
                miss_mems.append(m)


#miss_mems should be only seqs from virus 
with open('/home/plaza/projects/biorare/results/miss_ko_mems_aa.tsv', 'w') as fout:
    fout.write('\n'.join(miss_mems))