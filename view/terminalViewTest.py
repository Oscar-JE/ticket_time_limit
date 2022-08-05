import unittest
from terminalView import View
import terminalView

class TestTicket(unittest.TestCase):
    @unittest.skip("onödigt construktorn gör inget specielt")
    def test_constructor(self):
        my_view = View()
        print(my_view)

    def compareTerminalLength(self,first,second):
        print("#"+first+"#")
        print("#"+second+"#")

    def test_VisuelInspectionAvSpacing(self):
        testNr1 = 100
        testNr2 = -320
        self.compareTerminalLength(str(testNr1), terminalView.spacingOfIntInteger(testNr1))
        self.compareTerminalLength(str(testNr2),terminalView.spacingOfIntInteger(testNr2))

    def test_draw(self):
        result = [1,-2,3,4]
        choosenIndex = 2
        my_view = View()
        my_view.draw(choosenIndex,result)



if __name__ == "__main__":
    unittest.main()
