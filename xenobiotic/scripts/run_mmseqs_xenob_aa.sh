#!/bin/bash
#SBATCH -N 1
#SBATCH -n 40
#SBATCH --mem=188GB
#SBATCH -e slurm/mmseqs/mmseqs_xenob_total_aa.err
#SBATCH -o slurm/mmseqs/mmseqs_xenob_total_aa.out
#SBATCH -p long
#SBATCH -t 30-00:00


#####
#    Run mmseqs with all aa sequences from xenobiotc ko
#####




mmseqs easy-search  /home/plaza/projects/biorare/results/xenob_total_aa_seqs.fa /home/plaza/projects/biorare/gtdb_db/gtdb_nt_DB /home/plaza/projects/biorare/results/ko_mmseqs/xenob_total.result_mmseqs.tsv /home/plaza/projects/biorare/scripts/tmp --format-mode 4 --format-output "query,target,pident,alnlen,qstart,qend,qlen,tstart,tend,tlen,mismatch,gapopen,qcov,tcov,evalue,bits" --max-seqs 1000000 --search-type 3 --threads 40


