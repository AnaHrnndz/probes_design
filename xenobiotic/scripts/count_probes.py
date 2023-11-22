#!/usr/bin/env python
# A.H.P 2023
# Biorare

from Bio import SeqIO
import glob
from collections import defaultdict

"""
    Count number of original probes created per KO and number of probes created for low coverage
"""


ko2probes_reciprocal = defaultdict(dict)

for l in  glob.glob('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/result_insilico_test/*/v1/*.fasta'):
    ko = (l.split('/')[-3].split('_')[0])
    
    if  l.endswith('_recover_kmers.fasta'):
       fasta_recover = SeqIO.index(l, format="fasta")
       ko2probes_reciprocal[ko]['recover'] = str(len(fasta_recover) )

    elif not l.endswith('_recover_kmers.fasta'):
        fasta_original = SeqIO.index(l, format="fasta")
        ko2probes_reciprocal[ko]['original'] = str(len(fasta_original))

out_reciprocal = open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/result_insilico_test/reciprocal_probes_len.tsv', 'w')
out_reciprocal.write('\t'.join(['#ko','len_original', 'len_recover'+'\n']))
for ko, info in ko2probes_reciprocal.items():
    out_reciprocal.write('\t'.join([ko, info['original'], info['recover']+'\n']))
out_reciprocal.close()



