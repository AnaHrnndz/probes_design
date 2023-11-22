#!/usr/bin/env python
# A.H.P 2023
# Biorare

import json
from collections import defaultdict

"""
    Create genes to ko json file
"""

ko2genes = json.load(open('/home/plaza/projects/biorare/results/ko2genes.json'))
print(len(ko2genes))
genes2ko = defaultdict(list)

for ko, genes in ko2genes.items():
    for g in genes:
        genes2ko[g].append(ko)

print(len(genes2ko))
with open('/home/plaza/projects/biorare/results/genes2ko.json', 'w') as fout:
    json.dump(genes2ko, fout)