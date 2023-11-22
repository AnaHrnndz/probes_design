#!/usr/bin/env python
# A.H.P 2023
# Biorare

from collections import defaultdict
import statistics
import json
import numpy
from ete4 import NCBITaxa, GTDBTaxa

'''
    Scrip to parse mmseqs result table and get a summary table with stats, ko symbol, etc
'''

ncbi = NCBITaxa()
gtdb = GTDBTaxa()



def get_stats(info, prop):

    #Func to get some basic stats (mean, std, min and max)

    if len(info[prop]) == 0:
        mean_ = None
        std_desv = None
        min_ = None
        max_ = None 
    else:
    
        mean_ = numpy.mean(info[prop])
        std_desv = numpy.std(info[prop])
        min_ = min(info[prop])
        max_ = max(info[prop])

    return [mean_, std_desv, min_, max_]

#Global path are remove from results
global_kpath = ['01100', '01110', '01120', '01200', '01210', '01212', '01230', '01232', '01250', '01240', '01220']

#Load KO descriptions
ko2desc = json.load(open('/home/plaza/projects/biorare/results/ko2pathways_descriptions.json'))

#Load KO symbols
ko2symbol = defaultdict()
with open('/home/plaza/databases/kegg/tight_ko.list') as f:
    for line in f:
        ko, symbol = line.strip().split('\t')
        ko2symbol[ko] = symbol


#Load KO species code to ncbi taxid
code2taxid = defaultdict()
with open('/home/plaza/databases/kegg/taxonomic_rank') as fin:
    for line in fin:
        if not line.startswith('#'):
            info = line.strip().split('\t')
            code = info[0].strip()
            taxid = int(info[1].strip())
            code2taxid[code] = taxid
            # if bool(ncbi.get_taxid_translator([taxid])) == False:
                # tax_ = ncbi.get_name_translator([info[6]])
                # print(taxid, info[6], tax_)


ko2info = defaultdict(dict)
ko2total_query_genomes = defaultdict(set)
ko2total_hit_genome = defaultdict(set)
#Load mmseqs result table
with open('/home/plaza/projects/biorare/results/ko_mmseqs/xenob_total.result_mmseqs.tsv') as tin:
    for num, (line) in enumerate(tin):
     
        if not line.startswith('query'):
            info = line.strip().split('\t')
            query_ko_name = info[0].split('_',1)[0]
            query_seq_name = info[0].split('_',1)[1]
            query_genome_code = info[0].split('_',1)[1].split(':')[0]
            target_name = info[1]
            target_genome = info[1].split('_protein')[0]
            piden = float(info[2])
            alnlen = int(info[3])
            qlen = int(info[6])
            tlen = int(info[9])
            mismatch = int(info[10])
            qcov = float(info[12])
            tcov = float(info[13])
            evalue = float(info[14])
            bits = int(info[15])


            taxid = code2taxid[query_genome_code]

            ko2total_query_genomes[query_ko_name].add(taxid)
            ko2total_hit_genome[query_ko_name].add(target_genome)
           
            if float(qcov) >= 0.8:
                if not query_ko_name in ko2info.keys():
                    ko2info[query_ko_name]['original_query_seqs']  = list()
                    ko2info[query_ko_name]['query_genomes'] = list()
                    ko2info[query_ko_name]['sequence_targets'] = list()
                    ko2info[query_ko_name]['genome_targets'] = list()
                    ko2info[query_ko_name]['piden'] = list()
                    ko2info[query_ko_name]['alnlen'] = list()
                    ko2info[query_ko_name]['qlen'] = list()
                    ko2info[query_ko_name]['tlen'] = list()
                    ko2info[query_ko_name]['mismatch'] = list()
                    ko2info[query_ko_name]['qcov'] = list()
                    ko2info[query_ko_name]['tcov'] = list()
                    ko2info[query_ko_name]['evalue'] = list()
                    ko2info[query_ko_name]['bit'] = list()
                    
                    
                
                
                ko2info[query_ko_name]['original_query_seqs'].append(query_seq_name) 
                ko2info[query_ko_name]['query_genomes'].append(taxid)
                ko2info[query_ko_name]['sequence_targets'].append(target_name)
                ko2info[query_ko_name]['genome_targets'].append(target_genome)
                ko2info[query_ko_name]['piden'].append(piden)
                ko2info[query_ko_name]['alnlen'].append(alnlen)
                ko2info[query_ko_name]['qlen'].append(qlen)
                ko2info[query_ko_name]['tlen'].append(tlen)
                ko2info[query_ko_name]['mismatch'].append(mismatch)
                ko2info[query_ko_name]['qcov'].append(qcov)
                ko2info[query_ko_name]['tcov'].append(tcov)
                ko2info[query_ko_name]['evalue'].append(evalue)
                ko2info[query_ko_name]['bit'].append(bits)
                

        


#Write summary table 
tabout = open('/home/plaza/projects/biorare/results/ko_mmseqs/qcov_08_mmseqs_2.tsv', 'w') 

ko2expandseqs = open('/home/plaza/projects/biorare/results/ko_mmseqs/ko2expand_seqs_qcov_08_2.tsv', 'w') 

head = ['#KO', 'Num_query_seqs', 'Num_query_genomes','Total_genomes_KO','LCA_query_ncbi', 'LCA_KO', 'Num_hit_seqs', 'Num_hit_genomes','LCA_hit_gtdb',
        'Symbol', 'Kegg_pathways', 'Kegg_descriptions','mean_piden', 'std_piden', 'min_piden', 'max_piden', 'mean_alnlen', 'std_alnlen', 'min_alnlen', 'max_alnlen',
        'mean_qlen', 'std_qlen', 'min_qlen', 'max_qlen', 'mean_tlen', 'std_tlen', 'min_tlen', 'max_tlen',  'mean_mismatch', 'std_mismatch', 'min_mismatch', 'max_mismatch',
        'mean_qcov', 'std_qcov', 'min_qcov', 'max_qcov', 'mean_tcov', 'std_tcov', 'min_tcov', 'max_tcov',  'mean_evalue', 'std_evalue', 'min_evalue', 'max_evalue',
        'mean_bit', 'std_bit', 'min_bit', 'max_bit' 
        ]   

tabout.write('\t'.join(head)+'\n')
for ko, info in ko2info.items():
    print(ko)

    total_seqs = set()
    total_seqs.update(set(info['original_query_seqs']))
    total_seqs.update(set(info['sequence_targets']))


    ko2expandseqs.write(ko+'\t'+str(len(total_seqs))+'\t'+','.join(list(total_seqs))+'\n')

    pathways_list = list() 
    descriptions = list()

    props = ['piden', 'alnlen', 'qlen', 'tlen', 'mismatch', 'qcov', 'tcov', 'evalue', 'bit']

    out_results = list()

    #Number of original querys, number of sequence hits and number of genome hits, and taxonomical info
    out_results.append(str(len(set(info['original_query_seqs']))))
    
    query_genomes_list = list(set(info['query_genomes']))
    out_results.append(str(len(query_genomes_list)))
    
    species = list(ko2total_query_genomes[ko])
    out_results.append(str(len(set(species))))


    if len(query_genomes_list) == 1:
        lca_query_taxid = query_genomes_list[0]
    else:
        lca_query_taxid = ncbi.get_topology(query_genomes_list).taxid
    
    lca_query_name = ncbi.get_taxid_translator([lca_query_taxid])[lca_query_taxid]
    out_results.append(lca_query_name)

    
    if len(species) == 1:
        lca_taxid = species[0]
    else:
        lca_taxid = ncbi.get_topology(species).taxid
    lca_name = ncbi.get_taxid_translator([lca_taxid])[lca_taxid]
   
    out_results.append(lca_name)
    




    out_results.append(str(len(set(info['sequence_targets']))))
    out_results.append(str(len(set(info['genome_targets']))))
    

    gtdb_species = list(info['genome_targets'])
    if len(gtdb_species) == 1:
        gtdb_lca = str(gtdb_species[0])
    else:
        gtdb_topology = gtdb.get_topology(gtdb_species)
        if 'taxid' in gtdb_topology.props.keys():
            gtdb_lca = gtdb_topology.props.get('taxid')
        else:
            gtdb_lca = '@'.join(gtdb_species)

   
    out_results.append(str(gtdb_lca))




    #KO symbol
    if ko in ko2symbol.keys():
        out_results.append(ko2symbol[ko])
    else:
        out_results.append('None')

    #KO pathways info
    for pathways, descrp in ko2desc[ko].items():
        if pathways not in global_kpath:
            pathways_list.append(pathways)
            str_descp = pathways+'@'+descrp
            descriptions.append(str_descp)


    plist = ','.join(pathways_list)
    dlist = ','.join(descriptions)

    out_results.append(plist)
    out_results.append(dlist)

    # print(info['original_query_seqs'])
    # print(info['sequence_targets'])
    # print(info['genome_targets'])


    #Get stats 
    for p in props:
        results_stats = get_stats(info, p)
        for stat in results_stats:
            out_results.append(str(stat))


                    
    print(ko+'\t'+'\t'.join(out_results))
    tabout.write(ko+'\t'+'\t'.join(out_results)+'\n')

tabout.close()
           
ko2expandseqs.close()