# Andy Luong 1525166
# Zylabs 11.18

numbers = input()
list= [int(num) for num in numbers.split() if int(num) >= 0]
list.sort()

for num in list:
    if num >= 0:
        print(num, end=" ")