#!/bin/bash
#SBATCH -N 1
#SBATCH -n 10
#SBATCH -e /home/plaza/projects/biorare/scripts/slurm/diamond/probes_all_qcov08.err
#SBATCH -o /home/plaza/projects/biorare/scripts/slurm/diamond/probes_all_qcov08.out
#SBATCH -t 30-00:00
#SBATCH -p long

#######
#   Diamond blastx probes vs kegg-ko aa
#   without reciprocal gtdb vs kegg-ko aa db
#######



diamond blastx --threads 10 --db /home/plaza/projects/biorare/results/gtdb_vs_ko/dmnd_ko_aa.dmnd -q /home/plaza/projects/biorare/results/insilico_xenob/all_qcov_08_probes.fasta --out /home/plaza/projects/biorare/results/insilico_xenob/diamond/probes_all_qcov08_vs_ko_original.tsv