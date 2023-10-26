def ex1(a, b):
    a = set(a)
    b = set(b)
    union = a | b
    intersection = a & b
    difference_a_b = a - b
    difference_b_a = b - a
    s = []
    s += [union]
    s += [intersection]
    s += [difference_a_b]
    s += [difference_b_a]
    return s


print(ex1([1, 2, 3, 4], [3, 4, 5, 6]))
