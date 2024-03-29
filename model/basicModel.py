
try: # trixad lösning för att kunna köra det varifrån jag vill
    from .ticket.ticket import ticketsCreate
    from .ticket.ticket import Ticket
    from .container.orderedContainer import OrderedContainer
    from .randomDraws import *
except:
    from ticket.ticket import ticketsCreate
    from ticket.ticket import Ticket
    from container.orderedContainer import OrderedContainer
    from .randomDraws import *

class Model(object):
    """docstring forBasic."""
    maxbacklogLength = 5
    maximumNewTicketEachSprint = 10

    def __init__(self,values = []):
        tickets = ticketsCreate(values)                                # their buisinesValue from lowest to highest
        self.orderedContainer = OrderedContainer(tickets)
        self.currentIteration = 0
        self.completedValue = 0

    def getBuissenesValue(self):
        return self.completedValue

    def __str__(self):
        ticketsRep = "Tickets: " + self.orderedContainer.valuesRep()
        orderRep =   "Order  : " + self.orderedContainer.orderRep()
        return ticketsRep + "\n" + orderRep +"\n"

    def _generateNumberOfTicketsNextSprint(self):
        return uniform(Model.maximumNewTicketEachSprint)

    def _generateTickets(self,n):
        tickets = []
        for i in range(n):
            tickets.append(Ticket())
        return tickets

    def prepateNextGeneration(self):
        nrNextGen = self._generateNumberOfTicketsNextSprint()
        nextGenTickets = self._generateTickets(nrNextGen)
        for ticket in nextGenTickets:
            self.orderedContainer.input(ticket)
            if (len(self.orderedContainer)>self.maxbacklogLength):
                self.orderedContainer.pop()

    def pluckBestTicket(self):
        ticket , ticketIndex = self.orderedContainer.popLargest()
        return ticket , ticketIndex

    def pluckRandndom(self):
        length = len(self.orderedContainer)
        index = uniform(length)
        return self.orderedContainer.pop(index) , index

    def pluckTicket(self):
        return self.pluckBestTicket()
        #return self.pluckRandndom()

    def convertToValueList(self):
        return self.orderedContainer.asUnorderedList() # ska returnera returen från ordered container

    def calc(self):
        valueList = []
        choosenIndex = -1
        if (len(self.orderedContainer)):
            valueList = self.convertToValueList()
            ticket , choosenIndex = self.pluckTicket()
            self.completedValue += ticket.value()

        return  choosenIndex ,  valueList

    def endCondition(self):
        return self.nrIterations()

    def nrIterations(self):
        self.currentIteration += 1
        return self.currentIteration>= 150
