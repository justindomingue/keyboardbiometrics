class DataProcessor:
    def __init__(self, raw):
        self.data = raw['data']
        self.id = raw['id']

    def process(self):
        ''' Process the data

        Expect self.data to be of the form
            [ [ key, action, time ] ]
        '''

        self.digraphs = []

        bigrams = self.ngrams()

    def ngrams(self, lst, n=2):
        return zip(*[lst[i:] for i in range(n)])

