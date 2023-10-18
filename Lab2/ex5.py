def change_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i > j:
                matrix[i][j] = 0
    return matrix


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 1, 2, 3],
          [4, 5, 6, 7]]
print(change_matrix(matrix))
