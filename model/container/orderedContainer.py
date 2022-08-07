#ordered  Container


class OrderedContainer():
    """
    order elements in this container
    the demand on the element types are larger then operator ( '>')
    """

    def __init__(self, values = []):
        self._values = []
        self._orderedIndices = [] # order of the item according to > . largest at the end
        self.inputMany(values)

    def __len__(self):
        length = len(self._values)
        assert length == len(self._orderedIndices)
        return length

    def inputMany(self, values):
        for value in values:
            self.input(value)

    def input(self,value):
        self._inputOrder(value)
        self._values.append(value)

    def _inputOrder(self,value):
        positionInSizeOrder = self._findNrOfSmaler(value)
        #print("--- in _inputOrder ---")
        #print("printar sig själv")
        #print(self)
        #print("positionInSizeOrder = " + str(positionInSizeOrder))
        #print("len(self._orderedIndices) = " + str(len(self._orderedIndices)))
        self._orderedIndices.insert(positionInSizeOrder, len(self._orderedIndices))

    def _findNrOfSmaler(self,value): # den här lägger vi in lite test för
        nr_of_values_smaler = 0
        for val in self._values:
            if (val < value):
                nr_of_values_smaler += 1 # optimerar senare istället
        return nr_of_values_smaler

    def _incrementIndexesAbove(self,index):
        for  i , indexIt in enumerate(self._orderedIndices):
            if indexIt >= index:
                self._order[i] += 1

    def _indexOfLargestValue(self): # den är helt fel men den bordde vara rätt
        # dependent on the order of indexes
        return self._orderedIndices[-1]

    def _popIndexOfLargest(self):
        return self._orderedIndices.pop();

    def _decrementIndexLarger(self,index):
        for  i , indexIt in enumerate(self._orderedIndices):
            if indexIt >= index:
                self._order[i] -= 1

    def popLargest(self): # här sker det konstigheter
        index = self._popIndexOfLargest()
        value = self._values.pop(index)
        return value , index


    def orderRep(self):
        orderRep = ""
        for order in self._orderedIndices:
            orderRep += str(order) + " "
        return orderRep

    def valuesRep(self):
        valuesRep = ""
        for value in self._values:
            valuesRep += str(value) + " "
        return valuesRep

    def asUnorderedList(self):
        intList = []
        for value in self._values:
            intList.append(int(value))
        return intList


    def __str__(self):
        return "OrderIndices : " + self.orderRep() +"\n" + "Values: " + self.valuesRep()
