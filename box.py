import sys
import os
import argparse
import matplotlib.pyplot as plt


# parse arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description='The right way to pass parameters.',
        prog='box.py')

    # require file name as one of the inputs
    parser.add_argument('--output_file',
                        type=str,
                        help='Name of the output plot',
                        required=True)

    # require genes as one of the inputs
    parser.add_argument('--genes',
                        type=str,
                        help='Target genes. e.g. SDHB MEN1',
                        required=True)

    # require tissues as one of the inputs
    parser.add_argument('--tissues',
                        type=str,
                        help='Target tissues. e.g. Brain Heart',
                        required=True)

    # require meta file
    parser.add_argument('--meta_file',
                        type=str,
                        help='Meta file',
                        required=True)

    return parser.parse_args()


def boxplot(data, meta, y_label, title, out_file):
    """plot boxplot for input parallel array and save the result as a png file
    """
    plt.subplots(nrows=len(title), figsize=(12, 10))

    for i in range(len(title)):
        plt.subplot(len(title), 1, i+1)
        plt.boxplot(data[i])

        # Hide these grid behind plot objects
        plt.title(title[i])
        plt.ylabel(y_label)

        # set tick labels and export the result
        plt.xticks(range(1, len(meta) + 1), meta)

        if i == len(title) - 1:
            plt.xlabel('Gene')

    plt.savefig(out_file)


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
    if not os.path.exists(args.meta_file):
        print('Invalid meta file')
        sys.exit(1)

    sample_dict = {}
    meta_file = open(args.meta_file)
    for l in meta_file:
        sample_id = l.split(':')[0]
        sample_genes = l.split(':')[1].split()
        sample_dict[sample_id] = sample_genes
    meta_file.close()

    tissues = args.tissues.split()
    genes = args.genes.split()

    final = []
    for tissue in tissues:
        par = []
        sample_ids = sample_dict[tissue]
        for gene in genes:
            gene_dict = {}
            if not os.path.exists(gene + '_counts.txt'):
                continue
            count_file = open(gene + '_counts.txt')
            for l in count_file:
                gene_dict[l.split(':')[0]] = int(l.split(':')[1])
            count_file.close()
            count_list = []
            for sample_id in sample_ids:
                if sample_id in gene_dict.keys():
                    count_list.append(gene_dict[sample_id])
            par.append(count_list)
        final.append(par)
    boxplot(final, genes, 'Count', tissues, args.output_file)

    sys.exit(0)


if __name__ == '__main__':
    main()
