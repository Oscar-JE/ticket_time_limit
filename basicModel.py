
from ticket import Ticket
import random

class Model(object):
    """docstring forBasic."""
    maximumSprintTickets = 15
    teamsTicketCapacity = 6

    def __init__(self):
        self._tickets = []
        self._ticketIndexs = [] # order of the tickets according to
                                # their buisinesValue

    def __str__(self):
        ticketsRep = "Tickets: "
        orderRep = "Order: "
        for ticket in self._tickets:
            ticketsRep += str(ticket) + " "
        for index in self._ticketIndexs:
            orderRep += str(index) + " "
        return ticketsRep + "\n" + orderRep +"\n"

    def _generateNumberOfTicketsNextSprint(self):
        # warning random not state check
        return random.randrange(maximumSprintTickets)

    def _generateTickets(n):
        tickets = []
        for i in ragne(n):
            tickets.append(Ticket())
        return tickets

    # dela upp i mindre delar
    def _inputTicket(self,ticket):
        # start with stupid implementaton
        # assume already ordered lists (emplty list is regarded as sorted)
        for index in self._ticketIndexs:
            if ticket <= self._tickets[index]:
                self._ticketIndexs.insert(len(self._tickets),index)
                self._tickets.append(ticket)
                return
        self._ticketIndexs.append(len(self._tickets))
        self._tickets.append(ticket)

    def inputTickets(self, tickets):
        for ticket in tickets:
            self._inputTicket(ticket)

    def calc(self):
        return 5
