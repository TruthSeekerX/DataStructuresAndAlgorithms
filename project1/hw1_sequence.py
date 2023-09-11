def sequenceGenerator(N):
    list = []
    while N > 1:
        list.append(N)
        N = N//2 if N%2==0 else 3*N+1
    list.append(1)
    return list

def sequenceLength(N):
    return len(sequenceGenerator(N))

sequenceLengthList = []
for i in range (1, 101):
    sequenceLengthList.append(sequenceLength(i))
longestTerm = max(sequenceLengthList)
print(sequenceLengthList)
print(longestTerm)
print(sequenceLengthList.index(longestTerm) + 1)