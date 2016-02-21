import csv

class data_creator:
    def __init__(filename) :
        client1 = client("s001")
        client2 = client("s002")
        clients = dict()
        clients["s001"] = client1
        clients["s002"] = client2
        out=open(filename, 'rb')
        data = csv.reader(out)
        trials = []
        for row in data:




