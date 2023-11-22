import json
from collections import defaultdict
from Bio import SeqIO
import glob
import os


global_kpath = ['01100', '01110', '01120', '01200', '01210', '01212', '01230', '01232', '01250', '01240', '01220']
eko = defaultdict(set)

with open('/home/plaza/projects/biorare/results/eko2path.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        if info[1] not in global_kpath:
            eko[info[0]].add(info[1])

print(len(eko))

specific_eko = set()
for eko, kpath in eko.items():
    if len(kpath) <=2:
        specific_eko.add(eko)
        init_fasta = '/home/plaza/projects/biorare/results/ko_nucleotides/'+eko+'.fn'
        with open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_expanded/expanded_'+eko+'.fna', 'w') as fout:
            for record in SeqIO.parse(init_fasta, format="fasta"):
                fout.write('>'+record.id+'\n'+str(upper(record.seq))+'\n')

print(len(specific_eko))
#input()

gtdb2ko = dict()
ko2gtdb = defaultdict(set)
with open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/ko2gtdb.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')

        if info[0] in specific_eko:

            gtdb_seqs = set(info[2].split(','))
            ko2gtdb[info[0]] = gtdb_seqs

            for s in gtdb_seqs:
                new_s = s.replace('.faa_', '.fna_')
                gtdb2ko[new_s] = info[0]

print(len(gtdb2ko))


gtdb_fasta = '/home/plaza/projects/biorare/databases/gtdb_db/gtdb_proteins_nt_reps_r207_complete_id.fna'
for record in SeqIO.parse(gtdb_fasta, format="fasta"):
    if record.id in gtdb2ko.keys():
        ko = gtdb2ko[record.id]
        with open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_expanded/expanded_'+ko+'.fna', 'a') as fout:
            fout.write('>'+record.id+'\n'+str(upper(record.seq))+'\n')



