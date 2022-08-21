import unittest
from orderedContainer import OrderedContainer


class TestBasicModel(unittest.TestCase):

    def testInputOrder(self):
        values = [1,0,-3]
        myContainer = OrderedContainer(values)
        self.assertEqual(myContainer._orderedIndices, [2,1,0])

    def testInputTickets(self):
        values = [3,2,10,9]
        myContainer = OrderedContainer(values)
        self.assertEqual(myContainer._indexOfLargestValue(),2)

    def testPopLargest(self):
        values = [1,3,2,4]
        myContainer = OrderedContainer(values)
        poped1, _ = myContainer.popLargest()
        poped2, _ = myContainer.popLargest()
        poped3, _ = myContainer.popLargest()
        self.assertEqual(4, poped1)
        self.assertEqual(3,poped2)
        self.assertEqual(2,poped3)

    def testPop(self):
        values = [0,1,2,3,4,5,6,7]
        myContainer = OrderedContainer(values)
        value = myContainer.pop(2)
        self.assertEqual(value,2)
        self.assertEqual(myContainer._values[2],3)

    def testPopLargest(self):
        values = [0,1,2,3,50,4,5,6,7]
        myContainer = OrderedContainer(values)
        print(myContainer)
        value , index = myContainer.popLargest()
        self.assertEqual(value , 50)
        self.assertEqual(index, 4)
        print(myContainer)


    @unittest.skip("skipped due to print")
    def testStrRep(self):
        values = [7, 1]
        myContainer = OrderedContainer(values)
        print()
        print(myContainer)


if __name__ == "__main__":
    unittest.main()
