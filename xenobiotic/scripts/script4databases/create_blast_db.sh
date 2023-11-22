#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -e /home/plaza/projects/biorare/scripts/slurm/blast/create_total_ko_blastDB.err
#SBATCH -o /home/plaza/projects/biorare/scripts/slurm/blast/create_total_ko_blastDB.out
#SBATCH -t 30-00:00
#SBATCH -p long

######
#   Create blast DB for all KO nuc seqs 
######

makeblastdb -dbtype nucl -in /home/plaza/projects/biorare/results/gtdb_vs_ko/KO_total_nuc_seqs.fn