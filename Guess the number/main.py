from art import logo
print(logo)
import random
# # what difficulty?
# def set_difficulty():
#     level = input("do you want easy or hard?")
#     if level == "easy":
#        return 10
#     else:
#        return 5
# # now we let the user guess the number
# def the_guess(guess, guessed):
#     if guess > guessed:
#         return "you are too high"
#     elif guess < guessed:
#         return "you are too low"
#     elif guess == guessed:
#         return "you got the number"
# # we have to let the comp guess a number
# def game():
#     print("welcome!")
#     guessed = random.randint(1,100)
#     attempt = set_difficulty()
#     guess = 0
#     while guess != guessed:
#         print(f"you have {attempt} attempts left")
#         guess = int(input("guess the number: "))
#
#         check_the_guess(guess, guessed):
#         if guess != guessed:
#             attempt -= 1
#             if attempt == 0:
#                 print("youre finished")
#                 return
#             else:
#                 print("guess agin")
#
print("Welcome to 'Guess The Number'!")
print("I'm thinking of a number between 1 and 100.")
def set_difficulty():
    level = input("you want easy or hard?")
    if level == "easy":
        return 10
    else:
        return 5

def check_answer(guess, number):
    if guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    else:
        print("you got it")
def start_game():
    answer = random.randint(1, 100)
    attempts = set_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            return
        elif guess > answer:
            print("Too high.")
        else:
            print("Too low.")

        attempts -= 1
        if attempts == 0:
            print(f"You've run out of guesses. The number was {answer}.")
        else:
            print("Guess again.")


if __name__ == "__main__":
    start_game()



