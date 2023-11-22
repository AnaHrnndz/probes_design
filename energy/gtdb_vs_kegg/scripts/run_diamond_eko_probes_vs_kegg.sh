#!/bin/bash
#SBATCH -N 1
#SBATCH -n 10
#SBATCH -e slurm/diamond_eko_probes_vs_kegg.err
#SBATCH -o slurm/diamond_eko_probes_vs_kegg.out
#SBATCH -t 30-00:00
#SBATCH -p long



diamond blastx --threads 10 --db /home/plaza/projects/biorare/databases/dmnd_KEGG_ko_aa/dmnd_ko_aa.dmnd -q /home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_probes/total_probes.fasta \
     --out /home/plaza/projects/biorare/gtdb_vs_kegg/results/eko_probes/diamond_eko_probes_vs_kegg.tsv