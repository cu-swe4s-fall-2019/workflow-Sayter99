import unittest
import random
import os
import get_gene_counts


class TestGetGeneCounts(unittest.TestCase):
    def test_parser(self):
        gene = 'ACTA2'
        get_gene_counts.parse_gene_counts(gene, 'out.txt',
                                          'GTEx_Analysis_' +
                                          '2017-06-05_v8_RNASeQCv1.1.9' +
                                          '_gene_reads.acmg_59.gct.gz')
        self.assertTrue(os.path.exists('out.txt'))
        os.remove('out.txt')

    def test_linear_search(self):
        L = [1, 2, 3, 4, 5, 6]

        r = get_gene_counts.linear_search(3, L)
        self.assertEqual(r, 2)

        r = get_gene_counts.linear_search(10, L)
        self.assertEqual(r, -1)


if __name__ == '__main__':
    unittest.main()
