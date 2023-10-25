def validate_dict(rules, dictionary):
    for key in dictionary:
        items = list(filter(lambda e: e[0] == key, rules))
        if items:
            prefix = items[0][1]
            middle = items[0][2]
            suffix = items[0][3]
            string = dictionary[key].split(" ")
            if not ((string[0] == prefix or prefix == "") and
                    (string[-1] == suffix or suffix == "") and
                    (middle in string[1:-1] or middle == "")):
                return False
        else:
            return False
    return True


print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                    {"key1": "come inside , it's too cold out", "key3": "this is not valid"}
                    ))
