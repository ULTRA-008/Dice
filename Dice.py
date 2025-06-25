# The code below defines a simple dice rolling game where the user can roll two dice

import random

dice_drawings = {
    1: (
        "┌─────┐",
        "│  1  │",
        "│  ●  │",
        "│     │",
        "└─────┘"

    ),
    2: (
        "┌─────┐",
        "│  2  │",
        "│ ●   │",
        "│   ● │",
        "└─────┘"
    ),
    3: (
        "┌─────┐",
        "│  3  │",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘"
    ),
    4: (
        "┌─────┐",
        "│  4  │",
        "│ ● ● │",
        "│     │",
        "│ ● ● │",
        "└─────┘"
    ),
    5: (
        "┌─────┐",
        "│  5  │",
        "│ ● ● │",
        "│  ●  │",
        "│ ● ● │",
        "└─────┘"
    ),
    6: (
        "┌─────┐",
        "│  6  │",
        "│ ● ● │",
        "│ ● ● │",
        "│ ● ● │",
        "└─────┘"
    )
}

def roll_dice():
    roll = input("Roll the dice? (y/n): ")

    while roll.lower() == "y".lower():
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        print("dice rolled {} and {}".format(dice_1, dice_2))
        print("\n".join(dice_drawings[dice_1]))
        print("\n".join(dice_drawings[dice_2]))

        roll = input("Roll again? (y/n): ")

roll_dice()

