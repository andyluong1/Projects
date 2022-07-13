# Andy Luong 1525166
# Zylabs 11.22

list = input()
list = list.split()

for word in list:
        freq = list.count(word)
        print(word, freq)