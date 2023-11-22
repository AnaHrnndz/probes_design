#!/usr/bin/env python
# A.H.P 2023
# Biorare

from Bio import SeqIO

"""
    Create fasta file with all gtdb seqs hits from mmseqs search
"""

target_ids = set()
with open('/home/plaza/projects/biorare/results/gtdb_vs_ko/gtdb_hit_seqs.txt') as f:
    for line in f:
        target_ids.add(line.strip())

print(len(target_ids))
#fasta_file = '/home/plaza/projects/biorare/gtdb_db/gtdb_proteins_nt_reps_r207_complete_id.fna'
fasta_file = '/home/plaza/projects/biorare/gtdb_db/gtdb_aa/gtdb_proteins_aa_reps_r207_complete_id.faa'

#fout = open('/home/plaza/projects/biorare/results/gtdb_vs_ko/gtdb_hits_nt_v3.fna', 'w')
fout = open('/home/plaza/projects/biorare/results/gtdb_vs_ko/gtdb_hits_aa.faa', 'w')
for record in SeqIO.parse(fasta_file, format="fasta"):
    record_id_nt = record.id.replace('.faa', '.fna')
    if record_id_nt in target_ids: 
        fout.write('>%s\n%s\n' %(record.id, record.seq))

fout.close()


