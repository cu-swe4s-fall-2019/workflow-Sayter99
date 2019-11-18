#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle test_box.py
assert_no_stdout
run test_style pycodestyle box.py
assert_no_stdout

echo "...No Meta..."
run test_bad_meta python3 box.py --tissues "Brain Heart Blood Skin" --genes "SDHB MEN1 KCNH2 MSH2 MYL2 BRCA2" --output_file 111 --meta_file SMTS_sample.txt
assert_exit_code 1
assert_stdout
