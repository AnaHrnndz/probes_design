#AHP 2023

1. GTDB vs total_ko. Only 1 hit per gtdb seq
    run_diamond_gtdb_vs_kegg.sh

2.  get KO to gtdb seqs (qcov>=80.0)
    filter_seqs.py

3. Compare results with xenobiotic results
    compare_xenobiotics.py

4. Build energy-specific-KO gtdb expanded nucleotide fasta files (558 eko)
    build_eko_expanded.py

5. Run insilico probes
    combine_probes_eko.py
    run_probes_eko.sh

6. check probes againts total ko
    resume_eko_probes_diamons.py