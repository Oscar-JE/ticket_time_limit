import random

from ticket import Ticket
from ticket import ticketsCreate
from orderedContainer import OrderedContainer


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

    def calc(self):
        return 5
