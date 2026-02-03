# treasure hunting
print("welcome to treasure hunting.\n your mission is to find the treasure.")
direction = input("you are at a cross road. where do you want to go? type 'left' or 'right' \n").lower()
if direction == "left":
    print("you come to a lake. there is an island in the middle of the lake. type 'wait' to wait for a boat. type 'swim' to swim across.")
    lake = input().lower()
    if lake == "wait":
        print("you arrive at the island unharmed. there is a house with 3 doors. one red, one yellow and one blue. which color do you choose?")
        unharmed = input().lower()

        if unharmed == "yellow":
            print("YOU WIN!")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")
#print()