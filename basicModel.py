
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
        tickets = ticketsCreate(values)
        self._tickets = []
        self._ticketIndex = [] # order of the tickets according to
                                # their buisinesValue from lowest to highest
        self.inputTickets(tickets)

    def getOrdering(self): # kommer endast användas för test .Detta är väl dåligt
        return self._ticketIndex

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

    def indexOfLargestTicket(self):
        # dependent on the order of indexes
        return self._ticketIndex[-1]

    def popTicket(self,index):
        # släng ut ticket och uppdater index listan
        ticket = self._tickets.pop(index)

        # uppdatera index listan
        # tag bort index som relaterar till det elementet som togs bort
        #self._ticketIndex.del(index)
        # index mindre än det angivna är oförändrade
        # mappning som object kanske skulle göra saken lättare

        return ticket

    def calc(self):
        return 5
