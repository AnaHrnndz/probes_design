#!/usr/bin/env python
# A.H.P 2023
# Biorare

import glob

'''
    Get path to xenobiotic ko fastas
'''


ko_list = list()
with open('/home/plaza/projects/biorare/raw/Marker_functional_genes__xenobiotics_specific.tsv') as fin:
    for line in fin:
        if not line.startswith('#'):
            info = line.strip().split('\t')
            ko = info[2]
            ko_list.append(ko)


path2xeno_ko = open('/home/plaza/projects/biorare/results/path2xeno_ko.txt', 'w')
for ko in ko_list:
    if glob.glob('/home/plaza/projects/biorare/results/ko_nucleotides/'+ko+'.fn'):
        path = glob.glob('/home/plaza/projects/biorare/results/ko_nucleotides/'+ko+'.fn')[0]
        path2xeno_ko.write(path+'\n')
