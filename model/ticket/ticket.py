import time
import random

def ticketWithValue(value):
    assert value >= 0
    retTicket = Ticket()
    retTicket._buisinesValue= value
    return retTicket


def ticketsCreate(values):
    tickets = []
    for value in values:
        tickets.append(ticketWithValue(value))
    return tickets


class Ticket(object):
    """ main data class """
    def __init__(self,buisinesValue=None):
        if buisinesValue is None:
            self._buisinesValue = random.randrange(-10,10)
        else:
            self._buisinesValue = buisinesValue

        self._creationTime = time.time() # behöver jag verkligen detta ?

    def __str__(self):
        return str(self._buisinesValue)

    def __int__(self):
        return self._buisinesValue

    def value(self):
        return _buisinesValue

    def time(self):
        return _creationTime

    # need the ability to compare tickets
    def __le__(self,otherTicket):
        return self._buisinesValue <= otherTicket._buisinesValue

    def __gt__(self,otherTicket):
        return self._buisinesValue > otherTicket._buisinesValue
