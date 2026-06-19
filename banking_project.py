pin =1531
userpin=int(input("enter your pin"))

if userpin==pin:

    print("pin is succesfully verified ")

    print("welcome in my bank ")

    print("""

1.Deposit 
2.withdraw
3.Balence check
4.Exit 
      """)
balence = 5000

choice=int(input("enter your choice "))

if choice ==1:
    deposit=float(input("enter the amount to be deposite"))

    if deposit>0:
        balence+=deposit
        print("Rs",deposit,"has been deposited succesfully ","new balence is ",balence)

    else :
        print("invalid amount ")

elif choice ==2:
    withdraw=float(input("enter the amount to be withdraw "))
   
    if withdraw>0:
        if withdraw<=balence:
            balence-=withdraw
            print("Rs", withdraw,"has been withdraw successfully ")
        else:
            print("insufficient balence ")

        print("Rs",withdraw,"has been deposited succesfully ")

    else :
        print("invalid amount ")

elif choice==3:
    print("your balence is Rs ",balence)

elif choice ==4:
    print("thank you for banking with us ")

else:
    print("invalid choice ")

