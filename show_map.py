import random
from get_map import *
import typer

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

def compare_map_with_highlight(unresolved_map, solved_map, colors):
    all_colors = ["bright_black", "black", "bright_red", "red", "bright_green", 
                  "green", "bright_yellow", "yellow", "bright_blue", "blue", 
                  "bright_magenta", "magenta", "bright_cyan", "cyan", "bright_white", "white",]
    info_map = get_info_map(unresolved_map)
    for i in range(1, info_map["nbr_lines"] + 1):
        lines = "| "
        lines += unresolved_map[i]
        # print(lines, end="-")
        start = 0
        start_found = False
        end = len(solved_map[i])
        end_found = False
        for j in range(len(solved_map[i])):
            if solved_map[i][j] == info_map["full"] and start_found == False:
                start = j
                start_found = True
            elif solved_map[i][j] != info_map["full"] and start_found == True and end_found == False:
                end = j
                end_found = True
        if start_found == True:
            # RANDOM COLORS
            # highlight_square = typer.style(info_map["full"] * (end - start), fg=random.choice(all_colors))
            # STATIC COLOR
            highlight_square = typer.style(info_map["full"] * (end - start), fg=all_colors[colors - 1])

            typer.echo(f"{lines} | {solved_map[i][:start]}{highlight_square}{solved_map[i][end:]} |")
        else:
            print(f"{lines} | {solved_map[i]} |")
    
def show_highlight_square(map: list):
    all_colors = ["black", "red", "green", "yellow", "blue","magenta", "cyan", "white",
              "bright_black", "bright_red", "bright_green", "bright_yellow",
              "bright_blue", "bright_magenta", "bright_cyan", "bright_white"]
    info_map = get_info_map(map)
    for line in map[1:]:
        start = 0
        start_found = False
        end = len(line) - 1
        end_found = False
        for i in range(len(line)):
            if line[i] == info_map["full"] and start_found == False:
                start = i
                start_found = True
            elif line[i] != info_map["full"] and start_found == True and end_found == False:
                end = i
                end_found = True
        if start_found == True:
            # RANDOM COLORS
            # highlight_square = typer.style(info_map["full"] * (end - start), fg=random.choice(all_colors))
            # STATIC COLOR
            highlight_square = typer.style(info_map["full"] * (end - start), fg=typer.colors.BRIGHT_MAGENTA)

            typer.echo(f"{line[:start]}{highlight_square}{line[end:]}")
        else:
            print(line)

if __name__ == "__main__":
    map = get_full_map("map.txt")
    show_map(map)
    compare_map([map, map])