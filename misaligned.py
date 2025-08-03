def get_color_code(major_color, minor_color):
    return (major_color*5 + minor_color + 1)

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{get_color_code(i,j)} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(get_color_code(0,1) == 2)
assert(get_color_code(1,3) == 9)
assert(get_color_code(2,4) == 15)
assert(get_color_code(3,0) == 16)
assert(get_color_code(4,2) == 23)
