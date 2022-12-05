DECRYPTION = {
    "A": "rock",
    "B": "paper",
    "C": "scissor",
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

POINTS = {
    "win": 6,
    "draw": 3,
    "lose": 0,
}

OUTCOMES = {
    "rock": {
        "win": 2,
        "draw": 1,
        "lose": 3,
    },
    "paper": {
        "win": 3,
        "draw": 2,
        "lose": 1,
    },
    "scissor": {
        "win": 1,
        "draw": 3,
        "lose": 2,
    },
}

with open("input.txt", 'r') as file:
    content = file.read().strip()
    rounds = content.split("\n")
    rounds = [[DECRYPTION[hand] for hand in r.split()] for r in rounds]

    my_outcomes = [POINTS[r[1]] for r in rounds]
    my_hands = [OUTCOMES[r[0]][r[1]] for r in rounds]

    print("Total amount of my points:", sum(my_hands) + sum(my_outcomes))