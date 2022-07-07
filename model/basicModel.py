import random

try: # trixad lösning för att kunna köra det varifrån jag vill
    from .ticket.ticket import ticketsCreate
    from .container.orderedContainer import OrderedContainer
except:
    from ticket.ticket import ticketsCreate
    from container.orderedContainer import OrderedContainer


class Model(object):
    """docstring forBasic."""
    maximumSprintTickets = 15
    teamsTicketCapacity = 6

    def __init__(self,values = []):
        tickets = ticketsCreate(values)                                # their buisinesValue from lowest to highest
        self.orderedContainer = OrderedContainer(tickets)

    def __str__(self):
        ticketsRep = "Tickets: " + self.orderedContainer.valuesRep()
        orderRep = "Order: " + self.orderedContainer.orderRep()
        return ticketsRep + "\n" + orderRep +"\n"

    def _generateNumberOfTicketsNextSprint(self):
        return random.randrange(maximumSprintTickets)

    def _generateTickets(n):
        tickets = []
        for i in ragne(n):
            tickets.append(Ticket())
        return tickets

    def _appendTicket(ticket):
        pass

    def prepateNextGeneration(self):
        pass

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
