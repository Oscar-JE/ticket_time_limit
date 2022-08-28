# main class presenter

from model.basicModel import Model
from view.terminalView import View
from logger.logger import SingleLogger
from logger.logger import DistLogger
# behöver detta vara en class över huvud taget ?
class Presenter():
    """docstring for Presenter. responsible for coordinating model and view"""
    def __init__(self):

        self.model = self.newModel()
        self.view = View()
        self.businessValueLogger = SingleLogger()
        #self.ticketValudsDistLogger = DistLogger()

    def present(self):
        while True:
            chossenIndex, ticketValues = self.model.calc()
            self.view.draw(chossenIndex, ticketValues)
            if(self.model.endCondition()):
                buisinesValue = self.model.getBuissenesValue()
                self.businessValueLogger.log(buisinesValue)
                break
            self.model.prepateNextGeneration()


    def newModel(self):
        return Model([9,9,9,9,9])

    def resetModel(self):
        self.model = self.newModel()

    def logResult(self,businessSum,valuesSample):
        self.businessValLogger.update(businessSum)

def main():
  myPresenter = Presenter()
  myPresenter.present()
  bValue = myPresenter.businessValueLogger.getMean()
  print("acumulated buisinesvalue = "+ str(bValue))

if __name__=="__main__":
  main();
