import unittest
from basicModel import Model


class TestBasicModel(unittest.TestCase):

    #@unittest.skip("Skippad pga utskriften")
    def testStrRep(self):
        values = [3, 1]
        myModel = Model(values)
        print()
        print(myModel)

    def test_Calc(self):
        values = [1,2,3,4,50,6,7,8,9]
        myModel = Model(values)
        print("testar ordning och stuff")
        print(myModel)
        index , _ = myModel.calc()
        print("index = " + str(index))
        assert index == 4





if __name__ == "__main__":
    unittest.main()
