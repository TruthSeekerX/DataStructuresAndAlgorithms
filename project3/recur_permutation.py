import copy
def permutation(list, index, length)->{}:
    permutationCollection = []
    if index == (length - 1):
        return [list]
    elif index < (length - 1):
        for i in range(index, length):
            list[index], list[i] = list[i], list[index]
            permutationCollection += (permutation(copy.deepcopy(list), index + 1, length))
        return permutationCollection

myset = [1,2,3]
print(permutation(myset,0,3))
