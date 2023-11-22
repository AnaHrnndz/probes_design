#!/usr/bin/env python
# A.H.P 2023
# Biorare

from Bio import SeqIO
import glob
import os

"""
    Get medium size of genes selected per KO for insilico design
"""


fout = open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/info_input_size.tsv', 'w')
for fasta in glob.glob('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/*_recirocal_qcov08.fna'):
    ko_name = os.path.basename(fasta).strip().split('_')[0] 
    record_dict = SeqIO.to_dict(SeqIO.parse(fasta, "fasta"))
    length = list()
    for name,seq in record_dict.items():
        length.append(len(seq))
    fout.write('\t'.join([ko_name, str(len(record_dict)), str((round(sum(length)/len(record_dict), 3)))+'\n']))

fout.close()
