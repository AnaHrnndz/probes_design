#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 01-00:00
#SBATCH -p medium
#SBATCH -e /home/plaza/projects/biorare/scripts/slurm/diamond/create_dmnd_egg6.err
#SBATCH -o /home/plaza/projects/biorare/scripts/slurm/diamond/create_dmnd_egg6.out


######
#   Create Diamond DB for all EggNOG 6 aa seqs
######

diamond makedb --in /home/plaza/projects/biorare/results/dmnd_egg6/eggNOGv6_allseqs_clean.fa -d /home/plaza/projects/biorare/results/dmnd_egg6/dmnd_egg6