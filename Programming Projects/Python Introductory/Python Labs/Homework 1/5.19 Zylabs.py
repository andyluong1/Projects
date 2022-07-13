# Andy Luong 1525166
# Zylabs 5.19

services = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12}

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()

first = input("Select first service:\n")
second = input("Select second service:\n")

print()
print("Davy's auto shop invoice\n")
print("Service 1: " + first + str(",") + " $" + str(services[first]))
print("Service 2: " + second + str(",") + " $" + str(services[second]))
print()
total = services[first] + services[second]
print("Total: " + "$" + str(total))

