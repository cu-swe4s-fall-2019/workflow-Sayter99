import unittest
import random
import os
import box


class TestBox(unittest.TestCase):
    def test_boxplot(self):
        data = [[[1, 2, 3]]]
        meta = ['a', 'b', 'c']
        title = ['t']
        box.boxplot(data, meta, 'y', title, 'test.png')
        self.assertTrue(os.path.exists('test.png'))
        os.remove('test.png')


if __name__ == '__main__':
    unittest.main()
