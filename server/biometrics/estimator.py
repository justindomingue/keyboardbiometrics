from scipy import stats
from math import sqrt
from digraph import Digraph
import panda as pd

class Estimator:
    def __init__( self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def estimate(self):
        #we know that the sum of all the  n features Z~N(0,1) will give us a ~X^2 with df = 10
        df = len(self.v1)
        value = 0

        #going through every feature and calculating its normal value
        for i in range (0,df):
            normalized_mean =  self.v2[i].n * (self.v1[i].mean - self.v2[i].mean) / sqrt(self.v2[i].variance / self.v2[i].n)
            print(normalized_mean)
            value += normalized_mean*normalized_mean

        #getting here we have a value to plug in the Chi Square distribution
        print(value)
        print(df)
        result = stats.chi2.cdf(value, df)
        return result

    def estimate_distance(self):
        #simply calculate the distance between the two vectors.
        #remove all features with less than 2 observations.
        #make sure both vectors have the same number of observations for each features ( pick min )
        #calculate the distance of both vectors

        for i in range(0,10):
            print(0)


feat1 = Digraph("in" ,28, 4.912,0.066, 1.672,0 )
feat2 = Digraph("-a", 29, 4.921, 0.027, 0.950,0)
feat3 = Digraph("e-", 46, 4.928, 0.037, 0.082,0)

feat11 = Digraph("in",28,4.896,0.030, 0.826,0 )
feat12 = Digraph("-a", 27, 4.824, 0.05, 1.080,0)
feat13 = Digraph("e-", 44, 4.715, 0.055, 0.543,0)

list1 = [feat1,feat2,feat3]
list2 = [feat11,feat12,feat13]

myEst = Estimator(list1, list2)
print(myEst.estimate())


