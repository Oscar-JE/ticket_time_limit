# main class presenter

from basicModel import Basic as Model
from terminalView import View

class Presenter():
    """docstring for Presenter. responsible for coordinating model and view"""
    def __init__(self):
        self.model = Model()
        self.view = View()

    def firstIteration(self):
        result = self.model.calc()
        self.view.visuilize(result)

def main():
  myPresenter = Presenter()
  myPresenter.firstIteration()


if __name__=="__main__":
  main();
