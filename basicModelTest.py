import unittest
from basicModel import Model
from ticket import Ticket

def ticketWithValue(value):
    retTicket = Ticket()
    retTicket._buisinesValue= value
    return retTicket

def ticketsCreate(values):
    tickets = []
    for value in values:
        tickets.append(ticketWithValue(value))
    return tickets

class TestBasicModel(unittest.TestCase):
    def testInputIndex(self):
        values = [3,-1]
        tickets = ticketsCreate(values)
        myModel = Model()
        myModel.inputTickets(tickets)
        print("------- after input Ticket")
        testTicket = Ticket()
        testTicket._buisinesValue = 2.5
        print(myModel)
        index = myModel._findIndexOfTicket(testTicket)
        self.assertEqual(index, 1)

    def testInputOrder(self):
        values = [1,0,-3]
        tickets = ticketsCreate(values)
        myModel = Model()
        for ticket in tickets:
            myModel._inputTicket(ticket)
            print(myModel)

    def testInputTickets(self):
        values = [3,2,10,9]
        tickets = ticketsCreate(values)
        myModel = Model()
        myModel.inputTickets(tickets)
        print(myModel)




if __name__ == "__main__":
    unittest.main()
