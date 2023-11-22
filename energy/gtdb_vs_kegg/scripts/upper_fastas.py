from Bio import SeqIO


fout = open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_expanded_upper/test_K00223.fna', 'w')
with open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_expanded/expanded_K02203.fna' ) as fin:
    for record in SeqIO.parse(fin, format="fasta"):
        fout.write('>'+record.id+'\n'+str(record.seq).upper()+'\n')
fout.close()
