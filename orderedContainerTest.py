import unittest
from orderedContainer import OrderedContainer


class TestBasicModel(unittest.TestCase):

    #@unittest.skip("Ska skrivas om så att utskrifter inte sker")
    def testInputIndex(self):
        values = [3,-1]
        myContainer = OrderedContainer(values)
        index = myContainer._findIndexOfValue(2)
        self.assertEqual(index, 1)

    def testInputOrder(self):
        values = [1,0,-3]
        myContainer = OrderedContainer(values)
        self.assertEqual(myModel.getOrdering(), [2,1,0])

    def testInputTickets(self):
        values = [3,2,10,9]
        myContainer = OrderedContainer(values)
        self.assertEqual(myModel.indexOfLargestTicket(),2)





if __name__ == "__main__":
    unittest.main()
