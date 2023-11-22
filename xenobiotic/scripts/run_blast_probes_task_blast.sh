#!/bin/bash
#SBATCH -N 1
#SBATCH -n 8
#SBATCH -t 30-00:00
#SBATCH -p long
#SBATCH --mem=40GB
#SBATCH -e /home/plaza/projects/biorare/scripts/slurm/blast/probes_vs_ko_task_blastn.err
#SBATCH -o /home/plaza/projects/biorare/scripts/slurm/blast/probes_vs_ko_task_blastn.out

#####
#   Blastn of reciprocal filtered probes to kegg-ko nucleotides db
#####

blastn -task blastn -query /home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/total_probes_reciprocal_qcov08_v2.fasta \
    -db /home/plaza/projects/biorare/databases/blast_KEGG_ko_nt/KO_total_nuc_seqs.fn \
    -out /home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/results_blast/probes_vs_total_ko_task_blastn.tsv \
    -outfmt "6 qseqid qlen sseqid slen length qstart qend sstart send pident evalue bitscore qcovs qcovhsp qcovus" -num_threads 8