import random
x = 15
y = 15
density = 2
char = {
    "empty": ".",
    "obstacle": "o",
    "full": "x",
}

def create_map(x: int, y: int, density: int, nbr_map: int = 1, char: dict = {"empty": ".", "obstacle": "o", "full": "x",}):
    for i in range(nbr_map):
        with open(f"maps/map{i}", "w") as f:
            f.write(f"{y}{char['empty']}{char['obstacle']}{char['full']}\n")
            for i in range(y):
                for j in range(x):
                    if (random.randint(0, y) * 2 < density):
                        f.write(char['obstacle'])
                    else:
                        f.write(char['empty'])
                f.write("\n")