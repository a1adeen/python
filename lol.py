import math



colors = ["\033[31m", "\033[33m", "\033[32m", "\033[34m", "\033[36m", "\033[35m"]



tree_height = 10

trunk_height = 3

trunk_width = 3



for row in range(tree_height):

    for col in range(tree_height - row):

        print(" ", end="")

    for col in range(row * 2 + 1):

        level = math.floor((tree_height - row - 1) / 2)

        color = colors[level % len(colors)]

        print(color + "*", end="")

    print()




for row in range(trunk_height):

    for col in range(tree_height - trunk_width // 2):

        print(" ", end="")

    for col in range(trunk_width):

        print("\033[33m" + "#", end="")

    print()