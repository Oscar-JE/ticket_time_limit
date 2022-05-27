#ordered  Container


class OrderedContainer():
    """
    order elements in this container
    the demand on the element types are larger then operator ( '>')
    """

    def __init__(self, values = []):
        self._values = []
        self._order = [] # order of the item according to > . largest at the end
        self._totalValue = 0
        self.inputMany(values)


    def _inputOrder(self,value):
        index = self._findIndexOfValue(value)
        self._incrementIndexesAbove(index)
        self._order.insert(len(self._order) ,index)

    def input(self,value): # skulle vilja ha en begränsning på att value ska vara större lika med 0
        self._inputOrder(value)
        self._values.append(value)
        self._totalValue += value

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


    def indexOfLargestValue(self):
        # dependent on the order of indexes
        return self._order[-1]

    def orderRep(self):
        orderRep = ""
        for order in self._order:
            orderRep += str(order) + " "
        return orderRep

    def valuesRep(self):
        valuesRep = ""
        for value in self._values:
            valuesRep += str(value) + " "
        return valuesRep

    def __str__(self):
        return "Order: " + self.orderRep() +"\n" + "Values: " + self.valuesRep()
