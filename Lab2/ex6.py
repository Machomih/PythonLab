def make_list_based_on_x(*lists, x):
    freq = {}
    new_list = []
    for i in lists:
        for j in i:
            if j in freq:
                freq[j] += 1
            else:
                freq[j] = 1
    for key, value in freq.items():
        if value == x:
            new_list += [key]
    return new_list


print(make_list_based_on_x([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 5, "test"], x=2))
