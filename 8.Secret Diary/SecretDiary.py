SecretDiary  = []

def menu():
    print("\n1. Show Menu")
    print("2. Add Thought")
    print("3. Show Diary")
    print("4. Remove all thoughts")
    print("5. Exit\n")


def show_thoughts():

    with  open("SecretDiary.txt", "r") as f:
    
        lines = f.readlines()
    content = [line.strip() for line in lines]

    for index, thought in enumerate (content, start = 1):
        print(f"{index}. {thought}")

while True:

    menu()

    choice = input("Select : ")

    if choice == "1":
        menu()

    elif choice == "2":

        thought = input("What happened today? : ")
    

        with open("SecretDiary.txt", "a") as f :

            f.write(f"{thought}\n")
            print(f"{thought} saved!\n")

    elif choice == "3":

        show_thoughts()

    elif choice == "4":

        with open("SecretDiary.txt", "w") as f:

            print("All your thoughts deleted!")

    elif choice == "5":

        print("Exiting...")
        break

    else:
        print("Error")
