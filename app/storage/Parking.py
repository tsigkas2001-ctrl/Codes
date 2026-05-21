import datetime
import time


parked_cars = {}
garage_menu = [
    "Car List" ,
    "List a Car",
    "Car left",
    "Save and Exit"
]


separator = ("=" * 40)
parking_plates = ("Parking Plate's")

print(f"{separator}\n" + f"{parking_plates.center(40)}\n" + f"{separator}\n")

number = 0

for i in garage_menu:
    number = number + 1
    print(f"{number}. {i}")

while True:
    
    choice = int(input("\nSelect: "))

    if choice == 1:
        with open("parked_cars.txt", "r") as f:
            print("\n--- Parked Cars ---")
            for line in f:
                print(line.strip().replace(",", " | Είσοδος: "))

    elif choice == 2:
        # 1. Παίρνουμε την ώρα ΜΕΣΑ στην επιλογή για να είναι πάντα η τρέχουσα
        entry_time = datetime.datetime.now().strftime("%D %H:%M:%S")
        # 2. Μετατρέπουμε την πινακίδα σε κεφαλαία πριν την αποθήκευση
        plate = input("Car plate: ").upper()

        with open("parked_cars.txt", "a") as f:
            # 3. Προσθέτουμε το \n στο τέλος για να αλλάζει γραμμή
            f.write(f"{plate} | {entry_time}\n")
        print(f"Car {plate} registered!")

    elif choice == 3:
        left_time = datetime.datetime.now()
        plate_left = input("Enter the plate of the car that left: ").upper()
        
        with open("parked_cars.txt", "r") as f:
            lines = f.readlines()

        found = False
        with open("parked_cars.txt", "w") as f:
            for line in lines:
                # 1. Καθαρίζουμε τη γραμμή από το \n και τη σπάμε στο " | "
                # data[0] θα είναι η πινακίδα, data[1] θα είναι η ώρα
                data = line.strip().split(" | ")
                
                # 2. Ελέγχουμε αν η λίστα data έχει όντως 2 στοιχεία (για ασφάλεια)
                # και συγκρίνουμε ΑΚΡΙΒΩΣ την πινακίδα (data[0])
                if len(data) == 2 and data[0] == plate_left:
                    found = True
                    print(f"Car with plate: {plate_left} left at {left_time.strftime('%H:%M')}")
                    # Εφόσον το βρήκαμε, ΔΕΝ το ξαναγράφουμε στο αρχείο (διαγραφή)
                else:
                    # Αν δεν είναι αυτό που ψάχνουμε, το ξαναγράφουμε ως έχει
                    f.write(line)

        if not found:
            print("This plate was not found in the parking")

    elif choice == 4:
        print("Saving and Exiting...\n")
        break

    else:
        print("Choice not found!")