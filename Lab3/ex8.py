def loop(mapped):
    visited = []
    object_list = []
    current = mapped["start"]
    object_list += current
    visited += current
    second_loop = False

    while not second_loop:
        current = mapped[current]
        if current in visited:
            second_loop = True
        else:
            visited += current
            object_list += current

    return object_list


print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
