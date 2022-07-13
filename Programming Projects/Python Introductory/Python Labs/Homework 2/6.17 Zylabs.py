# Andy Luong 1525166
# Zylabs 6.17

password = input()
store = ""

for letter in password:
    if letter == "i":
        store += "!"
    elif letter == "a":
        store += "@"
    elif letter == "m":
        store += "M"
    elif letter == "B":
        store += "8"
    elif letter == "o":
        store += "."
    else:
        store += letter
store += "q*s"
print(store)