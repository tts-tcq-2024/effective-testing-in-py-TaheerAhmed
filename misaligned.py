def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append(f'{i * 5 + j} | {major} | {minor}')
    return color_map

def print_color_map():
    color_map = generate_color_map()
    for entry in color_map:
        print(entry)
    return len(color_map)

result = print_color_map()
assert(result == 25)

# Enhanced test for alignment and content
color_map = generate_color_map()
assert(color_map[0] == '0 | White | Blue')
assert(color_map[24] == '24 | Violet | Slate')
assert(len(color_map) == 25)

print("All is well (maybe!)\n")
