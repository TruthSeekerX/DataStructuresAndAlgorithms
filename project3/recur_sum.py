def recur_sum(arr, start, end) -> sum:
    if(start > end):
        raise IndexError("Error! start is smaller than end.")
    elif(start < 0):
        raise IndexError("Error! start is smaller than zero.")
    elif end > (len(arr)):
        raise IndexError("Error! end is greater than array length.")
    elif start == (end - 1):
        sum = arr[start]
    else:  
        sum = arr[start] + recur_sum(arr, start + 1, end)
    return sum

arr = [3,4,5,6,7]
print(recur_sum(arr,0,5))