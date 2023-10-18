def group_by_rhyme(words):
    groups = []
    for word in words:
        last2_chr = word[-2] + word[-1]
        found = False

        for i in range(0, len(groups)):
            if groups[i][0] == last2_chr:
                groups[i][1].append(word)
                found = True

        if not found:
            groups.append([last2_chr, [word]])

    return groups


print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
