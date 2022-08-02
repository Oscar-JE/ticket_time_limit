# main class presenter

from model.basicModel import Model
from view.terminalView import View

class Presenter():
    """docstring for Presenter. responsible for coordinating model and view"""
    def __init__(self):

        self.model = Model([9,9,9,9,9])
        self.view = View()

    def present(self):
        while True:
            chossenIndex, ticketValues = self.model.calc()
            self.view.draw(chossenIndex, ticketValues)
            if(self.model.endCondition()):
                break
            self.model.prepateNextGeneration()

def main():
  myPresenter = Presenter()
  myPresenter.present()


if __name__=="__main__":
  main();
