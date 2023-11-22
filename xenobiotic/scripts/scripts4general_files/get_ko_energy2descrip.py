#!/usr/bin/env python
# A.H.P 2023
# Biorare

import json
from collections import defaultdict

"""
    Get energy ko to description json file
"""

ko2path_desc = json.load(open('/home/plaza/projects/biorare/results/ko2pathways_descriptions.json'))

xenob_ko2path_desc = defaultdict(dict)
for ko, pathways in ko2path_desc.items():
    for p, descriptions in pathways.items():
        descriptions_info = descriptions.split('|')
        if descriptions_info[1] == 'Energy_metabolism':
            if ko.startswith('K'):
                xenob_ko2path_desc[ko] = pathways


for k, val in xenob_ko2path_desc.items():
    print(k, val)


with open('/home/plaza/projects/biorare/results/energy_ko2path_descp.json', 'w') as f:
    json.dump(xenob_ko2path_desc, f)
