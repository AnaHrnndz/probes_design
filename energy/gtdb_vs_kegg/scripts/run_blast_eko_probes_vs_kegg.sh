#!/bin/bash
#SBATCH -N 1
#SBATCH -n 8
#SBATCH -t 30-00:00
#SBATCH -p long
#SBATCH --mem=40GB
#SBATCH -e slurm/blast_eko_probes_vs_kegg.err
#SBATCH -o slurm/blast_eko_probes_vs_kegg.out

#####
#   Blastn of reciprocal filtered probes to kegg-ko nucleotides db
#####

blastn -query /home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_probes/total_probes.fasta \
    -db /home/plaza/projects/biorare/databases/blast_KEGG_ko_nt/KO_total_nuc_seqs.fn  \
    -out /home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_probes/blast_eko_probes_vs_kegg.tsv \
    -outfmt "6 qseqid qlen sseqid slen length qstart qend sstart send pident evalue bitscore qcovs qcovhsp qcovus" -num_threads 8