import glob
import sys
import os
from Bio import SeqIO



fout = open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_probes/total_probes.fasta', 'w')
for path in glob.glob('/home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_probes/expanded_*/v1/*.fasta'):
    eko_name = path.split('/')[8].split('_')[1]
    print(eko_name)
    for record in SeqIO.parse(path, format="fasta"):
        name_seq = '>'+eko_name+'@'+record.id
        fout.write(name_seq+'\n'+str(record.seq).upper()+'\n')

fout.close()


