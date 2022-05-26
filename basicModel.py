
from ticket import Ticket
import random

def ticketWithValue(value):
    retTicket = Ticket()
    retTicket._buisinesValue= value
    return retTicket


def ticketsCreate(values):
    tickets = []
    for value in values:
        tickets.append(ticketWithValue(value))
    return tickets


class Model(object):
    """docstring forBasic."""
    maximumSprintTickets = 15
    teamsTicketCapacity = 6

    def __init__(self,values = []):
        tickets = ticketsCreate(values)                                # their buisinesValue from lowest to highest
        self.inputTickets(tickets)

    def __str__(self):
        ticketsRep = "Tickets: "
        orderRep = "Order: "
        for ticket in self._tickets:
            ticketsRep += str(ticket) + " "
        for index in self._ticketIndex:
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


    def calc(self):
        return 5
