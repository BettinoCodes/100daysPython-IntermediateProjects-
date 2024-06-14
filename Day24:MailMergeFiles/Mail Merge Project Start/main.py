# #TODO: Create a letter using starting_letter.txt
# #for each name in invited_names.txt
# #Replace the [name] placeholder with the actual name.
# #Save the letters in the folder "ReadyToSend".
#
# #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
#
# def replace_skips(str_letter):
#     skips = 0
#     for i in range(len(str_letter)):
#         if str_letter[i] == "[":
#             start = i
#             while str_letter[start] != ',':
#                 skips += 1
#                 start += 1
#             i = start
#     return skips
#
#
# def replace_name1(list_names, str_let):
#     new_s = ''
#     skip = 0
#     for l in range(len(list_names)):
#         name = list_names[l]
#         for i in range(len(str_let)):
#             if skip > 0:
#                 skip -= 1
#                 continue
#             else:
#                 if str_let[i] == "[":
#                     new_s += name
#                     start = i
#                     while str_let[start] != ']':
#                         start += 1
#                         skip += 1
#                 else:
#                     new_s += str_let[i]
#     return new_s
#
place_holder = "[name]"

with open("Input/Names/invited_names.txt") as file_names:
    names = file_names.readlines()

# print(names)

with open("Input/Letters/starting_letter.txt") as letter:
    letter_str = letter.read()
    for name in names:
        new_name = name.strip()
        new_lett = letter_str.replace(place_holder, new_name)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as the_letter:
            the_letter.write(new_lett)

# print(letter_str)
# skips = replace_skips(letter_str)
#
# new_string = replace_name(list_of_names, letter_str)
# print(new_string)

