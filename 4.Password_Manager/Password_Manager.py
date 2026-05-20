separator = ("-"*40)
title = ("- Menu -")

passwords = {}
menu = [
    "Show Passwords",
    "Add Password",
    "Delete Password",
    "Save and Exit"
]

print(f"{separator}\n" + f"{title.center(40)}\n" + f"{separator}")

number = 0

for i in menu:
    number = number + 1
    print(f"{number}. {i}".center(40))


while True:

    choice = int(input("\nSelect: "))

    if choice == 1:
        with open("passwords.txt", "r") as f:
            print("--- Passwords ---".center(40))
            for line in f:
                print(line.strip().replace(",", " | "))

    if choice == 2:

        print("--- Press 0 to reset ---".center(40))
        pass_title = input("Site: ")
        if pass_title == "0":
            print("Returning on menu...")
            continue
            
        user = input("Enter username: ")
        if user == "0":
            print("Returning on menu...")
            continue

        while True:
            password = input("Enter password: ")
            pass_check = input("Enter password again: ")
            
            if  password == pass_check:
                
                print("Password are same!")
                break
                
            else:
                print("Passwords incorrect")
        
        with open("passwords.txt", "a") as f:
            f.write(f"{pass_title} | {user} | {password}\n")
        
        print(f"Account: {pass_title} saved!")

    if choice == 3:
        site_to_delete = input("Site to delete: ")
        with open("passwords.txt" , "r") as f:
            lines = f.readlines()

        found = False

        with open("passwords.txt", "w") as f:
            for line in lines:
                data = line.strip().split(" | ")

                if  data[0].upper() == site_to_delete.upper():
                    found = True
                    print(f"{data[0]} deleted!")
            
                else:
                    f.write(line)
                    

            if not found:
                print("We didn't found your pass!")

    elif choice == 4:
        print("Saving and Exiting...")
        break
    
    
       