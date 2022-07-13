# Andy Luong 1525166
# Zylabs 7.25

def exact_change(user_total):
    if user_total <= 0:
        print("no change")
    else:
        num_dollars = user_total // 100
        user_total %= 100
        num_quarters = user_total // 25
        user_total %= 25
        num_dimes = user_total // 10
        user_total %= 10
        num_nickels = user_total // 5
        user_total %= 5
        num_pennies = user_total // 1
        user_total %= 1

        if num_dollars > 1:
            print(str(num_dollars) + " dollars")
        elif num_dollars == 1:
            print(str(num_dollars) + " dollar")
        if num_quarters > 1:
            print(str(num_quarters) + " quarters")
        elif num_quarters == 1:
            print(str(num_quarters) + " quarter")
        if num_dimes > 1:
            print(str(num_dimes) + " dimes")
        elif num_dimes == 1:
            print(str(num_dimes) + " dime")
        if num_nickels > 1:
            print(str(num_quarters) + " nickels")
        elif num_nickels == 1:
            print(str(num_nickels) + " nickel")
        if num_pennies > 1:
            print(str(num_pennies) + " pennies")
        elif num_pennies == 1:
            print(str(num_pennies) + " penny")


inputval = 0
if inputval == 0:
    exact_change(int(input()))
else:
    exact_change(inputval)