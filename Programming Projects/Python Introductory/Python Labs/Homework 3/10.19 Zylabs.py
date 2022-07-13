# Andy Luong 1525166
# Zylabs 10.19

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_description(self):
        print(self.item_name + ":" + self.item_description)

class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2016", cart_items=None):
        if cart_items is None:
            cart_items = []
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        print("ADD ITEM TO CART")
        item_name = input("Enter the item name:\n")
        item_description = input("Enter the item description:\n")
        item_price = int(input("Enter the item price:\n"))
        item_quantity = int(input("Enter the item quantity:\n"))
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    def remove_item(self):
        print("REMOVE ITEM FROM CART")
        items = input("Enter name of item to remove:\n")
        for item in self.cart_items:
            if item.item_name == items:
                self.cart_items.remove(items)
            else:
                print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        print("CHANGE ITEM QUANTITY")
        itemName = input("Enter the item name:\n")
        for item in self.cart_items:
            if item.item_name == itemName:
                quantity = int(input("Enter the new quantity: "))
                item.item_quantity = quantity
            else:
                print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        count = 0
        for count in self.cart_items:
            count += count.item_quantity
        return count

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            cost = (item.item_price * item.item_quantity)
            total_cost += cost
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print("OUTPUT SHOPPING CART")
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print("Number of Items: " + str(ShoppingCart.get_num_items_in_cart(self)))
            print()
            print("SHOPPING CART IS EMPTY\n")
            for item in self.cart_items:
                print(item.item_name + item.item_quantity + item.item_price + (item.item_price * item.item_quantity))
            print("Total: $" + str(ShoppingCart.get_cost_of_cart(self)))
            print()

    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(self.customer_name + "'s Shopping Cart - " + self.current_date + "\n")
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.item_name + ": " + item.item_description)
        print()

def print_menu(ShoppingCart):
    cart = newCart
    menu = ("MENU\n"
    "a - Add item to cart\n"
    "r - Remove item from cart\n"
    "c - Change item quantity\n"
    "i - Output items' descriptions\n"
    "o - Output shopping cart\n"
    "q - Quit\n")

    command = ''
    while command != "q":
        print(menu)
        command = input("Choose an option:\n")
        while command != "a" and command != "o" and command != "i" and command != "r" and command != "c" and command != "q":
            command = input("Choose an option:\n")
        if command == "a":
            cart.add_item(ItemToPurchase)
        elif command == "r":
            cart.remove_item()
        elif command == "c":
            cart.modify_item(ItemToPurchase)
        elif command == "i":
            cart.print_descriptions()
        elif command == "o":
            cart.print_total()

if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()
    print("Customer name: " + customer_name)
    print("Today's date: " + current_date)
    print()
    newCart = ShoppingCart(customer_name, current_date)
    print_menu(newCart)