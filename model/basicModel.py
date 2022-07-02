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

    def chooseBestTicket(self):
        return orderedContainer.popLargest()

    def chosseTicket(self):
        return self.chooseBestTicket()

    def sprint(self):
        ticketCompleted = self.chosseTicket()
        newTickets = [] # fortsätt här nästa gång

    def calc2(self):
        valueList = self.convergeToValueList()
        choosenIndex = self.chosseTicket()

    def calc(self): # måste ta och skriva en vettig calc
        choosenIndex = 4  # här behöver vi tänka till lite
        valueList = [1,2,3,4,5] # kan vi får fram en funktion som gör detta smidigt?
        return choosenIndex, valueList
