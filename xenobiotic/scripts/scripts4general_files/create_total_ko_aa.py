#!/usr/bin/env python
# A.H.P 2023
# Biorare


from ete4 import SeqGroup
from collections import defaultdict
import json

'''
    Create a fasta file with all aa sequences in KEGG KO
'''

clean_fasta = SeqGroup('/home/plaza/projects/biorare/results/clean_total_aa_seqs.fa')

total_genes = set()
ko2genes = json.load(open('/home/plaza/projects/biorare/results/ko2genes.json'))

print(len(ko2genes))
genes2ko = defaultdict(list)
for ko, genes in ko2genes.items():
    total_genes.update(set(genes))
    for g in genes:
        genes2ko[g].append(ko)
    
print(len(total_genes))
miss_seqs = defaultdict(list)

fasta_ko = open('/home/plaza/projects/biorare/results/ko_vs_gtdb/KO_total_aa_seqs.fa', 'w')
for gene in total_genes:
    try:
        nuc = clean_fasta.get_seq(gene)
        fasta_ko.write('>'+gene+'\n'+nuc+'\n')
       
    except:
        ko = (genes2ko[gene])
        miss_seqs[gene] = ko  

fasta_ko.close()

miss_seqs_ko = open('/home/plaza/projects/biorare/results/ko_vs_gtdb/miss_seqs_aa.tsv', 'w')
for ko, miss_seqs in miss_seqs.items() :
    miss_seqs_ko.write(ko+'\t'+','.join(miss_seqs)+'\n')
miss_seqs_ko.close()

with open('/home/plaza/projects/biorare/results/ko_vs_gtdb/gene2ko.json', 'w') as fout:
    json.dump(genes2ko, fout)