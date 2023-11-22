#!/usr/bin/env python
# A.H.P 2023
# Biorare

from collections import defaultdict

"""
    Resume all info from different tables in one
"""

ko2summary = defaultdict(dict)
with open('/home/plaza/projects/biorare/results/ko_mmseqs/qcov_08_mmseqs_v1.tsv') as fin:
    for line in fin:
        if line.startswith('#'):
            head = line.split('\t')
        if not line.startswith('#'):
            info = line.split('\t')
            ko2summary[info[0]]['Num_query_seqs'] = info[1]
            ko2summary[info[0]]['Num_query_genomes'] = info[2]
            ko2summary[info[0]]['Total_genomes_KO'] = info[3]
            ko2summary[info[0]]['LCA_query_ncbi'] = info[4]
            ko2summary[info[0]]['LCA_KO'] = info[5]
            ko2summary[info[0]]['Num_hit_seqs'] = info[6]
            ko2summary[info[0]]['Num_hit_genomes'] = info[7]
            ko2summary[info[0]]['LCA_hit_gtdb'] = info[8]
            ko2summary[info[0]]['Symbol'] = info[9]
            ko2summary[info[0]]['Kegg_pathways'] = info[10]
            ko2summary[info[0]]['Kegg_descriptions'] = info[11]
     
            ko2summary[info[0]]['mean_piden'] =    round(float(info[12]),3)
            ko2summary[info[0]]['std_piden']=      round(float(info[13]),3)
            ko2summary[info[0]]['min_piden'] =     round(float(info[14]),3)
            ko2summary[info[0]]['max_piden'] =     round(float(info[15]),3)

            ko2summary[info[0]]['mean_alnlen'] =   round(float(info[16]),3)
            ko2summary[info[0]]['std_alnlen'] =    round(float(info[17]),3)
            ko2summary[info[0]]['min_alnlen'] =    round(float(info[18]),3)
            ko2summary[info[0]]['max_alnlen'] =    round(float(info[19]),3)

            ko2summary[info[0]]['mean_qlen'] =     round(float(info[20]),3)
            ko2summary[info[0]]['std_qlen'] =      round(float(info[21]),3)
            ko2summary[info[0]]['min_qlen'] =      round(float(info[22]),3)
            ko2summary[info[0]]['max_qlen'] =      round(float(info[23]),3)

            ko2summary[info[0]]['mean_tlen'] =     round(float(info[24]),3)
            ko2summary[info[0]]['std_tlen'] =      round(float(info[25]),3)
            ko2summary[info[0]]['min_tlen'] =      round(float(info[26]),3)
            ko2summary[info[0]]['max_tlen'] =      round(float(info[27]),3)

            ko2summary[info[0]]['mean_mismatch'] = round(float(info[28]),3)
            ko2summary[info[0]]['std_mismatch'] =  round(float(info[29]),3)
            ko2summary[info[0]]['min_mismatch'] =  round(float(info[30]),3)
            ko2summary[info[0]]['max_mismatch'] =  round(float(info[31]),3)

            ko2summary[info[0]]['mean_qcov'] =     round(float(info[32]),3)
            ko2summary[info[0]]['std_qcov'] =      round(float(info[33]),3)
            ko2summary[info[0]]['min_qcov'] =      round(float(info[34]),3)
            ko2summary[info[0]]['max_qcov'] =      round(float(info[35]),3)

            ko2summary[info[0]]['mean_tcov'] =     round(float(info[36]),3)
            ko2summary[info[0]]['std_tcov'] =      round(float(info[37]),3)
            ko2summary[info[0]]['min_tcov'] =      round(float(info[38]),3)
            ko2summary[info[0]]['max_tcov'] =      round(float(info[39]),3)

            ko2summary[info[0]]['mean_evalue'] =   round(float(info[40]),3)
            ko2summary[info[0]]['std_evalue'] =    round(float(info[41]),3)
            ko2summary[info[0]]['min_evalue'] =    round(float(info[42]),3)
            ko2summary[info[0]]['max_evalue'] =    round(float(info[43]),3)

            ko2summary[info[0]]['mean_bit'] =      round(float(info[44]),3)
            ko2summary[info[0]]['std_bit'] =       round(float(info[45]),3)
            ko2summary[info[0]]['min_bit'] =       round(float(info[46]),3)
            ko2summary[info[0]]['max_bit'] =       round(float(info[47]),3)


with open('/home/plaza/projects/biorare/results/ko_mmseqs/ko2expand_seqs_qcov_08_v1.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        ko2summary[info[0]]['hit_mmseqs_qcov08'] = info[1]  


with open('/home/plaza/projects/biorare/results/gtdb_vs_ko/qcov_08/ko2gtdb_seqs_expand.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        ko2summary[info[0]]['num_gtdb_expand'] = info[1]

with open('/home/plaza/projects/biorare/results/gtdb_vs_ko/qcov_08/ko2misleading_seqs.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        ko2summary[info[0]]['num_misleadind'] = info[1]

with open('/home/plaza/projects/biorare/results/gtdb_vs_ko/qcov_08/ko2multiko_seqs.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        ko2summary[info[0]]['num_multiKO_seqs'] = info[1]



with open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/info_input_size.tsv') as fin:
    for line in fin:
        info = line.strip().split('\t')
        ko2summary[info[0]]['input_seqs'] = info[1]
        ko2summary[info[0]]['medium_len'] = info[2]

with open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/result_insilico_test/reciprocal_probes_len.tsv') as fin:
    for line in fin:
        if not line.startswith('#'):
            info = line.strip().split('\t')
            ko2summary[info[0]]['num_ori_probes'] = info[1]
            ko2summary[info[0]]['num_rescue_probes'] = info[2]
            ko2summary[info[0]]['total_probes'] = int(info[1])+int(info[2] )

with open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/results_blast/reciprocal_probes_match_mismatch_5.tsv') as fin:
    for line in fin:
        if not line.startswith('#'):
            info = line.strip().split('\t')
            ko2summary[info[0]]['match_hit']  = info[1]
            ko2summary[info[0]]['bad_match_hit']  = info[2]
            ko2summary[info[0]]['mismatch_hit'] = info[3]
            ko2summary[info[0]]['hq_match_probes'] = info[4]
            ko2summary[info[0]]['match_probes'] = info[5]
            ko2summary[info[0]]['bad_probes'] = info[6]
            ko2summary[info[0]]['mismatch_probes'] = info[7]


outsummary = open('/home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/result_insilico_test/summary4.tsv', 'w' )
head = ['#ko',
            'Num_query_seqs',
            'Num_hit_seqs',
            'hit_mmseqs_qcov08',
            'num_gtdb_expand',
            'input_seqs',
            'medium_len',
            'total_probes',
            'num_ori_probes', 
            'num_rescue_probes',
            'hq_match_probes',
            'match_probes',
            'bad_probes',
            'mismatch_probes',
            'match_hit',
            'mismatch_hit',
            'Kegg_pathways',
            'Kegg_descriptions', 
            'Num_query_genomes', 
            'Total_genomes_KO',
            'LCA_query_ncbi',
            'LCA_KO',
            'Num_hit_genomes', 
            'LCA_hit_gtdb',
            'Symbol',
            'mean_piden',
            'std_piden',
            'min_piden',  
            'max_piden', 
            'mean_alnlen',
            'std_alnlen',
            'min_alnlen', 
            'max_alnlen',
            'mean_qlen', 
            'std_qlen',  
            'min_qlen',   
            'max_qlen',   
            'mean_tlen',  
            'std_tlen',   
            'min_tlen',   
            'max_tlen',   
            'mean_mismatch',
            'std_mismatch', 
            'min_mismatch', 
            'max_mismatch', 
            'mean_qcov',  
            'std_qcov',   
            'min_qcov',   
            'max_qcov',   
            'mean_tcov',  
            'std_tcov',  
            'min_tcov',   
            'max_tcov',   
            'mean_evalue',
            'std_evalue', 
            'min_evalue', 
            'max_evalue', 
            'mean_bit',   
            'std_bit',    
            'min_bit',    
            'max_bit',
            '\n']

outsummary.write('\t'.join(head))

for ko, info in ko2summary.items():
    if len(info.keys()) > 50:
        outsummary.write('\t'.join(map(str, [
            ko,
            info['Num_query_seqs'],
            info['Num_hit_seqs'],
            info['hit_mmseqs_qcov08'],
            info['num_gtdb_expand'],
            info['input_seqs'],
            info['medium_len'],
            info['total_probes'],
            info['num_ori_probes'], 
            info['num_rescue_probes'],
            info['hq_match_probes'],
            info['match_probes'],
            info['bad_probes'],
            info['mismatch_probes'],
            info['match_hit'],
            info['mismatch_hit'],
            info['Kegg_pathways'],
            info['Kegg_descriptions'], 
            info['Num_query_genomes'], 
            info['Total_genomes_KO'],
            info['LCA_query_ncbi'],
            info['LCA_KO'],
            info['Num_hit_genomes'], 
            info['LCA_hit_gtdb'],
            info['Symbol'],
            info['mean_piden'],
            info['std_piden'],
            info['min_piden'],  
            info['max_piden'], 
            info['mean_alnlen'],
            info['std_alnlen'],
            info['min_alnlen'], 
            info['max_alnlen'],
            info['mean_qlen'], 
            info['std_qlen'],  
            info['min_qlen'],   
            info['max_qlen'],   
            info['mean_tlen'],  
            info['std_tlen'],   
            info['min_tlen'],   
            info['max_tlen'],   
            info['mean_mismatch'],
            info['std_mismatch'], 
            info['min_mismatch'], 
            info['max_mismatch'], 
            info['mean_qcov'],  
            info['std_qcov'],   
            info['min_qcov'],   
            info['max_qcov'],   
            info['mean_tcov'],  
            info['std_tcov'],  
            info['min_tcov'],   
            info['max_tcov'],   
            info['mean_evalue'],
            info['std_evalue'], 
            info['min_evalue'], 
            info['max_evalue'], 
            info['mean_bit'],   
            info['std_bit'],    
            info['min_bit'],    
            info['max_bit'],
            '\n'
        ])))

    else:
        print(ko, info)
        