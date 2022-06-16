import unittest
from terminalView import View

class TestTicket(unittest.TestCase):
    def test_constructor(self):
        my_view = View()
        print(my_view)


if __name__ == "__main__":
    unittest.main()
