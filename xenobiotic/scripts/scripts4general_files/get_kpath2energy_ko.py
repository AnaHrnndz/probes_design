import json

eko = json.load(open('/home/plaza/projects/biorare/results/energy_ko2path_descp.json'))
fout = open('/home/plaza/projects/biorare/results/eko2path.tsv', 'w')
for ko, kpath in eko.items():

    for path, desc in kpath.items():
        fout.write(ko+'\t'+path+'\t'+desc+'\n')

fout.close()