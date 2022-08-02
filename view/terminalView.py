# terminal view
import os

def clearConsole():
    rows = os.get_terminal_size()[1]
    for i in range(rows-2):
        print()

class View(object,):
    """ Assumes that the value is sigle diget at the moment"""

    def visuilize(self,result): # ska bytas ut
        print(result)

    def choosenIndexRow(self, index , result):
        assert type(index) == int
        str = " "
        for i in range(index):
            str += "   "
            str += (result[index]<0)* " "
        marker = "v"
        str += marker
        print(str)

    def draw(self, choosenIndex, result):
        print("---- restult ----")
        self.choosenIndexRow(choosenIndex,result)
        self.visuilize(result)
