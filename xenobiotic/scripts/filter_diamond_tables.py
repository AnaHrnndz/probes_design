import pandas as pd


column_names = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore', 'qcovhsp', 'scovhsp']

df = pd.read_csv('/home/plaza/projects/biorare/ahp_results_energy/array_results/K18860_eKO_initial_dmnd.tsv', sep='\t')

print(df.head())