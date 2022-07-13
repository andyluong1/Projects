# Andy Luong 1525166
# Zylabs 2.19

lemon = int(input("Enter amount of lemon juice (in cups):\n"))
water = int(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
servings = int(input("How many servings does this make?\n"))
print()

print("Lemonade ingredients - yields", '{:.2f}'.format(servings), "servings")
print('{:.2f}'.format(lemon), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave), "cup(s) agave nectar")
print()

servings1 = int(input("How many servings would you like to make?\n"))
print()
lemon1 = 16
water1 = 128
agave1 = 20
gallon = 16

print("Lemonade ingredients - yields", '{:.2f}'.format(servings1), "servings")
print('{:.2f}'.format(lemon1), "cup(s) lemon juice")
print('{:.2f}'.format(water1), "cup(s) water")
print('{:.2f}'.format(agave1), "cup(s) agave nectar")
print()

print("Lemonade ingredients - yields", '{:.2f}'.format(servings1), "servings")

print('{:.2f}'.format(lemon1/gallon), "gallon(s) lemon juice")
print('{:.2f}'.format(water1/gallon), "gallon(s) water")
print('{:.2f}'.format(agave1/gallon), "gallon(s) agave nectar")