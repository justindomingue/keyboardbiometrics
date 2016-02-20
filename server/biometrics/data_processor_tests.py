import unittest

from data_processor import DataProcessor

class DataProcessorTests(unittest.TestCase):
    def setUp(self):
        dict = {
                "id":1,
                "data":[ [65,0,1456002930078], [65,1,1456002930200], [68,0,1456002938043], [68,1,1456002938133], [67,0,1456002939442], [67,1,1456002939569] ]
                }

        self.dp = DataProcessor(dict)

    def testNgrams(self):
        self.assertListEqual([ (1,2), (2,3), (3,4) ], self.dp.ngrams([1,2,3,4], 2))
        self.assertListEqual([ (1,2,3), (2,3,4), (3,4,5) ], self.dp.ngrams([1,2,3,4,5], 3))

    # def testProcess(self):



if __name__ == '__main__':
    unittest.main()
