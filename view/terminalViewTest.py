import unittest
from terminalView import View
import terminalView

class TestTicket(unittest.TestCase):
    @unittest.skip("onödigt construktorn gör inget specielt")
    def test_constructor(self):
        my_view = View()
        print(my_view)

    def test_clearConsole(self):
        print("clearConsole first line -----------------------")
        terminalView.clearConsole()
        print("second line ----------------------")

    def test_draw(self):
        result = [1,2,3,4]
        choosenIndex = 1
        my_view = View()
        my_view.draw(choosenIndex,result)



if __name__ == "__main__":
    unittest.main()
