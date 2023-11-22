#!/bin/bash
#SBATCH -N 1
#SBATCH -n 40
#SBATCH --mem=188GB
#SBATCH -e slurm/mmseqs/mmseqs_probes_vs_ko.err
#SBATCH -o slurm/mmseqs/mmseqs_probes_vs_ko.out
#SBATCH -p long
#SBATCH -t 30-00:00

#####
# MMseqs of probes to mmseqs kegg-ko nuc db
#####


mmseqs easy-search  /home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/total_probes_reciprocal_qcov08_v2.fasta /home/plaza/projects/biorare/databases/mmseqs_KEGG_ko/mmseqs_KO_total_nuc /home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/result_mmseqs/probes_vs_ko.result_mmseqs.tsv /home/plaza/projects/biorare/results/insilico_xenob/reciprocal_qcov08_v2/result_mmseqs/tmp --format-mode 4 --format-output "query,target,pident,alnlen,qstart,qend,qlen,tstart,tend,tlen,mismatch,gapopen,qcov,tcov,evalue,bits" --max-seqs 1000000 --search-type 3 --threads 40