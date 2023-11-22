#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 01-00:00
#SBATCH -p medium
#SBATCH -e /home/plaza/projects/biorare/scripts/slurm/diamond/create_dmnd_ko_aa_seqs.err
#SBATCH -o /home/plaza/projects/biorare/scripts/slurm/diamond/create_dmnd_ko_aa_seqs.out

######
#   Create Diamond DB for all KO aa seqs
######

diamond makedb --in /home/plaza/projects/biorare/results/ko_vs_gtdb/KO_total_aa_seqs.fa -d /home/plaza/projects/biorare/results/ko_vs_gtdb/dmnd_ko_aa