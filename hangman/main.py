# import math
# def paint_calc(height, width, coverage):
#     area = height * width
#     num_of_cans = math.ceil(area / coverage)
#
#     print(f"you need {num_of_cans} amount of can")
# test_h = int(input("Height of the wall; "))
# test_w = int(input("Width of the wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, coverage=coverage)
# #
# def prime_check(number):
#      prime = True
#      for i in range(2, number-1):
#          if number % i == 0:
#              prime = False
#      if prime is True:
#          print("prime")
#      else:
#          print("not prime")
#
#
# n = int(input("check number"))
# prime_check(number = n)

# to encode we add the shift amount
# to decode we sub the shift amount
# we use ord() to convert the letter to number and add the shift number and conert it to character

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
direction= input("write decode to decrypt or encode to encrypt the message: ")
text = input("type yor message: ").lower()
shift = int(input("the shift number: "))
#
# def encrypt(user_text, number_shift):
#     cypher = ""
#     for message in user_text:
#         position = alphabets.index(message)
#         new_position = position + shift
#         new_message = alphabets[new_position]
#         cypher += new_message
#     print(f"the encoded text is {cypher}")
# # encrypt(user_text = text, number_shift = shift)
#
# def decrypt(user_text, number_shift):
#     cypher = ""
#     for message in user_text:
#         position = alphabets.index(message)
#         new_position = position - shift
#         new_message = alphabets[new_position]
#         cypher += new_message
#     print(f"the decoded text is {cypher}")
# # decrypt(user_text=text, number_shift=shift)
#
# if direction == "encode":
#     encrypt(user_text = text, number_shift = shift)
# elif direction == "decode":
#     decrypt(user_text=text, number_shift=shift)
# else:
#     print("Wrong direction, please enter the correct direction")

def both(user_text, number_shift, user_direction):
    cypher = ""
    for message in user_text:
        # leave characters not in alphabet unchanged (spaces, punctuation)
        if message not in alphabets[:26]:
            cypher += message
            continue

        position = alphabets.index(message)
        if user_direction == "encode":
            new_position = (position + number_shift) % 26
        elif user_direction == "decode":
            new_position = (position - number_shift) % 26
        else:
            print("Wrong direction, please enter 'encode' or 'decode'")
            return

        new_message = alphabets[new_position]
        cypher += new_message

    # print the final result once
    if user_direction == "encode":
        print(f"the encoded text is {cypher}")
    else:
        print(f"the decoded text is {cypher}")
both(user_text = text, number_shift = shift, user_direction= direction)