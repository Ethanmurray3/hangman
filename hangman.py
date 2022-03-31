import random

def hangman(word):
    wrong = 0
    stages = ["",
    "________      ",
    "|             ",
    "|       |     ",
    "|       O     ",
    "|      /|\    ",
    "|      / \    ",
    "|             ",
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n" * 5)
        msg = "Guess a letter "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        b = " ".join(board)
        print(f"Word: {b}")
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print(f"You lose! It was {word}.")

words = ['cat', 'hat', 'bat', 'girl', 'boy', 'car', 'mississippi']

hangman(random.choice(words))