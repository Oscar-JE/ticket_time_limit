#ordered  Container


class OrderedContainer():
    """
    order elements in this container
    the demand on the element types are larger then operator ( '>')
    """

    def __init__(self, values = []):
        self._values = []
        self._order = [] # order of the item according to > . largest at the end
        self.inputMany(values)

    def _inputOrder(self,value):
        index = self._findIndexOfValue(value)
        self._incrementIndexesAbove(index)
        self._order.insert(len(self._order) ,index)

    def input(self,value):
        self._inputOrder(value)
        self._values.append(value)

    def inputMany(self, values):
        for value in values:
            self.input(value)

    # fortsätter här senare
    def _findIndexOfValue(self,value):
        nr_of_values_smaler = 0
        for index in self._order:
            if self._values[index] > value : # controlls the order
                break
            else:
                nr_of_values_smaler+=1
        return nr_of_values_smaler

    def _incrementIndexesAbove(self,index):
        for  i , indexIt in enumerate(self._order):
            if indexIt >= index:
                self._order[i] += 1


    def indexOfLargestTicket(self):
        # dependent on the order of indexes
        return self._order[-1]
