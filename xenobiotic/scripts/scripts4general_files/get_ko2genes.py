#!/usr/bin/env python
# A.H.P 2023
# Biorare


import json
from collections import defaultdict

"""
    Get KO to genes json file
"""

ko2genes = defaultdict(list)
ko2species = defaultdict(set)
with open('/home/plaza/databases/kegg/genes_ko.list') as f:
    for line in f:
        if not line.startswith('#'):
            info = line.strip().split('\t')
            ko = info[1].split(':')[1]
            gene = info[0]
            sp = info[0].split(':')[0]

            ko2genes[ko].append(gene)
            ko2species[ko].add(sp)

with open('/home/plaza/projects/biorare/results/ko2genes.json', 'w') as fout:
    json.dump(ko2genes, fout)