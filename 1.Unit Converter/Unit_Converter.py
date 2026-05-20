def km_to_miles(km):
    result = km * 0.621
    return result


def miles_to_km(miles):
    result = miles*1.621
    return result

def celcius_to_fahrenheit(c):
    result = (c * 1.8) + 32
    return result
    
def fahrenheit_to_celcius(f):
    result = ((f - 32)*5)/9
    return result

def menu():
    print("\n" + "--- Menu ---".center(40) + "\n")
    print("1. Convert Distance")
    print("2. Convert Temperature")
    print("3. Save and Exit\n")


while True:
    menu()

    choice = input("Select : ")

    if choice == "0":
        menu()

    if choice == "1":
        
        print("Press '1' to convert Km -> Miles\nPress '2' to convert Miles -> Km\n")
        choice2 = input("Select : ")
        
        if choice2 == "1":
            user_km = float(input("KM : "))

            miles = km_to_miles(user_km)
            print(f"Miles : {miles:.2f}")

        elif choice2 == "2":
            user_miles = float(input("Miles : "))

            km = miles_to_km(user_miles)
            print(f"Km : {km:.2f}")
        else:
            print("Error, Please try again!") 


    elif choice == "2":
        print("Press '1' to convert Celcius to Fahrenheit\nPress '2' to convert Fahrenheit to Celcius")
        choice2 = input("Select : ")
        
        if choice2 == "1":
            user_c =float(input("Celcius: "))

            c  = celcius_to_fahrenheit(user_c)
            print(f"Fahrenheit: {c:.2f} °C")

        elif choice2 == "2":
            user_f = float(input("Fahrenheit : "))
            
            f = fahrenheit_to_celcius(user_f)
            print(f"Celcius : {f} ℉")
        else:
            print("Error, Please try again!") 

    elif choice == "3":
        print("Saving and Exiting...")
        break

    else:
        print("Error, Please try again!")        