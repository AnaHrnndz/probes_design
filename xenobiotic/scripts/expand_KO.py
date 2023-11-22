#!/usr/bin/env python
# A.H.P 2023
# Biorare

from Bio import SeqIO
from collections import defaultdict
import json

"""
    Create fasta with original xenobiotic kegg-ko seq plus gtdb selected seqs for insilico probes design
"""


ori_ko2genes = json.load(open('/home/plaza/projects/biorare/results/ko2genes.json'))
xenob_ko = set() 
with open('/home/plaza/projects/biorare/results/gtdb_vs_ko/qcov_08/314_ko_list.txt') as f:
    for line in f:
        xenob_ko.add(line.strip())


gtdb_hits = '/home/plaza/projects/biorare/results/gtdb_vs_ko/gtdb_hits_nt.fna'
ko_seqs = '/home/plaza/projects/biorare/results/gtdb_vs_ko/KO_total_nuc_seqs.fn'


gtdb_seqs2include = set()
ko2seqs = defaultdict(set)
total_ko_set = set()
seqs2ko = defaultdict(set)

ko2seqs= defaultdict(set)
with open('/home/plaza/projects/biorare/results/gtdb_vs_ko/qcov_08/ko2gtdb_seqs_expand.tsv') as fin:
#with open('/home/plaza/projects/biorare/results/ko_mmseqs/ko2expand_seqs_qcov_08_v1.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        ko = info[0]
        total_ko_set.add(ko)

        seqs = set(info[2].split(','))
        ko2seqs[ko].update(seqs)

        gtdb_seqs2include.update(seqs)

        for s in seqs:
            seqs2ko[s].add(ko)


#add original KO seqs
for ko in xenob_ko:
    #keep only ko that had been expanded with mmseqs and diamond
    if ko in total_ko_set:
        oriseqs = ori_ko2genes[ko]
        
        ko2seqs[ko].update(set(oriseqs))
        for s in oriseqs:
            seqs2ko[s].add(ko)
            



seqs2keep = defaultdict(set)
for record in SeqIO.parse(ko_seqs, format="fasta"):
    if record.id in seqs2ko.keys():
        #if len(seqs2ko[record.id]) == 1:
        seqs2keep[record.id] = record.seq
        
        
#Keep only gtdb seqs that match with only 1 KO
for record in SeqIO.parse(gtdb_hits, format="fasta"):
    if record.id in seqs2ko.keys():
        if len(seqs2ko[record.id]) == 1:    
            seqs2keep[record.id] = record.seq
        
  


out_fasta = open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/expanded_KO_reciprocal_qcov08_.fna', 'w')

for ko, seqs in ko2seqs.items():
    ko_out = open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/'+ko+'_recirocal_qcov08.fna', 'w')
    #print(ko, seqs)
    for s in seqs:
       
        if s in seqs2keep.keys():
            ko = '|'.join(list(seqs2ko[s]))
            name = ko+'@'+s
            nt_seq = seqs2keep[s]
            
            out_fasta.write('>%s\n%s\n' %(name, nt_seq ))
            ko_out.write('>%s\n%s\n' %(name, nt_seq))
            
    ko_out.close()        
           

out_fasta.close()


         