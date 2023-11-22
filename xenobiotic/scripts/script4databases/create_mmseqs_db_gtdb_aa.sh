#!/bin/bash
#SBATCH -N 1
#SBATCH -n 40
#SBATCH --mem=1T
#SBATCH -e slurm/mmseqs/mmseqs_create_gtdb_db_aa.err
#SBATCH -o slurm/mmseqs/mmseqs_create_gtdb_db_aa.out
#SBATCH -p bigmem
#SBATCH -t 30-00:00



######
#   Create MMseqs DB for all GTDB aa seqs
######



#cat /home/plaza/projects/biorare/gtdb_db/gtdb_aa/gtdb_proteins_aa_reps_r207_complete_id.faa | mmseqs createdb stdin /home/plaza/projects/biorare/gtdb_db/gtdb_aa/gtdb_aa_DB --dbtype 1

mmseqs createindex /home/plaza/projects/biorare/gtdb_db/gtdb_aa/gtdb_aa_DB /home/plaza/projects/biorare/gtdb_db/gtdb_aa/tmp_aa
