def pascal_recursion(triangel, n, k):
    if n == 1:
        row = [1]
        triangel.append(row)
    elif n == 2:
        pascal_recursion(triangel, n-1, k)
        row = [1,1]
        triangel.append(row)
    elif n > 2:
        previousRow = pascal_recursion(triangel,n-1, k)
        endIndex = len(previousRow) - 1
        row = [1]
        for index in range(1,len(previousRow)):
            row.append(previousRow[index-1]+previousRow[index])
        row.append(1)
        triangel.append(row)
    if k <= n: print(row)
    return row

triangel = []
pascal_recursion(triangel, 10, 3)
# for row in triangel:
#     print(row, end='\n')
