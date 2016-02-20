import unittest
import pandas as pd

from data_processor import DataProcessor

class DataProcessorTests(unittest.TestCase):
    def setUp(self):
        dict = {
                "id":1,
                "data":[ [65,0,1], [65,1,3], [68,0,1], [68,1,7], [67,0,8], [67,1,9], [65,0,2], [68,0,1] ]
                }

        self.dp = DataProcessor(dict)

    def testNgrams(self):
        self.assertListEqual([ (1,2), (2,3), (3,4) ], self.dp.ngrams([1,2,3,4], 2))
        self.assertListEqual([ (1,2,3), (2,3,4), (3,4,5) ], self.dp.ngrams([1,2,3,4,5], 3))

    def testProcess(self):

        self.dict
        self.dp.preprocess()

        self.assertEqual()



if __name__ == '__main__':
    unittest.main()
