
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
        ticketsRep = "Tickets:" + str(self._tickets)
        orderRep = "Order:" + self._ticketIndexs
        return ticketsRep + "\n" + orderRep +"\n"

    def _generateNumberOfTicketsNextSprint(self):
        # warning random not state check
        return random.randrange(maximumSprintTickets)

    def _generateTickets(n):
        tickets = []
        for i in ragne(n):
            tickets.append(Ticket())
        return tickets

    def _inputTicket(self,ticket):
        # start with stupid implementaton
        # assume already ordered lists (emplty list is regarded as sorted)
        self._tickets.append(ticket)
        for index in _ticketIndexs:
            if ticket <= self._tickets[index]:
                self._ticketIndexs.insert(len(self._tickets),index)
                break

    def calc(self):
        return 5
