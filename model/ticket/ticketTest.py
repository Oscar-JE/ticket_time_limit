import unittest
from ticket import Ticket

class TestTicket(unittest.TestCase):
    def test_bla(self):
        myTicket = Ticket()
        myTicket._buisinesValue = 0
        larger = Ticket()
        larger._buisinesValue =10
        assert myTicket <= larger
        assert larger > myTicket


if __name__ == "__main__":
    unittest.main()
