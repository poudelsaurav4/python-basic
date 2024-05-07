import random

characters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol_list  = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+', '|', '\\', '/', '?']
upper_char = [letter.upper() for letter in characters_list]
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

allChar_list = characters_list+upper_char+nums
char_one = random.choice(characters_list)
sym_one = random.choice(symbol_list)
upp_one = random.choice(upper_char)
num_one = random.choice(nums)

length_pw = int(input("Enter the number of chars you want in you passowrd: "))
pw = ''
random_pw = pw.join(random.choice(allChar_list) for _ in range(length_pw-4))

main_pw = char_one + random_pw + sym_one + upp_one + num_one

print(main_pw)
