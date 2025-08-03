# function generate a six digit character random_user_id
import random
def generate_user_id():
    return ''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyz', k=6))
print(generate_user_id())
print("\n")
#
def user_id_gen_by_user():
    num_characters = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    for _ in range(num_ids):
        user_id = ''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyz', k=num_characters))
        print(user_id)
user_id_gen_by_user()
print("\n")
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"
rgb_color_gen = rgb_color_gen()
print(rgb_color_gen)
print("\n")
#
def list_of_hex_colors():
    hex_colors = []
    for _ in range(5):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        hex_colors.append(hex_color)
    return hex_colors
hex_colors = list_of_hex_colors()
print(hex_colors)
print("\n")
#
def list_of_rgb_colors():
    rgb_colors = []
    for _ in range(5):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_color = f"rgb({r}, {g}, {b})"
        rgb_colors.append(rgb_color)
    return rgb_colors
rgb_colors = list_of_rgb_colors()
print(rgb_colors)
print("\n")
#
def generate_colors(color_type, num):
    colors = []
    if color_type == 'hexa':
        for _ in range(num):
            hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
            colors.append(hex_color)
    elif color_type == 'rgb':
        for _ in range(num):
            r, g, b = random.randint(0,255), random.randint(0,255), random.randint(0,255)
            colors.append(f'rgb({r},{g},{b})')
    else:
        return "Invalid color type. Use 'hexa' or 'rgb'."
    return colors
print(generate_colors('hexa', 3))
print("\n")
#
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled
print(shuffle_list([1, 2, 3, 4, 5]))
print("\n")
#
def generate_unique_random():
    return random.sample(range(10), 7)
print(generate_unique_random())
