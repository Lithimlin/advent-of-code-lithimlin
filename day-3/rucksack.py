import numpy as np

def to_score(char_set):
    char = list(char_set)[0]
    if char.isupper():
        offset = 27-65 # A has score of 27 and ASCII Dec of 65
    else:
        offset = 1-97 # a has score of 1 and ASCII Dec of 97
    return offset + ord(char)


with open("input.txt", 'r') as file:
    content = file.read().strip()
    sacks = content.split('\n')
    compartment_sizes = [len(sack)//2 for sack in sacks]
    sacks = [[sack[:compartment_sizes[n]], sack[compartment_sizes[n]:]] for n, sack in enumerate(sacks)]

    duplicates = [set(sack[0]).intersection(sack[1]) for sack in sacks]
    scores = map(to_score, duplicates)
    print("Part one sum of priorities:",sum(scores))

    sacks = content.split('\n')
    grouped_sacks = np.array_split(np.array(sacks), len(sacks)//3)
    badges = [set(sack[0]).intersection(sack[1]).intersection(sack[2]) for sack in grouped_sacks]
    scores = map(to_score, badges)
    print("Part two sum of badge priorities:", sum(scores))