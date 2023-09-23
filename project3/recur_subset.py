def recur_subset(set, subsetLength):
    superSet = list()
    if len(set) == subsetLength:
        subset = list()
        superSet += recur_subset(set, subsetLength-1)
        superSet.append(set)
        return superSet
    elif subsetLength == 0:
        superSet.append(list())
        return superSet
    elif subsetLength == 1:
        subset = list()
        superSet += recur_subset(set, subsetLength-1)
        for i in range(len(set)):
            superSet.append([set[i]])
        return superSet
    elif subsetLength < len(set):
        superSet += recur_subset(set, subsetLength - 1)
        for index in range((len(set) - subsetLength) - 1):
            for eachSubset in superSet:
                subset = list()
                subset = [set[index]] + eachSubset
                superSet.append(subset)
        return superSet

mySet = [1,2,3]
print(recur_subset(mySet, 3))