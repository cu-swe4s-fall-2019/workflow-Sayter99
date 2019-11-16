import sys
import os
import argparse
import time


# parse arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description='The right way to pass parameters.',
        prog='get_tissue_samples.py')

    # require file name as one of the inputs
    parser.add_argument('--output_file',
                        type=str,
                        help='Name of the output plot',
                        required=True)

    # require group type as one of the inputs
    parser.add_argument('--group_type',
                        type=str,
                        help='The group type. e.g. SMTS',
                        required=True)

    # require meta file as one of the inputs
    parser.add_argument('--sample_attributes',
                        type=str,
                        help='A txt file containing meta data',
                        required=True)

    return parser.parse_args()


def linear_search(key, L):
    """ return index with matched key
    """
    for i in range(len(L)):
        if key == L[i]:
            return i
    return -1


def parse_meta(group, file):
    """ save meta data to samples and target_group
    """
    metadata_header = None
    target_group = []
    ht = {}
    f = open(file)
    for l in f:
        sample_info = l.rstrip().split('\t')

        if metadata_header is None:
            metadata_header = sample_info
            continue

        sample_idx = linear_search('SAMPID', metadata_header)
        target_idx = linear_search(group, metadata_header)
        if (target_idx == -1):
            return None, target_group
        key = sample_info[target_idx]
        value = sample_info[sample_idx]
        search = None
        if key in ht.keys():
            search = ht[key]
        if (search is None):
            ht[key] = [value]
            target_group.append(key)
        else:
            search.append(value)
    f.close()
    return ht, target_group


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
    if (not os.path.exists(args.sample_attributes)):
        print('Cannot find meta file')
        sys.exit(1)

    meta_map, target_group = parse_meta(args.group_type,
                                        args.sample_attributes)
    target_group.sort()

    if (meta_map is None):
        print('Cannot find group_type')
        sys.exit(1)
    else:
        output = open(args.output_file, 'w')
        for i in range(len(target_group)):
            output.write(target_group[i] + ': ')
            for j in range(len(meta_map[target_group[i]])):
                output.write(meta_map[target_group[i]][j])
                if j != len(meta_map[target_group[i]]) - 1:
                    output.write(' ')
            if i != len(target_group) - 1:
                output.write('\n')
        output.close()

    sys.exit(0)


if __name__ == '__main__':
    main()
