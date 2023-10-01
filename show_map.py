from get_map import *

def show_map(map: list):
    info_map = get_info_map(map)
    for i in range(1, info_map["nbr_lines"] + 1):
        print(map[i])

def compare_map(map_list: list):
    info_map = get_info_map(map_list[0])
    for i in range(1, info_map["nbr_lines"] + 1):
        lines = "| "
        for map in map_list:
            lines += map[i]
            lines += " | "
        lines = lines[:-1]
        print(lines)


if __name__ == "__main__":
    map = get_full_map("map.txt")
    show_map(map)
    compare_map([map, map])