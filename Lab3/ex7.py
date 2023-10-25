def ex7(*sets):
    dictionary = {}
    for i in sets:
        for j in sets:
            string = str(i) + " | " + str(j)
            dictionary[string] = i | j
            string = str(i) + " & " + str(j)
            dictionary[string] = i & j
            string = str(i) + " - " + str(j)
            dictionary[string] = i - j
            string = str(j) + " - " + str(i)
            dictionary[string] = j - i
    return dictionary


print(ex7({1,2}, {2, 3}))
