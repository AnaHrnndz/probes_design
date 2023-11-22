#!/usr/bin/env python
# A.H.P 2023
# Biorare

import json
from collections import defaultdict

"""
    Get kegg pathways to ko json file
"""


kpath2kko = defaultdict(list)
with open('/home/plaza/databases/kegg/ko/ko.list') as fin:
    for line in fin:
        info = line.strip().split()
        kpath = info[0].split(':')[1].replace('ko','')
        kko = info[1].split(':')[1]
        kpath2kko[kpath].append(kko)

print(len(kpath2kko))

with open('/home/plaza/projects/biorare/results/kpath2kko.json', 'w') as fout:
    json.dump(kpath2kko, fout)