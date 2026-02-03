"""Simple blind bidding script.

Collects names and numeric bids from users until no more bidders,
then prints the highest bidder and their amount.
"""

def main():
    bids = {}
    while True:
        name = input("What is your name? ").strip()
        if not name:
            print("Name cannot be empty. Try again.")
            continue

        try:
            bid_input = input("How much do you want to bid? ").strip()
            bid = float(bid_input)
        except ValueError:
            print("Please enter a valid number for the bid.")
            continue

        bids[name] = bid

        other = input("Is there any other person? (yes/no) ").strip().lower()
        if other in ("no", "n"):
            break
        elif other in ("yes", "y"):
            continue
        else:
            print("Unrecognized answer, assuming no more bidders.")
            break

    if not bids:
        print("No bids were placed.")
        return

    winner, amount = max(bids.items(), key=lambda item: item[1])
    if amount.is_integer():
        amount_to_print = int(amount)
    else:
        amount_to_print = amount

    print(f"{winner} bids the highest: {amount_to_print}")


if __name__ == "__main__":
    main()