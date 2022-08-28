# vad vill vi logga ?
# genomsnittliga fördelningen av det som finns i backloggen efter
# att modelen har gjort sin grej

class DistLogger(object):
    def __init__(self,maxbacklogLength):
        self._distribution= []
        for _i in range(maxbacklogLength):
            self._distribution.append(SingleLogger())

    def update(self,valueArray):
        for index , value in enumerate(valueArray):
            self._distribution[index].update(value)

    def getDistribution(self):
        retArray = []
        for logger in self._distribution:
            retArray.append(logger.getMean())
        return retArray

class SingleLogger(object):
    def __init__(self):
        self._meanValue = 0
        self._nrSampled = 0

    def log(self, value):
        self._meanValue = (self._meanValue * self._nrSampled + value) / (self._nrSampled + 1)
        self._nrSampled += 1

    def getMean(self):
        return self._meanValue
