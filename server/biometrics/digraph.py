class Digraph:
    def __init__(self, digraph, n, mean, variance, skewness=0, kurtosis=0):
        self.digraph = digraph
        self.n = n
        self.mean = mean
        self.variance = variance
        self.skewness = skewness
        self.kurtosis = kurtosis

