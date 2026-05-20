import datetime


print("-"*10, f"{'MENU':^6}", "-"*10)

order = []
menu = {}

print("="*28)
print(f"{'Type 0 to exit':^28}")

with open("menu.txt", "r") as file:
    
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(":")
        
        name = parts[0].strip()
        price = float(parts[1].strip())

        menu[name] = price

for name, price in menu.items():
    print(f"{name:<15} | {price:>5}$")

while True:
    choice = input("\nWhat you want to order?: ")

    if choice == "0":
        tora = datetime.datetime.now()
        imerominia = tora.strftime("%d/%m/%Y %H:%M")
        print("Saving...\n")
        break


    elif choice in menu:
        quantity = int(input("Quantity? : "))
        
        for i in range(quantity):
            order.append(choice)
        
        print(f"Added to your order : {choice} at {menu[choice]*quantity:.2f}$")


    else:
        print("We don't have this item!")

number = 0


with open("receipt.txt", "w") as file:
    
    title = f"{'Your Order':^25}\n"
    separator = "-"*25 + "\n"

    print(separator + title + separator, end="")

    print(f"{imerominia:>}\n")

    file.write(separator + title + separator)

    file.write(f"{imerominia:>}\n")

    total = 0

    for item in set(order):
        
        number = number + 1
        total = total + menu[item]
        
        vat = 1.24
        net_amount = total/vat
        vat_amount = total-net_amount
        
        quantity = order.count(item)

        receipt_line = f"{number:3}. {item:13} : {total:<5.2f} * {quantity:<5}$\n"
        vat_line  = f"{'VAT':<3}. {':':>15} {vat_amount:3.2f} {'$':>9}\n"    
        
        
        print(receipt_line, end="")
        print(vat_line, end="")
        file.write(receipt_line)

    footer = f"\nSummary of receipt : {total:.2f}$\nThank you for supporting us!\n"

    print(footer)
    file.write(footer)