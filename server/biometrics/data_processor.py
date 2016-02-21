from collections import defaultdict
import pandas as pd
import numpy as np
import operator
import json
from digraph import Digraph

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
            digraphs[name].append(delta)

        self.digraphs = digraphs

        # Create panda frame
        df = pd.DataFrame({k: pd.Series(v) for k,v in digraphs.items()})

        self.all_data = df

    def process(self):
        count = self.all_data.count()
        means = self.all_data.mean()
        var   = self.all_data.var()

        self.df = pd.concat([count, means, var], axis=1)

    def filter(self, data, action):
        return [x for x in data if x[1] == action]

    def ngrams(self, lst, n=2):
        return zip(*[lst[i:] for i in range(n)])


if __name__ == "__main__":
    with open('data/data.json','r') as f:
        data = json.load(f)

        frames = []
        for k,v in data.items():
            print ("=======")
            print (k)
            print ("=======")
            dp = DataProcessor(v)
            dp.preprocess()
            dp.process()

           # print (dp.digraphs)
           # print (dp.df)
            print(dp.df.index)

            frames.append(dp.df)
