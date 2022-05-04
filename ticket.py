import time
import random

class Ticket(object):
    """ main data class """
    def __init__(self):
        self._buisinesValue = random.randrange(-10,10)

    def value(self):
        return _buisinesValue

    def time(self):
        return _creationTime

    # need the ability to compare tickets
    def __le__(self,otherTicket):
        return self._buisinesValue<= otherTicket._buisinesValue

    def __gt__(self,ottherTicket):
        return self._buisinesValue > otherTicket._buisinesValue
