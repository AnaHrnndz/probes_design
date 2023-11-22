#   Biorare
#   AHP 2023


'''
    Workflow description for xenobiocts KO:
'''
1. Run mmseqs:
    script: run_mmseqs_xenob_ko.sh
    result: ko_mmseqs/xenob_total_v1.result_mmseqs.tsv

2. Parse mmseqs results
    script: parse_mmseqs_results.py
    result: ko_mmseqs/ko2expand_seqs_qcov_08_v1.tsv
            ko_mmseqs/qcov_08_mmseqs_v1.tsv

3. Create total-ko diamond database
    script: create_dmnd_db.sh
    result: databases/dmnd_KEGG_ko_aa/dmnd_ko_aa.dmnd

4. Create fasta with all GTDB hits (no filtered)
    script: get_gtdb_hit_seqs_v3.py
    result: gtdb_vs_ko/gtdb_hits_aa.faa

5. Run diamond blastx (reciprocal hit) (blastx gtdb_hits_aa.faa vs dmnd_ko_aa.dmnd)
    script: run_diamond_inv.sh
    result: gtdb_vs_ko/qcov_08/gtdb_vs_ko_blastx.tsv

6. Check gtdb reciprocal mapping
    script: check_gtdb_splits.py
    result: gtdb_vs_ko/qcov_08/ko2misleading_seqs.tsv
            gtdb_vs_ko/qcov_08/ko2multiko_seqs.tsv
            gtdb_vs_ko/qcov_08/ko2gtdb_seqs_expand.tsv

7. Expand KO with gtdb seqs after diamond reciproval search, expand only for gtdb seqs that in the original mmseqs search had qcov 0.8
    script: expand_KO.py
    result: results/insilico_xenob/reciprocal_qcov08_v2/K*_recirocal_qcov08.fna

9. Run insilico test
    script: run_insilico.sh
    result: results/insilico_xenob/reciprocal_qcov08_v2/result_insilico_test

10. Get number of probes per KO
     script:    count_probes.py
     result:    results/insilico_xenob/reciprocal_qcov08_v2/result_insilico_test/reciprocal_probes_len.tsv

11. Combine all probes from different KOs and run regular blast against all seqs from KO-KEGG
     script:    run_blast_probes.sh
     result:    insilico_xenob/reciprocal_qcov08_v2/results_blast/probes_vs_total_ko.tsv

12. Check that probes vs Kegg-KO seqs
    script: check_probes_vs_ko_original.py
    result: insilico_xenob/reciprocal_qcov08_v2/results_blast/reciprocal_probes_match_mismatch.tsv

13. Merge tables
    script: merge_tables_info.py
    result: insilico_xenob/reciprocal_qcov08_v2/result_insilico_test/summary.tsv

