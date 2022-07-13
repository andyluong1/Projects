# Andy Luong 1525166
# Coding Problem 1

from datetime import date

print("Birthday Calculator")
print("Current day")

month = int(input("Month: "))
day = int(input("Day: "))
year = int(input("Year: "))

print("Birthday")

month1 = int(input("Month: "))
day1 = int(input("Day: "))
year1 = int(input("Year: "))
birth = date(year1, month1, day1)
today = date(year, month, day)
today = today.year
birth = birth.year
age = (today - birth)

print("You are " + str(age) + " years old.")

if (month, day) == (month1, day1):
    print("Happy birthday!")

