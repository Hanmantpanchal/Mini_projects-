print("Welcome to the Shopping Application")

price = None

print("""
1. Electronics
2. Clothing
3. Groceries
4. Exit
""")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("""
1. Mobile (25000 Rs)
2. Laptop (45000 Rs)
3. TV (14000 Rs)
4. Exit
""")

    choice1 = int(input("Enter your choice: "))

    if choice1 == 1:
        price = 25000
        print("You have selected Mobile")
    elif choice1 == 2:
        price = 45000
        print("You have selected Laptop")
    elif choice1 == 3:
        price = 14000
        print("You have selected TV")
    elif choice1 == 4:
        print("Thank you for visiting")
    else:
        print("Invalid choice")

elif choice == 2:
    print("""
1. Shirt (500 Rs)
2. Pant (800 Rs)
3. T-shirt (300 Rs)
4. Exit
""")

    choice2 = int(input("Enter your choice: "))

    if choice2 == 1:
        price = 500
        print("You have selected Shirt")
    elif choice2 == 2:
        price = 800
        print("You have selected Pant")
    elif choice2 == 3:
        price = 300
        print("You have selected T-shirt")
    elif choice2 == 4:
        print("Thank you for visiting")
    else:
        print("Invalid choice")

elif choice == 3:
    print("""
1. Sakhar 1kg (40 Rs)
2. Milk 1ltr (50 Rs)
3. Nirma 1kg (30 Rs)
4. Exit
""")

    choice3 = int(input("Enter your choice: "))

    if choice3 == 1:
        price = 40
        print("You have selected Sakhar")
    elif choice3 == 2:
        price = 50
        print("You have selected Milk")
    elif choice3 == 3:
        price = 30
        print("You have selected Nirma")
    elif choice3 == 4:
        print("Thank you for visiting")
    else:
        print("Invalid choice")

elif choice == 4:
    print("Thank you for visiting")

else:
    print("Invalid choice")

# Billing section
if price is not None:

    quantity = int(input("Enter quantity: "))

    total = price * quantity
    print("Total amount is:", total)

    discount = 0

    if total > 30000:
        discount = total * 0.20
        print("You got 20% discount")
    elif total > 15000:
        discount = total * 0.10
        print("You got 10% discount")
    else:
        print("No discount")

    final_amount = total - discount

    print("Discount: Rs", discount)
    print("Final Amount: Rs", final_amount)
    print("Do visit again!")