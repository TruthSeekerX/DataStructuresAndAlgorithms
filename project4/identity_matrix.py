def identity_matrix(size):
    matrix = list()
    for row in range(size):
        rows = list()
        for col in range (size):
            if row == col:
                rows.append(1)
            else:
                rows.append(0)
        matrix.append(rows)
    return matrix

print(identity_matrix(5))