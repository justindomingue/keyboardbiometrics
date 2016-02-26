from collections import defaultdict
import pandas as pd
import numpy as np
import operator
import json
from scipy.spatial.distance import euclidean,pdist,seuclidean

THRESHOLD = 5

class DataProcessor:
    def __init__(self, raw):
        self.data = raw['data']
        self.id = raw['id']

    def preprocess(self):
        ''' Process the data

        Expect self.data to be of the form
            [ [ key, action, time ] ]
        '''

        data = self.data
        data = self.filter(data, 0)   # down=0, up=1

        # At this point, we have
        #   data = [ [key, DOWN/UP, timestamp], ... ]

        # Get ngrams
        bigrams = self.ngrams(data, 2)

        # Build a dictionary of observations
        # { digraph1: [ob1, ob2, ...], ... }
        digraphs = defaultdict(list)
        for bigram in bigrams:
            name = chr(bigram[0][0]) + chr(bigram[1][0])
            delta = bigram[1][2] - bigram[0][2] # time difference
            if delta < 500:
                digraphs[name].append(delta)

        self.digraphs = digraphs

        # Create panda frame
        df = pd.DataFrame({k: pd.Series(v) for k,v in digraphs.items()})

        print(df)
        self.all_data = df.sort_index()

    def process(self):
        count = self.all_data.count()
        means = self.all_data.mean()
        var   = self.all_data.var()

        count.name = "count"
        means.name = "means"
        var.name = "variance"

        self.df = pd.concat([count, means, var], axis=1)

        # Filter
        self.df = self.df[self.df[0] >= THRESHOLD]

    def filter(self, data, action):
        return [x for x in data if x[1] == action]

    def ngrams(self, lst, n=2):
        return zip(*[lst[i:] for i in range(n)])


if __name__ == "__main__":
    with open('data/s.txt','r') as f:
        data = json.load(f)

        all_means = pd.DataFrame()
        for k,v in data.items():
            print(k)

            dp = DataProcessor(v)
            dp.preprocess()
            dp.process()

            # print(dp.df)
            all_means = pd.concat([all_means, dp.df.loc[:,1:2]], axis=1, join='inner')

        print(all_means)
        # all_means_wo_na = all_means.dropna()

        # print(all_means_wo_na)
        #
        # for i in range(0,all_means_wo_na.shape[1],2):
        #     for j in range(0,all_means_wo_na.shape[1],2):
        #         print("{0} {1}".format(all_means_wo_na.loc[i], all_means_wo_na.loc[j]))
                # dist = seuclidean(all_means_wo_na.values[i], all_means_wo_na.values[j], all_means_wo_na.values[i+1])
                # print("{0},{1} {2}".format(i,j,dist))

        # print(all_means.dropna())
        # print(all_means)

    # print(euclidean(frames[0][1][0:200], frames[1][1][0:200]))

