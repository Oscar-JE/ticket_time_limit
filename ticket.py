import time
import random

class Ticket(object):
    """ main data class """
    def __init__(self,buisinesValue=None):
        if buisinesValue is None:
            self._buisinesValue = random.randrange(-10,10)
        else:
            self._buisinesValue = buisinesValue
            
    def __str__(self):
        return str(self._buisinesValue)

    def value(self):
        return _buisinesValue

    def time(self):
        return _creationTime

    # need the ability to compare tickets
    def __le__(self,otherTicket):
        return self._buisinesValue <= otherTicket._buisinesValue

    def __gt__(self,otherTicket):
        return self._buisinesValue > otherTicket._buisinesValue
