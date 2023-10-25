def make_operations(a, b):
    return [set(a).intersection(b), set(a + b), set(a).difference(b), set(b).difference(a)]


print(make_operations([1, 2, 3, 4, 5], [2, 4, 4, 6, 7, 8]))
