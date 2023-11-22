#!/bin/bash
#SBATCH -N 1
#SBATCH -n 40
#SBATCH --mem=180GB
#SBATCH -t 30-00:00
#SBATCH -p long
#SBATCH -e slurm/diamond_gtdb_vs_kegg.err
#SBATCH -o slurm/diamond_gtdb_vs_kegg.out

gtdb_seqs='/home/sbodi/SRV_Symborg/07-eggnogmapper/GTDB_TAXONOMY/GTDB_DATABASE/gtdb_proteins_aa_reps_r207_complete_id.faa'
kegg_db=' /home/plaza/projects/biorare/databases/dmnd_KEGG_ko_aa/dmnd_ko_aa.dmnd'

export PATH=/home/plaza/soft/2023_diamond/:$PATH

diamond blastp -q $gtdb_seqs --db $kegg_db  --top 1 --iterate --sensitive --threads 40 --memory-limit 170G \
    -o /home/plaza/projects/biorare/gtdb_vs_kegg/results/gtdb_vs_kegg.tsv  \
    -f 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qcovhsp scovhsp --tmpdir ./tmp