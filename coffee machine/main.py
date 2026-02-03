MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}


def change(total_money, cost):
    mels = total_money - cost
    print(f"Here is {mels} birr in change.")



def check_resources(order, resources):
    """Returns True when order can be made,
    False if ingredients are insufficient."""
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


resources = {"water":300, "milk": 200, "coffee": 100}


order = input("What would you like? (espresso/latte/cappuccino):")
print("please insert coins: ")
tens = input("how many 10 birrs: ")
ones = input("how many 5 birrs: ")
total_money = int(tens) * 10 + int(ones) * 5

hisab = MENU[order]["cost"]
if total_money >= hisab:
    change(total_money, hisab)
else:
    print("Sorry, not enough money. Refunding…")

