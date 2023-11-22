from collections import defaultdict

ko2gtdb = defaultdict(list)
with open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/gtdb_vs_kegg.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        ko = info[1].split('@')[0]
        if float(info[12]) >= 80.0:
            ko2gtdb[ko].append(info[0])

print(len(ko2gtdb))


fout = open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/ko2gtdb.tsv', 'w')
for ko, gtdb in ko2gtdb.items():
    fout.write(ko+'\t'+str(len(gtdb))+'\t'+','.join(gtdb)+'\n')
fout.close()