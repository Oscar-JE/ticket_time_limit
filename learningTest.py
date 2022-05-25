
def testListStringConversion():
    myList = [1,2,4,5]
    print(myList)

def testForLoopOfIndexList():
    indexes = []
    birbs = ["bird", "eagle"]
    for index in indexes:
        print("index = " + str(index))
        print(birbs[index])

def testEqualityBetweenLists():
    l1 = [1,2,3]
    l2 = [1,2,4]
    print(l1==l2)

def main():
    testEqualityBetweenLists()




if __name__ == "__main__":
    main()
