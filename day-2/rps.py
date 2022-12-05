DECRYPTION = {
    "A": "rock",
    "B": "paper",
    "C": "scissor",
    "X": "rock",
    "Y": "paper",
    "Z": "scissor",
}

POINTS = {
    "rock": 1,
    "paper": 2,
    "scissor": 3,
}

OUTCOMES = {
    "rock": {
        "rock": 3,
        "paper": 6,
        "scissor": 0,
    },
    "paper": {
        "rock": 0,
        "paper": 3,
        "scissor": 6,
    },
    "scissor": {
        "rock": 6,
        "paper": 0,
        "scissor": 3,
    },
}

with open("input.txt", 'r') as file:
    content = file.read().strip()
    rounds = content.split("\n")
    rounds = [[DECRYPTION[hand] for hand in r.split()] for r in rounds]

    my_hands = [POINTS[r[1]] for r in rounds]
    my_outcomes = [OUTCOMES[r[0]][r[1]] for r in rounds]

    print("Total amount of my points:", sum(my_hands) + sum(my_outcomes))