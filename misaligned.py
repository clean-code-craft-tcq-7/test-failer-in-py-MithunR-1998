
def get_color_code(major_color, minor_color):
    return (major_color*5 + minor_color + 1)

def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append((str(get_color_code(i,j)),major,minor))
    
    #Get max length
    major_max = max(len(i) for i in major_colors)
    minor_max = max(len(j) for j in minor_colors)
    code_max = max(len(k) for k,l,m in color_map)
    #print(code_max)
    #print(color_map)
    #print(major_max,minor_max)
    return code_max, major_max, minor_max, color_map

def print_color_map(code_max, major_max, minor_max, color_map):
    for code,major,minor in color_map:
        code_padded = code.ljust(code_max)
        major_padded = major.ljust(major_max)
        minor_padded = minor.ljust(minor_max)
        print (f'{code_padded} | {major_padded} | {minor_padded}')

(c_max, maj_max, min_max, gen_map) = generate_color_map()
print_color_map(c_max, maj_max, min_max, gen_map)
#result = print_color_map()
assert(get_color_code(0,1) == 2)
assert(get_color_code(1,3) == 9)
assert(get_color_code(2,4) == 15)
assert(get_color_code(3,0) == 16)
assert(get_color_code(4,2) == 23)
