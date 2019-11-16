#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle test_get_gene_counts.py
assert_no_stdout
run test_style pycodestyle get_gene_counts.py
assert_no_stdout

echo "...ACTA2..."
run test_acta2 python3 get_gene_counts.py --output_file out.txt --gene ACTA2 --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
assert_exit_code 0
assert_no_stdout
rm out.txt
