def ascii_list(x, string_list, flag):
    main_list = []
    for string in string_list:
        aux_list = []
        for i in range(0, len(string)):
            if ord(string[i]) % x == 0 and flag:
                aux_list += [string[i]]
            elif ord(string[i]) % x != 0 and not flag:
                aux_list += [string[i]]
        main_list += [aux_list]
    return main_list


print(ascii_list(2, ["test", "hello", "lab002"], True))
