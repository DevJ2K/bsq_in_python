import random
from pathlib import Path
x = 15
y = 15
density = 2
char = {
    "empty": ".",
    "obstacle": "o",
    "full": "x",
}

def create_map(x: int, y: int, density: int, char: dict = {"empty": ".", "obstacle": "o", "full": "x",}):
    num_map = 0
    cur_dir = Path.cwd()
    while (Path(f"{cur_dir}/maps/map{num_map}").is_file()):
        num_map += 1
    Path(f"{cur_dir}/maps/map{num_map}").touch()
    mapfile = f"maps/map{num_map}"
    with open(mapfile, "w") as f:
        f.write(f"{y}{char['empty']}{char['obstacle']}{char['full']}\n")
        for i in range(y):
            for j in range(x):
                if (random.randint(0, y) * 2 < density):
                    f.write(char['obstacle'])
                else:
                    f.write(char['empty'])
            f.write("\n")
    return (num_map)