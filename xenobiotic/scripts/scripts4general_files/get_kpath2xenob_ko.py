import json
from collections import defaultdict

xeKO2kpath = json.load(open('/home/plaza/projects/biorare/results/xenob_ko2path_descp.json'))

path2ko = defaultdict(dict)
ko2path = open('/home/plaza/projects/biorare/results/xKO2path.tsv', 'w')

for ko, kpath in xeKO2kpath.items():

    for path, descr in kpath.items():
        
        ko2path.write(ko+'\t'+path+'\t'+descr+'\n')
        
        if path not in path2ko.keys():
            path2ko[path] = defaultdict(list)
            path2ko[path]['KO'] = list()

        path2ko[path]['description'] = descr
        path2ko[path]['KO'].append(ko)

with open('/home/plaza/projects/biorare/results/xenob_path2ko.json', 'w') as fout:
    json.dump(path2ko, fout)

ko2path.close()