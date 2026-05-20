import os

# 1. Βρίσκουμε το σωστό μονοπάτι (για σιγουριά)
folder = os.path.dirname(__file__)
file_path = os.path.join(folder, "menu.txt")

menu = {}
order = []

# 2. ΓΕΜΙΣΜΑ ΤΟΥ MENU ΑΠΟ ΤΟ ΑΡΧΕΙΟ
# Αυτό ΠΡΕΠΕΙ να γίνει πρώτο!
try:
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line or ":" not in line: # Αγνοεί κενές γραμμές ή λάθος μορφή
                continue

            parts = line.split(":")
            name = parts[0].strip()
            # ΔΙΟΡΘΩΣΗ: Πρώτα strip(), μετά float()
            price = float(parts[1].strip()) 

            menu[name] = price
except FileNotFoundError:
    print("Σφάλμα: Το αρχείο menu.txt δεν βρέθηκε!")

# 3. ΕΜΦΑΝΙΣΗ ΤΟΥ MENU ΣΤΟ ΤΕΡΜΑΤΙΚΟ
print("-" * 10, f"{'MENU':^6}", "-" * 10)
if not menu:
    print("Το μενού είναι άδειο! Ελέγξτε το menu.txt")
else:
    for name, price in menu.items():
        print(f"{name:<12} | {price:>6}$")
print("=" * 28)
print(f"{'Type 0 to exit':^28}")

# 4. Η ΛΟΥΠΑ ΤΗΣ ΠΑΡΑΓΓΕΛΙΑΣ
while True:
    # Χρησιμοποιούμε strip() για να μην μας χαλάνε τα τυχαία κενά
    choice = input("\nWhat you want to order?: ").strip()

    if choice == "0":
        print("Saving...\n")
        break

    if choice in menu:
        order.append(choice)
        print(f"Added to your order: {choice} at {menu[choice]}$")
    else:
        print(f"We don't have '{choice}'! (Check spelling & caps)")

# 5. Η ΑΠΟΔΕΙΞΗ (RECEIPT)
total = 0
number = 0

with open("receipt.txt", "w") as file:
    title = f"{'Your Order':^25}\n"
    sep = "-" * 25 + "\n"
    
    print("\n" + sep + title + sep, end="")
    file.write(sep + title + sep)

    for item in order:
        number += 1
        total += menu[item]
        receipt_line = f"{number:3}. {item:12} : {menu[item]:>5}$\n"
        print(receipt_line, end="")
        file.write(receipt_line)

    footer = f"\nSummary of receipt : {total}$\nThank you for supporting us!\n"
    print(footer)
    file.write(footer)