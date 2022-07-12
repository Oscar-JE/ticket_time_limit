
try: # trixad lösning för att kunna köra det varifrån jag vill
    from .ticket.ticket import ticketsCreate
    from .ticket.ticket import Ticket
    from .container.orderedContainer import OrderedContainer
    from .randomDraws import *
except:
    from ticket.ticket import ticketsCreate
    from ticket.ticket import Ticket
    from container.orderedContainer import OrderedContainer
    import randomDraws

class Model(object):
    """docstring forBasic."""
    maximumSprintTickets = 15
    teamsTicketCapacity = 6
    maximumNewTicketEachSprint = 3

    def __init__(self,values = []):
        tickets = ticketsCreate(values)                                # their buisinesValue from lowest to highest
        self.orderedContainer = OrderedContainer(tickets)

    def __str__(self):
        ticketsRep = "Tickets: " + self.orderedContainer.valuesRep()
        orderRep = "Order: " + self.orderedContainer.orderRep()
        return ticketsRep + "\n" + orderRep +"\n"

    def _generateNumberOfTicketsNextSprint(self):
        return uniformDistribution(Model.maximumNewTicketEachSprint)

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

    def pluckBestTicket(self):
        ticket , ticketIndex = self.orderedContainer.popLargest()
        return ticket , ticketIndex

    def pluckTicket(self):
        return self.pluckBestTicket()

    def sprint(self):
        ticketCompleted, _ = self.pluckTicket()
        newTickets = [] # fortsätt här nästa gång

    def convertToValueList(self):
        return self.orderedContainer.asUnorderedList() # ska returnera returen från ordered container


    def endCondition(self):
        return not len(self.orderedContainer)>0

    def calc(self):
        valueList = []
        choosenIndex = -1
        if (len(self.orderedContainer)):
            valueList = self.convertToValueList()
            _ , choosenIndex = self.pluckTicket()
        return  choosenIndex ,  valueList
