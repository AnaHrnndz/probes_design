#!/usr/bin/env python
# A.H.P 2023
# Biorare

import json
from collections import defaultdict

"""
    Create KO to pathway description json file
"""

path2desc = json.load(open('/home/plaza/projects/biorare/results/path2descp.json'))

ko2path = defaultdict(set)

with open('/home/plaza/databases/kegg/ko/ko.list') as fin:
    for line in fin:
        path, ko = line.strip().split('\t')
        clean_path = path.split(':')[1].replace('ko', '')
        clean_ko = ko.split(':')[1]
        ko2path[clean_ko].add(clean_path)


ko2path_desc = defaultdict(dict)
xenob_ko2path_desc = defaultdict(dict)

for ko, paths in ko2path.items():
    total_desc = list()
    for p in paths:
        descriptions = path2desc[p]
        #str_descp = '|'.join(descriptions).replace('#', '')
        total_desc.append(descriptions)

        ko2path_desc[ko][p] = descriptions





with open('/home/plaza/projects/biorare/results/ko2pathways_descriptions.json', 'w') as fout:
    json.dump(ko2path_desc, fout)

