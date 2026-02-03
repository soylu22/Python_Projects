
# clear


from gamedata import data
import random
from art import logo, vs
import os
import os

score = 0
game_on = True
account_b = random.choice(data)


def clear_screen():
    # Check if the operating system is Windows ('nt') or Unix-like ('posix')
    if os.name == 'nt':
        _ = os.system('cls')  # For Windows
    else:
        _ = os.system('clear')  # For Linux/macOS
def rand_acc(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

def check(guess, acc_a_follower, acc_b_follower):
    if acc_a_follower > acc_b_follower:
        return guess == "a"
    else:
        return guess == "b"

# logo
print(logo)

while game_on:
    clear_screen()
    # generate random names
    account_a = account_b
    account_b = random.choice(data)
    # make sure a and b are not the same
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {rand_acc(account_a)}")
    print(vs)
    print(f"Against B: {rand_acc(account_b)}")

    # ask for who has more followers
    guess = input("who do you think have the higher instagram follower A or B: ").lower()

    # compare
    # get follower count

    acc_a_follower = account_a["follower_count"]
    acc_b_follower = account_b["follower_count"]
    check_ans = check(guess, acc_a_follower, acc_b_follower)

    # if acc_a_follower > acc_b_follower and guess == "a" or acc_a_follower < acc_b_follower and guess == "b":
    #
    #     print(f"you are right, your score is {score}")
    # else:
    #     print("you are wrong")

    if check_ans:
        score += 1
        print(f"you are right, your score is {score}")
    else:
        game_on = False
        print(f"you are wrong you got {score} points")
