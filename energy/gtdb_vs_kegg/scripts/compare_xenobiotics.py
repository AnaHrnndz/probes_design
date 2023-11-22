from collections import defaultdict


'''
Load xenobiotic results
'''

ko2gtdb_v1 = defaultdict(set)
with open('/home/plaza/projects/biorare/results/gtdb_vs_ko/qcov_08/ko2gtdb_seqs_expand.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        for s in info[2].split(','):
            if '.fna_' in s:
                s_new = s.replace('.fna_','.faa_')
                ko2gtdb_v1[info[0]].add(s_new)

#print(ko2gtdb_v1)

ko2gtdb_v2 = defaultdict(set)
with open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/ko2gtdb.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        if info[0] in ko2gtdb_v1.keys():
            ko2gtdb_v2[info[0]] = set(info[2].split(','))

fout = open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/compare_xenob_commons.tsv', 'w')
fout2 = open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/compare_xenob_diff.tsv', 'w')
for ko, seqs in ko2gtdb_v1.items():
    seqs_v2 = ko2gtdb_v2[ko]
    common = seqs.intersection(seqs_v2)
    pv1 = str(len(common) / len(seqs))
    pv2 = str(len(common) / len(seqs_v2))
    fout.write(ko+'\t'+str(len(common))+'\t'+pv1+'\t'+pv2+'\t'+str(len(seqs))+'\t'+str(len(seqs_v2))+'\n')

    dif = seqs.difference(seqs_v2)
    pdif = len(dif) / len(seqs)
    fout2.write(ko+'\t'+str(len(seqs))+'\t'+str(len(dif))+'\t'+str(pdif)+'\n')
fout.close()
