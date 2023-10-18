def who_cant_see(matrix):
    n = len(matrix)
    m = len(matrix[0])
    spec_list = []
    for j in range(0, m):
        for i in range(0, n - 1):
            for k in range(i + 1, n):
                if matrix[i][j] >= matrix[k][j]:
                    if not (k, j) in spec_list:
                        spec_list += [(k, j)]
    return spec_list


print(who_cant_see([[1, 2, 3, 2, 1, 1],
                    [2, 4, 4, 3, 7, 2],
                    [5, 5, 2, 5, 6, 4],
                    [6, 6, 7, 6, 7, 5]]))
