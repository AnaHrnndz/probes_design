#!/bin/bash
#SBATCH -N 1
#SBATCH -n 40
#SBATCH --mem=188GB
#SBATCH -e slurm/mmseqs/mmseqs_xenob_total_3.err
#SBATCH -o slurm/mmseqs/mmseqs_xenob_total_3.out
#SBATCH -p long
#SBATCH -t 30-00:00


#####
#    Run mmseqs with all sequences from xenobiotc ko
#####


# ko_path=$(cat /home/plaza/projects/biorare/results/path2xeno_ko.txt  | sed -n ${SLURM_ARRAY_TASK_ID}p)
# ko_name=$(echo $ko_path  | cut -d '/' -f 8  |cut -d '.' -f 1)

# mkdir -p /home/plaza/projects/biorare/scripts/tmp/$ko_name

# mmseqs easy-search  $ko_path /home/plaza/projects/biorare/gtdb_db/gtdb_nt_DB /home/plaza/projects/biorare/results/ko_mmseqs/$ko_name.result_mmseqs.tsv /home/plaza/projects/biorare/scripts/tmp/$ko_name --format-mode 4 --format-output "query,target,pident,alnlen,qstart,qend,qlen,tstart,tend,tlen,mismatch,gapopen,qcov,tcov,evalue,bits" --search-type 3 --threads 10


# rm -r /home/plaza/projects/biorare/scripts/tmp/$ko_name

mmseqs easy-search  /home/plaza/projects/biorare/results/xenob_total_nuc_seqs_2.fn /home/plaza/projects/biorare/gtdb_db/gtdb_nt_DB /home/plaza/projects/biorare/results/ko_mmseqs/xenob_total_3.result_mmseqs.tsv /home/plaza/projects/biorare/scripts/tmp_3 --format-mode 4 --format-output "query,target,pident,alnlen,qstart,qend,qlen,tstart,tend,tlen,mismatch,gapopen,qcov,tcov,evalue,bits" --max-seqs 1000000 --search-type 3 --threads 40


