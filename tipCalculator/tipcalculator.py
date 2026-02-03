#print Welcome to the tip calculator.
#input what was the total bill?
    #totBill
#input what percentage tip would you like to give? 10, 12 or 15?
    #if 10... totBill * 10 / 100
    #if 12... totBill * 12 / 100
    #if 15... totBill * 15 / 100
    #result
#input how many people to split the bill?
    #ppl
    # pay = result / ppl
#give result Each person should pay:
    #pay

print("Welcome to the tip calculator")
totBill = input("what was the total bill?")
percent = int(input("what percentage tip would you like to give? 10, 12 or 15?"))
if percent == 10:
    result = int(totBill) * 10 / 100
elif percent == 12:
    result = int(totBill) * 12 / 100
elif percent == 15:
    result = int(totBill) * 15 / 100
ppl = input("how many people to split the bill?")
pay = ( int(totBill) + int(result) ) / int(ppl)
final = f"Each person should pay: {pay}"
print(final)
