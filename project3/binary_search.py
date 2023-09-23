def binary_search(data, target, low, high):
    if low>high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

d =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
ind = binary_search(d, 1, 0, 15)
print(ind)
