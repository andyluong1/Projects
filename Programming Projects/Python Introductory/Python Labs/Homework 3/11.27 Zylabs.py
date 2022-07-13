# Andy Luong 1525166
# Zylabs 11.27

team = {}
x = 1
for i in range(5):
    jersey = int(input("Enter player " + str(x) + "'s jersey number:\n"))
    rating = int(input("Enter player " + str(x) + "'s rating:\n"))
    print()
    if (0 <= jersey <= 99) and (1 <= rating <= 9):
        team.update({jersey:rating})
        x += 1

print("ROSTER")
for key in sorted(team.keys()):
    print("Jersey number: " + str(key) + "," + " Rating: " + str(team[key]))

print()

def output():
    for key in sorted(team):
        print("Jersey number: " + str(key) + "," + " Rating: " + str(team[key]))
    print()

def add():
    jersey = int(input("Enter a new player's jersey number:\n"))
    rating = int(input("Enter the player's rating:\n"))
    if (0 <= jersey <= 99) and (1 <= rating <= 9):
        team.update({jersey:rating})

def delete():
    jersey = int(input("Enter a jersey number:\n"))
    del team[jersey]

def update():
    jersey = int(input("Enter a jersey number:\n"))
    rating = int(input("Enter a new rating for player:\n"))
    team[jersey] = rating

def above():
    rating = int(input("Enter a rating:\n"))
    print("ABOVE " + str(rating))
    for ratings in sorted(team.keys()):
        if team[ratings] > rating: #key in dictionary
            print("Jersey number: " + str(ratings) + ", Rating: " + str(team[ratings]))
    print()

menu = ("MENU\n"
    "a - Add player\n"
    "d - Remove player\n"
    "u - Update player rating\n"
    "r - Output players above a rating\n"
    "o - Output roster\n"
    "q - Quit\n")

command = ''
while command != "q":
    print(menu)
    command = input("Choose an option:\n")
    if command == "a":
        add()
    elif command == "d":
        delete()
    elif command == "u":
        update()
    elif command == "r":
        above()
    elif command == "o":
        output()