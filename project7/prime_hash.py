import math

def prime(N):
    N
    prime_list = []
    for k in range(2,N):
        s = math.floor(math.sqrt(k))
        if s*s == k: continue
        flag = True
        for i in range(2,s+1):
            if k%i == 0: 
                flag = False
                break
        if flag == True: 
            prime_list.append(k)
    return prime_list

def accumulative_sum(array, index):
    if index < len(array):
        sum_list = []
        sum_list.append(0)
        for i in range(index + 1):
            sum_list[0] += array[i]
        previousResult = accumulative_sum(array, index + 1)
        if previousResult is not None:
            sum_list += previousResult
        return sum_list
    else:
        return None

primeList= prime(100)
print(primeList)
sumList = accumulative_sum(primeList, 0)
print(sumList)

hashset=set()
for sum in sumList:
    sumhash = hash(sum)%100
    hashset.add(sumhash)
print(hashset)

hashList=list()
for sum in sumList:
    sumhash = hash(sum)%100
    hashList.append(sumhash)
print(hashList)

primeSumhashDict = dict()
for i in range(len(primeList)):
    sumhash = hash(sumList[i])%100
    if sumhash in primeSumhashDict:
        print("prime {}'s accumulative sum {}'s hash {} already existed.".format(primeList[i], sumList[i], sumhash))
    else:
        primeSumhashDict[sumhash] = primeList[i]
print(primeSumhashDict)

