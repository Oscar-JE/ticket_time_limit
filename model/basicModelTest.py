import unittest
from basicModel import Model


class TestBasicModel(unittest.TestCase):

    #@unittest.skip("Skippad pga utskriften")
    def testStrRep(self):
        values = [3, 1]
        myModel = Model(values)
        print()
        print(myModel)







if __name__ == "__main__":
    unittest.main()
