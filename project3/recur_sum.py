def recur_sum(arr, start, end) -> sum:
    if(start > end):
        raise IndexError("Error! start is smaller than end.")
    elif(start < 0):
        raise IndexError("Error! start is smaller than zero.")
    elif(end > (len(arr)-1)):
        raise IndexError("Error! end is greater than array length.")
    elif start == end:
        sum = arr[start]
    else:  
        sum = arr[start] + recur_sum(arr, start + 1, end)
    return sum

arr = [1,2,3,4,5,6,7,8,9]
print(recur_sum(arr,0,9))