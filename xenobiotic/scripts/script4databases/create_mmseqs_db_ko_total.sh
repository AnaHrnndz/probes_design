#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mem=500GB
#SBATCH -e slurm/mmseqs/mmseqs_create_db_ko.err
#SBATCH -o slurm/mmseqs/mmseqs_create_db_ko.out
#SBATCH -p bigmem
#SBATCH -t 30-00:00


######
#   Create MMseqs DB for all KO seqs for aa and nuc
######

#Nuc DB
echo Nuc DB

cat /home/plaza/projects/biorare/databases/blast_KEGG_ko_nt/KO_total_nuc_seqs.fn | mmseqs createdb stdin /home/plaza/projects/biorare/databases/mmseqs_KEGG_ko/mmseqs_KO_total_nuc --dbtype 2

mmseqs createindex /home/plaza/projects/biorare/databases/mmseqs_KEGG_ko/mmseqs_KO_total_nuc /home/plaza/projects/biorare/databases/mmseqs_KEGG_ko/tmp


#AA DB
echo aa DB

cat /home/plaza/projects/biorare/databases/dmnd_KEGG_ko_aa/KO_total_aa_seqs.fa | mmseqs createdb stdin /home/plaza/projects/biorare/databases/mmseqs_KEGG_ko/mmseqs_KO_total_aa --dbtype 1

mmseqs createindex /home/plaza/projects/biorare/databases/mmseqs_KEGG_ko/mmseqs_KO_total_aa  //home/plaza/projects/biorare/databases/mmseqs_KEGG_ko/tmp

