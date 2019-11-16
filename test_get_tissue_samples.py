import unittest
import random
import os
import get_tissue_samples


class TestGetTissueSamples(unittest.TestCase):
    def test_parser(self):
        sample = 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
        group_type = 'SMTS'
        a, b = get_tissue_samples.parse_meta(group_type, sample)
        self.assertNotEqual(a, None)
        b.sort()
        self.assertEqual(b[0], 'Adipose Tissue')
        self.assertEqual(b[30], 'Vagina')

    def test_linear_search(self):
        L = [1, 2, 3, 4, 5, 6]

        r = get_tissue_samples.linear_search(3, L)
        self.assertEqual(r, 2)

        r = get_tissue_samples.linear_search(10, L)
        self.assertEqual(r, -1)


if __name__ == '__main__':
    unittest.main()
