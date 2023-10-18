def sort_tuples(tuples):
    sorted_tuples = sorted(tuples, key=lambda t: (t[1][2]))
    return sorted_tuples


print(sort_tuples([('abc', 'bcd'), ('abc', 'zza'), ('ab', 'zzz'), ('iil', 'zzb')]))
