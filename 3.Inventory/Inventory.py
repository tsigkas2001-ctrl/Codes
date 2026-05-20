inventory = []

def menu():
    print("\n1. Show Inventory")
    print("2. Add Item to Inventory")
    print("3. Remove Item from Inventory")
    print("4. Save and Exit\n")

def add_item (inventory, item):
    inventory.append(item)
    print(f"{item} added to your bag!")

    return inventory

def show_inventory(inventory):
    print("\n--- YOUR INVENTORY ---")

    if len(inventory) == 0:
        print("Your bag is empty...")

    else:
        for index, item in enumerate(inventory, start=1):
            print(f"{index}.  {item}")

        print("-"*20)

def remove_item(inventory):
    item_to_remove = input("Enter the name of the item you want to remove: ")

    if item_to_remove in inventory:
        inventory.remove(item_to_remove)
        print(f"{item_to_remove} heas been removed from your inventory")

    else:
        print(f"Error: You dont have a {item_to_remove} in your bag")

    return inventory

while True:

    menu()
    choice = input("Select: ")

    if choice == "0":
        menu()

    elif choice == "1":
        show_inventory(inventory)

    elif choice == "2":
        new_item = input("What did you find? ")

        inventory = add_item(inventory, new_item)

    elif choice == "3":
        inventory = remove_item(inventory)

    elif choice == "4":
        print("Saving and Exiting...")
        break

