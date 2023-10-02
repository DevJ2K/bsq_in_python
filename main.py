from get_map import *
from show_map import *
from is_valid import *
from find_bsq import *
from create_map import *

# nbr_de_map = int(input("Combien de maps souhaitez-vous générer ? :"))
x = 13
y = 13
d = 1
create_map(x, y, d)
mapfile = "map"
map = get_full_map(mapfile)
if (map_is_valid(map)):
    info_map = get_info_map(map)
    answer = algorithm_to_find(map)
    map_replace = replace_by_square(map, answer["x"], answer["y"], answer["l"])
    # compare_map([map, map_replace])
    show_highlight_square(map_replace)
    print(answer)
else:
    print("map error")