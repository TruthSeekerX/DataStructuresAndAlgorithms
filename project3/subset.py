def subsetCalculator(setInput)->[]:
    setLength = len(setInput)
    setTotalNumber = 2 ** setLength
    subsetCollection = list()
    for setNumber in range(0, setTotalNumber):
        subset = list()
        index = setLength - 1
        while setNumber > 0:
            if (setNumber & 0x01):
                subset.append(setInput[index])
            setNumber = setNumber >> 1
            index -= 1
        subsetCollection.append(subset)
    return subsetCollection

if __name__ == "__main__":
    mySet = [1,2,3,4]
    print(subsetCalculator(mySet))