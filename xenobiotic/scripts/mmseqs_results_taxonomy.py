#!/usr/bin/env python
# A.H.P 2023
# Biorare

from collections import defaultdict
import json
from ete4 import NCBITaxa, GTDBTaxa

'''
    Get info about taxonomy for target species and hit species
'''

def get_taxonomy_counter(species_list):
    taxo_counter = defaultdict(list)
    for sp in species_list:
        lin = ncbi.get_lineage(sp)
        for l in lin:
            taxo_counter[l].append(sp)

    taxo_counter_num = defaultdict()
    for taxid, sp_list in taxo_counter.items():
        taxo_counter_num[taxid] = len(set(sp_list))

    return taxo_counter_num


ncbi = NCBITaxa()
gtdb = GTDBTaxa()

#print(ncbi.get_name_translator(['Lysobacter arenosi']))

code2taxid = defaultdict()
with open('/home/plaza/databases/kegg/taxonomic_rank') as fin:
    for line in fin:
        if not line.startswith('#'):
            info = line.strip().split('\t')
            code = info[0].strip()
            taxid = int(info[1].strip())
            code2taxid[code] = taxid
            # if bool(ncbi.get_taxid_translator([taxid])) == False:
                # tax_ = ncbi.get_name_translator([info[6]])
                # print(taxid, info[6], tax_)
           
#print(code2taxid)


ko2target_genome = defaultdict(list)
ko2hit_genome = defaultdict(list)

with open('/home/plaza/projects/biorare/results/ko_mmseqs/xenob_total.result_mmseqs.tsv') as tin:
    for num, (line) in enumerate(tin):
        if num < 1000:
     
            if not line.startswith('query'):
                info = line.strip().split('\t')
                query_ko_name = info[0].split('_',1)[0]
                query_genome_code = info[0].split('_',1)[1].split(':')[0]
                target_genome = info[1].split('_protein')[0]

                taxid = code2taxid[query_genome_code]

                ko2target_genome[query_ko_name].append(taxid)
                ko2hit_genome[query_ko_name].append(target_genome)

            

print(len(ko2target_genome))
print(len(ko2hit_genome))


for ko, species in ko2target_genome.items():
    
    lca_taxid = ncbi.get_topology(species).taxid
    lca_name = ncbi.get_taxid_translator([lca_taxid])[lca_taxid]

    gtdb_species = ko2hit_genome[ko]
    gtdb_lca = gtdb.get_topology(gtdb_species).taxid

        


    print(ko, lca_taxid, lca_name, gtdb_lca)

