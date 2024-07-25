def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            entry = f'{i * 5 + j:2} | {major:<6} | {minor:<6}'
            color_map.append(entry)
            print(entry)
    return len(color_map)

# Original test
result = print_color_map()
assert(result == 25)

# Enhanced test for alignment and content
color_map = [
    ' 0 | White  | Blue  ',
    ' 1 | White  | Orange',
    ' 2 | White  | Green ',
    ' 3 | White  | Brown ',
    ' 4 | White  | Slate ',
    ' 5 | Red    | Blue  ',
    ' 6 | Red    | Orange',
    ' 7 | Red    | Green ',
    ' 8 | Red    | Brown ',
    ' 9 | Red    | Slate ',
    '10 | Black  | Blue  ',
    '11 | Black  | Orange',
    '12 | Black  | Green ',
    '13 | Black  | Brown ',
    '14 | Black  | Slate ',
    '15 | Yellow | Blue  ',
    '16 | Yellow | Orange',
    '17 | Yellow | Green ',
    '18 | Yellow | Brown ',
    '19 | Yellow | Slate ',
    '20 | Violet | Blue  ',
    '21 | Violet | Orange',
    '22 | Violet | Green ',
    '23 | Violet | Brown ',
    '24 | Violet | Slate '
]

# Check if the output matches the expected format
output = [f'{i:2} | {major:<6} | {minor:<6}' for i, major in enumerate(["White", "Red", "Black", "Yellow", "Violet"]) for minor in ["Blue", "Orange", "Green", "Brown", "Slate"]]
assert output == color_map, "The color map output is misaligned or incorrect."

print("All is well (maybe!)\n")
