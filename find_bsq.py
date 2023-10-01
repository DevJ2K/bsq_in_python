from get_map import *
from show_map import *

def is_valid_square(map: list, x: int, y: int, l: int):
	info_map = get_info_map(map)
	map = map[1:]
	for i in range(x, x + l):
		for j in range(y, y + l):
			if map[j][i] == info_map["obstacle"]:
				return False
	return True

def replace_by_square(map: list, x: int, y: int, l: int):
	info_map = get_info_map(map)
	map_copy = map[1:]
	for i in range(y, y + l):
		line_length = len(map[i + 1])
		map_copy[i] = map_copy[i][:x] + info_map["full"] * l + map_copy[i][l + x:]
	map = [map[0]]
	for line in map_copy:
		map.append(line)
	return map

def algorithm_to_find(map: list):
	info_map = get_info_map(map)
	map_copy = map[1:]
	line_length = len(map_copy[0])
	x = 0
	y = 0
	l = 0
	for line in range(info_map["nbr_lines"]):
		for column in range(line_length):
			try:
				while (is_valid_square(map, column, line, l)):
					x = column
					y = line
					l += 1
			except:
				pass
				#print("erreur")

	return ({"x": x, "y": y, "l": l - 1})

if __name__ == "__main__":
	map = get_full_map("map.txt")
	x = 0
	y = 0
	l = 5
	show_map(map)
	answer = algorithm_to_find(map)
	print(answer)
	map_replace = replace_by_square(map, answer["x"], answer["y"], answer["l"])
	compare_map([map, map_replace])
	# if is_valid_square(map, x, y, l):
	# 	map_replace = replace_by_square(map, x, y, l)
	# else:
	# 	map_replace = map
	# compare_map([map, map_replace])