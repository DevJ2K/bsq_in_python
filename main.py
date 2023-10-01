from get_map import *
from show_map import *
from find_bsq import *

mapfile = "map.txt"
map = get_full_map(mapfile)
info_map = get_info_map(map)
x = 1
y = 1
l = 4
if is_valid_square(map, x, y, l):
    map_replace = replace_by_square(map, x, y, l)
else:
    map_replace = map
compare_map([map, map_replace])