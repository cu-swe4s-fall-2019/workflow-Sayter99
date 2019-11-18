GENES = ["SDHB", "MEN1", "KCNH2", "MSH2", "MYL2", "BRCA2"]
TISSUES = ["Brain", "Heart", "Blood", "Skin"]
TISSUE_GROUP = "SMTS"

rule all:
    input:
        'Brain-Heart-Blood-Skin_SDHB-MEN1-KCNH2-MSH2-MYL2-BRCA2.png'

rule tissue_samples:
    input:
        'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
    output:
        expand('{tg}_samples.txt', tg=TISSUE_GROUP)
    shell:
        'python get_tissue_samples.py --output_file {output} --group_type {TISSUE_GROUP} --sample_attributes {input}'

rule gene_sample_counts:
    input:
        'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz'
    output:
        expand('{gg}_counts.txt', gg=GENES)
    shell:
        'for GG in {GENES}; do ' \
        + 'python get_gene_counts.py --output_file $GG\_counts.txt --gene $GG --gene_reads {input}; ' \
        + 'done'

rule box:
    input:
        rules.tissue_samples.output,
        rules.gene_sample_counts.output
    output:
        'Brain-Heart-Blood-Skin_SDHB-MEN1-KCNH2-MSH2-MYL2-BRCA2.png'
    shell:
        'python box.py --output_file {output} --genes \"{GENES}\" --tissues \"{TISSUES}\" --meta_file {TISSUE_GROUP}_samples.txt'