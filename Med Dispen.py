#Creating an automatic cannabis ordering machine

#This is for verification
print("Hello, welcome to Red Garden Pharm.")
name = input("My name is Rooi and I will be your assistant today. What is your name?\n")

age = input("How old are you?\n")
while not int(age.isdigit()):
    print(f"{age} is an invalid input. Only numbers are allowed. Please present your age in numbers.")
    age = input("How old are you?\n")

password = "r3@lr3d3r"

access_pass = input("What is your access pass?\n")
while access_pass != password:
    print("OOPS! It seem that your password is incorrect. Please try again")
    access_pass = input("What is your access pass?\n")

if int(age) < 18:
    print(f"Hey {name}, it seems that you are currently {age} years old, therefore "
          f"unfortunately you cannot access this site.\nPerhaps a guardian may assist in "
          f"acquiring your medication. ")
    print("We look forward to seeing you again!")
    exit()

else:
    print(f"Nice to have you here {name}, please feel free to browse our menu.")

variant = input(f"Select variant:\n1.Sativa\n2.Indica\n3.Hybrid\n")


#This is the menu
sativa = ["1.Heavy", "2.Mid", "3.Light"]
indica = ["1.Heavy", "2.Mid", "3.Light"]
hybrid = ["Chocolate Gelato", "Blue Dream", "Girl Scout Cookies", "Bruce Banner", "Blue Mystic"]

if variant == "1" or variant == "sativa":
    sub_category = input(f"Intensity:\n{sativa}")
    if sub_category == "Heavy" or sub_category == "1":
        heavy_sativa = ["Malawi Gold", "Durban Poison", "Green Crack", "Jack Herer", "Lemon Skun"]
        choice = input(f"Choose your fighter:\n{heavy_sativa}\n")
        if choice == "Malawi Gold" or choice == "1":
            price = 180
            print(f"Malawi Gold is {price}")
        if choice == "Durban Poison" or choice == "2":
            price = 180
            print(f"DP is {price}")
        if choice == "Green Crack" or choice == "3":
            price = 180
            print(f"GC is {price}")
        if choice == "Jack Herer" or choice == "4":
            price = 180
            print(f"JH is {price}")
        if choice == "Lemon Skunk" or choice == "5":
            price = 180
            print(f"LS is {price}")
        else:
            print(f"{choice} is unavailable or invalid.")
            exit()

    if sub_category == "Mid" or sub_category == "2":
        mid_sativa = ["Trainwreck", "Super Lemon Haze", "Chocolope"]
        choice = input(f"Choose your fighter:\n{mid_sativa}\n")
        if choice == "Trainwreck" or choice == "1":
            price = 150
            print(f"Trainwreck is {price}")
        if choice == "Super Lemon Haze" or choice == "2":
            price = 150
            print(f"SLH is {price}")
        if choice == "Chocolope" or choice == "3":
            price = 140
            print(f"Chocolope is {price}")

    if sub_category == "Light" or sub_category == "3":
        lit_sativa = ["Northern Lights", "Haze", ]
        choice = input(f"Choose your fighter:\n{lit_sativa}\n")

        if choice == "Northern Lights" or choice == "1":
            price = 130
            print(f"Northern Lights is {price}")
        if choice == "Haze" or choice == "2":
            price = 180
            print(f"Haze is {price}")

    else:
        print("Potency level invalid or not available.")
        exit()

elif variant == "2" or variant == "indica":
    sub_category = input(f"Intensity:\n{indica}\n")
    if sub_category == "Heavy" or sub_category == "1":
        heavy_indica = ["OG Kush", "Northern Lights", "Purple Kush", "Harlequin"]
        choice = input(f"Choose your fighter:\n{heavy_indica}\n")
        if choice == "OG Kush" or choice == "1":
            price = 170
            print(f"OG Kush is R{price}")
        elif choice == "Northern Light" or choice == "2":
            price = 160
            print(f"Northern Light is R{price}")
        elif choice == "Purple Kush" or choice == "3":
            price = 165
            print(f"Purple Kush is R{price}")
        elif choice == "Harlequin" or choice == "4":
            price = 165
            print(f"Harlequin is R{price}")


    elif sub_category == "Mid" or sub_category == "2":
        mid_indica = ["Ghost OG", "Blueberry", "Grape Ape", "Master Kush", "Afghan Kush"]
        choice = input(f"Choose your fighter:\n{mid_indica}\n")
        if choice == "Ghost OG" or choice == "1":
            price = 150
            print(f"Ghost OG is R{price}")
        elif choice == "Blueberry" or choice == "2":
            price = 140
            print(f"Blueberry is R{price}")
        elif choice == "Grape Ape" or choice == "3":
            price = 145
            print(f"Grape Ape is R{price}")
        elif choice == "Master Kush" or choice == "4":
            price = 145
            print(f"Master Kush is R{price}")
        elif choice == "Afghan Kush" or choice == "5":
            price = 145
            print(f"Afghan Kush is R{price}")
        else:
            print(f"{choice} unavailable or invalid input.")
            exit()

    elif sub_category == "Light" or sub_category == "3":
        lit_indica = ["Blackberry Kush", "Critical Mass", "LA Confidential"]
        choice = input(f"Choose your fighter:\n{lit_indica}\n")

        if choice == "Blackberry Kush" or choice == "1":
            price = 130
            print(f"Blackberry Kush is R{price}")
        elif choice == "Critical Mass" or choice == "2":
            price = 120
            print(f"Critical Mass is R{price}")
        elif choice == "LA Confidential" or choice == "3":
            price = 120
            print(f"LA Confidential is R{price}")
        else:
            print(f"{choice} unavailable or invalid input.")
            exit()

    else:
        print("Potency level invalid or not available.")
        exit()

#Hybrid Menu
elif variant == "3" or variant == "hybrid":
    choice = input(f"Choose your fighter:\n{hybrid}\n")
    if choice == "Chocolate Gelato" or choice == "1":
        price = 180
        print(f"Chocolate Gelato is {price}")
    if choice == "Blue Dream" or choice == "2":
        price = 160
        print(f"Blue Dream is {price}")
    if choice == "Girl Scout Cookies" or choice == "3":
        price = 170
        print(f"Girl Scout Cookies is {price}")
    if choice == "Bruce Banner" or choice == "4":
        price = 175
        print(f"Bruce Banner is {price}")
    if choice == "Blue Mystic" or choice == "5":
        price = 160
        print(f"Blue Mystic is {price}")
    else:
        print(f"{choice} is unavailable or invalid.")
        exit()


else:
    print(f"{variant} is not either invalid or not available. Pardon for the inconvenience.\n"
          f"Please select 1, 2, 3:")
    exit()

quantity = int(input("How many of these would you like?\n"))

total = price * quantity

print(f"Your total is R{total}.\nEnjoy your flowers {name} and we look forward to seeing you again soon!")