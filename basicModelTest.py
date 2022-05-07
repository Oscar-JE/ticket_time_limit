import unittest
from basicModel import Model
from ticket import Ticket

def ticketWithValue(value):
    retTicket = Ticket()
    retTicket._buisinesValue= value
    return retTicket


class TestBasicModel(unittest.TestCase):
    def testInputTickets(self):
        values = [3,2,10,9]
        tickets = []
        for value in values:
            tickets.append(ticketWithValue(value))
        myModel = Model()
        myModel.inputTickets(tickets)
        print(myModel)

    def testToString(self):
        myModel = Model()
        print("To string test")
        print(myModel)





if __name__ == "__main__":
    unittest.main()
