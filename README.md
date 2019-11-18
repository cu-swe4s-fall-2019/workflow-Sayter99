# Workflow
Build a workflow using snakemake

## Data Sources
* https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
* https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

## Continuous Integration Status
![](https://travis-ci.com/cu-swe4s-fall-2019/workflow-Sayter99.svg?branch=master)

## Installation
To use this package, you need to have [Python3](https://www.python.org/download/releases/3.0/) in your environment. And the used packages are listed below.

### Used Packages
* os
* sys
* math
* time
* numpy
* random
* argparse
* unittest
* matplotlib
* pycodestyle

## Usage
Use `snakemake` to generate final boxplot. The workflow is
1. Generating gene_counts files
2. Generating tissue_samples files
3. Utilizing above files to generate boxplot

## Changes in this assignment
* Added both functional tests and unit tests for `box.py`, `get_gene_counts.py`, and `get_tissue_samples.py`
* Completed robust modules and scripts including `box.py`, `get_gene_counts.py`, and `get_tissue_samples.py`
    * completed `box.py` to generate boxplot by using counts and samples
    * completed `get_gene_counts.py` to get gene counts from GTEx data
    * completed `get_tissue_samples.py` to get samples from GTEx data
* Tested and developed iteratively
* Created `travis.yaml` to carry out added tests
* Completed the `README.md` followed the best practice
