
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
    gen_print_str = []
    for code,major,minor in color_map:
        code_padded = code.ljust(code_max)
        major_padded = major.ljust(major_max)
        minor_padded = minor.ljust(minor_max)
        gen_print_str.append (code_padded +' | ' + major_padded + ' | ' +minor_padded)
    for line in gen_print_str:
        print (f'{line}')
    return (gen_print_str)

(c_max, maj_max, min_max, gen_map) = generate_color_map()
generated_str = print_color_map(c_max, maj_max, min_max, gen_map)

#Asserts for color code
assert(get_color_code(0,1) == 2)
assert(get_color_code(1,3) == 9)
assert(get_color_code(2,4) == 15)
assert(get_color_code(3,0) == 16)
assert(get_color_code(4,2) == 23)

#Asserts for '|'
#Always string position 3 an 12 are |
assert(generated_str[0][3] == '|')
assert(generated_str[7][3] == '|')
assert(generated_str[13][12] == '|')
assert(generated_str[24][3] == '|')
assert(generated_str[17][12] == '|')

