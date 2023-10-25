def is_equal(dict1, dict2):
    if len(dict1) != len(dict2):
        return False
    for i in range(0, len(dict1)):
        if isinstance(dict1[i], (dict, list, tuple)):
            if not is_equal(dict1[i], dict2[i]):
                return False
        elif dict1[i] != dict2[i]:
            return False
    return True


print(is_equal({0: [1, 3, 4], 1: "A", 2: {0: "car"}}, {0: [1, 3, 4], 1: "A", 2: {0: "car"}}))

