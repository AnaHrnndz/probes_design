#!/bin/bash
#SBATCH -N 1
#SBATCH -c 20
#SBATCH -e /home/plaza/projects/biorare/scripts/slurm/diamond/gtdb_vs_ko_prot2prot.err
#SBATCH -o /home/plaza/projects/biorare/scripts/slurm/diamond/gtdb_vs_ko_prot2prot.out
#SBATCH -t 07-00:00
#SBATCH -p long

#####
#   Reciprocal diamond analysis
#   Diamond blastp gtdb hits aa seqs to kegg-ko aa db
#####


diamond blastp --threads 20 --db /home/plaza/projects/biorare/results/gtdb_vs_ko/dmnd_ko_aa.dmnd -q /home/plaza/projects/biorare/results/gtdb_vs_ko/gtdb_hits_aa.faa --out /home/plaza/projects/biorare/results/gtdb_vs_ko/gtdb_vs_ko_prot2prot.tsv --ultra-sensitive