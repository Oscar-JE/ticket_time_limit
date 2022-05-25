import unittest
from basicModel import Model
from ticket import Ticket


class TestBasicModel(unittest.TestCase):

    #@unittest.skip("Ska skrivas om så att utskrifter inte sker")
    def testInputIndex(self):
        values = [3,-1]
        myModel = Model(values)
        testTicket = Ticket(1)
        index = myModel._findIndexOfTicket(testTicket)
        self.assertEqual(index, 1)

    def testInputOrder(self):
        values = [1,0,-3]
        myModel = Model(values)
        self.assertEqual(myModel.getOrdering(), [2,1,0])

    @unittest.skip("Ska skrivas om eller tas bort")
    def testInputTickets(self):
        values = [3,2,10,9]
        tickets = ticketsCreate(values)
        myModel = Model()
        myModel.inputTickets(tickets)
        print(myModel)
        print("index of largest ticket")
        print(myModel.indexOfLargestTicket())

    #def testPopTicket(self):





if __name__ == "__main__":
    unittest.main()
