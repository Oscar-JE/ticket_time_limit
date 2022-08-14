# terminal view
def spacingOfIntInteger(integerToSpace):
    stringRep = str(integerToSpace)
    length = len(stringRep)
    spacing = ""
    for i in range(length):
        spacing += " "
    return spacing

class View(object,):
    """ Assumes that the value is sigle diget at the moment"""

    def visuilize(self,result): # ska bytas ut
        print(result)

    def choosenIndexRow(self, index , result):
        if len(result)>0:
            assert type(index) == int
            str = " " # initial [
            for i in range(index):
                str += spacingOfIntInteger(result[i])
                str+= " "*2 #, and spave
            if (result[index]<0):
                str += " "
            marker = "v"
            str += marker
            print(str)

    def draw(self, choosenIndex, result):
        print("---- restult ----")
        self.choosenIndexRow(choosenIndex,result)
        self.visuilize(result)
