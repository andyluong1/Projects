# Andy Luong 1525166
# Zylabs 10.17

class ItemToPurchase:
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(self.item_price * self.item_quantity))

if __name__ == "__main__":
    print("Item 1")
    item1 = ItemToPurchase()
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = int(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    print()

    item2 = ItemToPurchase()
    print("Item 2")
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = int(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    print()

    total_price = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity

    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print("Total: $" + str(total_price))