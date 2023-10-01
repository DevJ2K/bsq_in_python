from get_map import *

def info_is_valid(info):
	nbr_lines = ""
	authorized_char = ""
	for i in info:
		if i in "0123456789":
			nbr_lines += i
		else:
			authorized_char += i
	try:
		dico = {
			"nbr_lines": int(nbr_lines),
			"empty": authorized_char[0],
			"obstacle": authorized_char[1],
			"full": authorized_char[2]
		}
		return True
	except:
		return False


def map_is_valid(map):
	if not info_is_valid(map[0]):
		return False

	info_map = get_info_map(map)
	if info_map["nbr_lines"] != len(map) - 1 or len(map) == 1:
		return False
	
	lines_length = len(map[1])
	for i in range(1, info_map["nbr_lines"] + 1):
		if len(map[i]) != lines_length:
			return False

	for line in map[1:]:
		for char in line:
			if char not in [info_map["empty"], info_map["obstacle"], info_map["full"]]:
				return False
	return True

if __name__ == "__main__":
	map = get_full_map("map.txt")
	print(map_is_valid(map))