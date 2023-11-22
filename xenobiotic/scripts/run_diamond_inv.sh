#!/bin/bash
#SBATCH -N 1
#SBATCH -c 10
#SBATCH -e /home/plaza/projects/biorare/scripts/slurm/diamond/gtdb_vs_ori_ko.err
#SBATCH -o /home/plaza/projects/biorare/scripts/slurm/diamond/gtdb_vs_ori_ko.out
#SBATCH -t 01-00:00
#SBATCH -p medium

#####
#   Reciprocal analysis
#   Diamond blastx gtdb hits nuc seqs vs kegg-ko aa db
#####

diamond blastx --threads 10 --db /home/plaza/projects/biorare/results/gtdb_vs_ko/dmnd_ko_aa.dmnd -q /home/plaza/projects/biorare/results/ko_vs_gtdb/gtdb_hits_nt.fna --out /home/plaza/projects/biorare/results/ko_vs_gtdb/gtdb_vs_ko