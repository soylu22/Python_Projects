from art import logo
import random
import os
print(logo)
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, comp_score):
    if user_score > 21 and comp_score > 21:
        return "You went over. You lose"
    # draw
    if user_score == comp_score :
        return "Draw"
    # comp blacjack
    if comp_score == 0:
        return "you LOSE, comp got blackjack"
    # user blackjack
    if user_score == 0:
        return "you WIN, you got a blackjack"
    # over 21
    if user_score > 21:
        return "you LOSE, you went over"
    # comp over 21
    if comp_score > 21:
        return "you WIN, comp went over"
    # user > comp_score
    if user_score > comp_score:
        return "YOU WIN"
    else:
        return "YOU LOSE"

def play_game():

    user_cards = []
    comp_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not game_over:
        user_score = calc_score(user_cards)
        comp_score = calc_score(comp_cards)
        print(f"your cards {user_cards}, current score {user_score}")
        print(f"computer first card {comp_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_agree_to_cont = input("You want to add another card? Type y to yes and n to no: ")
            if user_agree_to_cont == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calc_score(comp_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))


while input("Do you want to play? Type 'y' or 'n': ") == "y":
    clear()
    play_game()