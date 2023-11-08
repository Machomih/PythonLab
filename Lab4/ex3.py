class Matrix:
    def __init__(self, n, m, initial_value=0):
        if n <= 0 or m <= 0:
            raise ValueError("Matrix dimensions must be greater than 0")
        self.n = n
        self.m = m
        self.data = [[initial_value for _ in range(m)] for _ in range(n)]

    def get_element(self, i, j):
        self._check_bounds(i, j)
        return self.data[i][j]

    def set_element(self, i, j, value):
        self._check_bounds(i, j)
        self.data[i][j] = value

    def _check_bounds(self, i, j):
        if i < 0 or i >= self.n or j < 0 or j >= self.m:
            raise IndexError("Index out of bounds")

    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed.set_element(j, i, self.get_element(i, j))
        return transposed

    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("Incompatible dimensions for matrix multiplication")

        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                sum_product = 0
                for k in range(self.m):
                    sum_product += self.get_element(i, k) * other.get_element(k, j)
                result.set_element(i, j, sum_product)
        return result

    def apply(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.data[i][j] = func(self.get_element(i, j))

    def __iter__(self):
        for row in self.data:
            for element in row:
                yield element

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


matrix = Matrix(3, 2)

matrix.set_element(0, 0, 0)
matrix.set_element(0, 1, 1)
matrix.set_element(1, 0, 2)
matrix.set_element(1, 1, 3)
matrix.set_element(2, 0, 4)
matrix.set_element(2, 1, 5)

print(matrix.get_element(0, 1))
print()

transposed_matrix = matrix.transpose()
print("Original matrix:")
print(matrix)
print()

print("Transposed matrix:")
print(transposed_matrix)
print()

matrix2 = Matrix(2, 3)
matrix2.set_element(0, 0, 1)
matrix2.set_element(1, 1, 1)

product_matrix = matrix.multiply(matrix2)
print("Multiplied matrix:")
print(product_matrix)
print()

matrix.apply(lambda x: x + 1)
print("Transformation matrix:")
print(matrix)
print()
