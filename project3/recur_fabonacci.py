def fabonacci(n)->[]:
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    elif n > 2:
        row = fabonacci(n-1)
        length = len(row)
        row.append(row[length-2] + row[length-1])
        return row

print(fabonacci(10))