import os
import sys
from collections import defaultdict
from Bio import SeqIO

import glob

global_kpath = ['01100', '01110', '01120', '01200', '01210', '01212', '01230', '01232', '01250', '01240', '01220']


eko2paths=defaultdict(dict)
with open('/home/plaza/projects/biorare/results/eko2path.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        if info[1] not in global_kpath:
            eko2paths[info[0]][info[1]] = info[2]
print('eko paths load')

eko2gtdb_results = defaultdict(dict)
with open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/ko2gtdb.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        if info[0] in eko2paths.keys():
            eko2gtdb_results[info[0]]['num_gtdb_seqs'] = info[1]
            eko2gtdb_results[info[0]]['gtdb_mems'] = info[2].split(',')
print('gtdb vs kegg load')

eko2original_num_seqs = defaultdict()
for eko, paths in eko2paths.items():
    init_fasta = '/home/plaza/projects/biorare/results/ko_nucleotides/'+eko+'.fn'
    record_list = list(SeqIO.parse(init_fasta, "fasta"))
    eko2original_num_seqs[eko] = len(record_list)
print('original fasta load')


eko2medium_length = defaultdict()
for path_fasta in glob.glob('/home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_expanded/expanded_*.fna'):
    eko_name = path_fasta.split('/')[-1].split('_')[-1].split('.')[0]
    record_dict = SeqIO.to_dict(SeqIO.parse(path_fasta, "fasta"))
    length = list()
    for name,seq in record_dict.items():
        length.append(len(seq))
    eko2medium_length[eko_name] = str((round(sum(length)/len(record_dict), 3)))
print('expanded fastas load')

eko2num_probes = defaultdict(dict)
for path in glob.glob('/home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_probes/expanded_*/v1/*.fasta'):
    eko_name = path.split('/')[8].split('_')[-1]
    name_fasta = (path.split('/')[-1])
    if name_fasta == 'expanded_'+eko_name+'_kmers.fasta':
        record_list = list(SeqIO.parse(path, "fasta"))
        eko2num_probes[eko_name]['ori_probes'] = len(record_list)
    else:
        record_list = list(SeqIO.parse(path, "fasta"))
        eko2num_probes[eko_name]['resc_probes'] = len(record_list)
print('probes info load')

probes2match= defaultdict(dict)
probes2mismatch = defaultdict(set)
with open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_probes/diamond_eko_probes_vs_kegg.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        ko_query = info[0].split('@')[0]
        ko_hit = info[1].split('@')[0]

        if ko_query != ko_hit:
            probes2mismatch[ko_query].add(info[0])

        elif ko_query == ko_hit:
            if ko_query not in probes2match.keys():
                probes2match[ko_query]['hq_match_probes'] = set()
                probes2match[ko_query]['match_probes'] = set()

            if ko_query == ko_hit:
                if float(info[11]) >= 80.0:
                    probes2match[ko_query]['hq_match_probes'].add(info[0])
                else:
                    probes2match[ko_query]['match_probes'].add(info[0])

print('insilico results load')


final_probes = defaultdict(dict)
for ko, mismatch_probes in probes2mismatch.items():

    hq_probes = probes2match[ko]['hq_match_probes']
    good_probes = probes2match[ko]['match_probes']

    if ko not in final_probes.keys():
        final_probes[ko]['hq_probes'] = set()
        final_probes[ko]['good_probes'] = set()
        final_probes[ko]['hq_and_good_probes'] = set()

    for probes in hq_probes:
        if probes not in mismatch_probes:
            final_probes[ko]['hq_probes'].add(probes)
    for probes in good_probes:
        if probes not in mismatch_probes:
            final_probes[ko]['good_probes'].add(probes)

    hq_and_good = final_probes[ko]['hq_probes'].intersection(final_probes[ko]['good_probes'])
    final_probes[ko]['hq_and_good_probes'] = hq_and_good


fout = open('/home/plaza/projects/biorare/gtdb_vs_kegg/results/resumen_diamond_probes.tsv', 'w')
for eko, kpaths in eko2paths.items():


    eko_paths = list()
    for knum, kdesc in kpaths.items():
        eko_paths.append(knum+'@'+kdesc)
    epaths = '|'.join(eko_paths)

    if eko in eko2original_num_seqs.keys():
        nseqs = eko2original_num_seqs[eko]
    else:
        nseqs = '-'

    if eko in eko2gtdb_results.keys():
        gtdb_hits = (eko2gtdb_results[eko]['num_gtdb_seqs'])
    else:
        gtdb_hits = '-'

    if eko in eko2medium_length.keys():
        mlength = eko2medium_length[eko]
    else:
        mlength = '-'

    if eko in eko2num_probes.keys():
        if 'ori_probes' in eko2num_probes[eko]:
            nori_probes = eko2num_probes[eko]['ori_probes']
        else:
            nori_probes = '-'

        if 'resc_probes' in eko2num_probes[eko].keys():
            nrec_probes = eko2num_probes[eko]['resc_probes']
        else:
            nrec_probes = '-'
    else:
        nori_probes = '-'
        nrec_probes = '-'

    if eko in final_probes.keys():
        nhq_probes = len(final_probes[eko]['hq_probes'])
        ngood_probes = len(final_probes[eko]['good_probes'])
        hq_and_good = len(final_probes[eko]['hq_and_good_probes'])

    else:
        nhq_probes = '-'
        ngood_probes = '-'
        hq_and_good = '-'

    if eko in probes2mismatch.keys():
        nbad_probes = len(probes2mismatch[eko])
    else:
        nbad_probes = '-'


    fout.write('\t'.join([eko, str(nseqs), str(gtdb_hits), str(mlength), str(nori_probes), str(nrec_probes), str(nhq_probes), str(ngood_probes), str(hq_and_good), str(nbad_probes), str(epaths)+'\n' ]))


fout.close()


