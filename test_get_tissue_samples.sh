#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle test_get_tissue_samples.py
assert_no_stdout
run test_style pycodestyle get_tissue_samples.py
assert_no_stdout

echo "...SMTS..."
run test_smts python3 get_tissue_samples.py --output_file out.txt --group_type SMTS --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
assert_exit_code 0
assert_no_stdout
rm out.txt
