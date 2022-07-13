# Andy Luong 1525166
# Zylabs 3.18

height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))
area = height * width
gallon = 350
cans = round(area/gallon)

print("Wall area:", area, "square feet")
print("Paint needed:", "{:.2f}".format(area / gallon), "gallons")
print("Cans needed:", cans, "can(s)")
print()

colors = {"red": 35, "blue": 25, "green": 23}

color = input("Choose a color to paint the wall:\n")
print("Cost of purchasing " + color + " paint: $"+str(colors[color]*cans))