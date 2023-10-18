def compose(notes, moves, start):
    song = []
    song += [notes[start]]
    for i in moves:
        start = start + i
        song += [notes[start]]
    return song


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, -3], 2))
