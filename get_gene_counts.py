import gzip
import sys
import os
import argparse


# parse arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description='The right way to pass parameters.',
        prog='get_gene_counts.py')

    # require file name as one of the inputs
    parser.add_argument('--output_file',
                        type=str,
                        help='Name of the output plot',
                        required=True)

    # require gene as one of the inputs
    parser.add_argument('--gene',
                        type=str,
                        help='Target gene. e.g. ACTA2',
                        required=True)

    # require gene data as one of the inputs
    parser.add_argument('--gene_reads',
                        type=str,
                        help='Database of genes',
                        required=True)

    return parser.parse_args()


def linear_search(key, L):
    """ return index with matched key
    """
    for i in range(len(L)):
        if key == L[i]:
            return i
    return -1


def parse_gene_counts(target_gene_name, output_file, data):
    output = open(output_file, 'w')
    # necessary header
    version = None
    dim = None
    rna_header = None
    for l in gzip.open(data, 'rt'):

        if version is None:
            version = l
            continue

        if dim is None:
            dim = l
            continue

        if rna_header is None:
            rna_header = l.rstrip().split('\t')
            description_idx = linear_search('Description', rna_header)
            continue

        rna_counts = l.rstrip().split('\t')

        if description_idx == -1:
            print('Gene not found in header')
            sys.exit(1)

        if rna_counts[description_idx] == target_gene_name:
            for i in range(description_idx + 1, len(rna_header)):
                output.write(rna_header[i] + ': ' + rna_counts[i])
                if i != len(rna_header) - 1:
                    output.write('\n')
            output.close()


def main():
    # get argument by arg parser
    args = parse_args()
    # check if it is a valid file name
    if not os.access(args.output_file, os.W_OK):
        try:
            open(args.output_file, 'w').close()
            os.unlink(args.output_file)
        except OSError:
            print('Invalid output file name')
            sys.exit(1)
    if (not os.path.exists(args.gene_reads)):
        print('Cannot find meta file')
        sys.exit(1)
    parse_gene_counts(args.gene, args.output_file, args.gene_reads)
    sys.exit(0)


if __name__ == '__main__':
    main()
