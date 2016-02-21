import unittest
import pandas as pd

from data_processor import DataProcessor

class DataProcessorTests(unittest.TestCase):
    def setUp(self):
        dict = {"id":1,"data":[[84,0,1456010413839],[72,0,1456010413903],[84,1,1456010413938],[73,0,1456010413979],[72,1,1456010414050],[83,0,1456010414079],[73,1,1456010414138],[83,1,1456010414214],[84,0,1456010414444],[89,0,1456010414508],[84,1,1456010414539],[89,1,1456010414587],[80,0,1456010414703],[80,1,1456010414799],[73,0,1456010414963],[78,0,1456010415063],[73,1,1456010415126],[78,1,1456010415182],[71,0,1456010415205],[71,1,1456010415332],[69,0,1456010415801],[69,1,1456010415892],[88,0,1456010416026],[88,1,1456010416125],[69,0,1456010416266],[82,0,1456010416350],[69,1,1456010416433],[82,1,1456010416461],[67,0,1456010416609],[67,1,1456010416684],[73,0,1456010416689],[67,0,1456010416777],[73,1,1456010416784],[67,1,1456010416900],[69,0,1456010416936],[69,1,1456010417027],[83,0,1456010417490],[83,1,1456010417593],[83,0,1456010419669],[83,1,1456010419756],[69,0,1456010419834],[69,1,1456010419941],[73,0,1456010420333],[83,0,1456010420406],[73,1,1456010420461],[83,1,1456010420497],[65,0,1456010420631],[65,1,1456010420759],[83,0,1456010420838],[83,1,1456010420950],[84,0,1456010421070],[84,1,1456010421133],[82,0,1456010421220],[82,1,1456010421324],[65,0,1456010421401],[78,0,1456010421510],[65,1,1456010421545],[71,0,1456010421602],[78,1,1456010421609],[69,0,1456010421702],[71,1,1456010421741],[69,1,1456010421853],[74,0,1456010422162],[74,1,1456010422261],[85,0,1456010422311],[85,1,1456010422415],[77,0,1456010422457],[66,0,1456010422545],[77,1,1456010422552],[66,1,1456010422652],[76,0,1456010422656],[76,1,1456010422760],[69,0,1456010422779],[69,1,1456010422912],[79,0,1456010423361],[79,1,1456010423460],[70,0,1456010423569],[70,1,1456010423649],[65,0,1456010423819],[65,1,1456010423954],[75,0,1456010424045],[75,1,1456010424160],[87,0,1456010424198],[87,1,1456010424310],[65,0,1456010424388],[65,1,1456010424532],[82,0,1456010424614],[82,1,1456010424722],[68,0,1456010424819],[68,1,1456010424926],[80,0,1456010425556],[80,1,1456010425667],[72,0,1456010425788],[82,0,1456010425856],[72,1,1456010425883],[82,1,1456010425943],[65,0,1456010426024],[83,0,1456010426120],[65,1,1456010426163],[83,1,1456010426235],[69,0,1456010426311],[69,1,1456010426406],[83,0,1456010426471],[188,0,1456010426567],[83,1,1456010426634],[188,1,1456010426706],[82,0,1456010427221],[82,1,1456010427312],[69,0,1456010427391],[80,0,1456010427439],[69,1,1456010427482],[80,1,1456010427546],[82,0,1456010427550],[82,1,1456010427630],[69,0,1456010427694],[69,1,1456010427797],[83,0,1456010427919],[83,1,1456010427994],[69,0,1456010428081],[69,1,1456010428177],[78,0,1456010428186],[78,1,1456010428281],[84,0,1456010428294],[84,1,1456010428397],[73,0,1456010428401],[78,0,1456010428490],[73,1,1456010428557],[71,0,1456010428578],[78,1,1456010428597],[71,1,1456010428717],[84,0,1456010428834],[72,0,1456010428901],[84,1,1456010428929],[72,1,1456010429025],[69,0,1456010429041],[69,1,1456010429165],[81,0,1456010429392],[85,0,1456010429496],[81,1,1456010429535],[73,0,1456010429544],[85,1,1456010429611],[73,1,1456010429663],[84,0,1456010429734],[84,1,1456010429817],[69,0,1456010429910],[69,1,1456010430005],[83,0,1456010430121],[83,1,1456010430176],[83,0,1456010430259],[83,1,1456010430354],[69,0,1456010430422],[78,0,1456010430486],[69,1,1456010430537],[67,0,1456010430586],[78,1,1456010430593],[69,0,1456010430682],[67,1,1456010430733],[69,1,1456010430829],[79,0,1456010430964],[70,0,1456010431079],[79,1,1456010431082],[70,1,1456010431187],[69,0,1456010431377],[69,1,1456010431465],[88,0,1456010431617],[88,1,1456010431708],[81,0,1456010431874],[85,0,1456010431942],[81,1,1456010431997],[73,0,1456010432006],[85,1,1456010432057],[73,1,1456010432089],[83,0,1456010432114],[73,0,1456010432194],[83,1,1456010432229],[73,1,1456010432289],[84,0,1456010432349],[84,1,1456010432424],[69,0,1456010432512],[69,1,1456010432640],[68,0,1456010432756],[73,0,1456010432848],[68,1,1456010432854],[73,1,1456010432959],[83,0,1456010432986],[83,1,1456010433093],[71,0,1456010434948],[82,0,1456010435056],[71,1,1456010435115],[82,1,1456010435191],[65,0,1456010435323],[65,1,1456010435474],[80,0,1456010435483],[80,1,1456010435593],[72,0,1456010435680],[83,0,1456010435760],[72,1,1456010435799],[83,1,1456010435919],[68,0,1456010436392],[73,0,1456010436480],[68,1,1456010436503],[73,1,1456010436587],[67,0,1456010436596],[67,1,1456010436707],[84,0,1456010436809],[84,1,1456010436877],[65,0,1456010436998],[84,0,1456010437158],[65,1,1456010437169],[69,0,1456010437262],[84,1,1456010437321],[69,1,1456010437405],[83,0,1456010437502],[83,1,1456010437653],[68,0,1456010437978],[68,1,1456010438114],[66,0,1456010438987],[89,0,1456010439107],[66,1,1456010439118],[89,1,1456010439238],[65,0,1456010439288],[65,1,1456010439471],[70,0,1456010440002],[79,0,1456010440070],[70,1,1456010440101],[79,1,1456010440193],[82,0,1456010440213],[82,1,1456010440309],[69,0,1456010440368],[73,0,1456010440428],[69,1,1456010440503],[78,0,1456010440528],[73,1,1456010440587],[78,1,1456010440659],[77,0,1456010441514],[73,0,1456010441599],[68,0,1456010441667],[77,1,1456010441678],[73,1,1456010441718],[68,1,1456010441782],[71,0,1456010441900],[71,1,1456010441996],[69,0,1456010442030],[84,0,1456010442115],[69,1,1456010442182],[84,1,1456010442222],[190,0,1456010442508],[190,1,1456010442631]]}

        self.dp = DataProcessor(dict)

    def testNgrams(self):
        self.assertListEqual([ (1,2), (2,3), (3,4) ], self.dp.ngrams([1,2,3,4], 2))
        self.assertListEqual([ (1,2,3), (2,3,4), (3,4,5) ], self.dp.ngrams([1,2,3,4,5], 3))

    def testProcess(self):

        self.dp.preprocess()
        f = self.dp.process()


if __name__ == '__main__':
    unittest.main()
