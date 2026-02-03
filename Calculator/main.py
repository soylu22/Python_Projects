
# add
def add(n1, n2):
    return n1 + n2
# sub
def sub(n1,n2):
    return n1 - n2
# multi
def multi(n1,n2):
    return n1 * n2
# div
def div(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : multi,
    "/" : div
}
num1 = float(input("enter the first number "))
for i in operations:
    print(i)
opp = input("pick operation from the line above ")
num2 = float(input("enter the second number "))

opps = operations[opp]
answer = opps(num1, num2)
print(f"{num1} {opp} {num2} = {answer}")



