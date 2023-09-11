def recur_pascal(triangel, n):
    if n == 1:
        row = [1]
        triangel.append(row)
        return row
    elif n == 2:
        recur_pascal(triangel, n-1)
        row = [1,2,1]
        triangel.append(row)
    elif n > 2:
        previousRow = recur_pascal(triangel,n-1)
        endIndex = len(previousRow) - 1
        row = [1]
        for index in range(1,len(previousRow)):
            row.append(previousRow[index-1]+previousRow[index])
        row.append(1)
        triangel.append(row)
    return row

triangel = []
recur_pascal(triangel, 10)
for row in triangel:
    print(row, end='\n')
