import unittest
from orderedContainer import OrderedContainer


class TestBasicModel(unittest.TestCase):

    def testInputIndex(self):
        values = [3,-1]
        myContainer = OrderedContainer(values)
        index = myContainer._findIndexOfValue(2)
        self.assertEqual(index, 1)

    def testInputOrder(self):
        values = [1,0,-3]
        myContainer = OrderedContainer(values)
        self.assertEqual(myContainer._order, [2,1,0])

    def testInputTickets(self):
        values = [3,2,10,9]
        myContainer = OrderedContainer(values)
        self.assertEqual(myContainer._indexOfLargestValue(),2)

    def testPopLargest(self):
        values = [1,3,2,4]
        myContainer = OrderedContainer(values)
        #print(myContainer)
        poped1, _ = myContainer.popLargest()
        poped2, _ = myContainer.popLargest()
        poped3, _ = myContainer.popLargest()
        #print(myContainer)
        self.assertEqual(4, poped1)
        self.assertEqual(3,poped2)
        self.assertEqual(2,poped3)

    @unittest.skip("skipped due to print")
    def testStrRep(self):
        values = [7, 1]
        myContainer = OrderedContainer(values)
        print()
        print(myContainer)


if __name__ == "__main__":
    unittest.main()
