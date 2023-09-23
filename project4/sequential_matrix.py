def sequential_matirx(size):
    counter = 1
    matrix = list()
    for r in range(size):
        row = list()
        for c in range(size):
            row.append(counter)
            counter += 1
        matrix.append(row)
    return matrix

print(sequential_matirx(5))