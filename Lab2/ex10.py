def make_tuples(*input_lists):
    max_length_of_list = max([len(x) for x in input_lists])
    main_tuple = ()
    for i in range(0, max_length_of_list):
        current_tuple = ()
        for current_list in input_lists:
            if i < len(current_list):
                current_tuple += (current_list[i],)
            else:
                current_tuple += ("None",)
        main_tuple += (current_tuple,)
    return main_tuple


print(make_tuples([1, 2, 3], [5, 6, 7], ["a", "b", "c"], [11, 33], ["f"]))
