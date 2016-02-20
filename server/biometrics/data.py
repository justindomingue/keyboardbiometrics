class Digraph:
    def __init__(digraph, n, mean, variance, skewness, kurtosis):
        self.digraph = digraph
        self.n = n
        self.mean = mean
        self.variance = variance
        self.skewness = skewness
        self.kurtosis = kurtosis

class Data:
    def process(dict):
        ''' Takes a dictionary of (key, up, down) points and makes the data easy to access '''
        for key, times in dict.items():
            RawPoint(key, times['up'], times['down'])

