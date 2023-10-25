def ex6(list_param):
    a = set(list_param)
    copy_list = list_param.copy()
    for i in range(0, len(list_param)):
        if list_param[i] in a:
            copy_list.remove(list_param[i])
            a.remove(list_param[i])

    # in copy_list we have the duplicates
    duplicates = set(copy_list)
    a = set(list_param)
    uniques = a - duplicates
    value = ()
    value += len(uniques),
    value += len(duplicates),
    return value


print(ex6([1, 1, 3, 3, 1, 2, 4, 4]))
