#!/bin/bash
#SBATCH -N 1
#SBATCH -c 1
#SBATCH --array=1-314
#SBATCH -e /home/plaza/projects/biorare/scripts/slurm/insilico/insilico_all_qcov_v1_%A_%a.err
#SBATCH -o /home/plaza/projects/biorare/scripts/slurm/insilico/insilico_all_qcov_v1_%A_%a.out
#SBATCH -t 01-00:00
#SBATCH -p medium


#####
#   Run Desing probes scripts
#   KO without reciprocal analysis
#####


#export PATH=/home/plaza/projects/biorare/scripts/insilico_scripts/kits_targeted/src:$PATH
#ml  BLAST+
#ml  CD-HIT
 

fasta_in=$(cat '/home/plaza/projects/biorare/results/insilico_xenob/all_qcov_08/path2expanded_ko.txt' | sed -n ${SLURM_ARRAY_TASK_ID}p)
name=$(basename  $fasta_in | sed 's/.fna//g')


kmsize=120
kmwind=60
cdhit_id=0.8
cdhit_cov=0.8
mapback_id=0.8
mapback_cov=0.8
main_outdir=/home/plaza/projects/biorare/results/insilico_xenob/all_qcov_08/result_insilico_test
src_dir=/home/plaza/projects/biorare/scripts/insilico_scripts/kits_targeted/src
specific_outdir=${main_outdir}/${name}/v1

mkdir -p $specific_outdir

echo $name, $kmsize, $kmwind, $cdhit_id, $cdhit_cov, $mapback_id, $mapback_cov, $specific_outdir

python $src_dir/kmers_fasta.py $fasta_in $name $kmsize $kmwind $cdhit_id $cdhit_cov $specific_outdir

create_genes_db.sh $fasta_in

mapback_kmers_sample.sh $specific_outdir/${name}_kmers.clustering $fasta_in $specific_outdir/${name}_kmers.clustering.blastn 2

mapback_kmers_filter_sample.sh $fasta_in $specific_outdir/${name}_kmers.clustering.blastn.gz $specific_outdir/${name}_kmers.clustering.blastn.filt $mapback_id $mapback_cov 

mapback_kmers_stats.sh $specific_outdir/${name}_kmers.clustering.blastn.filt $specific_outdir/${name}_kmers.clustering.blastn.filt.refs_cov >$specific_outdir/${name}_stats.out 2>$specific_outdir/${name}_stats.err

python $src_dir/recover_kmers_fasta.py $fasta_in $specific_outdir/${name}_kmers.clustering.blastn.filt.refs_cov $kmsize $kmwind $cdhit_id $cdhit_cov $specific_outdir