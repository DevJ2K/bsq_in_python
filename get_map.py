def get_full_map(mapfile):
    with open(mapfile, "r") as f:
        map = f.read().splitlines()
    return (map)

def get_info_map(map):
    nbr_lines = ""
    authorized_char = ""
    for i in map[0]:
        if i in "0123456789":
            nbr_lines += i
        else:
            authorized_char += i
    dico = {
        "nbr_lines": int(nbr_lines),
        "empty": authorized_char[0],
        "obstacle": authorized_char[1],
        "full": authorized_char[2]
    }
    return (dico)

if __name__ == "__main__":
    map = get_full_map("map.txt")
    print(map)
    info_map = get_info_map(map)
    print(info_map)