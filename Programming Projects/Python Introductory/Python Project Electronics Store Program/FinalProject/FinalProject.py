# Andy Luong 1525166
# Final Project

#PART 1
import csv
from datetime import datetime

def combine(dict1, dict2): #this function combines the dictionaries below
    for key in dict2:
        if key in dict1:
            dict1[key] = combine(dict1[key], dict2[key])
        else:
            dict1[key] = dict2[key]
    return dict1
file = input("Enter first file: ")
file2 = input("Enter second file: ")
file3 = input("Enter third file: ")

manufacturerInventory = {}#made an empty dictionary to add from csv file

with open(file, "r") as csv_file:#opened the first file
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:#go through each line
        manufacturerInventory[row[0]] = {"Name":row[1], "Type":row[2], "Damaged":row[3]} #added to dictionary based on a specific order

priceList = {}#dictionary for prices
with open(file2, "r") as csv_file:#open secondfile
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        priceList[row[0]] = {"Price":row[1]}#add to dictionary again based on an order

serviceDatesList = {}#dictionary for service dates
with open(file3, "r") as csv_file:#opens third file
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        serviceDatesList[row[0]] = {"ServiceDate":row[1]}#adds the ID and the date to the dictionary

Inventory = combine(manufacturerInventory, priceList)#created a variable to use the combine function above. This will combinte manufacturerInventory and the priceList

FullInventory = combine(Inventory, serviceDatesList)#created another variable to combine the third dictionary. With this, we have all 3 dictionaries into one dictionary
sortedInventory = sorted(FullInventory.items(), key = lambda x: x[1]['Name'])#This variable sorts the dictionary by alphabetical order based on the name of manufacturer.

with open("FullInventory.csv", "w", newline = "") as csv_file: #write to fullInventory file in correct order
    csv_writer = csv.writer(csv_file, delimiter=",")
    for key in sortedInventory:
        csv_writer.writerow([key[0]] + [key[1]["Name"]] + [key[1]["Type"]] + [key[1]["Price"]] + [key[1]["ServiceDate"]] + [key[1]["Damaged"]])#writes to fullInventory file based on specific order
typeList = []#created a list to store unique types for the function below
for key in sortedInventory:#goes through each item in sortedInventory
    if key[1]["Type"] not in typeList:#checks to see if the type is unique in the dictionary
        typeList.append(key[1]["Type"])#if it is unique then it is appended to the typeList list.
    else:
        continue

for type in typeList:#goes through each item in typeList
    filename = type.capitalize() + "Inventory.csv"#made a variable to make a new csv file regardless if the name entered is capitalized or not
    with open(filename, "w", newline = "") as csv_file:#open file to write
        csv_writer = csv.writer(csv_file, delimiter=",")
        for key in sortedInventory:#goes through each item in sortedInventory
            if key[1]["Type"] == type:#if the type found is equal to the same type in the dictionary
                csv_writer.writerow([key[0]] + [key[1]["Name"]] + [key[1]["Price"]] + [key[1]["ServiceDate"]] + [key[1]["Damaged"]])#it will write in this order based on its respective csv file created

sortedServiceDate = sorted(FullInventory.items(), key = lambda x: datetime.strptime(x[1]["ServiceDate"], '%m/%d/%Y'))#sort the dates of full inventory and puts it into variable from oldest to newest

with open("PastServiceDateInventory.csv", "w", newline = "") as csv_file:#open the service date file
    csv_writer = csv.writer(csv_file, delimiter=",")
    for key in sortedServiceDate:#go through the sorted time
        date = datetime.strptime(key[1]["ServiceDate"], '%m/%d/%Y')#turns the sorted string into date
        if date < datetime.today():#if the date is less than today's date, then its expired
            csv_writer.writerow([key[0]] + [key[1]["Name"]] + [key[1]["Type"]] + [key[1]["Price"]] + [key[1]["ServiceDate"]] + [key[1]["Damaged"]])#adds expired date to file

sortedDamagedInventory = sorted(FullInventory.items(), key = lambda x: x[1]['Damaged'], reverse=True)

with open("DamagedInventory.csv", "w", newline = "") as csv_file:#open DamagedInventory file
    csv_writer = csv.writer(csv_file, delimiter=",")
    for key in sortedDamagedInventory:#looks through the sorted inventory that is damaged
        if key[1]["Damaged"] == "damaged":#checks to see if item is damaged
            csv_writer.writerow([key[0]] + [key[1]["Name"]] + [key[1]["Price"]] + [key[1]["ServiceDate"]] + [key[1]["Damaged"]])#writes to the file

# PART 2
command = ''
while command != "q": #if you want to exit prompt, enter q for both command & command2
    command = input("Enter a manufacturer and type: ")
    if command == "q":
        break
    for key, value in FullInventory.items():#looks through keys & values in dictionary
        date = datetime.strptime(value["ServiceDate"], '%m/%d/%Y')#apply date variable which allows us to compare time
        if value["Name"] in command and value["Type"] in command:#if the values name & type is in command
            if value["Damaged"] == "damaged":#if it is damaged, pass
                pass
            if date < datetime.today():#if date is less than today, pass
                pass
            else:
                print(key, value,"\n")#prints the eligible items
                print("You may, also, consider: ")
                break
    else:
        print("No such item in inventory")

    for key, value in FullInventory.items():#looks through keys & values in dictionary
        date = datetime.strptime(value["ServiceDate"], '%m/%d/%Y')
        if value["Type"] in command and value["Name"] not in command:#if the type is in command, but the name is not
            if value["Damaged"] == "damaged": #if it is damaged, pass
                pass
            if date < datetime.today():#if date is less than today, pass
                pass
            else:
                print(key, value,"\n")#otherwise, print out eligible items
