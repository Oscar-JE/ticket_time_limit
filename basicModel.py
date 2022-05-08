
from ticket import Ticket
import random

class Model(object):
    """docstring forBasic."""
    maximumSprintTickets = 15
    teamsTicketCapacity = 6

    def __init__(self):
        self._tickets = []
        self._ticketIndex = [] # order of the tickets according to
                                # their buisinesValue from lowest to highest

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

    def _incrementIndexesAbove(self,index):
        for  i , indexIt in enumerate(self._ticketIndex):
            if indexIt >= index:
                self._ticketIndex[i] += 1

    def _findIndexOfTicket(self,ticket):
        nr_of_tickets_smaler = 0
        for index in self._ticketIndex:
            if self._tickets[index] > ticket : # controlls the order
                break
            else:
                nr_of_tickets_smaler+=1
        return nr_of_tickets_smaler

    def _inputOrder(self,ticket):
        index = self._findIndexOfTicket(ticket)
        self._incrementIndexesAbove(index)
        self._ticketIndex.insert(len(self._ticketIndex) ,index)

    def _inputTicket(self,ticket):
        self._inputOrder(ticket)
        self._tickets.append(ticket)

    def inputTickets(self, tickets):
        for ticket in tickets:
            self._inputTicket(ticket)

    def calc(self):
        return 5
