#!/usr/bin/env python
# A.H.P 2023
# Biorare

import json
from collections import defaultdict
from Bio import SeqIO

"""
    Check blast result probes to ko seqs
"""

gene2ko = json.load(open('/home/plaza/projects/biorare/results/genes2ko.json'))

#Load result from blast probes vs ko
ko2match_mismatch_hits = defaultdict(dict)
ko2match_mismatch_query = defaultdict(dict)
miss_genes = set()
total_probes = set()
probes2ko = defaultdict(set)
#with open('/home/plaza/projects/biorare/results/insilico_xenob/diamond/probes_reciprocal_qcov08_vs_ko_original.tsv') as fin:
with open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/results_blast/probes_vs_total_ko.tsv') as fin:
    for line in fin:
        info = line.split('\t')
        query = info[0]
        ko_query = query.split('@')[0]
        orihit = info[2]
        
        if orihit.startswith('Aci'):
            hit = 'tsa:'+orihit
        elif orihit.startswith('TP'):
            hit = 'tpa:'+orihit
        else:
            hit = orihit
            
        ko_hit = gene2ko[hit]
        probes2ko[query].update(set(ko_hit))
        total_probes.add(query)

        #init dict keys
        if ko_query not in ko2match_mismatch_hits.keys():
            ko2match_mismatch_hits[ko_query]['mismatch_hit'] = set()
            ko2match_mismatch_hits[ko_query]['match_hit'] = set()
            ko2match_mismatch_hits[ko_query]['bad_match_hit'] = set()

        if ko_query not in ko2match_mismatch_query.keys():
            ko2match_mismatch_query[ko_query]['mismatch_query'] = set()
            ko2match_mismatch_query[ko_query]['match_query'] = set()
            ko2match_mismatch_query[ko_query]['bad_match_query'] = set()
            
       
        #Save mismatch
        if ko_query not in ko_hit:
            ko2match_mismatch_hits[ko_query]['mismatch_hit'].add(hit)
            ko2match_mismatch_query[ko_query]['mismatch_query'].add(query)
        

        #Save matchs
        #if piden < 0.7 -> bad_match
        #if piden >0.7 -> match
        elif ko_query in ko_hit:
            if float(info[9]) >= 0.7 and int(info[12]) >=80:
                ko2match_mismatch_hits[ko_query]['match_hit'].add(hit)
                ko2match_mismatch_query[ko_query]['match_query'].add(query)
            elif float(info[9]) < 0.7 or int(info[12]) <80:
                ko2match_mismatch_hits[ko_query]['bad_match_hit'].add(hit)
                ko2match_mismatch_query[ko_query]['bad_match_query'].add(query)
            
            
            




probes2match_mismatch = defaultdict(dict)
ko2mistmatch_ko = defaultdict(set)
ko2other_matchs = defaultdict(set)
ko2bad_match = defaultdict(set)
for query, ko_hits in probes2ko.items():
    ko_query = query.split('@')[0]
    
    if ko_query not in probes2match_mismatch.keys():
        probes2match_mismatch[ko_query]['mismatch'] = set()
        probes2match_mismatch[ko_query]['match'] = set()
        probes2match_mismatch[ko_query]['bad_match'] = set()
        probes2match_mismatch[ko_query]['hq_match'] = set()

    if ko_query not in ko_hits:
        probes2match_mismatch[ko_query]['mismatch'].add(query)
        ko2mistmatch_ko[ko_query].update(ko_hits)

    elif ko_query  in ko_hits:
        if query in ko2match_mismatch_query[ko_query]['bad_match_query']:
            probes2match_mismatch[ko_query]['bad_match'].add(query)
            ko2bad_match[ko_query].update(ko_hits)
            

        elif query in ko2match_mismatch_query[ko_query]['match_query']:
            #if probes only have matches in the query_KO -> hq_match 
            #if probes have more than 1 match -> match
            if len(ko_hits) >1:
                probes2match_mismatch[ko_query]['match'].add(query)
                
                ko2other_matchs[ko_query].update(ko_hits)

            if len(ko_hits) ==1:
                probes2match_mismatch[ko_query]['hq_match'].add(query)
                
    
        
            




# fout_1 = open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/results_blast/reciprocal_probes_match_mismatch_5.tsv', 'w')
# fout_1.write('\t'.join(['#ko', 'match_hit', 'bad_match_hit', 'mismatch_hit', 'hq_match_probes', 'match_probes','bad_probes','mismatch_probes'+'\n']))

# for ko, info in ko2match_mismatch_hits.items():
    # fout_1.write('\t'.join([ko, str(len(info['match_hit'])), str(len(info['bad_match_hit'])), str(len(info['mismatch_hit'])), 
    # str(len(probes2match_mismatch[ko]['hq_match'])), str(len(probes2match_mismatch[ko]['match'])), str(len(probes2match_mismatch[ko]['bad_match'])), 
    # str(len(probes2match_mismatch[ko]['mismatch']))+'\n' ]))
# fout_1.close()


# list_ko2match_mismatch = defaultdict(dict)
# for ko_query, info in ko2match_mismatch_query.items():
    # list_ko2match_mismatch[ko_query]['mismatch_query'] = list(ko2match_mismatch_query[ko_query]['mismatch_query'])
    # list_ko2match_mismatch[ko_query]['match_query'] = list(ko2match_mismatch_query[ko_query]['bad_match_query'])
    # list_ko2match_mismatch[ko_query]['hq_match_query'] = list(ko2match_mismatch_query[ko_query]['match_query'])


# with open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/results_blast/ko2probes_4.json', 'w' ) as out:
    # json.dump(list_ko2match_mismatch, out)


# lost_probes = set()
# total_probes_fasta = '/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/total_probes_reciprocal_qcov08_v2.fasta'
# for record in SeqIO.parse(total_probes_fasta, format="fasta"):
    # if record.id not in total_probes:
        # lost_probes.add(record.id)

# with open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/results_blast/lost_probes_4.tsv', 'w') as out:
    # out.write('\n'.join(list(lost_probes)))

fout2 = open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/results_blast/ko_probes2otherko.tsv', 'w')
fout2.write('\t'.join(['#ko', 'other_match', 'bad_match', 'mismatch'+'\n']))
for ko, info in ko2match_mismatch_hits.items():
    
    fout2.write('\t'.join([ko,'|'.join(list(ko2other_matchs[ko])), '|'.join(list(ko2bad_match[ko])), '|'.join(list(ko2mistmatch_ko[ko]))+'\n']))

fout2.close()



