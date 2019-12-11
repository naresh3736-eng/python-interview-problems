def matrix_transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        result.append([row[i] for row in matrix])

    return result

