#!/usr/bin/env python
# A.H.P 2023
# Biorare


from collections import defaultdict
import json

'''
    Get descriptions to pathways json file
'''

group1 = None
group2 = None


desc2path = defaultdict(dict)
pathw2desc = defaultdict()
xenobiotic_pathways = set()
for line in open('/home/plaza/databases/kegg/pathway.list'):
    if line.startswith('##'):
        group2 = line[2:].strip().replace(' ', '_')
    elif line.startswith('#'):
        group1 = line[1:].strip().replace(' ', '_')
    else:
        pathw = line.split('\t')[0]
        descp = line.split('\t')[1].replace(' ', '_').replace('-', '_')
        
        pathw2desc[pathw] = descp.strip()+'|'+group2.strip()+'|'+group1.strip()
        
        if group1 in desc2path.keys():
            if group2 in desc2path[group1].keys():
                desc2path[group1][group2].append(pathw)
            else:
                desc2path[group1][group2] = list()
                desc2path[group1][group2].append(pathw)
        else:
            desc2path[group1] = dict()

        if group2 == 'Xenobiotics_biodegradation_and_metabolism':

            xenobiotic_pathways.add(pathw)

        
    
fout1 = open('/home/plaza/projects/biorare/results/desc2path.json', 'w')
json.dump(desc2path, fout1)
fout1.close()


fout2 = open('/home/plaza/projects/biorare/results/path2descp.json', 'w')
json.dump(pathw2desc, fout2)
fout2.close()

with open('/home/plaza/projects/biorare/results/xenobiotic_pathways.tsv', 'w') as f:
    f.write('\n'.join(list(xenobiotic_pathways)))
