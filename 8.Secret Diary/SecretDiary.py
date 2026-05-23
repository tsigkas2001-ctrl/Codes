SecretDiary  = []

def menu():
    print("\n1. Show Menu")
    print("2. Add Thought")
    print("3. Show Diary\n")


def show_thoughts(diary):

    with  open("SecretDiary.txt", "r") as f:
    
        lines = f.readlines()
        content = [line.strip() for line in lines]

        for index, thought in enumerate (content, start = 1):
            print(f"{index}. {thought}")

    return diary
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

        show_thoughts(diary)

    elif choice == "4":

        print("Exiting...")
        break

    else:
        print("Error")
