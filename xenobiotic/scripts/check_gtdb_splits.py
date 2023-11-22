#!/usr/bin/env python
# A.H.P 2023
# Biorare


from collections import defaultdict
import json

"""
    Check reciprocal mapping from gtdb hit seqs to ko seqs
"""


with open('/home/plaza/projects/biorare/results/genes2ko.json') as f:
    genes2ko = json.load(f)

with open('/home/plaza/projects/biorare/results/ko2genes.json') as f:
    ko2genes = json.load(f)


#Load mmseqs results filtered by qcov>=0.8

mmseqs_filt_ko2allseqs = defaultdict(set)
mmseqs_filt_allseqs2ko= defaultdict(set)
with open('/home/plaza/projects/biorare/results/ko_mmseqs/ko2expand_seqs_qcov_08_v1.tsv') as fin:
    for line in fin:
        if not line.startswith('#'):
            info = line.strip().split('\t')
            mmseqs_filt_ko2allseqs[info[0]] = set(info[2].split(','))
            for s in set(info[2].split(',')):
                mmseqs_filt_allseqs2ko[s].add(info[0])


#Load mmseqs results no-filtered

mmseqs_total_ko2seqs_gtdb = defaultdict(set)
mmseqs_total_seqs_gtdb2ko = defaultdict(set)
with open('/home/plaza/projects/biorare/results/ko_mmseqs/xenob_total_v1.result_mmseqs.tsv') as fin:
    for line in fin:
        if not line.startswith('#'):
            info = line.strip().split('\t')
            ko_name = info[0].split('_')[0]
            gtdb_seq = info[1]
            mmseqs_total_ko2seqs_gtdb[ko_name].add(gtdb_seq)
            mmseqs_total_seqs_gtdb2ko[gtdb_seq].add(ko_name)


#Load diamond results

diamond_gtdbseqs2ko_seqs = defaultdict(set)
diamond_gtdbseqs2ko_name = defaultdict(set)
with open('/home/plaza/projects/biorare/results/gtdb_vs_ko/gtdb_vs_ko') as fin:
    for line in fin:
        if not line.startswith('#'):
            info = line.strip().split('\t')
            gtdb_seq = info[0]
            ko_seq_name = info[1]
            ko_name = genes2ko[ko_seq_name]
            diamond_gtdbseqs2ko_seqs[gtdb_seq].add(ko_seq_name)
            diamond_gtdbseqs2ko_name[gtdb_seq].update(set(ko_name))


  
misleading_seqs = defaultdict(set)
multiKO_seqs = defaultdict(set)
ko2gtdbseqs_expand = defaultdict(set)
general_table = open('/home/plaza/projects/biorare/results/gtdb_vs_ko/gtdb_hit_splits.tsv', 'w')

#For each KO_name in mmseqs filtered
    #Get only gtdb seqs (allseqs contain also kegg seqs)
    #For each gtdb seq, get the KO_its from diamond mapping
        #If  KO_name not in KO_hits from diamond -> gtdb seq add to misleading_seqs[ko_name]
        #If KO_hits >1 -> gtdb_seq add to multiKO_seqs[ko_name]
        #Else -> gtdb seq add to ko2gtdbseqs_expand[ko_name]

for ko_name, allseqs in mmseqs_filt_ko2allseqs.items():

    if ko_name in ko2genes.keys():
        original_len_ko = len(ko2genes[ko_name])
    else:
        original_len_ko = 0

    
    gtdb_seqs_total = mmseqs_total_ko2seqs_gtdb[ko_name]
    gtdb_seqs_filt = allseqs.intersection(gtdb_seqs_total)

    original_multihit = set()
    diamond_hit_seqs = set()
    diamond_hit_ko_set = set()
    diamond_hit_ko_dict = defaultdict(set)
    
    
    for s in gtdb_seqs_filt:

        original_multihit.update(mmseqs_filt_allseqs2ko[s])
        diamond_hit_seqs.update(diamond_gtdbseqs2ko_seqs[s])
        diamond_hit_ko_set.update(diamond_gtdbseqs2ko_name[s])
        
        kos = diamond_gtdbseqs2ko_name[s]
        
        
        for ko in kos:
            diamond_hit_ko_dict[ko].add(s)

        
        if ko_name not in diamond_gtdbseqs2ko_name[s]:
            misleading_seqs[ko_name].add(s)
           
        elif len(diamond_gtdbseqs2ko_name[s]) >1:
            multiKO_seqs[ko_name].add(s)

        else:
            ko2gtdbseqs_expand[ko_name].add(s)


   
    diamond_hit_ko_dict_list = list()
    for ko, seqs in diamond_hit_ko_dict.items():
        diamond_hit_ko_dict_list.append(ko+'_'+str(len(seqs)))

    diamond_hit_ko_str = '@'.join(diamond_hit_ko_dict_list)
    
    general_table.write('\t'.join([ko_name, str(original_len_ko), str(len(gtdb_seqs_total)), str(len(gtdb_seqs_filt)), str(len(original_multihit)), 
                                    str(len(diamond_hit_seqs)), str(len(misleading_seqs)), str(len(multiKO_seqs)), str(len(diamond_hit_ko_set)), diamond_hit_ko_str+'\n']))


ko2misleading_seqs = open('/home/plaza/projects/biorare/results/gtdb_vs_ko/ko2misleading_seqs.tsv', 'w')
for ko, seqs in misleading_seqs.items():
    ko2misleading_seqs.write('\t'.join([ko, str(len(seqs)),','.join(list(seqs))+'\n']))

ko2multiko_seqs = open('/home/plaza/projects/biorare/results/gtdb_vs_ko/ko2multiko_seqs.tsv', 'w')
for ko, seqs in multiKO_seqs.items():
    ko2multiko_seqs.write('\t'.join([ko, str(len(seqs)),','.join(list(seqs))+'\n']))


ko2seqs_expand = open('/home/plaza/projects/biorare/results/gtdb_vs_ko/ko2gtdb_seqs_expand.tsv', 'w')
for ko, seqs in ko2gtdbseqs_expand.items():
    ko2seqs_expand.write('\t'.join([ko, str(len(seqs)),','.join(list(seqs))+'\n']))


ko2misleading_seqs.close()
ko2multiko_seqs.close()
ko2seqs_expand.close()
general_table.close()



    
    