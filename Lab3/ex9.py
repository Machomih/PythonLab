def ex9(*positional_arguments, **keyword_arguments):
    count = 0
    for key in keyword_arguments:
        if keyword_arguments[key] in positional_arguments:
            count += 1

    return count


print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
