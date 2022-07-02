# main class presenter

from model.basicModel import Model
from view.terminalView import View

class Presenter():
    """docstring for Presenter. responsible for coordinating model and view"""
    def __init__(self):
        self.model = Model()
        self.view = View()

    def firstIteration(self):
        chossenIndex, ticketValues = self.model.calc()
        self.view.draw(chossenIndex, ticketValues)

def main():
  myPresenter = Presenter()
  myPresenter.firstIteration()


if __name__=="__main__":
  main();
