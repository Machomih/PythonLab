def make_dictionary(word):
    dictionary = {}
    for i in range(0, len(word)):
        if word[i] in dictionary:
            dictionary[word[i]] += 1
        else:
            dictionary[word[i]] = 1
    return dictionary


print(make_dictionary("Ana has apples."))
